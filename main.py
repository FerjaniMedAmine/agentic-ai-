from llm_config import get_llm
from tools import all_tools
from langchain.agents import create_agent



llm=get_llm()

agent = create_agent(
    model=llm,
    tools=all_tools,
    system_prompt="You are a helpful assistant",
)

print("aslema kifeh najmou n3awnouk?. ekteb 'exit' bech to5rej.\n")
messages=[]

while True:
    user_input = input("User:")
    if user_input.lower() ==  "exit":
        print("liltek zina weld 3ami")
        break
    
    messages.append({"role": "user", "content": user_input})
    result = agent.invoke({"messages": messages})

    llm_response = result["messages"][-1].content
    print(f"Assistant: {llm_response}")
    messages.append({"role": "assistant", "content": llm_response})
