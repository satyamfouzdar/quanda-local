from django.urls import path
from . import views


urlpatterns = [
    path('questions/', views.questions, name="questions"),
    path('latestquestions/', views.latestquestions, name="latestquestions"),
    path('questions/tag/<slug:slug>',views.tagged,name='tags'),
    path('addquestion/', views.addquestion, name="addquestion"),
    path('question/<int:pk>', views.question_detail, name="question-detail"),
    path('addanswer/<int:q_id>', views.add_answer, name="addanswer"),
]

