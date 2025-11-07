from servicios.base_de_datos import engine
from sqlalchemy import text

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT NOW()"))
        print(" Conectado a Supabase. Hora del servidor:", result.scalar())
except Exception as e:
    print("Error de conexión:", e)
