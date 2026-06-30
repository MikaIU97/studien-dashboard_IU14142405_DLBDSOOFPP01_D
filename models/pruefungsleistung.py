from dataclasses import dataclass

@dataclass
class Pruefungsleistung:
    modul_name: str
    datum: str | None
    note: float | None
    ects: int
    bestanden: bool
    versuch: int