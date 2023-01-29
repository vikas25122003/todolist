from . import views
from django.urls import path


urlpatterns = [
    path("", views.home, name="homepage"),
    path("/signup", views.signup, name="signuppage"),
    path("/login", views.login, name="loginpage"),
    path("/logout", views.logout, name="logoutpage"),
    path("/tasks", views.task, name="taskpage"),
    path("/addtask", views.addtask, name="addnewtaskpage"),
    path("/viewtask", views.viewtask, name="viewtaskpage"),
    path("/comptasks", views.viewcomptask, name="completedtaskpage"),
    path("/overduetasks", views.overduetask, name="overduetaskpage"),
    path("/taskdone/<str:docId>", views.taskcomp, name="taskcomplete"),
    path("/deltask/<str:docId>", views.taskdel, name="deltask"),
]
