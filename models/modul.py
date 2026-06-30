from dataclasses import dataclass


@dataclass
class Modul:
    modul_id: str
    name: str
    ects: int
    ist_aktuell: bool = False