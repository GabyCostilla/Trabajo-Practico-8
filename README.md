# Proyecto Copa América 2024

Este proyecto gestiona y analiza los resultados de los partidos de la Copa América 2024. A través de un archivo CSV que contiene el calendario de partidos y otro archivo CSV con los resultados de los partidos jugados, el proyecto actualiza las estadísticas de los equipos y genera un informe con las posiciones de los equipos en sus respectivos grupos.

## Estructura del Proyecto

- **Equipo:** Clase que representa a un equipo y sus estadísticas en el torneo.
- **Partido:** Clase que representa un partido entre dos equipos y su resultado.
- **Funciones:**
  - `actualizar_resultados`: Actualiza los resultados de los partidos basados en un archivo CSV.
  - `calcular_posiciones`: Calcula las posiciones de los equipos en sus grupos basándose en los resultados de los partidos.
  - `generar_informe`: Genera un informe de las posiciones de los equipos en un archivo CSV de salida.

## Archivos Necesarios

1. **copa-america-2024-UTC.csv**: Archivo CSV que contiene el calendario de partidos de la Copa América 2024.
2. **resultados.csv**: Archivo CSV que contiene los resultados de los partidos jugados. Debe tener las siguientes columnas:
   - `Match Number`: Número del partido.
   - `Home Team Goals`: Goles del equipo local.
   - `Away Team Goals`: Goles del equipo visitante.

## Uso del Código

### Instalación de Dependencias

Asegúrate de tener instalada la librería `pandas`:

```bash
pip install pandas
