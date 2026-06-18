import re

class RegexDataSanitizer:
    @staticmethod
    def clean_team_name(raw_name: str) -> str:
        collapsed_spaces: str = re.sub(r'\s+', ' ', raw_name )
        return collapsed_spaces.strip().lower()

    @staticmethod
    def parse_scoreline(score_string: str) -> tuple[int,int]:
        pattern = r'^(\d+)-(\d+)$'
        match = re.match(pattern, score_string.strip())
        if match:
            return int(match.group(1)), int(match.group(2))
        return (0, 0)

