class Carta:

    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor
        self.face_up = False

    def flip(self):
        """Voltea la carta (cambia su estado de face_up)"""
        self.face_up = not self.face_up

    def __eq__(self, other):
        """Permite a Python encontrar la carta en la lista al arrastrarla"""
        if not isinstance(other, Carta):
            return False
        return self.valor == other.valor and self.palo == other.palo

    def __str__(self):
        return f"{self.valor} de {self.palo}"

    def __repr__(self):
        return self.__str__()