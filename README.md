# Project Overview

The project allows you to deploy a one-page website in Docker, which is a chat with chatGPT that implements semantic search. To implement the search, a vector database based on PGVector was prepared.
# Setup and Launch

These settings are necessary for the deployment and correct operation of the application and database.

## Environment Variables

## Server Configuration

- `FIRST_CHAT_FA_HOST`: The web server host in the Docker container.
- `FIRST_CHAT_FA_PORT`: The web server port in the Docker container.
- `FIRST_CHAT_EXTERNAL_FA_PORT`: The local port for connections to the web server Docker container.
- `OPENAI_API_KEY`: OpenAI API key.
- `SWAGGER`: Swagger configuration.
- `DATASET`: The dataset to be used.

## First Database Configuration

- `FIRST_DB_POSTGRES_USER`: The database user's login for the first database.
- `FIRST_DB_POSTGRES_PASSWORD`: The database user's password for the first database.
- `FIRST_DB_DB_HOST`: The database host for the first database.
- `FIRST_DB_INTERNAL_DB_PORT`: The internal port for the first database in the Docker container.
- `FIRST_DB_POSTGRES_DB`: The name of the first database.
- `FIRST_DB_COLLECTION_NAME`: The vector data collection name for the first database.

## Config DataBase First Example

- `DataBaseFirstExample_EMBEDDINGS_MODEL_NAME`: The name of the embeddings model.
- `DataBaseFirstExample_SEARCH_KWARGS`: Search keyword arguments (should be a valid Python dictionary).
- `DataBaseFirstExample_TEMPERATURE`: Temperature setting for the model (should be a float).
- `DataBaseFirstExample_CHAT_MODEL_NAME`: The name of the chat model.
- `DataBaseFirstExample_CHAIN_TYPE`: The type of chain to be used.
- `DataBaseFirstExample_TEMPLATE`: The template configuration.


After specifying the required settings, launch the containers using the following Docker command:
`docker compose up`

For example, the project provides an example of connecting multiple RAG tools.

When you first start the web service, it takes time to load some auxiliary libraries (about 2-3 minutes with a connection speed of 30 MB/s)

To access the website, you can use the local host address with the external web server port specified in .env


