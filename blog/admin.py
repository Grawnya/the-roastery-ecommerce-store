from django.contrib import admin
from .models import *

# Register your models here.

class OurStoryAdmin(admin.ModelAdmin):
    list_display = (
        'date_occurred',
        'event'
    )

    ordering = ('event_id',)

admin.site.register(OurStory, OurStoryAdmin)