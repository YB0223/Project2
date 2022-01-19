from django.contrib import admin

from IdeaShare.models import user_data,category_data,post_data,Time_stamp
# Register your models here.

admin.site.register(user_data)
admin.site.register(Time_stamp)
admin.site.register(category_data)
admin.site.register(post_data)

