from django.contrib import admin

# Register your models here.

from missingchild.models import MissingPersonModel,RecordModel,UserModel

admin.site.register(MissingPersonModel)
admin.site.register(RecordModel)
admin.site.register(UserModel)