from django.contrib import admin
from .models import BookStore, Author, Address, Countries


class BookStoreAdmin(admin.ModelAdmin):
    # readonly_fields = ('slug',)  # Read-only slug field
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('rating', 'author',)
    list_display = ('title', 'author')

# Register the BookStore model with its associated BookStoreAdmin class
admin.site.register(BookStore, BookStoreAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Countries)