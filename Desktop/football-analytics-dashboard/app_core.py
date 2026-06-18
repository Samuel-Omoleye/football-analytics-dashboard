# # ==============================================================================
# # STEP 1: SETUP FILE TRACKING (Samuel Omoleye)
# # Makes sure the files we need exist on the laptop before the app runs
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


class MatchAnalyzer:
    def calculate_fun_forecast(self, home_team: Team, away_team: Team) -> str:
        form_weights = {'W': 3, 'D': 1, 'L': 0}

        home_points = sum(form_weights.get(res, 0) for res in home_team.recent_form.split(','))
        away_points = sum(form_weights.get(res, 0) for res in away_team.recent_form.split(','))
        disclaimer = '(Playful estimate only o!)'

        if home_points > away_points:
            return f'Forecast: Advantage {home_team.name}! {disclaimer}'
        return f'Forecast: Close match bound for draw! {disclaimer}'