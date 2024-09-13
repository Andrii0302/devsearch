from .models import Project
from django.forms import ModelForm
from django import forms
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['vote_total', 'vote_ratio']

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
    def __init__(self,*args,**kwargs):
        super(ProjectForm,self).__init__(*args,**kwargs)

        # self.fields['title'].widget.attrs.update({'class':'input','placeholder':'Add Title'})
        # self.fields['description'].widget.attrs.update({'class':'input'})
        # self.fields['demo_link'].widget.attrs.update({'class':'input'})
        # self.fields['source_link'].widget.attrs.update({'class':'input'})
        # self.fields['tags'].widget.attrs.update({'class':'input'})
        for k,v in self.fields.items():
            v.widget.attrs.update({'class':'input'})
