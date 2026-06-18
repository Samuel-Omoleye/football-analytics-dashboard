from app_core import Team, Match, TeamNotFoundError
class SportsAPIClient: def init (self):
self._database_registry = {
'arsenal': Team('Arsenal", ['Founded in 1886.'], 'W-W-D-W-L'),
'chelsea': Team('Chelsea', ['Established in 1905.'], 'L-D-W-W-D')
def get team_data(self, requested team: str) -> Team:
lookup_key= requested_team.strip.lower() if lookup_key not in self._database_registry:
raise TeamNotFoundError(fClub (requested_team) unlisted.)
return self._database_registry[lookup_key]