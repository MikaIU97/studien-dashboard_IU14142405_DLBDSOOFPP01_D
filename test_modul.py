from dataclasses import dataclass

@dataclass
class Modul:
    name: str
    ects: int
    ist_aktuell: bool = False

    def __post_init__(self) -> None:
        if self.ects <= 0:
            raise ValueError("ECTS müssen größer als 0 sein.")

modul = Modul("Projekt Python", 5, True)
print(modul)
