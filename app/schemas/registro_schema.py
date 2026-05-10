from marshmallow import Schema, fields, validate


class RegistroSchema(Schema):
    id = fields.Int(dump_only=True)

    nivel_foco = fields.Int(
        required=True,
        validate=validate.Range(min=1, max=5)
    )

    tempo_minutos = fields.Int(
        required=True,
        validate=validate.Range(min=1)
    )

    comentario = fields.Str(
        required=True,
        validate=validate.Length(min=3, max=255)
    )

    categoria = fields.Str(required=False)