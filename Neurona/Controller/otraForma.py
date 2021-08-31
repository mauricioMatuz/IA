import xlrd
import pandas as pd
def ValoresTxT():
    archivoExcel = pd.read_excel("../doc/Matriz.xlsx")
    vias = archivoExcel["vias"]
    x1 = archivoExcel["x1"]
    x2 = archivoExcel["x2"]
    y = archivoExcel["y"]
    print(vias)

def main():
    ValoresTxT()


if __name__ == '__main__':
    main()