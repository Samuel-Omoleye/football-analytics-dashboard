# # ==============================================================================
# # STEP 1: SETUP FILE TRACKING (Samuel Omoleye)
# # Makes sure the files we need exist on the laptop before the app runs
# # ==============================================================================

import os
import sys


def initialize_project_environment():
    required_data_assets = ['bookmarks.json', 'notes.json']
    print('[INIT] Checking if local system files exist...')



