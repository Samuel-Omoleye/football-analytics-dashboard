import json

class DiskStorageManager:
    def __init__(self, bookmarks_path='bookmarks.json'):
        self.bookmarks_path = bookmarks_path
        
    def load_bookmarks(self) -> list:
        try:
            with open(self.bookmarks_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return []

    def save_bookmark(self, team_name: str):
        current = self.load_bookmarks()
        if team_name not in current:
            current.append(team_name)
            with open(self.bookmarks_path, 'w', encoding='utf-8') as f:
                json.dump(current, f, indent=4)
