from rest_framework import viewsets

from core.models import LeaderBoard
from core.serializers import LeaderBoardSerializer


class LeaderBoardViewSet(viewsets.ModelViewSet):
    '''
    Viewset for LeaderBoard Models
    '''

    serializer_class = LeaderBoardSerializer
    queryset = LeaderBoard.objects.all()