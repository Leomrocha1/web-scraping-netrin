# Web Scraping Netrin

## Descrição
Projeto para realizar web scraping e coletar dados de sites específicos usando Python e Docker.

## Tecnologias
- Python 3.8+
- Docker e Docker Compose

## Pré-requisitos
- **Python 3.8+**
- **Docker**

### Documentacao API
1. Disponível em:
    ```bash
    http://localhost:8000/docs

## Instalação e uso do projeto (Docker)
1. Clone o repositório:
   ```bash
   git clone https://github.com/Leomrocha1/web-scraping-netrin.git
   cd web-scraping-netrin

2. Rode o comando Docker:
    ```bash
    docker-compose up --build

## Intalação e uso do projeto (Local)
1. Instalação sem Docker (opcional): Caso prefira instalar e rodar o projeto sem Docker, crie um ambiente virtual e instale as dependências:
    ```bash
    ###API###
    python -m venv venv
    source venv/bin/activate  # Para Windows: venv\Scripts\activate
    cd app/
    pip install -r requirements.txt

    ###WORKER###
    python -m venv venv-worker
    source venv-worker/bin/activate  # Para Windows: venv-worker\Scripts\activate
    cd worker/
    pip install -r requirements.txt

1. Rodar o Projeto sem Docker (opcional):
    ```bash
    ###API### Com o passo 3 completo.
    cd app/
    uvicorn run:app --host 0.0.0.0 --port 8000

    ###WORKER### Com o passo 3 completo.
    cd worker
    python worker.py
