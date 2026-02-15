# src/db_manager.py
import psycopg2
import os


class DBManager:
    def __init__(self):
        # Si corre en Docker usa 'db', si corre afuera usa 'localhost'
        self.db_config = {
            "host": os.getenv('DB_HOST', 'localhost'),
            "database": "arbitrage_db",
            "user": "postgres",
            "password": "secret",
            "port": "5433" 
        }
    
    def get_connection(self):
        """Crea y devuelve una nueva conexión a la BD."""
        return psycopg2.connect(**self.db_config)
    
    def insert_snapshot(self, data):
        """Recibe el diccionario de datos y lo guarda en SQL."""
        conn = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            # Query Parametrizada
            # Nota: No insertamos 'id' ni 'timestamp' porque son SERIAL y DEFAULT respectivamente
            query = """
            INSERT INTO market_data 
            (ticker_adr, ticker_local, ccl_val, btc_usdt, btc_ars, dolar_cripto)
            VALUES (%s, %s, %s, %s, %s, %s);
            """
            
            # Mapeo de datos: Diccionario Python -> Columnas SQL
            values = (
                data.get('GGAL_NASDAQ'),   # ticker_adr
                data.get('GGAL_MERVAL'),   # ticker_local
                data.get('CCL_IMPLICITO'), # ccl_val
                data.get('BTC_USDT'),      # btc_usdt
                data.get('BTC_ARS'),       # btc_ars (NUEVO)
                data.get('DOLAR_CRIPTO')   # dolar_cripto (NUEVO)
            )
            
            cursor.execute(query, values)
            conn.commit() 
            print(f"✅ [DB] Snapshot guardado: CCL {data.get('CCL_IMPLICITO')} vs Cripto {data.get('DOLAR_CRIPTO')}")
            
        except Exception as e:
            print(f"❌ [DB Error] Fallo al insertar: {e}")
            if conn:
                conn.rollback() 
        finally:
            if conn:
                cursor.close()
                conn.close()