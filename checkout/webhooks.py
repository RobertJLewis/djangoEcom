from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def webhook(request):
    """
    Placeholder Stripe webhook handler.
    You can expand this later to handle Stripe events.
    """
    return HttpResponse(status=200)
