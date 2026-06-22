from core.models import Message


def unread_messages(request):
    if request.user.is_authenticated and request.path.startswith('/dashboard/'):
        return {'unread_count': Message.objects.filter(read=False).count()}
    return {}
