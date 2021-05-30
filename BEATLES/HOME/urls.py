from django.urls import path
from django.conf.urls import include
from HOME import views

urlpatterns = [
    path('',views.home,name='home'), 
    path('contact/',views.contact,name='contact'),
    # path('postcomments/',views.postcomments,name='postcomments'),
    path('search/',views.search,name='search'),
    path('signup/',views.handleSignup,name='signup'),
    path('login/',views.handleLogin,name='login'),
    path('logout/',views.handleLogOut,name='logout'),
]
