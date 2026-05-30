from core.reglas import GameRules


# Gestiona los movimientos entre pilas del tablero,
# delegando la validación de reglas a GameRules.
class MoveManager:

    def move_to_tableau(self, source_pile, target_pile, cards):
        """
        Intenta colocar un grupo de cartas en una columna del tableau.
        Retorna True si el movimiento es válido y se ejecutó, False en caso contrario.
        """

        if not cards:
            return False

        moving_card = cards[0]

        target_card = target_pile.top_card()

        # La carta base del grupo debe cumplir las reglas del tableau.
        if GameRules.can_move_to_tableau(moving_card, target_card):

            target_pile.add_cards(cards)

            return True

        return False

    def move_to_foundation(self, source_pile, foundation, card):
        """
        Intenta enviar una carta a su foundation correspondiente.
        Retorna True si el movimiento es válido y se ejecutó, False en caso contrario.
        """

        target_card = foundation.top_card()

        # La carta debe continuar la secuencia ascendente del palo.
        if GameRules.can_move_to_foundation(card, target_card):

            foundation.push_card(card)

            return True

        return False

    def move_between_tableaus(
        self,
        source_pile,
        target_pile,
        start_index
    ):
        """
        Traslada un bloque de cartas desde start_index hasta la cima
        de source_pile hacia target_pile.
        Revierte la operación automáticamente si el movimiento no es válido.
        """

        moving_cards = source_pile.remove_cards(start_index)

        success = self.move_to_tableau(
            source_pile,
            target_pile,
            moving_cards
        )

        # Movimiento inválido: restaurar las cartas a su posición original.
        if not success:

            source_pile.add_cards(moving_cards)

            return False

        # Exponer la nueva carta superior tras liberar la columna origen.
        source_pile.reveal_top_card()

        return True
