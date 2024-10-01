def scrape_followers(username):
    user_id = client.user_id_from_username(username)
    followers = client.user_followers(user_id)
    
    # Save to a file
    with open("followers.txt", "w") as f:
        for follower_id, follower_info in followers.items():
            f.write(f"{follower_info.username}\n")
    
    print(f"Followers of {username} saved to followers.txt.")

# Example usage
scrape_followers('target_username')  # Replace with the target username
