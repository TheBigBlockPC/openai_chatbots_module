import openAI_chatbots as chat

# Set your OpenAI API key
chat.setApiKey("<your api key>")

# Create a chatbot instance
chatbot = chat.chatbot()

# Create a function calling object
functions = chat.GPT_Functions.GPT_functions()

# Define a function to read a file
@functions.defineFunction("reads a file", {
    "type": "string",
    "name": "Path",
    "description": "the file path"
})
def ReadFile(Path):
    content = ""
    try:
        with open(Path, "r") as f:
            content = f.read()
        return "content:" + content
    except:
        return "error reading file"

# Define a function to write to a file
@functions.defineFunction("writes to a file", {
    "type": "string",
    "name": "Path",
    "description": "the file path"
}, {
    "type": "string",
    "name": "Content",
    "description": "the content of the file"
})
def WriteFile(Path, content):
    try:
        with open(Path, "w") as f:
            f.write(content)
        return "file written successfully"
    except:
        return "error writing file"

# Bind the function calling object to the chatbot
chatbot.setGptFunctions(functions)

# Chat loop
Running = True
while Running:
    prompt = input("You: ")
    if prompt == "end":
        Running = False
        print("Chat has ended")
    else:
        response = chatbot.chat(prompt)
        print("AI:", response)
