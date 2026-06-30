from repository.json_repository import JsonRepository
from services.dashboard_service import DashboardService
from ui.console_ui import ConsoleUI


repo = JsonRepository("data/studium.json")
studium = repo.lade_daten()

service = DashboardService(studium)
ui = ConsoleUI(service)

ui.starte()