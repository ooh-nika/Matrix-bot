
from fpdf import FPDF
import datetime

def generate_matrix_pdf(birthdate_str):
    day, month, year = map(int, birthdate_str.split('.'))
    digits = list(map(int, list(f"{day:02d}{month:02d}{year}")))
    total = sum(digits)
    reduced = sum(map(int, str(total)))
    arcana = reduced % 22 or 22

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Матрица судьбы для {birthdate_str}", ln=True)
    pdf.cell(200, 10, txt=f"Сумма всех цифр: {total}", ln=True)
    pdf.cell(200, 10, txt=f"Сумма цифр результата: {reduced}", ln=True)
    pdf.cell(200, 10, txt=f"Аркан: {arcana}", ln=True)

    filename = f"matrix_{birthdate_str.replace('.', '-')}.pdf"
    pdf.output(filename)
    return filename
