from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Skill,Message
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

class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        fields=['name','email','username','location','bio','short_intro','profile_image',
                'social_github','social_linkedin','social_twitter','social_youtube','social_website']
        # labels = {
        #     'name':'Name',
        # }
    def __init__(self,*args,**kwargs):
        super(ProfileForm,self).__init__(*args,**kwargs)

        for k,v in self.fields.items():
            v.widget.attrs.update({'class':'input'})
class SkillForm(ModelForm):
    class Meta:
        model=Skill
        fields='__all__'
        exclude=['owner']
    def __init__(self,*args,**kwargs):
        super(SkillForm,self).__init__(*args,**kwargs)
        for k,v in self.fields.items():
            v.widget.attrs.update({'class':'input'})

class MessageForm(ModelForm):
    class Meta:
        model=Message
        fields=['name','email','subject','body']
    def __init__(self,*args,**kwargs):
        super(MessageForm,self).__init__(*args,**kwargs)
        for k,v in self.fields.items():
            v.widget.attrs.update({'class':'input'})