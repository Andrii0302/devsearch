from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','email','username','password1','password2']
        labels = {
            'first_name':'Name',
        }
    def __init__(self,*args,**kwargs):
        super(CustomCreationForm,self).__init__(*args,**kwargs)

        for k,v in self.fields.items():
            v.widget.attrs.update({'class':'input'})