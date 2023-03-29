from langchain import OpenAI
from tools_creation import tools
from langchain.agents import initialize_agent
from API_keys import OPENAI_API_KEY
from langchain.memory import ConversationBufferMemory
from chat_GUI import ChatGUI
from langchain.chat_models import ChatOpenAI

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

llm=ChatOpenAI(temperature=0,openai_api_key=OPENAI_API_KEY)
agent = initialize_agent(tools, llm, agent="chat-conversational-react-description", verbose=True, memory=memory)


# answer = agent.run("Hello, how are you?")
# print(answer)

def callback(message):
    return agent.run(message)

chat_bot = ChatGUI(callback=callback)