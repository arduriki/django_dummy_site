from datetime import date
from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Jordi",
        "date": date(2024, 5, 18),
        "title": "Mountain Hiking",
        "excerpt": "Lorem ipsum dolor sit amet, consectetur adipisicing elit.",
        "content": """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquam animi aspernatur assumenda, dignissimos ex
            facere fugiat fugit ipsum iure nam nesciunt non omnis provident quaerat recusandae sapiente sed voluptate
            voluptatibus!
            """
    }
]


def get_date(post):
    return post['date']


# Create your views here.
def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    # next element that matches a condition
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
