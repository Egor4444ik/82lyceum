from django.contrib import admin
from .models import Score

@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ['user',

                    # 1 year
                    'result_1_year_items', 'result_1_year_project_skills', 'result_1_year_construction', 'result_1_year_olympics', 'result_1_year_scince_and_practical_results'
                    , 'result_1_year_engineer_competition_results', 'result_1_year_engineer_scince_week', 'result_1_year_creative', 'result_1_year_reflex', 'result_1_year_FG',

                    # 2 year
                    'result_2_year_items', 'result_2_year_project_skills', 'result_2_year_construction', 'result_2_year_olympics', 'result_2_year_scince_and_practical_results'
                    , 'result_2_year_engineer_competition_results', 'result_2_year_engineer_scince_week', 'result_2_year_creative', 'result_2_year_reflex', 'result_2_year_FG',

                    # 3 year
                    'result_3_year_items', 'result_3_year_project_skills', 'result_3_year_construction', 'result_3_year_olympics', 'result_3_year_scince_and_practical_results',
                    'result_3_year_engineer_competition_results', 'result_3_year_engineer_scince_week', 'result_3_year_creative', 'result_3_year_reflex', 'result_3_year_FG',

                    # 4 year
                    'result_4_year_items', 'result_4_year_project_skills', 'result_4_year_construction', 'result_4_year_olympics', 'result_4_year_scince_and_practical_results',
                    'result_4_year_engineer_competition_results', 'result_4_year_engineer_scince_week', 'result_4_year_creative', 'result_4_year_reflex', 'result_4_year_FG',

                    # 5 year
                    'result_5_year_items', 'result_5_year_project_skills', 'result_5_year_construction', 'result_5_year_olympics', 'result_5_year_scince_and_practical_results',
                    'result_5_year_engineer_competition_results', 'result_5_year_engineer_scince_week', 'result_5_year_creative', 'result_5_year_reflex', 'result_5_year_FG',

                    # 6 year
                    'result_6_year_items', 'result_6_year_project_skills', 'result_6_year_construction', 'result_6_year_olympics', 'result_6_year_scince_and_practical_results',
                    'result_6_year_engineer_competition_results', 'result_6_year_engineer_scince_week', 'result_6_year_creative', 'result_6_year_reflex', 'result_6_year_FG',

                    # 7 year
                    'result_7_year_items', 'result_7_year_project_skills', 'result_7_year_construction', 'result_7_year_olympics', 'result_7_year_scince_and_practical_results',
                    'result_7_year_engineer_competition_results', 'result_7_year_engineer_scince_week', 'result_7_year_creative', 'result_7_year_reflex', 'result_7_year_FG',

                    # 8 year
                    'result_8_year_items', 'result_8_year_project_skills', 'result_8_year_construction', 'result_8_year_olympics', 'result_8_year_scince_and_practical_results',
                    'result_8_year_engineer_competition_results', 'result_8_year_engineer_scince_week', 'result_8_year_creative', 'result_8_year_reflex', 'result_8_year_FG',

                    # 9 year
                    'result_9_year_items', 'result_9_year_project_skills', 'result_9_year_construction', 'result_9_year_olympics', 'result_9_year_scince_and_practical_results',
                    'result_9_year_engineer_competition_results', 'result_9_year_engineer_scince_week', 'result_9_year_creative', 'result_9_year_reflex', 'result_9_year_FG']
    raw_id_fields = ['user']
