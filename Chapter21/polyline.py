#ファイル名Chapter21/polyline.py
from reportlab.graphics.shapes import Drawing, String, PolyLine
from reportlab.graphics import renderPDF

# d = Drawing(300, 300)
# p = PolyLine([(0, 0), (100, 100), (100, 0), (0, 100)])
# d.add(p)
# renderPDF.drawToFile(d, 'polyline.pdf', 'polyline pdf file')

d = Drawing(200, 200)
p = PolyLine([(50, 50), (150, 150), (150, 50), (50, 150)])
d.add(p)
renderPDF.drawToFile(d, 'polyline.pdf', 'polyline pdf file')
