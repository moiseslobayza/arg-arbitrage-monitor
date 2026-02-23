# Real-Time Financial Arbitrage Monitor 📊

Este proyecto implementa un sistema de monitoreo de **arbitraje financiero** en tiempo real, diseñado para detectar ineficiencias de precios entre el mercado de capitales tradicional (CCL) y el mercado de criptoactivos (Dólar Cripto) en Argentina.

## 🚀 Descripción Técnica

El sistema está diseñado bajo una arquitectura de microservicios contenerizados, priorizando la precisión matemática y la persistencia de datos para análisis histórico.

### Lógica Cuantitativa

El núcleo del monitor calcula el spread entre dos tipos de cambio implícitos:

**1) Dólar CCL (Contado con Liqui).**  
Calculado a través del ratio del ADR de Grupo Galicia (NASDAQ: GGAL) y su contraparte local (BCBA: GGAL), aplicando el factor de conversión correspondiente.

$$
CCL=\frac{Precio_{Local}\times 10}{Precio_{ADR}}
$$

**2) Dólar Cripto (Implícito).**  
Calculado mediante triangulación de arbitraje utilizando Bitcoin como activo puente.

$$
D_{Cripto}=\frac{BTC_{ARS}}{BTC_{USDT}}
$$

**3) Spread (Brecha).**

$$
Spread_{pct}=\left(\frac{D_{Cripto}-CCL}{CCL}\right)\times 100
$$

## 🛠 Tech Stack

* **Lenguaje:** Python 3.10
* **Base de Datos:** PostgreSQL 15 (Series temporales de precios)
* **Contenerización:** Docker & Docker Compose
* **APIs:**
    * `ccxt`: Conexión optimizada a Binance (Manejo de Rate Limits y Latencia).
    * `yfinance`: Extracción de datos de Equity (NASDAQ/MERVAL).

## ⚙️ Instalación y Ejecución

El proyecto es agnóstico al sistema operativo gracias a Docker.

### Prerrequisitos
- Docker y Docker Compose instalados.

### Despliegue

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/moiseslobayza/arbitrage-monitor.git
   cd arbitrage-monitor


2. Iniciar el entorno:
   ```bash
   docker-compose up --build -d
   ```


3. Ver logs en tiempo real:
   ```bash
   docker logs -f python_arbitraje_app
   ```

## 🗄 Estructura de Datos

El sistema persiste cada *snapshot* del mercado en PostgreSQL para permitir análisis posteriores de volatilidad y reversión a la media.

| Columna | Tipo | Descripción |
| :--- | :--- | :--- |
| `timestamp` | TIMESTAMP | Momento exacto de la captura (UTC) |
| `ccl_val` | REAL | Valor calculado del Contado con Liqui |
| `dolar_cripto` | REAL | Valor calculado del Dólar Cripto |
| `ticker_adr` | REAL | Precio GGAL (NASDAQ) |
| `ticker_local` | REAL | Precio GGAL (MERVAL) |

## Próximos Pasos (Roadmap)

[ ] Implementación de aiohttp para peticiones asíncronas y reducción de latencia.

[ ] Integración de alertas via Telegram Bot ante spreads > 2%.

[ ] Dashboard en vivo (Streamlit/Power BI) conectado a la instancia de Postgres.

Autor: Moisés Lobayza

Proyecto desarrollado para análisis de microestructura de mercado.

## ⚖️ Disclaimer

Este software tiene fines puramente educativos y de investigación sobre la microestructura del mercado. El trading de activos financieros conlleva riesgos significativos. El autor no se responsabiliza por pérdidas financieras derivadas del uso de esta herramienta.


