# src/data_loader.py
import yfinance as yf
import ccxt
from datetime import datetime

class MarketFetcher:
    def __init__(self):
        # Conectamos a Binance (Público, sin claves por ahora)
        self.exchange = ccxt.binance()
    
    def get_stock_price(self, ticker):
        """Trae precio de Acciones desde Yahoo."""
        try:
            data = yf.download(ticker, period='1d', interval='1m', progress=False)
            if not data.empty:
                return data['Close'].iloc[-1].item()
            return None
        except Exception as e:
            print(f"[ERROR YF] Fallo al traer {ticker}: {e}")
            return None

    def get_crypto_price(self, symbol):
        """Trae precio Cripto desde Binance."""
        try:
            ticker = self.exchange.fetch_ticker(symbol)
            # Binance devuelve 'last' como el último precio operado
            return ticker['last']
        except Exception as e:
            print(f"[ERROR BINANCE] Fallo al traer {symbol}: {e}")
            return None
    
    def get_market_snapshot(self, stock_tickers, crypto_pairs):
        # 1. Extracción
        # Acciones desde Yahoo
        adr_price = self.get_stock_price(stock_tickers['ADR'])
        local_price = self.get_stock_price(stock_tickers['LOCAL'])
        
        # Cripto desde Binance (¡El cambio clave está aquí!)
        btc_usdt = self.get_crypto_price(crypto_pairs['BTC_USDT'])
        btc_ars = self.get_crypto_price(crypto_pairs['BTC_ARS'])
        
        # 2. Cálculos Financieros
        # CCL Implícito (Galicia)
        ccl_implied = (local_price / adr_price * 10) if (local_price and adr_price) else 0
        
        # Dólar Cripto (Arbitraje de BTC)
        # Fórmula: Cuánto me pagan el BTC en pesos / Cuánto vale en USDT
        dolar_crypto = (btc_ars / btc_usdt) if (btc_ars and btc_usdt) else 0
        
        return {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'GGAL_NASDAQ': adr_price,
            'GGAL_MERVAL': local_price,
            'CCL_IMPLICITO': round(ccl_implied, 2),
            'BTC_USDT': btc_usdt,
            'BTC_ARS': btc_ars,
            'DOLAR_CRIPTO': round(dolar_crypto, 2)
        }