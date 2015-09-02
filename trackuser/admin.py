from django.contrib import admin
from trackuser.models import Create



class NewUsers(admin.ModelAdmin):
	display_list = ['username','password']

	class Meta:
		model = Create
# Register your models here.
admin.site.register(Create,NewUsers)
