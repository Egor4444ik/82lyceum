from django.db import models
from django.conf import settings

class Score(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE, primary_key = True)
    result1 = models.IntegerField(blank = True, null = True)
    result2 = models.IntegerField(blank = True, null = True)
    result3 = models.IntegerField(blank = True, null = True)
    result4 = models.IntegerField(blank = True, null = True)
    result5 = models.IntegerField(blank = True, null = True)
    result6 = models.IntegerField(blank = True, null = True)
    result7 = models.IntegerField(blank = True, null = True)
    result8 = models.IntegerField(blank = True, null = True)
    result9 = models.IntegerField(blank = True, null = True)
    result10 = models.IntegerField(blank = True, null = True)
    result11 = models.IntegerField(blank = True, null = True)

    def __str__(self):
        return f'Успехи ученика {self.user.username}'