from langchain.agents import Tool
from langchain.agents import tool
from files_uploader import PdfLoader, vectorstore
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.llms import OpenAI
from API_keys import OPENAI_API_KEY 

pdf_loader = PdfLoader("files")
pdf_loader.load_files_in_pinecone(index_name='test')

@tool
def document_search(query: str):
    """Answers a question about a file in the database."""
    number_of_chunks = 3
    doc = vectorstore.similarity_search(query,k=number_of_chunks)
    chain = load_qa_with_sources_chain(OpenAI(temperature=0,openai_api_key=OPENAI_API_KEY), chain_type="stuff")
    chain({"input_documents": doc, "question": query}, return_only_outputs=True)
    return chain({"input_documents": doc, "question": query}, return_only_outputs=True)


@tool
def parsing_multiplier(string: str):
    """Multiplies two numbers together."""
    a, b = string.split(",")
    return float(a) * float(b)

tools = [
    Tool(
        name = "Document Search",
        func=document_search,
        description="useful for question answering about a specific document in the database. When you don't know the answer to a query this tool will help you find the answer."
    ),
        Tool(
        name = "Multiplier",
        func=parsing_multiplier,
        description="useful for when you need to multiply two numbers together. The input to this tool should be a comma separated list of numbers of length two, representing the two numbers you want to multiply together. For example, `1,2` would be the input if you wanted to multiply 1 by 2."
    ),
]

