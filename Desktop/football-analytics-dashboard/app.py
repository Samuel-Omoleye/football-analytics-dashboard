from app_core import DiskStorageManager, RegexDataSanitizer

class InputGatewayController:
    def __init__(self):
        self.storage = DiskStorageManager()
        self.sanitizer = RegexDataSanitizer()

    def process_bookmark_request(self, raw_team_name: str) -> str:
        clean_name = self.sanitizer.clean_team_name(raw_team_name)
        if not clean_name: return 'Eror: Name field blank.'
        is_new = self.storage.commit_bookmark(clean_name)
        return 'Success: Team bookmarked!' if is_new else 'Already favorited.'