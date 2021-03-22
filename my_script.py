from pystrich.datamatrix import DataMatrixEncoder

encoder = DataMatrixEncoder('This is a DataMatrix.')
encoder.sae('./datamatrix_test.png)
print(encoder.get_ascii())
print("Hello world!")
