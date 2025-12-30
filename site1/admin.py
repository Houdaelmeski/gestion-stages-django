from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Stage)
admin.site.register(Stagiaire)
admin.site.register(Encadrent)
admin.site.register(Document)
#admin.site.register(document)