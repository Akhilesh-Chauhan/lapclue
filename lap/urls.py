"""lapclue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path
from lap import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index,name='index'),
    path('login', views.login,name='login'),
    path('signup', views.signup,name='signup'),
    path('profile/<str:pk>',views.profile,name='profile'),
    path('editprofile/<str:pk>',views.editprofile,name='editprofile'),
    path('logout',views.logout,name='logout'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('companies',views.companies,name='companies'),
    path('products/<str:category>',views.products,name='products'),
    path('productdetails/<str:pk>',views.productdetails,name='productdetails'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('cart_display', views.cart_display,name='cart_display'),
    path('order/<str:code>', views.order,name='order'),
    path('cancel/<str:code>', views.cancel,name='cancel'),
    path('order_display', views.order_display,name='order_display'),
    path('cart/<str:code>', views.cart,name='cart'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
