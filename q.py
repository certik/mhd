from tables import openFile, IsDescription, Int32Col, Float64Col
from numpy import array
import IPython

class TimeStep(IsDescription):
    n = Int32Col()
    C = Float64Col(shape=(3201, 800))

hout = openFile("data-new.h5", "w")
hout.createGroup("/", 'data', 'data to be plotted')
hout.createTable(hout.root.data, 'Cdata', TimeStep, "C data for plotting")

h = openFile("data.h5")
table = h.root.data.Cdata
X = array(h.root.common.X)
hout.createArray(hout.root.data, 'X', X, "the X array")
Y = array(h.root.common.X)
hout.createArray(hout.root.data, 'Y', Y, "the Y array")
table_out = hout.root.data.Cdata
for i in range(91, 246):
    n = int(table.cols.n[i])
    print n, i
    step = table_out.row
    step["n"] = n
    C = table.cols.C[i]
    step["C"] = C
    step.append()
for i in range(58, 91):
    n = int(table.cols.n[i])
    print n, i
    step = table_out.row
    step["n"] = n
    C = table.cols.C[i]
    step["C"] = C
    step.append()
for i in range(58):
    n = int(table.cols.n[i])
    print n, i
    step = table_out.row
    step["n"] = n
    C = table.cols.C[i]
    step["C"] = C
    step.append()
