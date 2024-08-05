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


def main():

    authenticate_user()

    if st.session_state.authenticated:
        start_app()


def authenticate_user():

    # Create OAuth2Component instance
    oauth2 = OAuth2Component(CLIENT_ID, CLIENT_SECRET, AUTHORIZE_URL, TOKEN_URL, REFRESH_TOKEN_URL, REVOKE_TOKEN_URL)

    # Check if token exists in session state
    if 'token' not in st.session_state:

        introduction = st.empty()

        with introduction:
            st.header("⚠️ Please authenticate by clicking on button bellow !")

        # If not, show authorize button
        result = oauth2.authorize_button("Log in", REDIRECT_URI, SCOPE)
        if result and 'token' in result:
            # If authorization successful, save token in session state
            st.session_state.token = result.get('token')
            st.session_state.authenticated = True
            introduction.empty()
            st.rerun()
        else:
            st.session_state.authenticated = False
            
    else:
        st.session_state.token = oauth2.refresh_token(st.session_state.token)

        if "token" not in st.session_state or not isinstance(st.session_state.token,OAuth2Token):
            st.header("Something went wrong...")


def start_app():

    st.title("🎉 You have sucessfuly logged in to Streamlit app !")
    st.header("Your session is running.")

    st.text("Your access token:")
    st.json(st.session_state.token)


#Main function call for chat_app
if __name__ == "__main__":
    main()