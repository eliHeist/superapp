import datetime
from django.forms import inlineformset_factory
from projects.models import Photo, Project, current_year
from django.forms import ModelForm, TypedChoiceField

def year_choices():
        # where r is the year
        return [(r,r) for r in range(2010, datetime.date.today().year+1)]


class ProjectModelForm(ModelForm):
    class Meta:
        model = Project
        fields = (
            'name',
            'client',
            'year',
            'picture',
            'status',
            'description',
        )
    year = TypedChoiceField(coerce=int, choices=year_choices, initial=current_year) 


class PhotoModelForm(ModelForm):
    class Meta:
        model = Photo
        fields = (
            'image',
            'slide'
        )


PhotoFormset = inlineformset_factory(Project, Photo, PhotoModelForm, extra=3)