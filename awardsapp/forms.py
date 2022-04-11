# from dataclasses import fields
# from pyexpat import model
from .models import Post,Ratings,Profile,User

from django import forms


# class captionForm(forms.Form):
#     new_caption=forms.CharField(max_length=200)


class newPost(forms.Form):

    title = forms.CharField(max_length=200)
    project_image = forms.ImageField() 
    description =forms.CharField(max_length=500)
    url=forms.CharField(max_length=200)

class ratesForm(forms.ModelForm):
    class Meta:
        model= Ratings
        fields = ('design','userbility','content')
    

class UuserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required.')
    class Meta:
        model = User
        fields = ('username', 'email')

class UprofileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profilePhoto','bio']

    
  

# class NewsletterForms(forms.Form):
#     your_name=forms.CharField(label='First Name',max_length=30)
#     email=forms.EmailField(label='Email')

    
# class signUp(forms.Form):
#     username=forms.CharField(label='enter name',max_length=40)
#     first_name=forms.CharField(label= 'user name',max_length=50)
#     last_name=forms.CharField(label= 'user name',max_length=50)
#     email = forms.EmailField(max_length=254, help_text='Required.')
#     password= forms.PasswordInput()
#     password_confirm=forms.PasswordInput()

# class commentForm(forms.Form):
#     comment= forms.CharField(label='post your comment here')

# class UuserForm(forms.ModelForm):
#     email = forms.EmailField(max_length=254, help_text='Required.')
#     class Meta:
#         model = User
#         fields = ('username', 'email')

# class UprofileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['profilePhoto','bio']

# class NewCommentForm(forms.ModelForm):
#     class Meta:
#         model=Comments
#         fields=['comment',]