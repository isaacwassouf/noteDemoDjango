from django import forms

class logInForm(forms.Form):
    username= forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password= forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'Password'}))


class SignUpForm(forms.Form):
    firstname= forms.CharField(label='First Name: ')
    lastname= forms.CharField(label='Last Name: ')
    username= forms.CharField(label='Username: ')
    password= forms.CharField(label='Password', widget=forms.PasswordInput)

class PostForm(forms.Form):
    title=forms.CharField(label='')
    content =forms.CharField( label='', widget=forms.Textarea)

class Secret(PostForm):
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={
        'id':'secretPass',
        'placeholder': 'password for the secret item'
    }))
