from django.contrib import admin
from .models import Skill, Job, Bid


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    class Meta:
        model = Skill
        fields = '__all__'


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    class Meta:
        model = Job
        fields = '__all__'


@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    class Meta:
        model = Bid
        fields = '__all__'
