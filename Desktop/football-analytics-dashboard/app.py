

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

