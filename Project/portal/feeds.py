from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.utils.feedgenerator import Atom1Feed
from .models import rssfeed

class ArchiveFeed(Feed):
    feed_type = Atom1Feed
    title = 'Archive Feed'
    description = 'Archive Feed'
    link = '/archive/'
    
    def items(self):
        return rssfeed.objects.all().order_by('-date')
    
    def item_title(self,item):
        s = str(item.title)+' --- '+item.date.strftime('%A, %B %d, %Y %H:%M:%S' )
        #print(s)
        return s
    
    def item_description(self,item):
        return item.msg
    
    def item_link(self,item):
        return '/archive/'