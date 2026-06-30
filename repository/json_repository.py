import json
from pathlib import Path

from models.modul import Modul
from models.semester import Semester
from models.studium import Studium
from models.pruefungsleistung import Pruefungsleistung


class JsonRepository:
    """Lädt die Daten des Studiums aus einer JSON-Datei."""
    def __init__(self, dateipfad: str) -> None:
        self.dateipfad = Path(dateipfad)

    def lade_daten(self) -> Studium:
        """Liest die JSON-Datei und erstellt ein Studium-Objekt mit den geladenen Daten."""
        with self.dateipfad.open("r", encoding="utf-8") as file:
            daten = json.load(file)

        semester_liste = []
        for semester_daten in daten["semester"]:
            module = [
                Modul(
                    modul_id=modul["modul_id"],
                    name=modul["name"],
                    ects=modul["ects"],
                    ist_aktuell=modul["ist_aktuell"]
                )
                for modul in semester_daten["module"]
            ]

            semester_liste.append(
                Semester(
                    nummer=semester_daten["nummer"],
                    status=semester_daten["status"],
                    module=module
                )
            )

        pruefungsleistungen = [
            Pruefungsleistung(
                modul_name=p["modul_name"],
                datum=p["datum"],
                note=p["note"],
                ects=p["ects"],
                bestanden=p["bestanden"],
                versuch=p["versuch"]
            )
            for p in daten["pruefungsleistungen"]
        ]

        return Studium(
            studiengang_name=daten["studiengang_name"],
            regelstudienzeit_semester=daten["regelstudienzeit_semester"],
            ziel_notenschnitt=daten["ziel_notenschnitt"],
            ziel_ects_pro_semester=daten["ziel_ects_pro_semester"],
            ziel_ects_gesamt=daten["ziel_ects_gesamt"],
            startdatum=daten["startdatum"],
            semester=semester_liste,
            pruefungsleistungen=pruefungsleistungen
        )

    def speichere_daten(self, studium: Studium) -> None:
        # Für den Prototypen wird diese Methode vorbereitet.
        # Die konkrete Schreibfunktion kann später ergänzt werden.
        raise NotImplementedError("Speichern wird in diesem Prototyp noch nicht unterstützt.")
