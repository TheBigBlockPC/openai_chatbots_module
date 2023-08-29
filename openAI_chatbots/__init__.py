import openai
import json
import openAI_chatbots.GPT_Functions as GPT_Functions
print("openai chatbots v1.0")
_apiKeySet = False
def setApiKey(key):
    global _apiKeySet
    _apiKeySet = True
    openai.api_key = key
class chatbot:
    msgLog = []
    prefix = ""
    _gptFunctionsObject : GPT_Functions.GPT_functions = None
    def __init__(self,system_prompt = None,prefix = "",generate=False):
        if not _apiKeySet:
            raise Exception("Openai key not set")
        if system_prompt:
            self.msgLog.append({"role": "system", "content":system_prompt})
    def addMsg(self,role,content): 
        self.msgLog.append({"role": role, "content":content})
    def chat(self,content):
        if self.prefix == "":
            self.addMsg("user",f"{content}")
        else:
            self.addMsg("user",f"{self.prefix}:{content}")
        return self.generate()
    def generate(self):
        GPT_Model = "gpt-3.5-turbo"#"gpt-3.5-turbo-0613"
        if self._gptFunctionsObject:
            Reapeat = True
            while Reapeat:
                print("generating...")
                response = openai.ChatCompletion.create(
                    model=GPT_Model,
                    messages=self.msgLog,
                    functions=self._gptFunctionsObject.functions,
                    function_call="auto",  # auto is default, but we'll be explicit
                )
                response_message = response["choices"][0]["message"]
                if response_message.get("function_call"):
                    function_name = response_message["function_call"]["name"]
                    function_response = self._gptFunctionsObject.CallFunction(response_message)
                    self.msgLog.append(response_message)  # extend conversation with assistant's reply
                    self.msgLog.append(
                        {
                            "role": "function",
                            "name": function_name,
                            "content": function_response,
                        }
                    )
                else:
                    Reapeat = False
                    return response_message["content"]
        else:
            response = openai.ChatCompletion.create(
                model=GPT_Model,
                messages=self.msgLog
            )
            response_message = response["choices"][0]["message"]
            return response_message["content"]
    def setGptFunctions(self,GPT_Functions_Object):
        self._gptFunctionsObject = GPT_Functions_Object
