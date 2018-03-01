from django import forms
from .models import Restaurant,Item

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        #fields = ['name', 'description','opening_time','closing_time','image']
        fields = '__all__'

        widgets = {
        	"opening_time": forms.TimeInput(attrs={"type":"time"}),
        	"closing_time": forms.TimeInput(attrs={"type":"time"}),
        }

class ItemForm(forms.ModelForm):
	"""docstring for ItemForm"""
	class Meta:
		model = Item
		fields = '__all__'
		exclude = ['restaurant']