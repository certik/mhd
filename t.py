from tables import openFile
import IPython

h = openFile("data.h5")
table = h.root.data.Cdata
print repr(table)
IPython.set_trace()
