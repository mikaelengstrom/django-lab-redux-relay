from graphene import (relay, ObjectType)
from graphene.contrib.django.filter import DjangoFilterConnectionField
from graphene.contrib.django.types import (DjangoNode, )

from .models import (Ticket, Milestone, Project)


class ProjectNode(DjangoNode):
    class Meta:
        model = Project
        filter_fields = ['title']


class MilestoneNode(DjangoNode):
    class Meta:
        model = Milestone
        filter_fields = ['title', 'project', 'tickets']
        filter_order_by = ['project', 'title']


class TicketNode(DjangoNode):
    class Meta:
        model = Ticket
        filter_fields = {
            'title': ['exact', 'icontains'],
            'done': ['exact'],
            'milestone': ['exact']
        }
        filter_order_by = ['title']


class Query(ObjectType):
    project = relay.NodeField(ProjectNode)
    all_projects = DjangoFilterConnectionField(ProjectNode)

    milestone = relay.NodeField(MilestoneNode)
    all_milestones = DjangoFilterConnectionField(MilestoneNode)

    ticket = relay.NodeField(TicketNode)
    all_tickets = DjangoFilterConnectionField(TicketNode)

    class Meta:
        abstract = True

