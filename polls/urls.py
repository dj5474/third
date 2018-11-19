from click import edit
from django.contrib import admin
from django.urls import path
from imageio import save

from polls import views
from polls.views import index, detail, detail2, vote

urlpatterns = [
    path('', index),
    path('<int:question_id>/', detail, name='detail'),
    #    polls/1/, polls/100/
    path('<int:num1>/<int:num2>', detail2),
    # path('<int:question_id>/results/', results),
    path('<int:question_id>/vote/', vote),
    path('<int:question_id>/edit', edit),
    path('<int:question_id>/save', save)
]
