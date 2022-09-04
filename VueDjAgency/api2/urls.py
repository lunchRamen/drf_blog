from django.urls import path,include
from rest_framework import routers
# from api2.views import CommentViewSet
# from api2.views import PostViewSet
# from api2.views import UserViewSet
from api2 import views

# router = routers.DefaultRouter()
# router.register(r'user',UserViewSet)
# router.register(r'post',PostViewSet)
# router.register(r'comment',CommentViewSet)

urlpatterns=[
    path('post/', views.PostListAPIView.as_view(), name = 'post-list'),
    path('post/<int:pk>/',views.PostRetrieveAPIView.as_view(),name='post-detail'),
    path('comment/',views.CommentCreateAPIView.as_view(),name='comment-create'),
    path('post/<int:pk>/like/', views.PostLikeAPIView.as_view(), name='post-like'),

]
