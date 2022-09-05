from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(Me)
admin.site.register(Clients)
admin.site.register(CodingSkill)
admin.site.register(Frameworks)
admin.site.register(Portfolio)
admin.site.register(Certificates)
admin.site.register(Testimonials)
admin.site.register(Blogs_Links)