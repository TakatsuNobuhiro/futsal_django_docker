import factory
from factory import fuzzy

from ..models import Member, Club


class MemberFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Member

    first_name = fuzzy.FuzzyText(length=5)
    last_name = fuzzy.FuzzyText(length=3)


class ClubFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Club

    name = fuzzy.FuzzyText(length=5)
