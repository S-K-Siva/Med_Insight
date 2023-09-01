from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.shortcuts import redirect,render
from django.db.models import Q


def loginView(request):
    if request.method == "POST":
        userName = request.POST["username"]
        passWord = request.POST["password"]
        # checking whether the user exist or not

        try:
            user = User.objects.get(username=userName)
        except:
            messages.error(request, "Username doesn't exist!")
            return redirect('login')
        user = authenticate(request, username=userName, password=passWord)
        if user is not None:
            # user exists!
            login(request, user)
            messages.success(request, "User loggedIn successfully!")
            return redirect("profiles")
        else:
            messages.error(request, "Username or password is incorrect")
            return redirect('login')
    return render(request, 'users/login_register.html')


@login_required(login_url="login")
def logoutView(request):
    logout(request)
    return redirect('login')


def registerView(request):
    form = UserForm()
    if request.method == "POST":
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            # login(request,user)
            messages.success(request, "User Created Successfully!")
            return redirect('login')
        else:
            messages.error(request, "Error has occurred while registering!")

    return render(request, 'users/login_register.html', {"form": form, "page": "register"})

#
# def profiles(request):
#     profiles, search_query = searchProfiles(request)
#     paginator, count_range, profiles = getPagination(request, profiles)
#     return render(request, 'users/profiles.html',
#                   {'profiles': profiles, 'search_query': search_query, 'paginator': paginator,
#                    'count_range': count_range})
