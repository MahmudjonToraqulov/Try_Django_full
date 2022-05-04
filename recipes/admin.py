from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import RecipeIngredient,Recipe

User = get_user_model()
 
class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    extra = 0

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = [ 'name','user' ]
    readonly_fields = [ 'timestamp','updated'  ]
    raw_id_fields = ['user']

admin.site.register(Recipe,RecipeAdmin)

