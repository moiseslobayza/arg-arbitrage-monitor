# Real-Time Financial Arbitrage Monitor (Argentina) 📈

Sistema de monitoreo en tiempo real diseñado para detectar y alertar sobre oportunidades de arbitraje financiero, con un enfoque específico en las brechas del mercado argentino (Dólar MEP, CCL, Cripto y activos locales).

Este proyecto está desarrollado como parte de mi portafolio profesional, demostrando habilidades en manejo de datos financieros, conectividad vía APIs/WebSockets y optimización de algoritmos de cálculo.

## 🚀 Descripción

El monitor analiza flujos de datos en tiempo real de diversos exchanges y fuentes de mercado para identificar ineficiencias de precios. Está diseñado para procesar grandes volúmenes de datos con baja latencia, permitiendo visualizar el "spread" neto antes de que el mercado se equilibre.

## 🛠️ Stack Tecnológico

* **Lenguaje:** Python.
* **Gestión de Datos:** Manejo de estructuras eficientes para cálculo de spreads.
* **Seguridad:** Arquitectura basada en variables de entorno para protección de secretos.
* **Entorno de Desarrollo:** Optimizado para hardware de alto rendimiento (NVIDIA RTX 5070).

## 📊 Características Principales

* **Detección de Arbitraje:** Cálculo instantáneo de brechas entre múltiples plataformas.
* **Filtro de Comisiones:** Los cálculos descuentan automáticamente los fees de cada plataforma para mostrar la ganancia real.
* **Arquitectura Robusta:** Manejo de errores de conexión y reconexión automática a WebSockets.
* **Seguridad Primero:** Implementación estricta de `.gitignore` para evitar la filtración de claves privadas.

## ⚙️ Instalación y Configuración

1. **Clonar el repositorio:**
```bash
git clone https://github.com/moiseslobayza/arg-arbitrage-monitor.git
cd arg-arbitrage-monitor

```


2. **Configurar el entorno virtual:**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt

```


3. **Variables de Envorno:**
Crea un archivo `.env` en la raíz del proyecto y completa con tus credenciales. **Nunca compartas este archivo.**
```env
# API Keys de Exchanges
API_KEY_EXCHANGE_A=tu_clave_aqui
API_SECRET_EXCHANGE_A=tu_secreto_aqui

# Configuración de Alertas
TELEGRAM_TOKEN=tu_token_si_aplica

```


4. **Ejecutar el Monitor:**
```bash
python main.py

```



## 📝 Roadmap

* [ ] Integración de notificaciones push vía Telegram.
* [ ] Interfaz gráfica (Dashboard) para visualización histórica de spreads.
* [ ] Implementación de lógica para arbitraje triangular.

## ⚖️ Disclaimer

Este software tiene fines puramente educativos y de monitoreo. El trading de activos financieros conlleva riesgos. El autor no se responsabiliza por decisiones financieras tomadas basadas en los datos proporcionados por esta herramienta.