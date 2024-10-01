from instagrapi.exceptions import UserNotFound

def send_bulk_message(usernames, message):
    for username in usernames:
        try:
            user_id = client.user_id_from_username(username)
            client.direct_send(message, [user_id])
            print(f"Message sent to {username}")
        except UserNotFound:
            print(f"User {username} not found.")
        except Exception as e:
            print(f"Failed to send message to {username}: {str(e)}")

# Example list of Instagram usernames
usernames = ['user1', 'user2', 'user3']  # Replace with actual usernames

# The message to send
message = "Hello from Python script!"

# Send messages
send_bulk_message(usernames, message)
