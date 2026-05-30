VALORES_CARTAS = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
}

class GameRules:

    @staticmethod
    def puede_mover_a_columna(carta, carta_destino):
        if carta_destino is None:
            return carta.valor == "K"

        return (
            carta.color != carta_destino.color
            and VALORES_CARTAS[carta.valor]
            == VALORES_CARTAS[carta_destino.valor] - 1
        )

    @staticmethod
    def puede_mover_a_base(carta, carta_destino):
        if carta_destino is None:
            return carta.valor == "A"
        return (
            carta.palo == carta_destino.palo
            and VALORES_CARTAS[carta.valor]
            == VALORES_CARTAS[carta_destino.valor] + 1
        )

    @staticmethod
    def juego_ganado(bases):
        return all(len(base.cartas) == 13 for base in bases)
