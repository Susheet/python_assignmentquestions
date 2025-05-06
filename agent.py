from openai import OpenAI
from dotenv import load_dotenv
import json
import requests

load_dotenv()

client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def get_weather(location: str):
    print("Tool called: get_weather", location)

    url = f"https://wttr.in/{location}?format=%C=%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather of {location} is {response.text}"
    return "Unable to fetch the weather data"
    


available_tools = {
    "get_weather": {
        "fn": get_weather,
        "description": "Get the weather of the given location"
    }

}

tool_descriptions = "\n".join(
    [f"- {name}: {tool['description']}" for name, tool in available_tools.items()]
)

system_prompt = f"""
    You are an helpful AI assistant who is specialised in resolving user query.
    You work on start, plan, action, observe mode.
    For the given user query and available tools, plan the step by step execution, based on planning,
    select the relevant tool from the available tool. Based on the tool selection you perform an action to call the tool.
    Wait for the observation and based on the observation from the tool call resolve the user query.
    
    Rules:
    1. Follow the strict JSON output as per output schema.
    2. Always peform one step at a time and wait for next input.
    3. Carefully analyse the user query.

    Output JSON Format:
    {{
        "step": "string", 
        "content": "string",
        "function": "The name of function only if step is action",
        "input": "The input parameter for the function only if step is action",
    }}

    Available tools:
    {tool_descriptions}

    Example:
    User query: What is the weather of Bengaluru?
    Output: {{"step": "plan", "content": "The user is interested in weather data of Bengalure"}}
    Output: {{"step": "plan", "content": "From the available tools I should call get_weather"}}
    Output: {{"step": "action", "function": "get_weather", "input": "Bengaluru"}}
    Output: {{"step": "observe", "output": "12 Degree Celsius"}}
    Output: {{"step": "output", "content": "The weather of Bengaluru is 12 Degree Celsius"}}

"""

messages = [
    {"role": "system", "content": system_prompt}
]

while True:

    user_query = input('> ')

    messages.append({"role": "user", "content": user_query})

    while True:
        response = client.chat.completions.create(
            model='gemini-2.0-flash',
            response_format={"type": "json_object"},
            messages=messages
        )

        parsed_output = json.loads(response.choices[0].message.content)
        messages.append({"role": "assistant", "content": json.dumps(parsed_output)})

        if parsed_output.get("step") == "plan":
            print(f"🧠: {parsed_output.get('content')}")
            continue

        if parsed_output.get("step") == "action":
            tool_name = parsed_output.get("function")
            tool_input = parsed_output.get("input")

            if available_tools.get(tool_name, False) != False:
                output = available_tools[tool_name]["fn"](tool_input)
                messages.append({"role": "assistant", "content": json.dumps({"step": "observe", "output": output})})
                continue
        
        if parsed_output.get("step") == "output":
            print(f"🤖: {parsed_output.get('content')}")
            break
            
