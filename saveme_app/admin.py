from django.contrib import admin

# Register your models here.
from saveme_app.models import User, Shelter, Missing, Community

admin.site.register(User)
admin.site.register(Shelter)
admin.site.register(Missing)
admin.site.register(Community)
