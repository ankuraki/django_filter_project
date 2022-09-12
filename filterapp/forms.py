from django import forms 

class UserRegisterForm(forms.Form):
    username=forms.CharField( 
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':"Enter Your Username",
            }
        )
    )


    first_name=forms.CharField( 
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter First Name',
            }
        )
    )

    last_name=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Last Name',
            }
        )
    )

    password1=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your password',
            }
        )
    )

    password2=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Confirm password',
            }
        )
    )


    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your Email',
            }
        )
    )



class UserLoginForm(forms.Form):
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Username',

            }
        )
    )

    password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your password',
            }
        )
    )
