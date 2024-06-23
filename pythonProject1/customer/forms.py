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