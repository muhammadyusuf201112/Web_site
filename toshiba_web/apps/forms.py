from django import forms

class PaymentForm(forms.Form):
    card_number = forms.CharField(label="Karta raqami", max_length=16)
    expiry_date = forms.CharField(label="Amal qilish muddati (MM/YY)", max_length=5)
    cvc = forms.CharField(label="CVC", max_length=3)


# from django.forms import ModelForm
# from django.contrib.auth.forms import UserCreationForm
# from apps.models import User, Service, Blog, Skill, Comment, Portfolio
# from django.forms import Form, CharField, EmailField

# class UserModelForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'image', 'phone', 'job', 'about_me', 'email', 'username', 'password']


# class ServisModelForm(ModelForm):
#     class Meta:
#         model = Service
#         fields = ['title', 'dis', 'user_id']


# class BlogModelForm(ModelForm):
#     class Meta:
#         model = Blog
#         fields = ['image', 'title', 'dis', 'user_id']


# class UserUpdateForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'phone', 'job', 'about_me', 'email', 'password']


# class AddSkillForm(ModelForm):
#     class Meta:
#         model = Skill
#         fields = ['title', 'level', 'user_id']


# class PortfolioModelForm(ModelForm):
#     class Meta:
#         model = Portfolio
#         fields = ['user_id', 'image', 'dis', 'category', 'company', 'title']


# class CommentsForm(ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['text', 'email', 'name', 'post_id', 'author_id']


# class ContactForm(Form):
#     name = CharField(max_length=255)
#     email = EmailField(max_length=255)
#     message = CharField()