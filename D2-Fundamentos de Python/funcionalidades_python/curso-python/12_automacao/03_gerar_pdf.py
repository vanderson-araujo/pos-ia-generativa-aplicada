"""
Gerando PDF com reportlab.
Instale com:
pip install reportlab
"""

try:
    from reportlab.pdfgen import canvas
except ImportError:
    print("Instale a biblioteca com: pip install reportlab")
else:
    arquivo = "relatorio.pdf"
    pdf = canvas.Canvas(arquivo)
    pdf.drawString(100, 800, "Relatorio simples gerado com Python")
    pdf.drawString(100, 780, "Total de vendas: R$ 1500,00")
    pdf.save()
    print("PDF criado:", arquivo)

