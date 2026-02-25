"""SQLAlchemy ORM models (database tables)."""

import uuid
from datetime import datetime
from sqlalchemy import Column, String, Text, DateTime, Index
from app.database import Base


class Alerta(Base):
    """Stores the result of each TamboEngine AI analysis."""

    __tablename__ = "alertas"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    id_establecimiento = Column(String, nullable=False, index=True)
    periodo = Column(String, nullable=False)
    estado_general = Column(String, nullable=False)       # "normal" | "alerta" | "critico"
    resumen_ejecutivo = Column(Text, nullable=False)
    desvios_json = Column(Text, nullable=False)            # JSON serializado
    recomendaciones_json = Column(Text, nullable=False)    # JSON serializado
    creado_en = Column(DateTime, default=datetime.utcnow, nullable=False)

    __table_args__ = (
        Index("ix_alertas_establecimiento_fecha", "id_establecimiento", "creado_en"),
    )
