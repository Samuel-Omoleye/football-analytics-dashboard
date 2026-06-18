from app_core import DiskStorageManager, RegexDataSanitizer


class InputGatewayController:
    def __init__(self):
        self.storage = DiskStorageManager()
        self.sanitizer = RegexDataSanitizer()

    def process_bookmark_request(self, raw_team_name: str) -> str:
        clean_name = self.sanitizer.clean_team_name(raw_team_name)

        if not clean_name: 
            return 'Error: Name field blank.'
        
        is_new = self.storage.commit_bookmark(clean_name)

        if is_new:
            return 'Success: Team bookmarked!'
        else:
            return 'Already favorited.'
    
    def process_diary_note_request(
        self,
        home: str, 
        away: str, 
        date: str, 
        raw_note: str
    ) -> str:
        
        if not raw_note or not raw_note.strip(): 
            return 'Rejected: Notes field empty'
        
        key = f'{home.strip().lower()}_{away.stri().lower()}_{date}'.replace(' ','_')

        self.storage.commit_match_note(key, raw_note)

        return 'Success: Commentary committed to system disk storage files!'