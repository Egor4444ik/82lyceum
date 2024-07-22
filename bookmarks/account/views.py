from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, \
    UserEditForm
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

        def gradefunc(count):
            count+=1
            return count

        try:
            result_1_year = user_data.result1
            result_2_year = user_data.result2
            result_3_year = user_data.result3
            result_4_year = user_data.result4
            result_5_year = user_data.result5
            result_6_year = user_data.result6
            result_7_year = user_data.result7
            result_8_year = user_data.result8
            result_9_year = user_data.result9
            result_10_year = user_data.result10
            result_11_year = user_data.result11

            graph_of_score = get_plot(range(12)[1:], [result_1_year, result_2_year, result_3_year,
                                                      result_4_year, result_5_year, result_6_year,
                                                      result_7_year, result_8_year, result_9_year,
                                                      result_10_year, result_11_year])

            results = [result_1_year, result_2_year, result_3_year, result_4_year, result_5_year,
                       result_6_year, result_7_year, result_8_year, result_9_year, result_10_year,
                       result_11_year,]

            return render(request, 'account/score.html', {'results': results, 'show_result': graph_of_score, 'gradefunc': gradefunc(count)})
        except Score.DoesNotExist:
            return render(request, 'account/score.html', {'error': 'Запись не найдена'})
    else:
        return render(request, 'login.html')