# openai_chatbots_module
a python module that makes creating chatbots easyer.

# installation
1. install the open ai package using 
```bash
pip install openai
```
2. copy the [openAI_chatbots](openAI_chatbots) folder in to your project
3. have fun with the module (:

# demo
a demo of the module is included with this repo:[demo](demo.py)

## try this prompts:
```
read the file <filename><br>
```
```
write "<your text>" to the file <filename>
```
# documantation
## inital setup:
```python
import openAI_chatbots as chat
chat.setApiKey("<your api key>")
```

## creating a chatbot:
```python
# Create a chatbot instance
# You can provide a system prompt and a prompt prefix if desired
# Optional: <system prompt>, <prompt prefix>
chatbot = chat.chatbot(system_prompt="<system prompt>", prompt_prefix="<prompt prefix>")
```

## function calling:

creating a function calling object:
```python
functions = chat.GPT_Functions.GPT_functions()
```

adding a function to the function calling object:
```python
@functions.defineFunction("<description of your function>",
{
    "type":"string",
    "name":"<name of the parameter>",
    "description":"<description of the parameter>"
},...
)
def yourFunction(parameter1,...):
  return "<return value>"
```

binding the function calling object to a chatbot:
```python
chatbot.setGptFunctions(functions)
```

## chatting with the bot:
```python
output = chatbot.chat("<prompt>")
```

## generating output without prompt:
```python
output = chatbot.generate()
```
