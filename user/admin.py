from django.contrib import admin
from .models.user import User
from .forms.user import UserAdminForm
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    model = User
    add_form = UserAdminForm
    form = UserAdminForm
    list_display = ['email', 'admin', 'last_login']
    search_fields = ['email']
    list_filter = ['admin', 'staff', 'active']


admin.site.register(User, UserAdmin)