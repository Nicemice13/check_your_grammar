from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import logging

logger = logging.getLogger(__name__)

def auth_page(request):
    if request.user.is_authenticated:
        return redirect('user_page')
    return render(request, 'user_page/auth.html')

@require_http_methods(["POST"])
def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        return HttpResponse('<p class="success">Успешный вход! <a href="/user_page/">Перейти в профиль</a></p>')
    return HttpResponse('<p class="error">Неверное имя пользователя или пароль</p>')

@require_http_methods(["POST"])
def register_view(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    
    if password1 != password2:
        return HttpResponse('<p class="error">Пароли не совпадают</p>')
    
    if User.objects.filter(username=username).exists():
        return HttpResponse('<p class="error">Пользователь с таким именем уже существует</p>')
    
    user = User.objects.create_user(username=username, email=email, password=password1)
    login(request, user)
    return HttpResponse('<p class="success">Регистрация успешна! <a href="/user_page/">Перейти в профиль</a></p>')

@login_required
def edit_user_info(request):
    return render(request, 'user_page/user_info_form.html', {'user': request.user})

@login_required
@require_http_methods(["POST"])
def save_user_info(request):
    from .models import UserInfo
    
    try:
        user_info = request.user.userinfo
    except UserInfo.DoesNotExist:
        user_info = UserInfo(user=request.user)
    
    user_info.phone = request.POST.get('phone', '')
    birthday = request.POST.get('birthday')
    if birthday:
        user_info.birthday = birthday
    
    gender = request.POST.get('gender')
    if gender == 'True':
        user_info.gender = True
    elif gender == 'False':
        user_info.gender = False
    else:
        user_info.gender = None
    
    if 'photo' in request.FILES:
        user_info.photo = request.FILES['photo']
    
    user_info.save()
    return render(request, 'user_page/user_details.html', {'user': request.user})

@login_required
def logout_view(request):
    logout(request)
    return redirect('auth_page')

@login_required
def user_page(request):
    logger.info(f"User: {request.user.username}")
    try:
        userinfo = request.user.userinfo
        logger.info(f"UserInfo exists: phone={userinfo.phone}, photo={userinfo.photo}")
        logger.info(f"Photo path: {userinfo.photo.name if userinfo.photo else 'No photo'}")
        logger.info(f"Photo URL: {userinfo.photo.url if userinfo.photo else 'No URL'}")
    except Exception as e:
        logger.error(f"UserInfo error: {e}")
    
    context = {'user': request.user}
    if request.user.is_superuser:
        context['all_users'] = User.objects.all().order_by('id')
    
    return render(request, 'user_page/user_page.html', context)

@login_required
def refresh_user_info(request):
    logger.info(f"Refresh called for user: {request.user.username}")
    return render(request, 'user_page/user_details.html', {'user': request.user})
