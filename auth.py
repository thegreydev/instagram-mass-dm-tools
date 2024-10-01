from instagrapi import Client
import os

# Instagram credentials (replace with your credentials)
USERNAME = 'your_instagram_username'
PASSWORD = 'your_instagram_password'

# Create a client instance
client = Client()

# Login and save session
def login_and_save_session():
    # Check if session exists
    session_file = 'instagram_session.json'
    if os.path.exists(session_file):
        # Load session if it exists
        client.load_settings(session_file)
    else:
        # Login to Instagram
        client.login(USERNAME, PASSWORD)
        # Save session
        client.dump_settings(session_file)
        print("Logged in and session saved.")

login_and_save_session()
