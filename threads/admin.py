from django.contrib import admin
from threads.models import Thread, Post, Like

admin.site.register(Thread)
admin.site.register(Post)
admin.site.register(Like)
