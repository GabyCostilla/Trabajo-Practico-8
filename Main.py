import pandas as pd

# Leer el archivo CSV
file_path = '/mnt/data/copa-america-2024-UTC.csv'
fixture_df = pd.read_csv(file_path)
print(fixture_df.head())

# Clase Equipo
class Equipo:
    def __init__(self, nombre, grupo):
        self.nombre = nombre
        self.grupo = grupo
        self.puntos = 0
        self.partidos_jugados = 0
        self.victorias = 0
        self.empates = 0
        self.derrotas = 0
        self.goles_a_favor = 0
        self.goles_en_contra = 0

    def actualizar_estadisticas(self, goles_a_favor, goles_en_contra):
        self.partidos_jugados += 1
        self.goles_a_favor += goles_a_favor
        self.goles_en_contra += goles_en_contra
        if goles_a_favor > goles_en_contra:
            self.victorias += 1
            self.puntos += 3
        elif goles_a_favor == goles_en_contra:
            self.empates += 1
            self.puntos += 1
        else:
            self.derrotas += 1

    def diferencia_goles(self):
        return self.goles_a_favor - self.goles_en_contra

# Clase Partido
class Partido:
    def __init__(self, numero, ronda, fecha, ubicacion, equipo_local, equipo_visitante, grupo):
        self.numero = numero
        self.ronda = ronda
        self.fecha = fecha
        self.ubicacion = ubicacion
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.grupo = grupo
        self.resultado = None

    def actualizar_resultado(self, goles_local, goles_visitante):
        self.resultado = (goles_local, goles_visitante)
        self.equipo_local.actualizar_estadisticas(goles_local, goles_visitante)
        self.equipo_visitante.actualizar_estadisticas(goles_visitante, goles_local)

# Función para actualizar resultados
def actualizar_resultados(partidos, archivo_resultados):
    resultados_df = pd.read_csv(archivo_resultados)
    for _, row in resultados_df.iterrows():
        numero_partido = row['Match Number']
        goles_local = row['Home Team Goals']
        goles_visitante = row['Away Team Goals']
        if numero_partido in partidos:
            partidos[numero_partido].actualizar_resultado(goles_local, goles_visitante)

# Función para calcular posiciones
def calcular_posiciones(partidos, equipos):
    for partido in partidos.values():
        if partido.resultado:
            goles_local, goles_visitante = partido.resultado
            equipos[partido.equipo_local].actualizar_estadisticas(goles_local, goles_visitante)
            equipos[partido.equipo_visitante].actualizar_estadisticas(goles_visitante, goles_local)

    posiciones = {}
    for equipo in equipos.values():
        grupo = equipo.grupo
        if grupo not in posiciones:
            posiciones[grupo] = []
        posiciones[grupo].append(equipo)

    for grupo in posiciones:
        posiciones[grupo].sort(key=lambda e: (e.puntos, e.diferencia_goles(), e.goles_a_favor), reverse=True)

    return posiciones

# Función para generar informe
def generar_informe(posiciones, archivo_salida):
    with open(archivo_salida, 'w') as f:
        f.write("Grupo,Equipo,Puntos,PartidosJugados,Victorias,Empates,Derrotas,GolesAFavor,GolesEnContra,DiferenciaDeGoles\n")
        for grupo, equipos en posiciones.items():
            for equipo in equipos:
                f.write(f"{grupo},{equipo.nombre},{equipo.puntos},{equipo.partidos_jugados},{equipo.victorias},{equipo.empates},{equipo.derrotas},{equipo.goles_a_favor},{equipo.goles_en_contra},{equipo.diferencia_goles()}\n")

