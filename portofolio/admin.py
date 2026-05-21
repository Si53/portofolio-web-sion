from django.contrib import admin
from .models import (
    Skill,
    Experience,
    ExperiencePoint,
    ExperienceLink,
    Education,
    ContactLink,
)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "image_path", "order")
    list_editable = ("order",)
    search_fields = ("name",)


class ExperiencePointInline(admin.TabularInline):
    model = ExperiencePoint
    extra = 1


class ExperienceLinkInline(admin.TabularInline):
    model = ExperienceLink
    extra = 1


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("title", "period", "image_path", "order")
    list_editable = ("order",)
    search_fields = ("title", "period")
    inlines = [ExperiencePointInline, ExperienceLinkInline]


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("institution", "year", "major", "logo_path", "order")
    list_editable = ("order",)
    search_fields = ("institution", "major")


@admin.register(ContactLink)
class ContactLinkAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "icon_class", "order")
    list_editable = ("order",)
    search_fields = ("name",)