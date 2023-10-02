from village.models import Village

def run():
    villages = Village.objects.all()
    villages.delete()