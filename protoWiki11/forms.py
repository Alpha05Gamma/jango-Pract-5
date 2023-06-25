from typing import Any, Dict, Mapping, Optional, Type, Union
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import *
from django.forms import ModelForm


class PlayerForm(ModelForm):

    class Meta:
        model = Player
        fields = ('name', 'region', 'rating')
    def __init__(self, *args, **kwargs):
        super(PlayerForm, self).__init__(*args, **kwargs)
        self.fields['name'].label='Nicname'
        self.fields['region'].label = 'Регион'
        self.fields['rating'].label = 'Рейтинг'
        