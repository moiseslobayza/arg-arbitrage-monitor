import yfinance as yf
import ccxt
import time
from datetime import datetime

class MarketFetcher:
    def __init__(self):
        # Configuración de CCXT con timeout para evitar bloqueos
        self.exchange = ccxt.binance({
            'enableRateLimit': True,  # CCXT gestiona la espera básica automáticamente
            'options': {'defaultType': 'spot'}
        })
    
    def get_stock_price(self, ticker):
        """Trae precio de Acciones desde Yahoo con manejo de errores."""
        try:
            # interval='1m' es inestable en yfinance gratuito. Usamos '1d' para cierre o validamos
            data = yf.download(ticker, period='1d', interval='1m', progress=False)
            if not data.empty:
                # Accedemos al último valor disponible
                return float(data['Close'].iloc[-1].item())
            return None
        except Exception as e:
            print(f"⚠️ [WARN YF] Fallo al traer {ticker}: {e}")
            return None

    def get_crypto_price(self, symbol):
        """Trae precio Cripto desde Binance con manejo de Rate Limits."""
        try:
            ticker = self.exchange.fetch_ticker(symbol)
            return float(ticker['last'])
        except ccxt.RateLimitExceeded as e:
            print(f"🛑 [RATE LIMIT] Binance nos frenó. Esperando 5s... ({e})")
            time.sleep(5) # Backoff simple
            return None
        except ccxt.NetworkError as e:
            print(f"⚠️ [NETWORK] Error de conexión con Binance: {e}")
            return None
        except Exception as e:
            print(f"❌ [ERROR BINANCE] Fallo crítico en {symbol}: {e}")
            return None
    
    def get_market_snapshot(self, stock_tickers, crypto_pairs):
        # 1. Extracción
        adr_price = self.get_stock_price(stock_tickers['ADR'])
        local_price = self.get_stock_price(stock_tickers['LOCAL'])
        
        btc_usdt = self.get_crypto_price(crypto_pairs['BTC_USDT'])
        btc_ars = self.get_crypto_price(crypto_pairs['BTC_ARS'])
        
        # Validamos que tengamos TODOS los datos antes de calcular
        if None in [adr_price, local_price, btc_usdt, btc_ars]:
            return None # Retornamos None para que el Main sepa que falló

        # 2. Cálculos Financieros.
        
        # Factor de conversión GGAL: 1 ADR = 10 Acciones Locales
        CONVERSION_FACTOR = 10 
        ccl_implied = (local_price / adr_price * CONVERSION_FACTOR)
        
        # Dólar Cripto: Precio Implícito de arbitraje BTC/ARS vs BTC/USDT
        dolar_crypto = (btc_ars / btc_usdt)
        
        return {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'GGAL_NASDAQ': adr_price,
            'GGAL_MERVAL': local_price,
            'CCL_IMPLICITO': round(ccl_implied, 2),
            'BTC_USDT': btc_usdt,
            'BTC_ARS': btc_ars,
            'DOLAR_CRIPTO': round(dolar_crypto, 2)
        }