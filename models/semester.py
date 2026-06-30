from dataclasses import dataclass, field

from models.modul import Modul


@dataclass
class Semester:
    nummer: int
    status: str
    module: list[Modul] = field(default_factory=list)

    @property
    def ects_erreicht(self) -> int:
        return sum(modul.ects for modul in self.module)