from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import EmailRegistrationForm, UserDetailsForm
from .models import CustomUser
from django.contrib.sessions.models import Session

def registration_step1(request):
    if request.method == 'POST':
        form = EmailRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            
            # Check if user with this email already exists
            if CustomUser.objects.filter(email=email).exists():
                form.add_error('email', 'This email is already registered.')
            else:
                # Store email in session
                request.session['registration_email'] = email
                request.session['registration_step'] = 2
                
                # Create a temporary user record
                user = CustomUser.objects.create(
                    email=email,
                    registration_step=2,
                    temp_session_key=request.session.session_key
                )
                user.set_unusable_password()
                user.save()
                
                return redirect('registration_step2')
    else:
        form = EmailRegistrationForm()

    return render(request, 'accounts/step1_email.html', {'form': form})


def registration_step2(request):
    # Проверяем наличие email в сессии
    if 'registration_email' not in request.session:
        return redirect('registration_step1')
    
    email = request.session.get('registration_email')
    
    try:
        user = CustomUser.objects.get(email=email, temp_session_key=request.session.session_key)
    except CustomUser.DoesNotExist:
        return redirect('registration_step1')
    
    if request.method == 'POST':
        form = UserDetailsForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            user.registration_step = 3  # Отмечаем завершение регистрации
            user.temp_session_key = None
            user.is_active = True  # Активируем пользователя
            user.save()
            
            # Логиним пользователя
            login(request, user)
            
            # Очищаем сессию, проверяя наличие ключей
            if 'registration_email' in request.session:
                del request.session['registration_email']
            if 'registration_step' in request.session:
                del request.session['registration_step']
            
            return redirect('home')  # Добавлен отсутствующий return
    
    else:
        form = UserDetailsForm(instance=user)
    
    return render(request, 'accounts/step2_details.html', {
        'form': form,
        'email': email
    })

def signin_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Перенаправление после успешного входа
        else:
            # Обработка ошибки аутентификации
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
    return render(request, 'accounts/login.html')