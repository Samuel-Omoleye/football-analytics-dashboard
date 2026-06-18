

# ==============================================================================
# STEP 1: SETUP FILE TRACKING (Samuel Omoleye)
# Makes sure the files we need exist on the laptop before the app runs
# ==============================================================================


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

##OOP: Using classes to hold related info together to avoid parsing random variables

class Team:
    def __init__(self, name: str, trivia: list, recent_form: str):
        self.name = name                 
        self.trivia = trivia             
        self.recent_form = recent_form   

class Match:
    def __init__(self, home_team: str, away_team: str, date: str, score: str = None):
        self.home_team = home_team       
        self.away_team = away_team       
        self.date = date                 
        self.score = score               
