from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from boards import views
urlpatterns = [
    path('', views.home, name='home'),
    path('boards/<int:pk>/', views.board_topics, name='board_topics'),
    path('boards/<int:pk>/new/', views.new_topic, name='new_topic'),
    path('boards/<pk>/topics/<topic_pk>', views.topic_posts, name='topic_posts'),
    path('boards/<pk>/topics/<topic_pk>/reply', views.reply_topic, name='reply_topic'),
    path('boards/<pk>/topics/<topic_pk>/posts/<post_pk>/edit',
        views.PostUpdateView.as_view(), name='edit_post'),
    path('admin/', admin.site.urls),
]