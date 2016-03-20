from django.contrib import admin

from .models import (
    Project,
    Milestone,
    Ticket,
)

# Inline´s

class TicketInline(admin.TabularInline):
    model = Ticket


class MilestoneInline(admin.TabularInline):
    model = Milestone


# ModelAdmin´s

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [TicketInline, MilestoneInline]
