from rest_framework import serializers

from core.models import LeaderBoard


class LeaderBoardSerializer(serializers.ModelSerializer):
    '''
    Serializer for LeaderBoard Models
    '''

    class Meta:
        model = LeaderBoard
        fields = '__all__'