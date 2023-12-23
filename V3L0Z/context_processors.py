from home.models import Setting

def settings(request):
    return {'settings': Setting.objects.first()}