from fpdf import FPDF
import pandas as pd
import glob

filepaths = glob.glob("test/*txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    #df = pd.read_csv(filepath)
    pdf.add_page()
    name = filepath[5:].split(".")[0]
    title = name.title()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=title)

pdf.output("p.pdf")