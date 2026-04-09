from dataclasses import dataclass

@dataclass
class Pruefungsleistung:
    modul_name: str
    note: float
    ects: int
    bestanden: bool = True

def berechne_notenschnitt(pruefungen: list[Pruefungsleistung]) -> float:
    bestandene_pruefungen = [
        p for p in pruefungen if p.bestanden
    ]

    if not bestandene_pruefungen:
        return 0.0

    durchschnitt = sum(p.note for p in bestandene_pruefungen) / len(bestandene_pruefungen)
    return durchschnitt


pruefungen = [
    Pruefungsleistung("Einführung Python", 2.0, 5, True),
    Pruefungsleistung("Datenbanken", 2.7, 5, True),
    Pruefungsleistung("Mathematik", 5.0, 5, False)
]

print("Notendurchschnitt:", round(berechne_notenschnitt(pruefungen), 2))
