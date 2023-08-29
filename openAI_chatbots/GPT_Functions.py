import json
class GPT_functions(object):
    functions = []
    _functionRefs = {}
    def __init__(self):
        pass
    def defineFunction(self,description,*args):
        def real_decorator(original_function):
            argParams = {}
            requiredArgs = []
            
            argNames = []
            for i in args:
                name = i["name"]
                argNames.append(name)
                requiredArgs.append(name)
                argParams[name] = {
                    "type":i["type"],
                    "description":i["description"]
                }
            self._functionRefs[original_function.__name__] = {
                "function":original_function,
                "parameternames":argNames,
                "prepend":None
            }
            data = {
    "name": original_function.__name__,
    "description": description,
    "parameters": {
        "type": "object",
        "properties": argParams,
        "required": requiredArgs
    },
}
            
            self.functions.append(data)
            return original_function
        return real_decorator
    def CallFunction(self,response_message):
        function_name = response_message["function_call"]["name"]
        fuction_data = self._functionRefs[function_name]
        fuction_to_call = fuction_data["function"]
        function_args = json.loads(response_message["function_call"]["arguments"])
        prepend = fuction_data["prepend"]
        args = []
        if prepend:
            args = [prepend]
        for i in fuction_data["parameternames"]:
            args.append(function_args.get(i))
        return fuction_to_call(
            *args
        )
    def merge(self,other):
        self.functions += other.functions
        self._functionRefs = {**self._functionRefs,**other._functionRefs}
    def setPrepend(self,val):
        for key in self._functionRefs:
            self._functionRefs[key]["prepend"] = val
