from django.core.management.base import BaseCommand
from core.models import Forum, Category
from decouple import config
import requests
from django.conf import settings
import os

class Command(BaseCommand):
    help = "Query NASA API and save and save the result to the database"


    def handle(self, *args, **kwargs):
        API_KEY = config('API_KEY')
        URL = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"
        response = requests.get(URL)
        data = response.json()
        img_link = data['url']
        img_name = data['url'].split('/')[-1]
        r = requests.get(img_link)
        img = r.content
        media_picture = 'Forum_pic/'
        relative_path = os.path.join(settings.MEDIA_ROOT, media_picture, img_name)
        with open(relative_path, "wb") as file:
            file.write(img)

        try:
            category = Category.objects.filter(Category_name='Geography')
            Geo_data = Forum.objects.create(Category_name = category[0], title=data['title'], description=data['explanation'], picture=f'{media_picture}/{img_name}')
            Geo_data.save()
        except Exception as e:
            raise e

        self.stdout.write(self.style.SUCCESS("Data inserted successfully"))

    