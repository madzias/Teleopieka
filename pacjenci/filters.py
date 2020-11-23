import django_filters
from django_filters import *
from .models import *
from .forms import *
from dal import autocomplete

class ZglosznieFilter(django_filters.FilterSet):
    class Meta:
        model = Zgloszenie
        fields = ['status', 'rodzaj']
        widgets = {
        }

class PacjentFilter(django_filters.FilterSet):
    class Meta:
        model = Pacjent
        fields = '__all__'
        exclude = ['telefon', 'data_dodania', 'dom']

class PacjentFilterAll(django_filters.FilterSet):
    class Meta:
        model = Pacjent
        fields = '__all__'
        exclude = ['telefon', 'data_dodania']