from django.contrib import admin

# Register your models here.
from .models import Join

class JoinAdmin(admin.ModelAdmin):
    class Meta:
        model = Join


admin.site.register(Join, JoinAdmin)
