import requests
from langchain_core.tools import tool



@tool
def get_weather(city:str) :
    """Get the current weather for a given city."""
    try:
        url = f"https://wttr.in/{city}?format=%C+%t"
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            return f"The current weather in {city} is {response.text.strip()}."
        else:
            return f"Could not look up weather for {city} right now."
    except Exception as e:
        return f"Error connecting to weather service: {str(e)}"
    


all_tools = [get_weather]