from langchain_community.llms import ollama


class Agency:
    def __init__(self) -> None:
        self.agents = []
        self.tasks = []
        self.results = None
        
    def add_agent(self):
        pass
    
    def add_task(self):
        pass
    
    def run_tasks(self,task):
        pass
    
    def print_result(self):
        pass

    def save_result(self,file_name="file.txt"):
        pass
    