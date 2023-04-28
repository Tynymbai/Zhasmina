from django import forms
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()


class EmployeeRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=10, label="Имя пользователя")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")
    email = forms.EmailField(label='Почта')
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [

            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'confirm_password',

        ]

    def __init__(self, *args, **kwargs):
        super(EmployeeRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter your first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter your last name'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your username'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter a valid e-mail'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter your password'
        self.fields['confirm_password'].widget.attrs['placeholder'] = 'Enter confirm password'

class EmployeeLoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(EmployeeLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(EmployeeLoginForm, self).clean(*args, **kwargs)
