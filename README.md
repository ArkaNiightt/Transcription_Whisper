# Audio Transcription Script

Este projeto é um script Python para transcrição de arquivos de áudio usando a API OpenAI Whisper, com uma interface de usuário criada em Streamlit para fornecer feedback sobre o progresso do processo. Ele suporta transcrições de arquivos grandes dividindo-os em partes menores, se necessário.

## Funcionalidades

- Transcrição de arquivos de áudio nos formatos `.mp3`, `.wav` e `.m4a`.
- Suporte para divisão de arquivos de áudio grandes em partes menores para transcrição.
- Interface Streamlit para fornecer notificações sobre o progresso e possíveis problemas.
- As transcrições são salvas em arquivos de texto na pasta de saída.

## Pré-requisitos

- Python 3.7 ou superior
- OpenAI Python Client
- Pydub
- Streamlit
- ffmpeg (necessário para Pydub)

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/ArkaNiightt/Transcription_Whisper.git
   ```

2. Crie um ambiente virtual e ative-o:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Certifique-se de que o `ffmpeg` está instalado e disponível no PATH do sistema.

5. Crie um arquivo `.env` na raiz do projeto e adicione sua chave de API OpenAI:

   ```
   OPENAI_API_KEY=seu_api_key
   ```

## Uso

1. Coloque os arquivos de áudio na pasta `audio_files`.
2. Execute o script usando Streamlit:

   ```bash
   streamlit run script.py
   ```

3. A interface do Streamlit fornecerá feedback, como avisos se a pasta de entrada estiver vazia ou notificações sobre a conclusão da transcrição.

## Estrutura do Projeto

- `audio_files/`: Pasta onde você deve colocar os arquivos de áudio que deseja transcrever.
- `transcriptions/`: Pasta onde as transcrições de texto serão salvas.
- `temp_audio_chunks/`: Pasta temporária usada para armazenar partes dos arquivos grandes.
- `script.py`: Script principal para processar os arquivos de áudio.

## Problemas Conhecidos

- Arquivos de áudio muito grandes podem demorar bastante para serem processados, mesmo após a divisão em partes menores.
- Certifique-se de que o `ffmpeg` está instalado, caso contrário, o script não conseguirá processar arquivos de áudio.

## Contribuição

Sinta-se à vontade para abrir issues e pull requests para melhorias ou correções.

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

