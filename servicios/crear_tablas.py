from servicios.base_de_datos import Base, engine
from modelos.producto import Producto 

print("Creando tablas en Supabase...")
Base.metadata.create_all(bind=engine)
print("Tablas creadas o ya existentes.")
