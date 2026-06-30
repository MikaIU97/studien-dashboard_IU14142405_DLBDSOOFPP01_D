from dataclasses import dataclass

@dataclass
class Pruefungsleistung:
    """Repräsentiert eine Prüfungsleistung innerhalb eines Studiums, einschließlich der Modul-ID, des Modulnamens, des Datums, der Note, der ECTS-Punkte, des Bestehensstatus und des Versuchs."""
    modul_name: str
    datum: str | None
    note: float | None
    ects: int
    bestanden: bool
    versuch: int
