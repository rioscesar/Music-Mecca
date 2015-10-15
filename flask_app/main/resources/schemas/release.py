from marshmallow import fields
from marshmallow import Schema


class ReleaseSchema(Schema):
    """Marshmallow Schema class for the Release model."""
    id = fields.Integer()
    name = fields.String(required=True)
    year = fields.String(allow_none=True)

    artist = fields.List(fields.Nested('ArtistSchema'))

