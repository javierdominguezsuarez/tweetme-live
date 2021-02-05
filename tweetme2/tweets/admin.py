from account.models import Profile
from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from .models import Tweet
# Register your models here.
class TweetAdmin (admin.ModelAdmin):
    list_display = ['content','user']
    search_fields = ['content','user__username','user__email']
    class Meta:
        model = Tweet
admin.site.site_header = "TweetTea"
#Add table to admin view (modifie-add-delete objects)
admin.site.register(Tweet,TweetAdmin)