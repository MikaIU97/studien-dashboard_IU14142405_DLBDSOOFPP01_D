from dataclasses import dataclass, field

@dataclass
class Modul:
    name: str
    ects: int
    ist_aktuell: bool = False

@dataclass
class Semester:
    nummer: int
    module: list[Modul] = field(default_factory=list)

    @property
    def ects_erreicht(self) -> int:
        return sum(modul.ects for modul in self.module)

@dataclass
class Studium:
    regelstudienzeit_semester: int
    semester: list[Semester] = field(default_factory=list)

    def add_semester(self, semester: Semester) -> None:
        self.semester.append(semester)

semester_3 = Semester(
    nummer=3,
    module=[
        Modul("Projekt Python", 5, True),
        Modul("Pentesting", 5, True)
    ]
)

studium = Studium(regelstudienzeit_semester=6)
studium.add_semester(semester_3)

print("Anzahl Semester:", len(studium.semester))
print("ECTS im 3. Semester:", semester_3.ects_erreicht)
