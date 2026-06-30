from datetime import datetime

from services.dashboard_service import DashboardService


class ConsoleUI:
    """Stellt die Benutzeroberfläche für die Konsole bereit."""
    def __init__(self, service: DashboardService) -> None:
        self.service = service
    
    def formatiere_datum(self, datum: str) -> str:
        return datetime.strptime(datum, "%Y-%m-%d").strftime("%d.%m.%Y")
    
    def ueberschrift(self, titel: str) -> None:
        print()
        print("-" * 50)
        print(titel)

    def zeige_dashboard(self) -> None:
        """Zeigt das Dashboard mit den wichtigsten Informationen zum Studium an."""
        studium = self.service.studium
        aktuelles_semester = self.service.hole_aktuelles_semester()

        semester_text = "-"
        if aktuelles_semester is not None:
            semester_text = f"{aktuelles_semester.nummer} / {studium.regelstudienzeit_semester}"

        print("\n" + "=" * 50)
        print("                 STUDIEN-DASHBOARD")
        print("=" * 50)

        print(f"Studiengang:           {studium.studiengang_name}")
        print(f"Startdatum:            {self.formatiere_datum(studium.startdatum)}")
        
        self.ueberschrift("STUDIENDAUER")
        print(f"Semester:              {semester_text}")
        print(f"Zeitstatus:            {self.service.berechne_zeitstatus()}")

        self.ueberschrift("ZIEL-NOTENSCHNITT")
        print(f"Aktuelle Note:         {self.service.berechne_notenschnitt():.2f}")
        print(f"Ziel:                  {studium.ziel_notenschnitt:.2f}")

        ects_gesamt = self.service.berechne_ects_gesamt()
        ects_semester = self.service.berechne_ects_aktuelles_semester()

        prozent_gesamt = ects_gesamt / studium.ziel_ects_gesamt * 100
        prozent_semester = ects_semester / studium.ziel_ects_pro_semester * 100

        self.ueberschrift("ECTS-FORTSCHRITT")
        print(f"Gesamt:                {ects_gesamt} / {studium.ziel_ects_gesamt} ECTS ({prozent_gesamt:.0f} %)")
        print(f"Aktuelles Semester:    {ects_semester} / {studium.ziel_ects_pro_semester} ECTS ({prozent_semester:.0f} %)")

        self.ueberschrift("AKTUELLE KURSE")
        for kurs in self.service.hole_aktuelle_kurse():
            print(f"- {kurs.name} ({kurs.ects} ECTS)")

        self.ueberschrift("PRÜFUNGSERGEBNISSE")
        for pruefung in self.service.hole_pruefungsergebnisse():
            note = "-" if pruefung.note is None else pruefung.note

            if pruefung.datum is None:
                if pruefung.note is None:
                    print(f"- {pruefung.modul_name}: bestanden, {pruefung.ects} ECTS")
                else:
                    print(f"- {pruefung.modul_name}: Note {note}, {pruefung.ects} ECTS")
            else:
                datum = self.formatiere_datum(pruefung.datum)

                if pruefung.note is None:
                    print(f"- {datum} | {pruefung.modul_name}: bestanden, {pruefung.ects} ECTS")
                else:
                    print(f"- {datum} | {pruefung.modul_name}: Note {note}, {pruefung.ects} ECTS")


    def zeige_kurse(self) -> None:
        """Zeigt alle aktuellen Kurse an."""
        print("\n" + "=" * 50)
        print("AKTUELLE KURSE")
        print("=" * 50)

        kurse = self.service.hole_aktuelle_kurse()

        if not kurse:
            print("Keine aktuellen Kurse vorhanden.")
        else:
            for kurs in kurse:
                print(f"Modul: {kurs.name}")
                print(f"ECTS : {kurs.ects}")
                print("-" * 50)

    def zeige_pruefungsergebnisse(self) -> None:
        """Zeigt alle Prüfungsergebnisse an."""
        print("\n" + "=" * 50)
        print("PRÜFUNGSERGEBNISSE")
        print("=" * 50)

        pruefungen = self.service.hole_pruefungsergebnisse()

        if not pruefungen:
            print("Keine Prüfungsergebnisse vorhanden.")
        else:
            for p in pruefungen:

                note = "-"
                if p.note is not None:
                    note = p.note

                datum = "-"
                if p.datum is not None:
                    datum = self.formatiere_datum(p.datum)

                print(f"Modul : {p.modul_name}")
                print(f"Datum : {datum}")
                print(f"Note  : {note}")
                print(f"ECTS  : {p.ects}")
                print("-" * 50)

    def zeige_studieninformationen(self) -> None:
        """Zeigt die allgemeinen Informationen zum Studium an."""
        studium = self.service.studium

        print("\n" + "=" * 50)
        print("STUDIENINFORMATIONEN")
        print("=" * 50)

        print(f"Studiengang          : {studium.studiengang_name}")
        print(f"Startdatum           : {self.formatiere_datum(studium.startdatum)}")
        print(f"Regelstudienzeit     : {studium.regelstudienzeit_semester} Semester")
        print(f"Ziel-Notenschnitt    : {studium.ziel_notenschnitt}")
        print(f"ECTS pro Semester    : {studium.ziel_ects_pro_semester}")
        print(f"Gesamt-ECTS          : {studium.ziel_ects_gesamt}")

    def starte(self) -> None:
        """Startet die Benutzeroberfläche und zeigt das Hauptmenü an."""

        while True:

            print("\n" + "=" * 50)
            print("MENÜ")
            print("=" * 50)

            print("1 - Dashboard anzeigen")
            print("2 - Aktuelle Kurse anzeigen")
            print("3 - Prüfungsergebnisse anzeigen")
            print("4 - Studieninformationen anzeigen")
            print("0 - Programm beenden")

            auswahl = input("\nAuswahl: ")

            if auswahl == "1":
                self.zeige_dashboard()

            elif auswahl == "2":
                self.zeige_kurse()

            elif auswahl == "3":
                self.zeige_pruefungsergebnisse()

            elif auswahl == "4":
                self.zeige_studieninformationen()

            elif auswahl == "0":
                print("\nProgramm beendet.")
                break

            else:
                print("\nUngültige Eingabe.")
