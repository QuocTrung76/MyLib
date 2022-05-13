from datetime import date
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
# Register your models here.
from .models import Author, Genre, Book, BookInstance

class BooksInline(admin.TabularInline):
    model = Book
    extra=0

#@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]
    #date_hierarchy='date_of_birth'
    #add another selection for date of birth
    # actions_on_bottom = True
    # actions_on_top = False
    # actions_selection_counter = True
    #list_display = ('date_of_birth',)

    # @admin.display(empty_value='???')
    # def date_of_birth(self, obj):
    #     return obj.first_name

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra=0

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

    inlines = [BooksInstanceInline]
    #list_filter = ('title',)
    #pass

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('book','status', 'borrower', 'due_back','id')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )

#admin.site.register(Book)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
#admin.site.register(BookInstance)



#@admin.register(Author)
# class AuthorAdminFilteradmin.SimpleListFilter):
#     pass


