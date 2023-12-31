from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ('owner', 'flat')

@admin.register
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    inlines = [OwnerInline, ]

@admin.register
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat',)

@admin.register
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats', )



