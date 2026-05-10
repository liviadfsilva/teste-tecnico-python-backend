from flask import Blueprint, jsonify, request
from app.schemas.registro_schema import RegistroSchema
from marshmallow import ValidationError
from app.models.registro import Registro
from app.models.db import db

registro = Blueprint("registro", __name__)

@registro.route("/diagnostico-produtividade", methods=["GET"])
def diagnostico_produtividade():
    registros = Registro.query.all()

    if not registros:
        return jsonify({"message": "Nenhum registro encontrado."}), 404

    total_registros = len(registros)

    soma_foco = sum(registro.nivel_foco for registro in registros)

    media_foco = round(soma_foco / total_registros, 2)

    tempo_total = sum(registro.tempo_minutos for registro in registros)

    if media_foco < 3:
        feedback = (
            "Seu nível de foco está baixo. "
            "Tente reduzir notificações e fazer pausas estratégicas."
        )

    elif media_foco < 4:
        feedback = (
            "Você está mantendo uma produtividade consistente, "
            "mas ainda há espaço para melhorar seu estado de flow."
        )

    else:
        feedback = (
            "Você está em uma maratona produtiva de alto nível 🚀"
        )

    return jsonify({
        "media_nivel_foco": media_foco,
        "tempo_total_focado": tempo_total,
        "feedback": feedback
    }), 200

@registro.route("/registro-foco", methods=["GET"])
def listar_registros():
    registros = Registro.query.all()
    schema = RegistroSchema(many=True)

    return jsonify(schema.dump(registros)), 200

@registro.route("/registro-foco", methods=["POST"])
def registrar_foco():
    data = request.get_json()
    schema = RegistroSchema()

    try:
        dados_validados = schema.load(data)

    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    novo_registro = Registro(**dados_validados)

    db.session.add(novo_registro)
    db.session.commit()

    resultado = schema.dump(novo_registro)

    return jsonify(resultado), 201