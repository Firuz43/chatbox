from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    # Styling Registration form fields with bootstrap
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter username ...'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter password ...'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Confirm password ...'})
