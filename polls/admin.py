# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Question, Choice, Item

class ItemAdmin(admin.ModelAdmin):
	class Media:
		css = {
			"cal": ("static/schedule.css",)
		}
		js = ("static/schedule.js",)

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 	{'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question_text']	

admin.site.register(Question, QuestionAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.site_header = 'Administration stuffs'
# Register your models here.
