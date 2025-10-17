from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'style': 'margin-left: 30px; height: 20px; width: 400px;',
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'style': 'margin-left: 30px; height: 20px; width: 400px;',
            }),
        }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'style': 'margin-left: 30px; height: 20px; width: 400px;',
        })
        self.fields['password2'].widget.attrs.update({
            'style': 'margin-left: 30px; height: 20px; width: 400px;',
        })
