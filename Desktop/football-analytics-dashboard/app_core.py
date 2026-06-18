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


