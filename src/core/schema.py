import graphene

from apps.todo import schema as apps_schema


class Query(apps_schema.Query):
    pass


schema = graphene.Schema(name='Todo Schema')
schema.query = Query
