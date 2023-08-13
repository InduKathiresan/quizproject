from django.urls import path
from .views import QuizListView,quiz_view,quiz_data_view,save_quiz_view,handlelogin,signup,handlelogout

app_name = 'quizes'

urlpatterns = [
    path('quiz/',QuizListView.as_view(),name='main-view'),
    path('',handlelogin, name = "handlelogin"),
    path('logout/',handlelogout, name = "handlelogout"),
    path('signup/',signup, name = "signup"),
    path('quiz/<pk>/',quiz_view,name='quiz-view'),
    path('quiz/<pk>/save/',save_quiz_view,name='save-view'),
    path('quiz/<pk>/data/',quiz_data_view,name='quiz-data-view'),
]

