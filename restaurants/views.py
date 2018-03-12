from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Restaurant
from .forms import RestaurantForm,ItemForm, UserSignup, UserLogin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def like(request,restaurant_id):
	restaurant_obj= Restaurant.objects.get(id=restaurant_id)
	like_obj, created = Like.objects.get_or_create(user=request.user, restaurant=restaurant_obj)

	if created:
		action="like"
	else:
		action="unlike"
		like_obj.delete()

	like_count = restaurant_obj.favrest_set.all().count()


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
		restaurant_obj= restaurant_obj.filter(title__contains=query)

	like_obj= []
	likes= request.user.favrest_set.all()
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
		form = RestaurantForm(request.POST,request.FILES, instance=restaurant_obj)
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

def usersignup(request):
	context = {}
	form= UserSignup()
	context['form']= form
	if request.method == 'POST':
		form= UserSignup(request.POST)
		if form.is_valid():
			user = form.save(commit= False)
			#username= user.username
			#password= user.password

			user.set_password(password)
			user.save()

			#auth_user= authenticate(username=username,password=password)
			#login(request,auth_user)

			return redirect("restaurant_list")
	return render(request, 'signup.html', context)


def userlogin(request):
    context = {}
    form = UserLogin()
    context['form'] = form
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect('restaurant_list')
    return render(request, 'login.html', context)


def userlogout(request):
    logout(request)
    return redirect("restaurant_list")



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