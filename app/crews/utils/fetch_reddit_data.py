import os
import praw

def fetch_reddit_data(research_goal: str) -> list:
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT")
    )
    search_results = reddit.subreddit("all").search(research_goal, limit=20, sort="relevance")
    user_data = []

    for submission in search_results:
        author = submission.author
        if author and author.name not in [user["Username"] for user in user_data]:
            try:
                user = reddit.redditor(author.name)
                user_info = {
                    "Username": user.name,
                    "Profile URL": f"https://reddit.com/user/{user.name}",
                    "Link Karma": user.link_karma,
                    "Comment Karma": user.comment_karma
                }
                user_data.append(user_info)
                if len(user_data) >= 5:
                    break
            except Exception as e:
                print(f"Error with user {author.name}: {e}")

    return user_data
