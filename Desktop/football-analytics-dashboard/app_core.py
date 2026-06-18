# # ==============================================================================
# # STEP 1: SETUP FILE TRACKING (Samuel Omoleye)
# # Makes sure the files we need exist on the laptop before the app runs
# # ==============================================================================







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

