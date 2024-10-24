from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile, StudentCategory
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('login')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home') 
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
            return redirect('login')  

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        # Collect form data
        prefix = request.POST.get('prefix')
        first_name = request.POST.get('first_name')
        surname = request.POST.get('surname')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        institute = request.POST.get('institute')
        designation = request.POST.get('designation')
        education = request.POST.get('education')
        category = request.POST.get('category')
        address = request.POST.get('address')
        state = request.POST.get('state')
        country = request.POST.get('country')
        pin_code = request.POST.get('pin_code')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')

        # Create the user
        user = User.objects.create_user(username=email, email=email, password=password)
        user.save()

        # Handle student category
        student_category = None
        if category == 'Student':
            student_type = request.POST.get('student_category')
            bona_fide = request.FILES.get('bona_fide')
            student_category = StudentCategory.objects.create(category=student_type, bona_fide=bona_fide)
            student_category.save()

        # Handle regular category
        regular_category = request.POST.get('regular_category')
        if regular_category == 'Other':
            regular_category = request.POST.get('other_category')

        # Create user profile
        user_profile = UserProfile.objects.create(
            user=user,
            prefix=prefix,
            first_name=first_name,
            surname=surname,
            gender=gender,
            email=email,
            date_of_birth=dob,
            institute=institute,
            designation=designation,
            highest_education=education,
            category=category,
            student_category=student_category if category == 'Student' else None,
            regular_category=regular_category if category == 'Regular' else None,
            address=address,
            state=state,
            country=country,
            pin_code=pin_code,
            mobile_number=mobile,
        )
        user_profile.save()

        # Show success message and redirect to login
        messages.success(request, 'Registration successful! You can now log in.')
        return redirect('login')

    return render(request, 'registration.html')
