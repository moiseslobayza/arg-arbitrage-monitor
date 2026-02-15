import time

from src.config import TICKERS_YFINANCE, CRYPTO_PAIRS 
from src.data_loader import MarketFetcher
from src.db_manager import DBManager

def run():
    print("--- Iniciando Monitor de Arbitraje v2.0 (Multi-Source) ---")
    print(f"Modo: Acciones via Yahoo | Cripto via Binance")
    
    fetcher = MarketFetcher()
    db_manager = DBManager()
    
    try:
        while True:
            # 1. Extracción (Ahora pasamos los dos diccionarios de configuración)
            print("⏳ Obteniendo snapshot del mercado...")
            data = fetcher.get_market_snapshot(TICKERS_YFINANCE, CRYPTO_PAIRS)
            
            # 2. Validación y Persistencia
            # Verificamos que tengamos al menos los datos críticos para calcular arbitraje
            if data['GGAL_NASDAQ'] and data['BTC_USDT'] and data['BTC_ARS']:
                
                db_manager.insert_snapshot(data)
                
                # Feedback visual en consola para que sepas que está vivo
                print(f"   📊 GGAL Local: ${data['GGAL_MERVAL']:.2f} | ADR: ${data['GGAL_NASDAQ']:.2f}")
                print(f"   💰 CCL Implícito: ${data['CCL_IMPLICITO']:.2f}")
                print(f"   🪙 Dólar Cripto:  ${data['DOLAR_CRIPTO']:.2f}")
                
                # ¡EL DATO CLAVE! La brecha de arbitraje
                spread = data['DOLAR_CRIPTO'] - data['CCL_IMPLICITO']
                spread_pct = (spread / data['CCL_IMPLICITO']) * 100
                print(f"   ⚡ BRECHA: {spread_pct:.2f}% (${spread:.2f} ARS)")
                print("-" * 50)
                
            else:
                print("⚠️ Datos incompletos (posible fallo de API), reintentando en breve...")
            
            # 3. Espera (60 segundos)
            time.sleep(60)
            
    except KeyboardInterrupt:
        print("\n🛑 Monitor detenido por el usuario.")
    except Exception as e:
        print(f"\n💥 Error Crítico en Main: {e}")

if __name__ == "__main__":
    run()