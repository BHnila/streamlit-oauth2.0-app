import streamlit as st
from streamlit_oauth import OAuth2Component
from httpx_oauth.oauth2 import OAuth2Token
import os

# Set environment variables
AUTHORIZE_URL = os.getenv('AUTHORIZE_URL')
TOKEN_URL = os.getenv('TOKEN_URL')
REFRESH_TOKEN_URL = os.getenv('REFRESH_TOKEN_URL')
REVOKE_TOKEN_URL = os.getenv('REVOKE_TOKEN_URL')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')
SCOPE = os.getenv('SCOPE')


# Main function for Streamlit app:
def main():

    # Authenticate user and maintain authentication state during session 
    authenticate_user()

    # Start Streamlit app if user is authenticated
    if st.session_state.authenticated:
        start_app()


# Function that uses OAuth 2.0 protocol to authenticate user
def authenticate_user():

    # Create OAuth2Component instance
    oauth2 = OAuth2Component(CLIENT_ID, CLIENT_SECRET, AUTHORIZE_URL, TOKEN_URL, REFRESH_TOKEN_URL, REVOKE_TOKEN_URL)

    # Check if token exists in session state
    if 'token' not in st.session_state:

        # Create a container to display login instructions
        introduction = st.empty()

        with introduction:
            st.header("⚠️ Please authenticate by clicking on button bellow !")

        # If token doesnt exist in session state, show authorize button
        result = oauth2.authorize_button("Log in", REDIRECT_URI, SCOPE)

        if result and 'token' in result:

            # If authentication successful, save token in session state
            st.session_state.token = result.get('token')
            st.session_state.authenticated = True

            # Remove login instructions and rerun application
            introduction.empty()
            st.rerun()

        else:
            st.session_state.authenticated = False
            
    else:
        # If access token is present in session state, check if it is valid
        # If token expired or if it is invalid, refresh token
        st.session_state.token = oauth2.refresh_token(st.session_state.token)

        # If token refresh fail, inform user
        if "token" not in st.session_state or not isinstance(st.session_state.token,OAuth2Token):
            st.header("Something went wrong...")


# App content that requires user to be authenticated
def start_app():

    st.title("🎉 You have sucessfuly logged in to Streamlit app !")
    st.header("Your session is running.")

    st.text("Your access token:")
    st.json(st.session_state.token)


# Main function call for chat_app
if __name__ == "__main__":
    main()