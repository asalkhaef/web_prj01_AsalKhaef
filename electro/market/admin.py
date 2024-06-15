from django.contrib import admin
from .models import *
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
# Register your models here.

# admin.site.register(Category)
# admin.site.register(Product)
# admin.site.register(Video)
# admin.site.register(Image)
# admin.site.register(DiscountCode)
# admin.site.register(PriceHistory)
# admin.site.register(User)
# admin.site.register(Cart)
# admin.site.register(Banner)

User = get_user_model()


class CustomUserAdmin(UserAdmin):
    # Customize the UserAdmin as needed
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login')


# Unregister the default UserAdmin
admin.site.unregister(User)

# Register User with CustomUserAdmin
admin.site.register(User, CustomUserAdmin)


# Register your models here.
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Discount)
admin.site.register(Product)
admin.site.register(Media)
admin.site.register(ProductPriceHistory)
admin.site.register(Color)
admin.site.register(Category)
admin.site.register(Banner)
