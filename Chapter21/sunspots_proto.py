#ファイル名Chapter21/sunspots_proto.py (listing21-2.py)
from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF

data = [
#    Year  Month   Predicted    High   Low
    (2019, 10,     3.4,       10.4, 0.0),
    (2019, 11,     3.2,       11.2, 0.0),
    (2019, 12,     3.1,       12.1, 0.0),
    (2020, 1,      3.3,       12.3, 0.0),
    (2020, 2,      3.4,       13.4, 0.0),
    (2020, 3,      3.4,       13.4, 0.0),
    (2020, 4,      3.0,       13.0, 0.0),
    (2020, 5,      2.8,       12.8, 0.0),
    (2020, 6,      2.6,       12.6, 0.0),
    (2020, 7,      2.4,       12.4, 0.0),
    ]

drawing = Drawing(200, 150)

factor = 3;
base = 50;
# pred = [row[2]-40 for row in data]
# high = [row[3]-40 for row in data]
# low = [row[4]-40 for row in data]
pred = [row[2]*factor+base for row in data]
high = [row[3]*factor+base for row in data]
low = [row[4]*factor+base for row in data]
times = [200*((row[0] + row[1]/12.0) - 2019)-150 for row in data]

drawing.add(PolyLine(list(zip(times, pred)), strokeColor=colors.blue))
drawing.add(PolyLine(list(zip(times, high)), strokeColor=colors.red))
drawing.add(PolyLine(list(zip(times, low)), strokeColor=colors.green))

drawing.add(String(65, 115, 'Sunspots', fontSize=18, fillColor=colors.red))
renderPDF.drawToFile(drawing, 'report1.pdf', 'Sunspots')
