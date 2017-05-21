import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

from src import models


class MeetupGroup(SQLAlchemyObjectType):
    class Meta:
        model = models.MeetupGroup
        interfaces = (relay.Node,)


class TeamUpCalendar(SQLAlchemyObjectType):
    class Meta:
        model = models.TeamUpCalendar
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_meetup_groups = SQLAlchemyConnectionField(MeetupGroup)
    all_teamup_groups = SQLAlchemyConnectionField(TeamUpCalendar)


schema = graphene.Schema(query=Query, types=[MeetupGroup, TeamUpCalendar])
