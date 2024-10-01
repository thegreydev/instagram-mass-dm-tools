def scrape_following(username):
    user_id = client.user_id_from_username(username)
    following = client.user_following(user_id)
    
    # Save to a file
    with open("following.txt", "w") as f:
        for following_id, following_info in following.items():
            f.write(f"{following_info.username}\n")
    
    print(f"Following of {username} saved to following.txt.")

# Example usage
scrape_following('target_username')  # Replace with the target username
