from models.studium import Studium
from models.modul import Modul
from models.pruefungsleistung import Pruefungsleistung
from datetime import datetime


class DashboardService:
    def __init__(self, studium: Studium) -> None:
        self.studium = studium

    def berechne_notenschnitt(self) -> float:
        benotete_pruefungen = [
            p for p in self.studium.pruefungsleistungen
            if p.bestanden and p.note is not None
        ]

        if not benotete_pruefungen:
            return 0.0

        return sum(p.note for p in benotete_pruefungen) / len(benotete_pruefungen)

    def berechne_ects_gesamt(self) -> int:
        return sum(
            p.ects for p in self.studium.pruefungsleistungen if p.bestanden
        )

    def hole_aktuelles_semester(self):
        for semester in self.studium.semester:
            if semester.status == "laufend":
                return semester
        return None

    def berechne_ects_aktuelles_semester(self) -> int:
        aktuelles_semester = self.hole_aktuelles_semester()

        if aktuelles_semester is None:
            return 0

        return aktuelles_semester.ects_erreicht

    def berechne_zeitstatus(self) -> str:
        ects_aktuelles_semester = self.berechne_ects_aktuelles_semester()

        if ects_aktuelles_semester >= self.studium.ziel_ects_pro_semester:
            return "im Plan"

        return "verzögert"

    def hole_aktuelle_kurse(self) -> list[Modul]:
        aktuelles_semester = self.hole_aktuelles_semester()

        if aktuelles_semester is None:
            return []

        return [
            modul for modul in aktuelles_semester.module if modul.ist_aktuell
        ]

    def hole_pruefungsergebnisse(self) -> list[Pruefungsleistung]:
        def sortierschluessel(pruefung: Pruefungsleistung):
            if pruefung.datum is None:
                return datetime.min

            return datetime.strptime(pruefung.datum, "%Y-%m-%d")

        return sorted(
            self.studium.pruefungsleistungen,
            key=sortierschluessel,
            reverse=True
        )