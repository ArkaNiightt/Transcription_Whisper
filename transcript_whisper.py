from openai import OpenAI
import os
from dotenv import load_dotenv
from pydub import AudioSegment
import math
from textwrap import dedent
import streamlit as st

temperatura = 0.2

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

input_folder = "audio_files"
output_folder = "transcriptions"
temp_folder = "temp_audio_chunks"

os.makedirs(output_folder, exist_ok=True)
os.makedirs(temp_folder, exist_ok=True)

def split_audio(file_path, max_size_mb=50):
    audio = AudioSegment.from_file(file_path)
    max_size_bytes = max_size_mb * 1024 * 1024
    duration_ms = len(audio)
    chunk_size_ms = max(
        5000,
        min(
            duration_ms // 10, max_size_bytes // (audio.frame_rate * audio.channels * 2)
        ),
    )

    chunks = []
    for i in range(0, duration_ms, chunk_size_ms):
        chunk = audio[i : i + chunk_size_ms]
        chunk_path = os.path.join(temp_folder, f"chunk_{i}.mp3")
        chunk.export(chunk_path, format="mp3")
        chunks.append(chunk_path)

    return chunks

def process_audio_file(filename):
    input_path = os.path.join(input_folder, filename)
    output_filename = os.path.splitext(filename)[0] + ".txt"
    output_path = os.path.join(output_folder, output_filename)

    print(f"Processando: {filename}")

    try:
        full_transcript = ""
        if os.path.getsize(input_path) > 25 * 1024 * 1024:
            chunks = split_audio(input_path)
            for chunk in chunks:
                with open(chunk, "rb") as audio_file:
                    try:
                        transcript = client.audio.transcriptions.create(
                            model="whisper-1",
                            file=audio_file,
                            temperature=temperatura,
                        )
                        full_transcript += transcript["text"] + " "
                    except Exception as error:
                        print(f"Erro ao processar {filename}: {str(error)}")
                        break
                os.remove(chunk)
        else:
            with open(input_path, "rb") as audio_file:
                try:
                    transcript = client.audio.transcriptions.create(
                        model="whisper-1",
                        file=audio_file,
                        temperature=temperatura,
                    )
                    full_transcript = transcript["text"]
                except Exception as error:
                    print(f"Erro ao processar {filename}: {str(error)}")
                    return

        with open(output_path, "w", encoding="utf-8") as file:
            file.write(full_transcript.strip())

        print(f"Transcrição salva em {output_path}")
    except Exception as e:
        print(f"Erro ao processar {filename}: {str(e)}")

if not os.listdir(input_folder):
    st.warning("A pasta de entrada está vazia. Por favor, adicione arquivos de áudio para processar.")
else:
    for filename in os.listdir(input_folder):
        if filename.endswith((".mp3", ".wav", ".m4a")):
            process_audio_file(filename)

    st.success("Todas as transcrições foram concluídas.")
