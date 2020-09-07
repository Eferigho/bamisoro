from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from .models import Post


class LatestPostsFeed(Feed):
    title = 'Recent Post'
    link = reverse_lazy('posts:main-post-view')
    description = 'Recent post by our people'

    def items(self):
        return Post.title[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)
