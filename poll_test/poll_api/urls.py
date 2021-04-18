from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.user_login, name='login'),
    path('pol/<int:pk>/questions/', views.IndexDetailView.as_view(), name='question_list'),
    # Получить всех пользователей
    path('users/', views.UserList.as_view()),
    # Детальная информация по конкретному пользователю
    path('users/<int:pk>/', views.UserDetail.as_view()),
    # Получить все опросы
    path('polls/', views.PollList.as_view(), name='api'),
    # Выбрать конкретный опросник
    path('polls/<int:poll_id>/', views.PollDetail.as_view()),
    # Получить все вопросы по конкретному опроснику
    path('polls/<int:poll_id>/questions/', views.QuestionList.as_view()),
    # Получить определённый вопрос у текущего опросника
    path('polls/<int:poll_id>/questions/<int:question_id>/', views.QuestionDetail.as_view()),
    # Получить все ответы по текущему вопросу
    path('polls/<int:poll_id>/questions/<int:question_id>/answers/', views.AnswerList.as_view()),
    # Получить конкретный ответ у текущего вопроса
    path('polls/<int:poll_id>/questions/<int:question_id>/answers/<int:answer_id>/', views.AnswerDetail.as_view()),
    # Итоговая информация
    path('fills/', views.FillPollList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
