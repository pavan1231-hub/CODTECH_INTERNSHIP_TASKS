import csv
from fpdf import FPDF

#Data reading from CSV
def read_csv(file_path):
    data = []
    with open(file_path, mode="r") as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)  # Get headers
        for row in csv_reader:
            data.append(row)
    return headers, data

# Generating PDF report
class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Automated Report", align="C", ln=True)
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def add_table(self, headers, data):
        self.set_font("Arial", "B", 10)
        for header in headers:
            self.cell(40, 10, header, border=1, align="C")
        self.ln()
        self.set_font("Arial", "", 10)
        for row in data:
            for item in row:
                self.cell(40, 10, item, border=1, align="C")
            self.ln()

# Main execution
if __name__ == "__main__":
    # File path
    csv_file = "C:/Users/premc/Downloads/customers-100.csv" #Give your csv file path
    pdf_file = "Report.pdf"

    # Read and process data
    headers, data = read_csv(csv_file)

    # Generate PDF
    pdf = PDFReport()
    pdf.add_page()
    pdf.add_table(headers, data)
    pdf.output(pdf_file)
    print(f"Report generated: {pdf_file}")
