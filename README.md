# PROVA - Jackson Wellington Silva de Aguiar

## Instruções de Instalação e Execução

1. Clone o repositório:
    ```bash
    git clone https://github.com/jacksonwsaguiar/prova-m10
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd prova-m10
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
    
## Executando o projeto

Para executar, use o seguinte comando:
    ```bash
    python3 app.py 
    ```
## Executando o projeto com Docker
Para executar, use o seguinte comando:

1. Build a imagem:
    ```bash
    docker build -t prova .
    ```

2. Execute o container:
    ```bash
    docker run --name prova-container -p 5000:5000 -d prova
    ```

## Explicação dos arquivos

1. app.py: Servidor da aplicação contendo todas as rotas.
2. Dockerfile: Imagem da aplicação.
3. requirements.txt: Todos os requisitos da aplicação.
4. collections: Coleção de rotas geradas pelo insomnia.
