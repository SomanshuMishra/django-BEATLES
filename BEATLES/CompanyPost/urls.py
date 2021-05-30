from django.urls import path
from django.conf.urls import include
from CompanyPost import views

urlpatterns = [
    path('postComments/',views.postComments,name="postComments"),
    path('',views.posthome,name="posthome"),
    
    path('<str:slug>/',views.postcontent,name="postcontent"),
]
