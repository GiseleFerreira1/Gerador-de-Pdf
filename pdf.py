import os
from fpdf import FPDF

projeto = input("Digite a descrição do projeto: ")
horas_estimadas = input("Digite o total de horas estimadas: ")
valor_hora = input("Digite o valor da hora trabalhada: ")
prazo_estimado = input("Digite o prazo estimado: ")

valor_total_estimado = int(horas_estimadas) * int(valor_hora)
print(valor_total_estimado)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial")
pdf.image("img/template1.jpg", x=0, y=0)

pdf.cell(0, 10, projeto, ln=True, align='C')
pdf.cell(0, 10, horas_estimadas, ln=True, align='C')
pdf.cell(0, 10, valor_hora, ln=True, align='C')
pdf.cell(0, 10, prazo_estimado, ln=True, align='C')
pdf.cell(0, 10, str(valor_total_estimado), ln=True, align='C')

pdf_file = "orcamento.pdf"
pdf.output(pdf_file)
print("Orçamento gerado com sucesso!")

# Abrir o PDF no visualizador padrão
os.startfile(pdf_file)
