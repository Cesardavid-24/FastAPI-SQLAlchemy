import os 
import json

class DBJson(path = 'db.json'):
    def __init__(self, path):
        self.path = path
        self.data = {}
        self.load()
    
    def _load(self):
        if os.path.exists(self.path):
            with open(self.path, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = {}
        
    def get_all(self):
        return self.data.dict()


    
