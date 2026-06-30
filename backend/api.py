from fastapi import FastAPI
from pydantic import BaseModel

from backend.llm_config import get_llm, clean_up, setup_cache
from backend.tools import all_tools
from langchain.agents import create_agent

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


setup_cache()
llm,llama_process =get_llm()
agent = create_agent(
    model=llm,
    tools=all_tools,
    system_prompt="You are a helpful assistant"
)

messages =[]
class ChatRequest(BaseModel):
    message:str


@app.post("/chat")
def chat(req:ChatRequest):
    messages.append({"role": "user", "content": req.message})
    result =agent.invoke({"messages": messages})
    response = result["messages"][-1].content
    messages.append({"role": "assistant", "content": response})
    return{
        "response":response
    }

