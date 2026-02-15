# src/config.py

# 1. Tickers para Yahoo Finance (SOLO Acciones)
TICKERS_YFINANCE = {
    'ADR': 'GGAL',
    'LOCAL': 'GGAL.BA'
}

# 2. Pares para Binance (Toda la Cripto)
# Binance tiene el par BTC/ARS directo, usémoslo.
CRYPTO_PAIRS = {
    'BTC_USDT': 'BTC/USDT',
    'BTC_ARS': 'BTC/ARS'
}