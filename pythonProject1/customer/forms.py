from django import forms

from customer.models import Customer, User


class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ()


class LoginForm(forms.Form):
#    email = forms.EmailField()
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    password = forms.CharField(max_length=255)

    def clean_phone(self):
        phone_number = self.data.get('phone')
        if not User.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError('Phone does not exist')
        return phone_number

    def clean_password(self):
        phone_number = self.cleaned_data.get('email')
        password = self.data.get('password')
        try:
            user = User.objects.get(phone_number=phone_number)
            print(user)
            if not user.check_password(password):
                raise forms.ValidationError('Password did not match')
        except User.DoesNotExist:
            raise forms.ValidationError(f'{phone_number} does not exists')
        return password

class LogoutForm(forms.Form):
    confirm = forms.BooleanField(
        label="Chiqish uchun tasdiqlang",
        required=True
    )

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User

        fields = ['username', 'phone_number']

    def clean_password2(self):
        cd = self.cleaned_data

        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']