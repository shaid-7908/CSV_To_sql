
from langchain_openai import ChatOpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent
import pandas as pd

data = pd.read_csv('BCMlabs324.csv')



agent = create_pandas_dataframe_agent(llm,data,verbose=True,allow_dangerous_code=True)

result = agent.run("Show me all data for 2024 try like this")

print(result)