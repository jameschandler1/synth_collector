from django.urls import path
from . import views


# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('index/', views.Index.as_view(), name='index'),
    path('synths/', views.SynthList.as_view(), name='synths'),
    path('synths/new/', views.NewSynth.as_view(), name='new_synth'),
    path('synths/<int:pk>/', views.SynthInfo.as_view(), name='synth_info'),
    path('synths/<int:pk>/update/', views.SynthUpdate.as_view(), name='synth_update'),
    path('synths/<int:pk>/delete/', views.SynthDelete.as_view(), name='synth_del_confirm'),
    path('synths/<int:pk>/reviews/', views.NewReview.as_view(), name='new_review'),
    path('synths/reviews/', views.NewReviewFromNav.as_view(), name='nav_new_review'),
    path('synths/<int:pk>/reviews/<int:review>/edit/', views.ReviewEdit.as_view(), name='edit_review'),
    path('registation/signup/', views.SignUp.as_view(), name="signup")
]