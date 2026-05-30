import flet as ft
from core.deck import Deck
from board.tableau import TableauPile
from board.foundation import FoundationPile
from board.stock import StockPile
from board.move_manager import MoveManager
from ui.game_view import GameView
from ui.card_view import CardView
from core.reglas import GameRules
from core.game_controller import GameController

class GameApp:

    def __init__(self, page):
        self.page = page
        self.controller = GameController()
        
        self.deck = Deck()
        self.deck.shuffle()
        
        self.move_manager = MoveManager()
        
        # 1. Crear las estructuras lógicas de las pilas
        self.tableau_piles = [
            TableauPile() for _ in range(7)
        ]
        
        self.foundation_piles = [
            FoundationPile() for _ in range(4)
        ]
        
        self.stock_pile = StockPile(self.deck.cards)
        self.game_view = GameView()
        
        # 2. VINCULACIÓN: Conectamos los objetos reales con el controlador
        self.controller.vincular_tablero(
            self.tableau_piles, 
            self.foundation_piles, 
            self.stock_pile
        )

    def setup_tableau(self):
        """Reparte las cartas iniciales en las 7 columnas del tablero"""
        for column_index in range(7):
            for row_index in range(column_index + 1):
                card = self.stock_pile.stock.pop()
                if row_index == column_index:
                    card.face_up = True
                self.tableau_piles[column_index].add_cards([card])

    def handle_card_click_v2(self, carta_clickeada, pile_index):
        """Maneja la selección y transferencia real de cartas entre columnas y mazo"""
        # CASO 1: No hay carta seleccionada en memoria -> Seleccionamos origen
        if not self.controller.carta_seleccionada:
            if carta_clickeada.face_up:  
                self.controller.carta_seleccionada = carta_clickeada
                self.controller.pila_origen_seleccionada = pile_index
                print(f"--> Seleccionada como ORIGEN: {carta_clickeada.valor} de {carta_clickeada.palo} desde pila {pile_index}")
        
        # CASO 2: Ya hay una carta en memoria -> Este clic es el DESTINO
        else:
            origen_idx = self.controller.pila_origen_seleccionada
            destino_idx = pile_index
            carta_mover = self.controller.carta_seleccionada

            # Evitamos mover una carta sobre sí misma
            if origen_idx != destino_idx:
                pila_destino = self.tableau_piles[destino_idx]

                # SUB-CASO A: La carta viene del mazo de descarte (Waste Pile)
                if origen_idx == -1:
                    try:
                        # Extraemos la carta del tope del descarte
                        carta_descarte = self.stock_pile.waste.pop()
                        # La agregamos a la columna del tablero
                        pila_destino.add_cards([carta_descarte])
                        print(f"¡Carta del mazo movida con éxito a la columna {destino_idx}!")
                    except Exception as e:
                        print(f"Error al mover desde el mazo: {e}")

                # SUB-CASO B: La carta viene de otra columna del tablero (Tableau)
                elif origen_idx >= 0:
                    pila_origen = self.tableau_piles[origen_idx]
                    try:
                        idx_carta = pila_origen.cards.index(carta_mover)
                        cartas_a_mover = pila_origen.cards[idx_carta:]
                        
                        pila_origen.cards = pila_origen.cards[:idx_carta]
                        pila_destino.add_cards(cartas_a_mover)

                        if pila_origen.cards:
                            pila_origen.cards[-1].face_up = True
                        print(f"¡Movidas {len(cartas_a_mover)} cartas entre columnas con éxito!")
                    except ValueError:
                        pass
            
            # Limpiamos la selección de memoria y redibujamos la pantalla
            self.controller.carta_seleccionada = None
            self.controller.pila_origen_seleccionada = None
            self.render_board()

    def handle_empty_pile_click(self, destino_idx):
        """Permite mover cartas a una columna que se quedó completamente vacía"""
        if self.controller.carta_seleccionada:
            origen_idx = self.controller.pila_origen_seleccionada
            carta_mover = self.controller.carta_seleccionada
            
            pila_origen = self.tableau_piles[origen_idx]
            pila_destino = self.tableau_piles[destino_idx]

            try:
                idx_carta = pila_origen.cards.index(carta_mover)
                cartas_a_mover = pila_origen.cards[idx_carta:]
                
                pila_origen.cards = pila_origen.cards[:idx_carta]
                pila_destino.add_cards(cartas_a_mover)

                if pila_origen.cards:
                    pila_origen.cards[-1].face_up = True
            except ValueError:
                pass

            self.controller.carta_seleccionada = None
            self.controller.pila_origen_seleccionada = None
            self.render_board()

    def handle_stock_click(self, e):
        """Captura el clic en el mazo para robar una carta"""
        print("Click en el mazo de robo...")
        if self.controller.draw_card():
            self.render_board()

    def render_board(self):
        """Limpia y reconstruye la interfaz gráfica con el estado actual"""
        self.game_view.top_row.controls.clear()
        self.game_view.tableau_row.controls.clear()
        
        # 1. Mazo de Robo (Stock)
        stock_box = ft.GestureDetector(
            mouse_cursor=ft.MouseCursor.CLICK,
            on_tap=self.handle_stock_click,
            content=ft.Container(
                width=100,
                height=150,
                bgcolor=ft.Colors.BLUE_GREY_800 if self.stock_pile.stock else ft.Colors.GREEN_900,
                border=ft.Border.all(2, ft.Colors.WHITE70 if self.stock_pile.stock else ft.Colors.WHITE24),
                border_radius=8,
                alignment=ft.Alignment(0, 0),
                content=ft.Text("MAZO" if self.stock_pile.stock else "VACÍO", color=ft.Colors.WHITE)
            )
        )
        self.game_view.add_foundation_pile(stock_box)
        
        # 2. Descarte (Waste Pile)
        waste_card = self.stock_pile.top_waste_card()
        if waste_card:
            waste_view = ft.GestureDetector(
                mouse_cursor=ft.MouseCursor.CLICK,
                on_tap=lambda e, c=waste_card: self.handle_card_click_v2(c, -1),
                content=CardView(waste_card)
            )
            self.game_view.add_foundation_pile(waste_view)
        else:
            waste_placeholder = ft.Container(width=100, height=150)
            self.game_view.add_foundation_pile(waste_placeholder)

        self.game_view.add_foundation_pile(ft.Container(width=40))

        # 3. Fundaciones ("F")
        for pile in self.foundation_piles:
            if pile.cards:
                top_card_view = ft.GestureDetector(
                    mouse_cursor=ft.MouseCursor.CLICK,
                    on_tap=lambda e, c=pile.cards[-1]: self.handle_card_click_v2(c, -2),
                    content=CardView(pile.cards[-1])
                )
                self.game_view.add_foundation_pile(top_card_view)
            else:
                foundation_box = ft.Container(
                    width=100,
                    height=150,
                    border=ft.Border.all(2, ft.Colors.WHITE24),
                    border_radius=8,
                    alignment=ft.Alignment(0, 0),
                    content=ft.Text("F", color=ft.Colors.WHITE24)
                )
                self.game_view.add_foundation_pile(foundation_box)

        # 4. Columnas del Tablero (Tableau)
        for i, pile in enumerate(self.tableau_piles):
            pile_column = self.create_tableau_column(pile, i)
            self.game_view.add_tableau_pile(pile_column)
            
        self.game_view.refresh_board()

    def create_tableau_column(self, pile, pile_index):
        """Estructura las cartas en cascada vertical (Stack) asignando origen"""
        controls = []
        
        if not pile.cards:
            empty_space = ft.GestureDetector(
                mouse_cursor=ft.MouseCursor.CLICK,
                on_tap=lambda e: self.handle_empty_pile_click(pile_index),
                content=ft.Container(
                    width=100,
                    height=150,
                    border=ft.Border.all(2, ft.Colors.WHITE10),
                    border_radius=8,
                    alignment=ft.Alignment(0, 0),
                    content=ft.Text("Vacío", color=ft.Colors.WHITE10)
                )
            )
            controls.append(empty_space)
        
        for index, card in enumerate(pile.cards):
            card_view = CardView(card)
            
            interactive_card = ft.GestureDetector(
                mouse_cursor=ft.MouseCursor.CLICK,
                on_tap=lambda e, c=card: self.handle_card_click_v2(c, pile_index),
                top=index * 35,
                left=0,
                content=card_view
            )
            controls.append(interactive_card)
            
        return ft.Stack(
            controls=controls,
            width=100,
            height=500
        )

    def run(self):
        self.controller.start_game()
        self.setup_tableau()
        self.page.add(self.game_view)
        self.render_board()
        self.page.update()

def main(page: ft.Page):
    page.title = "Solitario Klondike"
    page.window_width = 1400
    page.window_height = 900
    page.padding = 20
    page.bgcolor = "#0B6623"

    app = GameApp(page)
    app.run()

ft.app(target=main)