# # ==============================================================================
# # STEP 1: SETUP FILE TRACKING (Samuel Omoleye)
# # Makes sure the files we need exist on the laptop before the app runs
# i.e. This just makes sure the important files the app depends on are already there.
# # If they’re missing, it creates them so everything doesn’t break later.
# # ==============================================================================

import os
import sys


def initialize_project_environment():
    required_data_assets = ['bookmarks.json', 'notes.json']
    print('[INIT] Checking if local system files exist...')

    for asset in required_data_assets:
        if not os.path.exists(asset):
            print(
                f'[WARN] {asset} missing! Creating default blank storage file now...')
            with open(asset, 'w', encoding='utf-8') as file_handle:
                file_handle.write('[]' if 'bookmarks' in asset else '{}')
        else:
            print(f'[OK] Validated tracking file asset signature: {asset}')




# ------------------------------------------------------------------------------
# STEP 2: SIMPLE DATA CLASSES (OOP BASICS) (Samuel Omoleye)
# These classes just bundle related info together so we don’t keep passing
# random variables everywhere in the program.
# ------------------------------------------------------------------------------
class Team:
    def __init__(self, name: str, trivia: list, recent_form: str):
        self.name = name                         # Team name
        self.trivia = trivia                     # Fun facts about the team
        self.recent_form = recent_form           # Recent match results

class Match:
    def __init__(self, home_team: str, away_team: str, date: str, score: str = None):
        self.home_team = home_team               # Home team name
        self.away_team = away_team               # Away team name
        self.date = date                         # Match date
        self.score = score                       # Match score (can be empty at first)


# ------------------------------------------------------------------------------
# STEP 3: ERROR HANDLING (SO APP DOESN'T CRASH) (Leonard Onwuzurike)
# This part just makes sure wrong searches or missing data don’t crash everything.
# Instead, we catch the errors and respond nicely.
# ------------------------------------------------------------------------------
class TeamNotFoundError(Exception): pass
class MissingFixtureError(Exception): pass

def safe_database_lookup(mock_database, user_query):
    try:
        normalized_query = user_query.strip().lower()
        if normalized_query not in mock_database:
            raise TeamNotFoundError(f'Target key {user_query} absent.')
        return mock_database[normalized_query]
    except TeamNotFoundError as e:
        return f'Intercepted Error: {e}'



# ------------------------------------------------------------------------------
# STEP 4: CLEANING USER INPUT (REGEX STUFF) (Usman Abdullahi)
# This part cleans messy user input and helps extract numbers like scores
# from strings using pattern matching.
# ------------------------------------------------------------------------------
import re

class RegexDataSanitizer:
    @staticmethod
    def clean_team_name(raw_name: str) -> str:
        # Turns multiple spaces/tabs into just one space so names stay clean
        clean_spaces = re.sub(r'\s+', ' ', raw_name)
        return clean_spaces.strip().lower()

    @staticmethod
    def parse_scoreline(score_string: str) -> tuple:
        pattern = r'^(\d+)-(\d+)$'
        match = re.match(pattern, score_string.strip())
        if match:
            # Converts score text into actual numbers we can work with
            return int(match.group(1)), int(match.group(2))
        return (0, 0)


# ------------------------------------------------------------------------------
# STEP 5: SAVING DATA TO FILES (JSON STORAGE) (Ibrahim Aminu)
# This handles saving and loading data so things like bookmarks don’t disappear
# when the app closes.
# ------------------------------------------------------------------------------

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

    def save_bookmark(self, team_name: str) -> bool:
        current = self.load_bookmarks()
        if team_name not in current:
            current.append(team_name)
            with open(self.bookmarks_path, 'w', encoding='utf-8') as f:
                json.dump(current, f, indent=4)
            return True # means we actually saved a new bookmark
        return False # means it was already saved before


# ------------------------------------------------------------------------------
# STEP 6: FAKE SPORTS API (JUST SAMPLE DATA) (Joy Ashoko)
# Since there’s no real API here, we just simulate one using hardcoded team data.
# ------------------------------------------------------------------------------
class SportsAPIClient:
    def __init__(self):
        # This is just sample team data we’re using for testing
        self._database_registry = {
            'arsenal': Team('Arsenal', ['Founded in 1886.'], 'W-W-D-W-L'),
            'chelsea': Team('Chelsea', ['Established in 1905.'], 'L-D-W-W-D'),
            'liverpool': Team('Liverpool', ['Established in 1892.'], 'W-D-W-W-D'),
            'wolves': Team('Wolves', ['Established in 1877.'], 'D-L-W-D-D')
        }

    def get_team_data(self, requested_team: str) -> Team:
        lookup_key = requested_team.strip().lower()
        if lookup_key not in self._database_registry:
            raise TeamNotFoundError(f'Club {requested_team} unlisted.')
        return self._database_registry[lookup_key]


# ------------------------------------------------------------------------------
# STEP 7: MATCH PREDICTION LOGIC (SIMPLE FUN ANALYSIS) (David Umoh)
# This checks recent form and assigns points just to guess which team looks stronger.
# It’s not serious stats, just a fun prediction system.
# ------------------------------------------------------------------------------
class MatchAnalyzer:
    def calculate_fun_forecast(self, home_team: Team,away_team: Team) -> str:
        form_weights = {'W': 3, 'D': 1, 'L': 0}
          
        # Breaks the form string and adds up points for each result
        home_points = sum(form_weights.get(res, 0) for res in home_team.recent_form.split('-'))
        away_points = sum(form_weights.get(res, 0) for res in away_team.recent_form.split('-'))
        disclaimer = '(Playful estimate only o!)'
        summary_lose = f'Solid Performance from {home_team.name} but an unfortunate outcome' 
        summary_win = f'{home_team.name} gets the job done and brings it home'
          
        if home_points > away_points:
            return f'{home_team.name} 2-0 {away_team.name}\n\n{summary_win} {disclaimer}'
        elif home_points < away_points:
            return f'{home_team.name} 1-2 {away_team.name}\n\n{summary_lose}{disclaimer}'
        else:
            return f'Forecast: Close match bound for draw! {disclaimer}'



        # if home_points > away_points:
        #     return f'Forecast: Advantage {home_team.name}! {disclaimer}'
        # return f'Forecast: Close match bound for draw! {disclaimer}'


# ------------------------------------------------------------------------------
# STEP 8: INPUT CONTROLLER (CONNECTS EVERYTHING) (Lois Binkat)
# This is basically the middle layer that takes user input, cleans it,
# then sends it to storage or other parts of the system.
# ------------------------------------------------------------------------------
class InputGatewayController:
    def __init__(self):
        self.storage = DiskStorageManager()
        self.sanitizer = RegexDataSanitizer()

    def process_bookmark_request(self, raw_team_name: str) -> str:
        clean_name = self.sanitizer.clean_team_name(raw_team_name)
        if not clean_name:
            return 'Error: Team field cannot be blank.'
          
        # Sends cleaned name to storage and checks if it already exists
        is_new = self.storage.save_bookmark(clean_name)
        return 'Success: Added!' if is_new else 'Notice: Already pinned.'