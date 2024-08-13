from django.db import models
from django.conf import settings

class Score(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE, primary_key = True)
    #results for 1 year
    result_1_year_items = models.IntegerField(blank = True, null = True)
    result_1_year_project_skills = models.IntegerField(blank=True, null=True)
    result_1_year_construction = models.IntegerField(blank=True, null=True)
    result_1_year_olympics = models.IntegerField(blank=True, null=True)
    result_1_year_scince_and_practical_results = models.IntegerField(blank=True, null=True)
    result_1_year_engineer_competition_results = models.IntegerField(blank=True, null=True)
    result_1_year_engineer_scince_week = models.IntegerField(blank=True, null=True)
    result_1_year_creative = models.IntegerField(blank=True, null=True)
    result_1_year_reflex = models.IntegerField(blank=True, null=True)
    result_1_year_FG = models.IntegerField(blank=True, null=True)

    # results for 2 year
    result_2_year_items = models.IntegerField(blank=True, null=True)
    result_2_year_project_skills = models.IntegerField(blank=True, null=True)
    result_2_year_construction = models.IntegerField(blank=True, null=True)
    result_2_year_olympics = models.IntegerField(blank=True, null=True)
    result_2_year_scince_and_practical_results = models.IntegerField(blank=True, null=True)
    result_2_year_engineer_competition_results = models.IntegerField(blank=True, null=True)
    result_2_year_engineer_scince_week = models.IntegerField(blank=True, null=True)
    result_2_year_creative = models.IntegerField(blank=True, null=True)
    result_2_year_reflex = models.IntegerField(blank=True, null=True)
    result_2_year_FG = models.IntegerField(blank=True, null=True)

    # results for 3 year
    result_3_year_items = models.IntegerField(blank=True, null=True)
    result_3_year_project_skills = models.IntegerField(blank=True, null=True)
    result_3_year_construction = models.IntegerField(blank=True, null=True)
    result_3_year_olympics = models.IntegerField(blank=True, null=True)
    result_3_year_scince_and_practical_results = models.IntegerField(blank=True, null=True)
    result_3_year_engineer_competition_results = models.IntegerField(blank=True, null=True)
    result_3_year_engineer_scince_week = models.IntegerField(blank=True, null=True)
    result_3_year_creative = models.IntegerField(blank=True, null=True)
    result_3_year_reflex = models.IntegerField(blank=True, null=True)
    result_3_year_FG = models.IntegerField(blank=True, null=True)

    # results for 4 year
    result_4_year_items = models.IntegerField(blank=True, null=True)
    result_4_year_project_skills = models.IntegerField(blank=True, null=True)
    result_4_year_construction = models.IntegerField(blank=True, null=True)
    result_4_year_olympics = models.IntegerField(blank=True, null=True)
    result_4_year_scince_and_practical_results = models.IntegerField(blank=True, null=True)
    result_4_year_engineer_competition_results = models.IntegerField(blank=True, null=True)
    result_4_year_engineer_scince_week = models.IntegerField(blank=True, null=True)
    result_4_year_creative = models.IntegerField(blank=True, null=True)
    result_4_year_reflex = models.IntegerField(blank=True, null=True)
    result_4_year_FG = models.IntegerField(blank=True, null=True)

    # results for 5 year
    result_5_year_items = models.IntegerField(blank=True, null=True)
    result_5_year_project_skills = models.IntegerField(blank=True, null=True)
    result_5_year_construction = models.IntegerField(blank=True, null=True)
    result_5_year_olympics = models.IntegerField(blank=True, null=True)
    result_5_year_scince_and_practical_results = models.IntegerField(blank=True, null=True)
    result_5_year_engineer_competition_results = models.IntegerField(blank=True, null=True)
    result_5_year_engineer_scince_week = models.IntegerField(blank=True, null=True)
    result_5_year_creative = models.IntegerField(blank=True, null=True)
    result_5_year_reflex = models.IntegerField(blank=True, null=True)
    result_5_year_FG = models.IntegerField(blank=True, null=True)

    # results for 6 year
    result_6_year_items = models.IntegerField(blank=True, null=True)
    result_6_year_project_skills = models.IntegerField(blank=True, null=True)
    result_6_year_construction = models.IntegerField(blank=True, null=True)
    result_6_year_olympics = models.IntegerField(blank=True, null=True)
    result_6_year_scince_and_practical_results = models.IntegerField(blank=True, null=True)
    result_6_year_engineer_competition_results = models.IntegerField(blank=True, null=True)
    result_6_year_engineer_scince_week = models.IntegerField(blank=True, null=True)
    result_6_year_creative = models.IntegerField(blank=True, null=True)
    result_6_year_reflex = models.IntegerField(blank=True, null=True)
    result_6_year_FG = models.IntegerField(blank=True, null=True)

    # results for 7 year
    result_7_year_items = models.IntegerField(blank=True, null=True)
    result_7_year_project_skills = models.IntegerField(blank=True, null=True)
    result_7_year_construction = models.IntegerField(blank=True, null=True)
    result_7_year_olympics = models.IntegerField(blank=True, null=True)
    result_7_year_scince_and_practical_results = models.IntegerField(blank=True, null=True)
    result_7_year_engineer_competition_results = models.IntegerField(blank=True, null=True)
    result_7_year_engineer_scince_week = models.IntegerField(blank=True, null=True)
    result_7_year_creative = models.IntegerField(blank=True, null=True)
    result_7_year_reflex = models.IntegerField(blank=True, null=True)
    result_7_year_FG = models.IntegerField(blank=True, null=True)

    # results for 8 year
    result_8_year_items = models.IntegerField(blank=True, null=True)
    result_8_year_project_skills = models.IntegerField(blank=True, null=True)
    result_8_year_construction = models.IntegerField(blank=True, null=True)
    result_8_year_olympics = models.IntegerField(blank=True, null=True)
    result_8_year_scince_and_practical_results = models.IntegerField(blank=True, null=True)
    result_8_year_engineer_competition_results = models.IntegerField(blank=True, null=True)
    result_8_year_engineer_scince_week = models.IntegerField(blank=True, null=True)
    result_8_year_creative = models.IntegerField(blank=True, null=True)
    result_8_year_reflex = models.IntegerField(blank=True, null=True)
    result_8_year_FG = models.IntegerField(blank=True, null=True)

    # results for 9 year
    result_9_year_items = models.IntegerField(blank=True, null=True)
    result_9_year_project_skills = models.IntegerField(blank=True, null=True)
    result_9_year_construction = models.IntegerField(blank=True, null=True)
    result_9_year_olympics = models.IntegerField(blank=True, null=True)
    result_9_year_scince_and_practical_results = models.IntegerField(blank=True, null=True)
    result_9_year_engineer_competition_results = models.IntegerField(blank=True, null=True)
    result_9_year_engineer_scince_week = models.IntegerField(blank=True, null=True)
    result_9_year_creative = models.IntegerField(blank=True, null=True)
    result_9_year_reflex = models.IntegerField(blank=True, null=True)
    result_9_year_FG = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'Успехи ученика {self.user.username}'