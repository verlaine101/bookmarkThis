from django.contrib import admin
from bookmarkThis.bookmarkEntry.models import bookmarkEntry

class bookmarkEntryAdmin(admin.ModelAdmin):
    pass
admin.site.register(bookmarkEntry, bookmarkEntryAdmin)

