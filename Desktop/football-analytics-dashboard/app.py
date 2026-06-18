# ==============================================================================
#  MODULE - STREAMLIT USER INTERFACE (DASHBOARD APP) (app.py)
# ==============================================================================

# # STEP 9: BACKEND COUPLING & IMPORTS (Samuel Omoleye)
# # Importing all the code engines my teammates built in app_core.py
# ==============================================================================

import streamlit as st
import app_core

# 1. Make sure the backend setup runs first so files and storage are ready
app_core.initialize_project_environment()

# 2. Create backend objects that the UI will use when buttons are clicked
api_client = app_core.SportsAPIClient()
analyzer = app_core.MatchAnalyzer()
gateway = app_core.InputGatewayController()
storage_manager = app_core.DiskStorageManager()

# ==============================================================================
# STEP 10: BUILDING THE STREAMLIT FRONT-END DASHBOARD (Lois Binkat)
# This is the part that creates everything the user actually sees — buttons,
# text boxes, layouts, and displays. It connects the backend logic to a simple
# interactive UI so users can play around with the system.
# ==============================================================================

# 3. Basic page setup and welcome text
st.set_page_config(page_title="Football Analytics Dashboard", layout="centered")
st.title("⚽ Football Analytics & Match Prediction Dashboard")
st.subheader("Senior Software Engineering Capstone Companion Workspace")
st.write("Welcome to your offline football companion app! Search clubs, manage bookmarks, and view form predictions.")

st.markdown("---")

# 4. SEARCH SECTION FOR CLUB INFO
st.header("🔍 Club Performance Lookup")
user_search = st.text_input("Enter Football Club Name (e.g., Arsenal, Chelsea):", "")

if user_search:
    try:
        # Sends the user input to the backend to fetch team data
        team_data = api_client.get_team_data(user_search)
        
        # Show basic team info on screen in a clean way
        st.success(f"Club Match Located: **{team_data.name}**")
        st.info(f"📋 **Historic Club Trivia:** {team_data.trivia[0]}")
        st.warning(f"📈 **Recent Matches Form Signature:** {team_data.recent_form}")
        
        # Button to save the team to bookmarks
        if st.button(f"📌 Pin {team_data.name} to Bookmarks"):
            gateway_response = gateway.process_bookmark_request(user_search)
            st.toast(gateway_response)
            
    except app_core.TeamNotFoundError as e:
        # If something goes wrong or team isn't found, show this message instead of crashing
        st.error(f"Search Failure: Could not locate profile data. Details: {e}")

st.markdown("---")
