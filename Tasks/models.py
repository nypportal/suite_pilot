from django.db import models
from django.forms import ModelForm
from django import forms

PRIORITIES = (
        ('adanger', 'اولویت زیاد؟'),
        ('bwarning', 'اولویت متوسط؟'),
        ('csuccess', 'اولویت کم؟')
    )

# Create your models here.
class Username(models.Model):
    username = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.username

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.ForeignKey(Username, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, blank=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(
                    max_length=30,
                    choices=PRIORITIES,
                    default=PRIORITIES[0][0]
                )
    complete = models.IntegerField(default=0)

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['complete', 'date_of_creation', 'username']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control form-control-solid, bg-light-warning","placeholder":"به چی فکر میکنی؟"}),
            'description': forms.Textarea(attrs={"class": "form-control form-control-solid","placeholder":"متن یا توضیحات..."}),
            'priority': forms.Select(attrs={"class": "form-control form-control-solid bg-light-warning"})
        }

class UsernameForm(ModelForm):
    class Meta:
        model = Username
        fields = '__all__'

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': "Enter a username"}),
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        queryset = Username.objects.filter(username=username).count()
        if queryset > 0:
            raise forms.ValidationError('This username is already taken! Try a different one :)')
        return username