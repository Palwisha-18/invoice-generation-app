import glob

import pandas as pd

from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")


for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    filename = Path(filepath).stem
    invoice_num = filename.split('-')[0]
    invoice_date = filename.split('-')[1]

    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_num}", align="L", ln=1, border=0)
    pdf.output(f"PDFs/{filename}.pdf")
