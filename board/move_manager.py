from core.reglas import GameRules


# Esta clase coordina los movimientos entre pilas.
# Aquí conectamos las reglas con el tablero real.
class MoveManager:

    def move_to_tableau(self, source_pile, target_pile, cards):
        """
        Intenta mover cartas hacia una columna tableau.
        """

        if not cards:
            return False

        moving_card = cards[0]

        target_card = target_pile.top_card()

        # Validamos el movimiento usando las reglas del juego.
        if GameRules.can_move_to_tableau(moving_card, target_card):

            target_pile.add_cards(cards)

            return True

        return False

    def move_to_foundation(self, source_pile, foundation, card):
        """
        Intenta mover una carta a una foundation.
        """

        target_card = foundation.top_card()

        # Verificamos si el movimiento es válido.
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
        Mueve un bloque completo de cartas
        entre columnas del tableau.
        """

        moving_cards = source_pile.remove_cards(start_index)

        success = self.move_to_tableau(
            source_pile,
            target_pile,
            moving_cards
        )

        # Si el movimiento no fue válido,
        # regresamos las cartas a su lugar original.
        if not success:

            source_pile.add_cards(moving_cards)

            return False

        # Después del movimiento,
        # revelamos la carta superior restante.
        source_pile.reveal_top_card()

        return True