# instagram-mass-dm-tools
a tool that automatically sends bulk message to a list of instagram users and performs other functions like auto comment, mass liking, e.t.c

developer: https://t.me/pysmart

# How the Code Works:
- Login and Save Session: The login credentials are passed to instagrapi.Client. If a session exists, it loads the session from a file to avoid re-logging in. Otherwise, it logs in and saves the session.

developer: https://t.me/pysmart

- Bulk Messaging: The script sends a direct message to a list of users by their usernames. It uses client.direct_send() to send the message to each user’s ID.

- Scraping Followers and Following: The script fetches the followers or following of a given username, stores the usernames in a dictionary, and writes them to a text file (followers.txt or following.txt)

developer: https://t.me/pysmart

# Key Points:
- Rate Limits: Instagram has rate limits, and you should ensure that you're not exceeding them, especially for actions like messaging or scraping data.
- Account Security: Automating actions like bulk messaging and scraping could result in temporary account restrictions or bans if Instagram detects unusual activity.
- Session Handling: The script saves the session to avoid logging in multiple times, making future interactions faster and less risky (as repeated logins could trigger security checks).

developer: https://t.me/pysmart

an automated tool for sending bulk messages to instagram users
