from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Notice, Problem, Member, Solve

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class MemberInline(admin.StackedInline):
    model = Member
    can_delete = False
    verbose_name_plural = 'member'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (MemberInline, )


admin.site.register(Notice)
admin.site.register(Problem)
admin.site.register(Solve)
# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)