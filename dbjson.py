import os 
import json , asyncio

class DBJson:

    def __init__(self, path = './posts.json'):
        self.path = path
        self.data = {}
    
    async def _load(self):
        if os.path.exists(self.path):
            try:
                with open(self.path, 'r') as f:
                    self.data = await asyncio.to_thread(json.load, f)
            except FileNotFoundError:
                raise FileNotFoundError('File not found')

    async def get_all(self):
        return await self.data.dict()


    
