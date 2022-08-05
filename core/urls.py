from django.urls import path
from rest_framework.routers import DefaultRouter
from core.viewsets import LeaderBoardViewSet
from core.views import LeaderBoardAPIView

urlpatterns = [
    path('test', LeaderBoardAPIView.as_view(), name='test')
]

router = DefaultRouter()
router.register('leader-board', LeaderBoardViewSet, 'leader-board')

urlpatterns += router.urls