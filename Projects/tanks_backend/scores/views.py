import json

from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt

from .models import Scores

@csrf_exempt
def get_scores(request):
    try:
        order = request.GET.get('order');
        if not order:
            order = '-level'
        scores = Scores.objects.all().order_by(order)
        scores_list = []
        for score in scores:
            scores_list.append({
                'user': score.user,
                'level': score.level,
                'seconds_survived': score.seconds_survived,
                'missiles_fired': score.missiles_fired,
                'tanks_destroyed': score.tanks_destroyed
            })
        return JsonResponse(scores_list, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)})

@csrf_exempt
def post_score(request):
    try:
        data = json.loads(request.body)
        user = data['user']
        level = data['level']
        seconds_survived = data['seconds_survived']
        missiles_fired = data['missiles_fired']
        tanks_destroyed = data['tanks_destroyed']
        score = Scores(
            user=user,
            level = level,
            seconds_survived = seconds_survived,
            missiles_fired = missiles_fired,
            tanks_destroyed =  tanks_destroyed
            )
        score.save()
        return JsonResponse({"message": 'Score Saved'})
    except Exception as e:
        return JsonResponse({'error': f'Error posting score {e}'})
