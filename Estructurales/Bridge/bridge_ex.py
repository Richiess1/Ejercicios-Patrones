from abc import ABC, abstractmethod

class Exporter(ABC):
    @abstractmethod
    def export(self, report_type):
        pass

class PDFExporter(Exporter):
    def export(self, report_type):
        print(f"Exporting {report_type} Report to PDF...")

class HTMLExporter(Exporter):
    def export(self, report_type):
        print(f"Exporting {report_type} Report to HTML...")

class JSONExporter(Exporter):
    def export(self, report_type):
        print(f"Exporting {report_type} Report to JSON...")

class Report(ABC):
    def __init__(self, exporter: Exporter):
        self.exporter = exporter

    @abstractmethod
    def generate(self):
        pass

class UserReport(Report):
    def generate(self):
        self.exporter.export("User")

class SalesReport(Report):
    def generate(self):
        self.exporter.export("Sales")

class InventoryReport(Report):
    def generate(self):
        self.exporter.export("Inventory")

if __name__ == "__main__":
    report1 = UserReport(PDFExporter())
    report1.generate()

    report2 = SalesReport(HTMLExporter())
    report2.generate()

    report3 = InventoryReport(JSONExporter())
    report3.generate()
