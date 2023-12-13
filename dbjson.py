import os 
import json

class DBJson:

    def __init__(self, path ='posts.json'):
        self.path = path
        self.data = {}
    
    def _load(self):
        if os.path.exists(self.path):
            try:
                with open(self.path, 'r') as f:
                    self.data = json.load(f)
            except FileNotFoundError:
                raise FileNotFoundError('File not found')
    
    def _save(self):
        try:
            with open(self.path, 'w') as f:
                json.dump(self.data, f, indent=4)
        except FileNotFoundError:
            raise FileNotFoundError('File not found')

    def get_all(self):
        self._load()
        return self.data

    def get_by_id(self, id: str):
        self._load()
        for post in self.data:
            if post['id'] == id:
                return post
            
    def create(self, post):
        try:
            self._load()
            self.data.append(post)
            self._save()
            return post
        except Exception:
            raise Exception('Error creating post')

    def update_post(self, id, post):
        try:
            self._load()
            for index, post in enumerate(self.data):
                if post['id'] == id:
                    self.data[index] = post
                    self._save()
                    return {"message": "Post updated successfully"}
        except Exception:
            raise Exception('Error updating post')

    def delete_post(self, id):
        try:
            self._load()
            for index, post in enumerate(self.data):
                if post['id'] == id:
                    self.data.pop(index)
                    self._save()
                    return {"message": "Post deleted successfully"}
        except Exception:
            raise Exception('Error deleting post')
