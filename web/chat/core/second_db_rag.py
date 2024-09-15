from langchain import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.prompts.chat import (
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
    ChatPromptTemplate,
)
from langchain.vectorstores import PGVector

from config import ConfigDataBaseSecondExample as CONF
from db_alchemy.second_db.connect import db

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

store = PGVector(
    collection_name=db.COLLECTION_NAME,
    connection_string=db.SYNC_CONNECTION_STRING,
    embedding_function=embeddings,
)

retriever = store.as_retriever(search_kwargs=CONF.search_kwargs)

llm = ChatOpenAI(temperature=CONF.temperature, model_name=CONF.chat_model)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type=CONF.chain_type,
    retriever=retriever,
    return_source_documents=True,
)

prompt = ChatPromptTemplate(
    input_variables=["context", "question"],
    output_parser=None,
    partial_variables={},
    messages=[
        SystemMessagePromptTemplate(
            prompt=PromptTemplate(
                input_variables=["context"],
                output_parser=None,
                partial_variables={},
                template=CONF.template,
                template_format="f-string",
                validate_template=True,
            ),
            additional_kwargs={},
        ),
        HumanMessagePromptTemplate(
            prompt=PromptTemplate(
                input_variables=["question"],
                output_parser=None,
                partial_variables={},
                template="{question}",
                template_format="f-string",
                validate_template=True,
            ),
            additional_kwargs={},
        ),
    ],
)
qa_chain.combine_documents_chain.llm_chain.prompt = prompt
