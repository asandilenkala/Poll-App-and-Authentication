from django.urls import path
from . import views

# Define the namespace for the app's URL names
app_name = 'polls'

# Define the URL patterns for the polls app
urlpatterns = [
    # URL pattern for the index view (homepage of the polls app)
    path('', views.index, name='index'),

    # URL pattern for the register view (user registration page)
    path('register/', views.register, name='register'),

    # URL pattern for the login view (user login page)
    path('login/', views.user_login, name='login'),

    # URL pattern for the detail view (detailed view of a specific question)
    path('<int:question_id>/', views.detail, name='detail'),

    # URL pattern for the results view (results of a specific question)
    path('<int:question_id>/results/', views.results, name='results'),

    # URL pattern for the vote view (submitting a vote for a specific question)
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
