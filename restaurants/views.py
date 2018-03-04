from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Restaurant
from .forms import RestaurantForm,ItemForm
from django.contrib.auth.models import User


def like(request,restaurant_id):
	restaurant_obj= Restaurant.objects.get(id=restaurant_id)
	like_obj, created = Like.objects.get_or_create(user=request.user, restaurant=restaurant_obj)

	if created:
		action="like"
	else:
		action="unlike"
		like_obj.delete()

	like_count = restaurant_obj.like_set.all().count()


	message = "Hello"
	context =  {
		"action": action,
		"count": like_count,
	}
	return JsonResponse(context, safe=False)

def list(request):
	restaurant_obj= Restaurant.objects.all()
	restaurant_obj=restaurant_obj.order_by('name')
	query= request.GET.get('q')
	if query:
		restaurant_obj= restaurant_obj.filter(title_contains=query)

	like_obj= []
	likes= request.user.like_set.all()
	for like in likes:
		like_obj.append(like.restaurant)
	context = {
	"restaurants": restaurant_obj,
	"my_likes": like_obj,

	}
	return render(request, 'restaurant_list.html', context)


	# calls the html file detailview.html


def detail(request, restaurant_id):
	context = {
	"restaurant_detail": Restaurant.objects.get(id=restaurant_id),

	}


	return render(request, 'restaurant_detail.html', context)

def create(request):
	form = RestaurantForm()
	if request.method == "POST":
		form = RestaurantForm(request.POST, request.FILES or None)
		if form.is_valid():
			form.save()
			return redirect("restaurant_list")
	context = {
		"create_form" : form,
	}
	return render(request,'restaurant_create.html',context)

def update(request, restaurant_id):
	restaurant_obj = Restaurant.objects.get(id=restaurant_id)
	form = RestaurantForm(instance = restaurant_obj)
	if request.method == "POST":
		form = RestaurantForm(request.POST, instance=restaurant_obj)
		if form.is_valid():
			form.save()
			return redirect("restaurant_detail",restaurant_id=restaurant_obj.id)
	context = {
		"restaurant_obj": restaurant_obj,
		"create_form" : form,
	}
	return render(request,'restaurant_update.html',context)

def delete(request, restaurant_id):
	Restaurant.objects.get(id=restaurant_id).delete()
	return redirect("restaurant_list")

def item_create(request, restaurant_id):
	restaurant_obj = Restaurant.objects.get(id=restaurant_id)
	form = ItemForm()
	if request.method=="POST":
		form = ItemForm(request.POST)
		if form.is_valid():
			item= form.save(commit = False)
			item.restaurant = restaurant_obj
			item.save()
			return redirect ('restaurant_detail',restaurant_id=restaurant_id)
	context = {
		'form': form,
		'restaurant': restaurant_obj
	}
	return render (request,'item_create.html',context)



		# meals_dictionary = {
	# 	"meals": [
	# 	  {
	# 		 "title": "Swiss Cheese Burger",
	# 		 "content": "Description, ingredients, sauces, vegetables, calories",
	# 		 "created": "2018-02-05",
	# 		 "updated": "2018-02-06",
	# 	   },
	# 	   {
	# 		 "title": "Classic Cheese Burger",
	# 		 "content": "Description, ingredients, sauces, vegetables, calories",
	# 		 "created": "2018-02-02",
	# 		 "updated": "2018-02-04",
	# 	   },
	# 	   {
	# 		 "title": "Barbecue Burger",
	# 		 "content": "Description, ingredients, sauces, vegetables, calories",
	# 		 "created": "2018-02-06",
	# 		 "updated": "2018-02-09",
	# 	   },
	# 	   {
	# 		 "title": "Special Burger",
	# 		 "content": "Description, ingredients, sauces, vegetables, calories",
	# 		 "created": "2018-02-01",
	# 		 "updated": "2018-02-01",
	# 	   }
	# ]
	# }