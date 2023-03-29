from langchain import OpenAI
from tools_creation import tools
from langchain.agents import initialize_agent
from API_keys import OPENAI_API_KEY
from langchain.memory import ConversationBufferMemory
from chat_GUI import ChatGUI
from langchain.chat_models import ChatOpenAI
from pdf_viewer import pdfViewer

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

llm=ChatOpenAI(temperature=0,openai_api_key=OPENAI_API_KEY)
agent = initialize_agent(tools, llm, agent="chat-conversational-react-description", verbose=True, memory=memory)


def callback(message):
    response = agent.run(message)
    return response

chat_bot = ChatGUI(callback=callback)