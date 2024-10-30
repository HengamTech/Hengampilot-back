from django.contrib import admin
from .models import FeatureRequest

# Register your models here.


class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ["user", "status", "description"]
    list_filter = [
        "status",
    ]
    search_fields = [
        "user",
    ]


admin.site.register(FeatureRequest, FeatureRequestAdmin)
