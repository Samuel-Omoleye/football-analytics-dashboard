

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


