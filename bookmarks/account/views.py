from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm
from django.contrib.auth.decorators import login_required
from .models import Score
from django.contrib import messages
import matplotlib.pyplot as plt
import base64
from io import BytesIO

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Пользователь обновлен ' \
                                      'успешно')
        else:
            messages.error(request, 'Ошибка при обновлении пользователя')
    else:
        user_form = UserEditForm(instance=request.user)
    return render(request,
                  'account/edit.html',
                  {'user_form': user_form})


@login_required
def dashboard(request):
    return render(request,
        'account/dashboard.html',
        {'section': 'dashboard'})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            # Создать новый объект пользователя,
            # но пока не сохранять его
            new_user = user_form.save(commit=False)
            # Установить выбранный пароль
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Сохранить объект User
            new_user.save()
            # Создать успехи пользователя
            Score.objects.create(user=new_user)
            return render(request,
                          'account/template/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/template/register.html',
                  {'user_form': user_form})


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x,y):
    plt.switch_backend('AGG')
    plt.title('График оценок от класса обучения')
    plt.plot(x,y)
    plt.xticks(rotation=45)
    plt.xlabel('Класс обучения')
    plt.ylabel('Оценка когнитивных способностей')
    plt.tight_layout
    graph = get_graph()
    return graph
def student_score(request):
    if request.user.is_authenticated:
        user_data = Score.objects.get(user = request.user)

        try:
            # 1 year
            result_1_year_items = user_data.result_1_year_items
            result_1_year_project_skills = user_data.result_1_year_project_skills
            result_1_year_construction = user_data.result_1_year_construction
            result_1_year_olympics = user_data.result_1_year_olympics
            result_1_year_scince_and_practical_results = user_data.result_1_year_scince_and_practical_results
            result_1_year_engineer_competition_results = user_data.result_1_year_engineer_competition_results
            result_1_year_engineer_scince_week = user_data.result_1_year_engineer_scince_week
            result_1_year_creative = user_data.result_1_year_creative
            result_1_year_reflex = user_data.result_1_year_reflex
            result_1_year_FG = user_data.result_1_year_FG

            # 2 year
            result_2_year_items = user_data.result_2_year_items
            result_2_year_project_skills = user_data.result_2_year_project_skills
            result_2_year_construction = user_data.result_2_year_construction
            result_2_year_olympics = user_data.result_2_year_olympics
            result_2_year_scince_and_practical_results = user_data.result_2_year_scince_and_practical_results
            result_2_year_engineer_competition_results = user_data.result_2_year_engineer_competition_results
            result_2_year_engineer_scince_week = user_data.result_2_year_engineer_scince_week
            result_2_year_creative = user_data.result_2_year_creative
            result_2_year_reflex = user_data.result_2_year_reflex
            result_2_year_FG = user_data.result_2_year_FG

            # 3 year
            result_3_year_items = user_data.result_3_year_items
            result_3_year_project_skills = user_data.result_3_year_project_skills
            result_3_year_construction = user_data.result_3_year_construction
            result_3_year_olympics = user_data.result_3_year_olympics
            result_3_year_scince_and_practical_results = user_data.result_3_year_scince_and_practical_results
            result_3_year_engineer_competition_results = user_data.result_3_year_engineer_competition_results
            result_3_year_engineer_scince_week = user_data.result_3_year_engineer_scince_week
            result_3_year_creative = user_data.result_3_year_creative
            result_3_year_reflex = user_data.result_3_year_reflex
            result_3_year_FG = user_data.result_3_year_FG

            # 4 year
            result_4_year_items = user_data.result_4_year_items
            result_4_year_project_skills = user_data.result_4_year_project_skills
            result_4_year_construction = user_data.result_4_year_construction
            result_4_year_olympics = user_data.result_4_year_olympics
            result_4_year_scince_and_practical_results = user_data.result_4_year_scince_and_practical_results
            result_4_year_engineer_competition_results = user_data.result_4_year_engineer_competition_results
            result_4_year_engineer_scince_week = user_data.result_4_year_engineer_scince_week
            result_4_year_creative = user_data.result_4_year_creative
            result_4_year_reflex = user_data.result_4_year_reflex
            result_4_year_FG = user_data.result_4_year_FG

            # 5 year
            result_5_year_items = user_data.result_5_year_items
            result_5_year_project_skills = user_data.result_5_year_project_skills
            result_5_year_construction = user_data.result_5_year_construction
            result_5_year_olympics = user_data.result_5_year_olympics
            result_5_year_scince_and_practical_results = user_data.result_5_year_scince_and_practical_results
            result_5_year_engineer_competition_results = user_data.result_5_year_engineer_competition_results
            result_5_year_engineer_scince_week = user_data.result_5_year_engineer_scince_week
            result_5_year_creative = user_data.result_5_year_creative
            result_5_year_reflex = user_data.result_5_year_reflex
            result_5_year_FG = user_data.result_5_year_FG

            # 6 year
            result_6_year_items = user_data.result_6_year_items
            result_6_year_project_skills = user_data.result_6_year_project_skills
            result_6_year_construction = user_data.result_6_year_construction
            result_6_year_olympics = user_data.result_6_year_olympics
            result_6_year_scince_and_practical_results = user_data.result_6_year_scince_and_practical_results
            result_6_year_engineer_competition_results = user_data.result_6_year_engineer_competition_results
            result_6_year_engineer_scince_week = user_data.result_6_year_engineer_scince_week
            result_6_year_creative = user_data.result_6_year_creative
            result_6_year_reflex = user_data.result_6_year_reflex
            result_6_year_FG = user_data.result_6_year_FG

            # 7 year
            result_7_year_items = user_data.result_7_year_items
            result_7_year_project_skills = user_data.result_7_year_project_skills
            result_7_year_construction = user_data.result_7_year_construction
            result_7_year_olympics = user_data.result_7_year_olympics
            result_7_year_scince_and_practical_results = user_data.result_7_year_scince_and_practical_results
            result_7_year_engineer_competition_results = user_data.result_7_year_engineer_competition_results
            result_7_year_engineer_scince_week = user_data.result_7_year_engineer_scince_week
            result_7_year_creative = user_data.result_7_year_creative
            result_7_year_reflex = user_data.result_7_year_reflex
            result_7_year_FG = user_data.result_7_year_FG

            # 8 year
            result_8_year_items = user_data.result_8_year_items
            result_8_year_project_skills = user_data.result_8_year_project_skills
            result_8_year_construction = user_data.result_8_year_construction
            result_8_year_olympics = user_data.result_8_year_olympics
            result_8_year_scince_and_practical_results = user_data.result_8_year_scince_and_practical_results
            result_8_year_engineer_competition_results = user_data.result_8_year_engineer_competition_results
            result_8_year_engineer_scince_week = user_data.result_8_year_engineer_scince_week
            result_8_year_creative = user_data.result_8_year_creative
            result_8_year_reflex = user_data.result_8_year_reflex
            result_8_year_FG = user_data.result_8_year_FG

            # 9 year
            result_9_year_items = user_data.result_9_year_items
            result_9_year_project_skills = user_data.result_9_year_project_skills
            result_9_year_construction = user_data.result_9_year_construction
            result_9_year_olympics = user_data.result_9_year_olympics
            result_9_year_scince_and_practical_results = user_data.result_9_year_scince_and_practical_results
            result_9_year_engineer_competition_results = user_data.result_9_year_engineer_competition_results
            result_9_year_engineer_scince_week = user_data.result_9_year_engineer_scince_week
            result_9_year_creative = user_data.result_9_year_creative
            result_9_year_reflex = user_data.result_9_year_reflex
            result_9_year_FG = user_data.result_9_year_FG

            result_1_year_tech = 0
            result_1_year_chem_bio = 0
            result_1_year_gum = 0

            if result_1_year_project_skills >= 70:
                result_1_year_tech += 1
            elif result_1_year_project_skills < 70 and result_1_year_project_skills >= 50:
                result_1_year_chem_bio += 1
                comment_project_skills_1_year = 'Если Вы увеличите свои старания в проектной деятельности, сможете повысить свои качества для сферы технического образования.'
            else:
                result_1_year_gum += 1
                comment_project_skills_1_year = 'Если Вы увеличите свои старания в проектной деятельности, сможете повысить свои качества для сферы хим-био или технического образования.'

            if result_1_year_construction >= 70:
                result_1_year_tech += 1
            elif result_1_year_construction < 70 and result_1_year_construction >= 50:
                result_1_year_chem_bio += 1
                comment_construction_1_year = 'Если Вы увеличите свои старания в конструировании, сможете повысить свои качества для сферы технического образования.'
            else:
                result_1_year_gum += 1
                comment_construction_1_year = 'Если Вы увеличите свои старания в конструировании, сможете повысить свои качества для сферы хим-био или технического образования.'

            if result_1_year_olympics >= 70:
                result_1_year_tech += 1
            elif result_1_year_olympics < 70 and result_1_year_olympics >= 50:
                result_1_year_chem_bio += 1
                comment_olympics_1_year = 'Если Вы увеличите свои старания в олимпиадах, сможете повысить свои качества для сферы технического образования.'
            else:
                result_1_year_gum += 1
                comment_olympics_1_year = 'Если Вы увеличите свои старания в олимпиадах, сможете повысить свои качества для сферы хим-био или технического образования.'

            if result_1_year_scince_and_practical_results >= 70:
                result_1_year_tech += 1
                comment_scince_and_practical_1_year = 'У Вас превосходные инженерно-соревновательные компетенции.'
            elif result_1_year_scince_and_practical_results < 70 and result_1_year_scince_and_practical_results >= 50:
                result_1_year_chem_bio += 1
                comment_scince_and_practical_1_year = 'Если Вы увеличите свои старания в научно-практической направленности, сможете повысить свои качества для сферы технического образования.'
            else:
                result_1_year_gum += 1
                comment_scince_and_practical_1_year = 'Если Вы увеличите свои старания в научно-практической направленности, сможете повысить свои качества для сферы хим-био или технического образования.'


            if result_1_year_engineer_competition_results >= 70:
                result_1_year_tech += 1
                comment_engineer_competition_1_year = 'У Вас превосходные инженерно-соревновательные компетенции.'
            elif result_1_year_engineer_competition_results < 70 and result_1_year_engineer_competition_results >= 50:
                result_1_year_chem_bio += 1
                comment_engineer_competition_1_year = 'Если Вы увеличите свои старания в инженерных конкурсах, сможете повысить свои качества для сферы технического образования.'
            else:
                result_1_year_gum += 1
                comment_engineer_competition_1_year = 'Если Вы увеличите свои старания в инженерных конкурсах, сможете повысить свои качества для сферы хим-био или технического образования.'

            if result_1_year_engineer_scince_week >= 70:
                result_1_year_tech += 1
            elif result_1_year_engineer_scince_week < 70 and result_1_year_engineer_scince_week >= 50:
                result_1_year_chem_bio += 1
                comment_engineer_scince_week_1_year = 'Если Вы увеличите свои старания на неделях инженерных наук, сможете повысить свои качества для сферы технического образования.'
            else:
                result_1_year_gum += 1
                comment_engineer_scince_week_1_year = 'Если Вы увеличите свои старания на неделях инженерных наук, сможете повысить свои качества для сферы хим-био или технического образования.'

            if result_1_year_creative >= 70:
                result_1_year_tech += 1
            elif result_1_year_creative < 70 and result_1_year_creative >= 50:
                result_1_year_chem_bio += 1
                comment_creative_1_year = 'Если Вы застимулируете свою креативность, сможете повысить свои качества для сферы технического образования.'
            else:
                result_1_year_gum += 1
                comment_creative_1_year = 'Если Вы застимулируете свою креативность, сможете повысить свои качества для сферы хим-био или технического образования.'

            if result_1_year_reflex >= 70:
                result_1_year_tech += 1
            elif result_1_year_reflex < 70 and result_1_year_reflex >= 50:
                result_1_year_chem_bio += 1
                comment_reflex_1_year = 'Если Вы застимулируете свою рефлексию, сможете повысить свои качества для сферы технического образования.'
            else:
                result_1_year_gum += 1
                comment_reflex_1_year = 'Если Вы застимулируете свою рефлексию, сможете повысить свои качества для сферы хим-био или технического образования.'

            if result_1_year_FG >= 70:
                result_1_year_tech += 1
            elif result_1_year_FG < 70 and result_1_year_FG >= 50:
                result_1_year_chem_bio += 1
                comment_FG_1_year = 'Если Вы застимулируете свою флюораграфию (я не знаю, что такое ФГ), сможете повысить свои качества для сферы технического образования.'
            else:
                result_1_year_gum += 1
                comment_FG_1_year = 'Если Вы застимулируете свою флюораграфию (я не знаю, что такое ФГ), сможете повысить свои качества для сферы хим-био или технического образования.'

            max_result_1_year = max(result_1_year_chem_bio, result_1_year_tech, result_1_year_gum)

            if max_result_1_year == result_1_year_chem_bio:
                result_1_year = 'Предрасположенность к хим-био специальности.', comment_project_skills_1_year, comment_construction_1_year, comment_olympics_1_year, comment_scince_and_practical_1_year, \
                    comment_engineer_competition_1_year, comment_engineer_scince_week_1_year, comment_creative_1_year, comment_reflex_1_year, comment_FG_1_year
            elif max_result_1_year == result_1_year_tech:
                result_1_year = 'Предрасположенность к технической специальности', comment_project_skills_1_year, comment_construction_1_year, comment_olympics_1_year, comment_scince_and_practical_1_year, \
                    comment_engineer_competition_1_year, comment_engineer_scince_week_1_year, comment_creative_1_year, comment_reflex_1_year, comment_FG_1_year
            else:
                result_1_year = 'Предрасположенность к гуманитарной специальности', comment_project_skills_1_year, comment_construction_1_year, comment_olympics_1_year, comment_scince_and_practical_1_year, \
                    comment_engineer_competition_1_year, comment_engineer_scince_week_1_year, comment_creative_1_year, comment_reflex_1_year, comment_FG_1_year

            result_2_year_tech = 0
            result_2_year_chem_bio = 0
            result_2_year_gum = 0

            if result_2_year_project_skills >= 70:
                result_2_year_tech += 1
            elif result_2_year_project_skills < 70 and result_2_year_project_skills >= 50:
                result_2_year_chem_bio += 1
                comment_project_skills_2_year = 'Если Вы увеличите свои старания в проектной деятельности, сможете повысить свои качества для сферы технического образования.'
            else:
                result_2_year_gum += 1
                comment_project_skills_2_year = 'Если Вы увеличите свои старания в проектной деятельности, сможете повысить свои качества для сферы хим-био или технического образования.'

            if result_2_year_construction >= 70:
                result_2_year_tech += 1
            elif result_2_year_construction < 70 and result_1_year_construction >= 50:
                result_2_year_chem_bio += 1
                comment_construction_2_year = 'Если Вы увеличите свои старания в конструировании, сможете повысить свои качества для сферы технического образования.'
            else:
                result_2_year_gum += 1
                comment_construction_2_year = 'Если Вы увеличите свои старания в конструировании, сможете повысить свои качества для сферы хим-био или технического образования.'

            if result_2_year_olympics >= 70:
                result_2_year_tech += 1
            elif result_2_year_olympics < 70 and result_2_year_olympics >= 50:
                result_2_year_chem_bio += 1
                comment_olympics_2_year = 'Если Вы увеличите свои старания в олимпиадах, сможете повысить свои качества для сферы технического образования.'
            else:
                result_2_year_gum += 1
                comment_olympics_2_year = 'Если Вы увеличите свои старания в олимпиадах, сможете повысить свои качества для сферы хим-био или технического образования.'

            if result_2_year_scince_and_practical_results >= 70:
                result_2_year_tech += 1
            elif result_2_year_scince_and_practical_results < 70 and result_2_year_scince_and_practical_results >= 50:
                result_2_year_chem_bio += 1
                comment_scince_and_practical_2_year = 'Если Вы увеличите свои старания в научно-практической направленности, сможете повысить свои качества для сферы технического образования.'
            else:
                result_2_year_gum += 1
                comment_scince_and_practical_2_year = 'Если Вы увеличите свои старания в научно-практической направленности, сможете повысить свои качества для сферы хим-био или технического образования.'

            if result_2_year_engineer_competition_results >= 70:
                result_2_year_tech += 1
            elif result_2_year_engineer_competition_results < 70 and result_2_year_engineer_competition_results >= 50:
                result_2_year_chem_bio += 1
                comment_engineer_competition_2_year = 'Если Вы увеличите свои старания в инженерных конкурсах, сможете повысить свои качества для сферы технического образования.'
            else:
                result_2_year_gum += 1
                comment_engineer_competition_2_year = 'Если Вы увеличите свои старания в инженерных конкурсах, сможете повысить свои качества для сферы хим-био или технического образования.'

            if result_2_year_engineer_scince_week >= 70:
                result_2_year_tech += 1
            elif result_2_year_engineer_scince_week < 70 and result_2_year_engineer_scince_week >= 50:
                result_2_year_chem_bio += 1
                comment_engineer_scince_week_2_year = 'Если Вы увеличите свои старания на неделях инженерных наук, сможете повысить свои качества для сферы технического образования.'
            else:
                result_2_year_gum += 1
                comment_engineer_scince_week_2_year = 'Если Вы увеличите свои старания на неделях инженерных наук, сможете повысить свои качества для сферы хим-био или технического образования.'

            if result_2_year_creative >= 70:
                result_2_year_tech += 1
            elif result_2_year_creative < 70 and result_2_year_creative >= 50:
                result_2_year_chem_bio += 1
                comment_creative_2_year = 'Если Вы застимулируете свою креативность, сможете повысить свои качества для сферы технического образования.'
            else:
                result_1_year_gum += 1
                comment_creative_2_year = 'Если Вы застимулируете свою креативность, сможете повысить свои качества для сферы хим-био или технического образования.'

            if result_2_year_reflex >= 70:
                result_2_year_tech += 1
            elif result_2_year_reflex < 70 and result_2_year_reflex >= 50:
                result_2_year_chem_bio += 1
                comment_reflex_2_year = 'Если Вы застимулируете свою рефлексию, сможете повысить свои качества для сферы технического образования.'
            else:
                result_2_year_gum += 1
                comment_reflex_2_year = 'Если Вы застимулируете свою рефлексию, сможете повысить свои качества для сферы хим-био или технического образования.'

            if result_2_year_FG >= 70:
                result_2_year_tech += 1
            elif result_2_year_FG < 70 and result_2_year_FG >= 50:
                result_2_year_chem_bio += 1
                comment_FG_2_year = 'Если Вы застимулируете свою флюораграфию (я не знаю, что такое ФГ), сможете повысить свои качества для сферы технического образования.'
            else:
                result_2_year_gum += 1
                comment_FG_2_year = 'Если Вы застимулируете свою флюораграфию (я не знаю, что такое ФГ), сможете повысить свои качества для сферы хим-био или технического образования.'

            max_result_2_year = max(result_2_year_chem_bio, result_2_year_tech, result_2_year_gum)

            if max_result_2_year == result_2_year_chem_bio:
                result_2_year = 'Предрасположенность к хим-био специальности.', comment_project_skills_2_year, comment_construction_2_year, comment_olympics_2_year, comment_scince_and_practical_2_year, \
                    comment_engineer_competition_2_year, comment_engineer_scince_week_2_year, comment_creative_2_year, comment_reflex_2_year, comment_FG_2_year
            elif max_result_2_year == result_2_year_tech:
                result_2_year = 'Предрасположенность к технической специальности', comment_project_skills_2_year, comment_construction_2_year, comment_olympics_2_year, comment_scince_and_practical_2_year, \
                    comment_engineer_competition_2_year, comment_engineer_scince_week_2_year, comment_creative_2_year, comment_reflex_2_year, comment_FG_2_year
            else:
                result_2_year = 'Предрасположенность к гуманитарной специальности', comment_project_skills_2_year, comment_construction_2_year, comment_olympics_2_year, comment_scince_and_practical_2_year, \
                    comment_engineer_competition_2_year, comment_engineer_scince_week_2_year, comment_creative_2_year, comment_reflex_2_year, comment_FG_2_year




            graph_of_score = get_plot(range(3)[1:], [max_result_1_year, max_result_2_year])

            results = [result_1_year, result_2_year]

            return render(request, 'account/score.html', {'results': results, 'show_result': graph_of_score})
        except Score.DoesNotExist:
            return render(request, 'account/score.html', {'error': 'Запись не найдена'})
    else:
        return render(request, 'login.html')