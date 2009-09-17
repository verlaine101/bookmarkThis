from django.contrib import admin
from bookmarkThis.bookmarkEntry.models import bookmarkEntry,vote,verdict

class bookmarkEntryAdmin(admin.ModelAdmin):
    pass
admin.site.register(bookmarkEntry, bookmarkEntryAdmin)

class verdictAdmin(admin.ModelAdmin):
    pass
admin.site.register(verdict, verdictAdmin)

class voteAdmin(admin.ModelAdmin):
    pass
admin.site.register(vote, voteAdmin)
