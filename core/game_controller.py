class GameController:

    def __init__(self):
        # Variables necesarias para la selección de cartas en la UI
        self.carta_seleccionada = None
        self.pila_origen_seleccionada = None
        
        # Estructuras lógicas del tablero
        self.tableau_piles = []
        self.foundation_piles = []
        self.stock_pile = []

    def vincular_tablero(self, tableau, foundation, stock):
        """Conecta las pilas reales del juego con el controlador"""
        self.tableau_piles = tableau
        self.foundation_piles = foundation
        self.stock_pile = stock

    def start_game(self):
        """Inicializa el estado del juego"""
        print("¡Juego iniciado en el controlador!")
        self.carta_seleccionada = None
        self.pila_origen_seleccionada = None

    def draw_card(self):
        """Maneja el robo de cartas del mazo (Stock a Waste)"""
        if hasattr(self.stock_pile, 'draw'):
            return self.stock_pile.draw()
        
        # Si no tienes el método draw implementado aún, hacemos un comportamiento básico:
        if self.stock_pile.stock:
            carta = self.stock_pile.stock.pop()
            carta.face_up = True
            self.stock_pile.waste.append(carta)
            return True
        elif self.stock_pile.waste:
            # Reabastecer mazo si se vacía
            self.stock_pile.stock = list(reversed(self.stock_pile.waste))
            self.stock_pile.waste.clear()
            for c in self.stock_pile.stock:
                c.face_up = False
            return True
        return False