from django.contrib import admin
from .models import Note
from .models import Assignment, Submission
from .models import LiveClass

admin.site.register(Note)
admin.site.register(Assignment)
admin.site.register(Submission)
admin.site.register(LiveClass)

