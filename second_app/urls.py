from django.urls import path
from . import views


urlpatterns = [
    # path('api/token/', views.obtain_jwt_token, name='token_obtain_pair'),
    # path('', views.get_Movies , name='get_Movies'),
    #  path('login/', views.login, name='login'),
    # path('Movies/create/', views.create_Movies, name='create_Movies'),
    # path('Movies/update/<int:pk>/', views.update_Movies, name='update_Movies'),
    # path('Movies/delete/<int:pk>/', views.delete_Movies, name='update_Movies'),

    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('test_token/', views.test_token, name='test_token'),
]
