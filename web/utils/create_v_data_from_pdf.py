from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.embeddings import HuggingFaceEmbeddings

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.pgvector import PGVector


def remove_null_chars(texts):
    for doc in texts:
        doc.page_content = doc.page_content.replace("\x00", "")
    return texts


def start_per_folder(fold, db):
    loader = DirectoryLoader(
        fold,
        glob="./*.pdf",
        loader_cls=PyPDFLoader,
    )
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2"
    )

    return PGVector.from_documents(
        embedding=embeddings,
        documents=remove_null_chars(texts),
        collection_name=db.COLLECTION_NAME,
        connection_string=db.SYNC_CONNECTION_STRING,
    )
