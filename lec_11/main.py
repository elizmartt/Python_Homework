import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def fetch_filtered_posts():
    response = requests.get(f"{BASE_URL}/posts")
    if response.status_code == 200:
        data = response.json()
        filtered_posts = [
            post for post in data
            if len(post['title'].split()) <= 6 and post['body'].count('\n') <= 3
        ]
        print("Filtered Posts (GET request):")
        for post in filtered_posts:
            print(f"ID: {post['id']}, Title: {post['title']}")
        return filtered_posts
    else:
        print(f"Failed to retrieve posts.")
        return []

def create_new_post():
    payload = {
        "title": "uvnsivmew grbi svnego nsiegv wangfi naigw ngwai9o",
        "body": "Trying to add i hope it will work",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    if response.status_code == 201:
        created_post = response.json()
        print("New Post Created:", created_post)
        return created_post
    else:
        print(f"Failed to create post. Status code: {response.status_code}")
        return None



def delete_existing_post(post_id):
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    if response.status_code == 200:
        print(f"Post with ID {post_id} successfully deleted.")
        return True
    else:
        print(f"Failed to delete post")
        return False




print("\nCreate a New Post ")
created_post = create_new_post()
print("\nFilter Posts ")
filtered_posts = fetch_filtered_posts()
print("\n--- Delete the Post ---")
if created_post:
    delete_existing_post(created_post['id'])
