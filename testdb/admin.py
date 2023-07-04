from django.contrib import admin
from .models import Post, Focal, Report, Paper, stations

admin.site.register(Post)
admin.site.register(Focal)
admin.site.register(Report)
admin.site.register(Paper)
admin.site.register(stations)