from django import forms
from .models import Restaurant

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        #fields = ['name', 'description','opening_time','closing_time','image']
        fields = '__all__'

        widgets = {
        	"opening_time": forms.TimeInput(attrs={"type":"time"}),
        	"closing_time": forms.TimeInput(attrs={"type":"time"}),
        }