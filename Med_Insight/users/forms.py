from .models import Profile 
from django.forms import ModelForm,forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from api.models import Profile
class ProfileForm(ModelForm,forms.Form):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ['created','id','author']


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']
        labels = {
            'first_name': 'Name',

        }





