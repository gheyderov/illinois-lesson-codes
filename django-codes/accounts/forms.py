from typing import Any, Dict
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UsernameField

User = get_user_model()

class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=40, widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Password',
               
            }))
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'image',
            'password',
        )
        widgets = {
            'first_name' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'First Name'
            }),
            'last_name' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Last Name'
            }),
            'username' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Username'
            }),
            'email' : forms.EmailInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Your email'
            }),
            'password' : forms.PasswordInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Password'
            })
            
        }

    def clean(self) -> Dict[str, Any]:
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Password does not match')
        return super().clean()

    def save(self, commit: bool = ...) -> Any:
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.is_active = False
        user.save()
        return user
    

class LoginForm(AuthenticationForm):
    username = UsernameField(max_length=40, widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
            }))
    password = forms.CharField(max_length=40, widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password',
            }))