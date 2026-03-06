from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import  User,OrderItem, Product
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['email', 'username', 'first_name', 'is_staff']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('username', 'email', 'password1', 'password2'),
    }),
)
admin.site.register(User, CustomUserAdmin)

class OrderItemInline(admin.TabularInline):  # Corrected to use TabularInline
    
    model = OrderItem
    extra = 1
    fields = ['product', 'quantity', 'price']
    readonly_fields = ['price']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description']
    search_fields = ['name']
    list_filter = ['price']

    inlines = [OrderItemInline
               
               
]



admin.site.register(Product, ProductAdmin)

# Register your models here.



