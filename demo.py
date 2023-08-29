import openAI_chatbots as chat
chat.setApiKey("<your api key>")
chatbot = chat.chatbot()
functions = chat.GPT_Functions.GPT_functions()
@functions.defineFunction("reads a file",{
    "type":"string",
    "name":"Path",
    "description":"the file path"
})
def ReadFile(Path):
    content = ""
    try:
        with open(Path,"r") as f:
            content = f.read()
        return "content:"+content
    except:
        return "error"

@functions.defineFunction("writes to a file",{
    "type":"string",
    "name":"Path",
    "description":"the file path"
},{
    "type":"string",
    "name":"Content",
    "description":"the content of the file"
})
def WriteFile(Path,content):
    try:
        with open(Path,"w") as f:
            f.write(content)
        return "file written to"
    except:
        return "error"
chatbot.setGptFunctions(functions)
Running = True
while Running:
    prompt = input("user: ")
    if prompt == "end":
        Running = False
        print("chat has ended")
    else:
        print("AI: ",chatbot.chat(prompt))
