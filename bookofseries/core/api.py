from ninja import NinjaAPI, Schema

api = NinjaAPI()


class Item(Schema):
    name_column: list


@api.post("/filter")
def filter(request, item: Item):

    return 1



