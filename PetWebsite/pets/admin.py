from django.contrib import admin
from pets.models import Pet,Contact

# Register your models here.



class PetAdmin(admin.ModelAdmin):
	list_display = ('name', 'age', 'gender','sterilization','region','health','other','pic_name','contact')
	

class ContactAdmin(admin.ModelAdmin):
	list_display = ('name','gender','phone','email','address')




admin.site.register(Pet,PetAdmin)
admin.site.register(Contact,ContactAdmin)

