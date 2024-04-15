from django.conf import settings

def ioi_settings(request):
    return {'settings': {
        'SITE_TITLE': 'BOI 2024 Task Translation System',
        'CONTEST_TITLE': 'BOI 2024',
        'TIME_ZONE': settings.TIME_ZONE,
        'IMAGES_URL': '/media/images/',
    }}
