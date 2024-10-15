# Single Responsibility Principle states that a class should have only one reason to change or class
# should have only one responsibility

# In the below example if we combine both content of Report and ReportPrinter it will violate the SRP since it has two responsibility 
# one to create report and other to print the report
# so its best to create two seperate classes for creating and printing the report.

class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class ReportPrinter:
    def printer(self, report:Report):
        print(f"title: {report.title}")
        print(f"content: {report.content}")

if __name__ == "__main__":
    report = Report("Report 1","Content inside my report 1")

    reportPrinter = ReportPrinter()

    reportPrinter.printer(report)