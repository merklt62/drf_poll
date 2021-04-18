from django.contrib import admin
from .models import Poll, Question, Answer


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 2


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('poll_name',)

    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'order', 'poll')

    inlines = [AnswerInline]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'text', 'order')


# @admin.register(FillPoll)
# class FillPollAdmin(admin.ModelAdmin):
#     list_display = ('answer_choice',)
