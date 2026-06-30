from dataclasses import dataclass


@dataclass
class Modul:
    """Repräsentiert ein Modul innerhalb eines Semesters, einschließlich seiner ID, seines Namens, der ECTS-Punkte und seines aktuellen Status."""
    modul_id: str
    name: str
    ects: int
    ist_aktuell: bool = False
