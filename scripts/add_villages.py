import json
from village.models import Village
def run():
    with open("locations.json", "r") as f:
        location_data = json.load(f)

    for location in location_data:
        Village.objects.create(
            name=location["name"],
            latitude=location["latitude"],
            longitude=location["longitude"]
        )

    for location in Village.objects.all():
        location.save()
