from django.contrib import admin
from .models import *
# from django_cassandra_engine.models import DjangoCassandraModelAdmin

admin.site.register(Post)
admin.site.register(CarCountry)
admin.site.register(CarType)
admin.site.register(CarProblemLocation)
admin.site.register(PostType)
