from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum

from core.models import LeaderBoard


class LeaderBoardAPIView(APIView):
    '''
    APIView for Fetching all data using date range
    and username
    '''

    def post(self, request):
        '''
        Take post data and return result on basis of the data posted
        '''

        try:
            start_date = request.data.get('start_date')
            end_date = request.data.get('end_date')
            username = request.data.get('username')

            result = LeaderBoard.objects.filter(timestamp__gt=start_date).filter(timestamp__lt=end_date).order_by('-score').annotate(total_score=Sum('score'))[:10]

            # Checking the user present or not
            found = 0
            for person in result:
                if person.user == username:
                    found = 1
                    break
            
            # if user not present we fetch user then previous record 
            #    from that user and next record from that user
            if found == 0:
                second_result = LeaderBoard.objects.get(user=username)
                prev_rec = second_result.id - 1
                next_rec = second_result.id + 1
                third_result = LeaderBoard.objects.get(id=prev_rec)
                fourth_result = LeaderBoard.objects.get(id=next_rec)
                result = result + second_result + third_result + fourth_result

            response_list = [
                {
                    "id": item.id,
                    "score": item.score,
                    "timestamp": item.timestamp
                }

                for item in result
            ]

            return Response(response_list)
        except Exception as e:
            return Response("error": e)