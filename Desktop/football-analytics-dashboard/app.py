
# ------------------------------------------------------------------------------
# BACKEND COUPLING & IMPORTS (Samuel Omoleye)
# Importing all the code engines my teammates built in app_core.py
# ------------------------------------------------------------------------------

import streamlit as st

# Linking the files together
from app_core import (
    initialize_project_environment,
    MatchDataEngine,
    PredictiveModelEngine,
    StorageOperationsManager
)

# Run the file check right away
initialize_project_environment()

# Turn on the engines so Lois can connect them to the buttons
data_engine = MatchDataEngine()
prediction_engine = PredictiveModelEngine()
storage_manager = StorageOperationsManager()