# src/create_tables.py
import psycopg2

def create_tables():
    try:
        conn = psycopg2.connect(host="localhost", database="arbitrage_db", user="postgres", password="secret")
        cursor = conn.cursor()
        
        # 1. BORRAMOS la tabla vieja (Reset)
        cursor.execute("DROP TABLE IF EXISTS market_data;")
        
        # 2. Creamos la nueva con las columnas extra: btc_ars y dolar_cripto
        create_query = """
        CREATE TABLE market_data (
            id SERIAL PRIMARY KEY,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            ticker_adr REAL,
            ticker_local REAL,
            ccl_val REAL,
            btc_usdt REAL,
            btc_ars REAL,        -- Nuevo
            dolar_cripto REAL    -- Nuevo (El cálculo final)
        );
        """
        cursor.execute(create_query)
        conn.commit()
        print("✅ Tabla 'market_data' RE-creada con nuevas columnas.")
        conn.close()
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    create_tables()