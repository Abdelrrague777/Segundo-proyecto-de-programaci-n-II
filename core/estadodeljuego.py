class EstadoJuego:

    def __init__(self):
        self.tableau = []
        self.foundations = []
        self.stock = None
        self.waste = []
        self.historial_movimientos = []

    def guardar_movimiento(self, datos_movimiento):
        self.historial_movimientos.append(datos_movimiento)

    def deshacer_movimiento(self):
        if self.historial_movimientos:
          return self.historial_movimientos.pop()
        return None

    def reiniciar_juego(self):
        self.tableau.clear()
        self.foundations.clear()
        self.waste.clear()
        self.historial_movimientos.clear()