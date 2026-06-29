import time
import subprocess
from langchain_openai import ChatOpenAI
import gc

from langchain.globals import set_llm_cache
from langchain_community.cache import SQLiteCache


def setup_cache():
    set_llm_cache(SQLiteCache(database_path=".langchain_cache.db"))



def get_llm():
    command = [
        r"C:\Users\Za7lou9\Downloads\llama-b9760-bin-win-cuda-12.4-x64\llama-server.exe",
        "-m",
        r"C:\Users\Za7lou9\.cache\huggingface\hub\models--google--gemma-4-E2B-it-qat-q4_0-gguf\snapshots\1894d1fc0a19d86697abd40483f5983c867df03f\gemma-4-E2B_q4_0-it.gguf",
        "--host", "127.0.0.1",
        "--port", "8000",
        "-c", "4096",
        "-ngl", "99",
    ]

    llama_process=subprocess.Popen(command)

    time.sleep(10)


    llm = ChatOpenAI(
        base_url="http://127.0.0.1:8000/v1",
        api_key="none",
        model="gemma-4",
        temperature=0.75,
    )

    return llm, llama_process



def clean_up(llama_process):
    llama_process.terminate()
    llama_process.wait()
    gc.collect()