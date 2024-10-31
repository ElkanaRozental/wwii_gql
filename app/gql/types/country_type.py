from graphene import ObjectType, Int, Date, String


class CountryType(ObjectType):
    country_id = Int()
    country_name = String()
