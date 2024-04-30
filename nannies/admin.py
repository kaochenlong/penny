from django.contrib import admin
from .models import Nanny


class NannyAdmin(admin.ModelAdmin):
    list_display = "name", "gender", "tel"
    list_filter = ("gender",)
    fields = ("name", "gender"), "nickname", "tel", "description"
    readonly_fields = ("nickname",)


# Register your models here.
admin.site.register(Nanny, NannyAdmin)
