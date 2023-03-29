from langchain import OpenAI
from tools_creation import tools
from langchain.agents import initialize_agent
from API_keys import OPENAI_API_KEY


llm=OpenAI(temperature=0,openai_api_key=OPENAI_API_KEY)
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)



agent.run("Look for the number of particpants to the poll twitter and multiplied it by 7.")