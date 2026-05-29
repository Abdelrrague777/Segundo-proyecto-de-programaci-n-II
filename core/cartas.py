from dataclasses import dataclass

@dataclass
class Card:
    suit: str
    rank: str
    face_up: bool = False

    @property
    def color(self) -> str:
        """
        Determina automáticamente el color de la carta
        dependiendo de su palo.
        """
        return "red" if self.suit in ["hearts", "diamonds"] else "black"

    def flip(self):
        """
        Cambia el estado visual de la carta.
        """
        self.face_up = not self.face_up

    def __str__(self):
        """
        Representación amigable de la carta.
        """
        return f"{self.rank} of {self.suit}"