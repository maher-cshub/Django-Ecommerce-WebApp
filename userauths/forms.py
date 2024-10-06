from django.contrib.auth.forms import UserCreationForm
from userauths.models import User

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "username"]
