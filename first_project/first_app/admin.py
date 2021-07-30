from django.contrib import admin
from first_app.models import Topic,Webpage,Access_record,custom_form_modal
# Register your models here.

admin.site.register(Access_record)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(custom_form_modal)

#redskull