from django.contrib import admin
from .models import *


admin.site.register(Post)
admin.site.register(CarCountry)
admin.site.register(CarType)
admin.site.register(CarProblemLocation)
admin.site.register(Like)
admin.site.register(Comment)
