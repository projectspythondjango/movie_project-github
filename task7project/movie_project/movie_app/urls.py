from django.urls import path
from . import views
app_name='movie_app'

urlpatterns=[
    path('',views.index,name='index'),
    path('movie/<int:movieid>/',views.detail,name='detail'),
    path('add/',views.add_movies,name='add_movies'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')

]
