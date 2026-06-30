from dataclasses import dataclass, field

from models.semester import Semester
from models.pruefungsleistung import Pruefungsleistung


@dataclass
class Studium:
    studiengang_name: str
    regelstudienzeit_semester: int
    ziel_notenschnitt: float
    ziel_ects_pro_semester: int
    ziel_ects_gesamt: int
    startdatum: str

    semester: list[Semester] = field(default_factory=list)
    pruefungsleistungen: list[Pruefungsleistung] = field(default_factory=list)