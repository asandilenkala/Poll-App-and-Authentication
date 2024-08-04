from django.contrib import admin
from .models import Question, Choice

# Register your models here.

# The ChoiceInline class allows you to edit choices related to a question directly in the Question admin page.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # Number of extra empty choice forms to display

# The QuestionAdmin class customizes the admin interface for the Question model.
class QuestionAdmin(admin.ModelAdmin):
    # fieldsets allows grouping of related fields in the admin form layout.
    fieldsets = [
        (None, {'fields': ['question_text']}),  # Group containing the question text field.
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),  # Group containing the publication date field, initially collapsed.
    ]
    inlines = [ChoiceInline]  # Adds the ChoiceInline to the Question admin page.
    
    # list_display defines the columns to display on the change list page.
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    
    # list_filter adds filters in the right sidebar of the change list page.
    list_filter = ['pub_date']
    
    # search_fields adds a search box at the top of the change list page.
    search_fields = ['question_text']

# Register the Question model with the QuestionAdmin configuration.
admin.site.register(Question, QuestionAdmin)
