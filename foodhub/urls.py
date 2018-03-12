"""foodhub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from restaurants import views
from django.conf import settings
from django.conf.urls.static import static
from api.views import RestaurantListAPIView,RestaurantDetailAPIView,RestaurantDeleteAPIView,RestaurantCreateAPIView,RestaurantUpdateAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', views.list, name="restaurant_list"),
    path('restaurant_detail/<int:restaurant_id>/', views.detail, name="restaurant_detail"),
    path('create/',views.create,name="restaurant_create"),
    path('update/<int:restaurant_id>/',views.update,name="restaurant_update"),
    path('delete/<int:restaurant_id>/',views.delete,name="restaurant_delete"),
    path('item/create/<int:restaurant_id>/',views.item_create,name="item_create"),
    path('like/<int:restaurant_id>/', views.like, name= 'like_button'),
    path('signup/', views.usersignup, name="signup"),
    path('login/', views.userlogin, name="login"),
    path('logout/', views.userlogout, name="logout"),

    path('apilist/',RestaurantListAPIView.as_view()),
    path('apidetail/<int:restaurant_id>/',RestaurantDetailAPIView.as_view()),
    path('apidelete/<int:restaurant_id>/',RestaurantDeleteAPIView.as_view()),
    path('apicreate/',RestaurantCreateAPIView.as_view()),
    path('apiupdate/<int:restaurant_id>/',RestaurantUpdateAPIView.as_view()),

    # path('burgermenu_list_page/', views.burger_menu_list),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# you choose whatever url you want. views."the_function_defined_in_the views_file"
# you import the views file from the app