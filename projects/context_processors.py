from projects.models import Social

def social(request):
    social = Social.objects.last()
    return {'social': social}