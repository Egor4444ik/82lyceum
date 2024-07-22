from django.contrib import admin
from .models import Score

@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ['user', 'result1', 'result2', 'result3', 'result4', 'result5'
                    , 'result6', 'result7', 'result8', 'result9', 'result10', 'result11']
    raw_id_fields = ['user']
