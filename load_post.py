from main.models import Post

posts = Post.query.all()

for post in posts:
    print(post)

posts = Post.query.paginate()
dir(posts)

posts.per_page
posts.page

for post in posts.items:
    print(post)