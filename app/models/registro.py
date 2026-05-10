from .db import db
from .base import Base

class Registro(Base):
    __tablename__ = "registros"

    nivel_foco = db.Column(db.Integer, nullable=False)
    tempo_minutos = db.Column(db.Integer, nullable=False)
    comentario = db.Column(db.String(255), nullable=False)
    categoria = db.Column(db.String(250), nullable=True)