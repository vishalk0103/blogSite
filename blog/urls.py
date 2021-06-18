from django.urls import path
from . import views

urlpatterns = [
    path("",views.Home,name="home"),
    path("about/",views.About.as_view(),name="about"),
    path("contactpage/",views.Contact,name="contact"),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("logout/",views.user_logout,name="logout"),
    path("signup/",views.user_signup,name="signup"),
    path("login/",views.user_login,name='login'),
    path("addpost/",views.AddPost,name='addpost'),
    path('updatePost/<int:id>/',views.UpdatePost, name='updatepost'),
    path('Delete/<int:id>',views.DeletPost, name='deletepost')
]
