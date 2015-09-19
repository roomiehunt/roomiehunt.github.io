from django.contrib import admin
from .models import messages,threads,thread_messages


admin.site.register(messages)
admin.site.register(threads)

admin.site.register(thread_messages)
# Register your models here.
