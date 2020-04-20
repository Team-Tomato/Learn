from fpdf import FPDF
f = open("q_paper.txt", "w+")
print("Enter 5 questions: ")
q1=5
lines = ""
for i in range(q1):
    lines+=input()+"\n"

f.writelines(lines)
pdf =FPDF()
pdf.add_page()
pdf.set_font('Times','I',size=15)

pdf.cell(200, 10, txt= lines, ln = 1, align='L')
pdf.output("qpaper.pdf")
