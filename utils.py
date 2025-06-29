from datetime import datetime
from fpdf import FPDF

def calculate_matrix(date_str):
    # Предположим формат даты: "27.07.1996"
    digits = [int(d) for d in date_str if d.isdigit()]
    s1 = sum(digits)
    s2 = sum(int(d) for d in str(s1))
    arcana = s2 % 22
    return [arcana]

def generate_pdf(date_str, result):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Matrix Calculation for {date_str}", ln=True)
    pdf.cell(200, 10, txt=f"Resulting Arcana: {result}", ln=True)
    output_filename = f"matrix_{date_str.replace('.', '-')}.pdf"
    pdf.output(output_filename)
    return output_filename
