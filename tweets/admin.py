from django.contrib import admin

from .models import Tweet

# Register your models here.



class TweetModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Tweet


admin.site.register(Tweet, TweetModelAdmin)
