from llm_config import get_llm
from tools import all_tools
from langchain.agents import create_agent



llm=get_llm()

agent = create_agent(
    model=llm,
    tools=all_tools,
    system_prompt="You are a helpful assistant",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
)
print(result["messages"][-1].content)