import wpf
import clr
import sys
import itertools
from random import randint
from System import Array
from System.Windows import Application, Window
from System.Windows.Controls import Label

class MyWindow(Window):
    def __init__(self, content):
        wpf.LoadComponent(self, 'Main.xaml')  
        self.lbl.Content = content
        #self.lbl.Content = "Initial content"

if __name__ == '__main__':    
    s = "Empty content"    
    try:
        clr.AddReferenceByName("MatematikoCountScores.dll")
        from MatematikoCountScores import ResultCounter
        result_counter = ResultCounter
        field_lght = 5
        #field = [[1 for j in range(5)] for i in range(5)]
        #field1D = list(itertools.chain.from_iterable(field))
        #arr = Array.CreateInstance(int, 5, 5)
        #for i in range(5):
        #    for j in range(5):
        #           arr[i, j] = field[i][j]        
        field1D = [randint(1,13) for i in range(field_lght*field_lght)]
        arr = Array.CreateInstance(int, field_lght*field_lght)
        #for i in range(5):
        #    for j in range(5):
        #           arr[i, j] = field[i][j]  
        for i in range(len(field1D)):
            arr[i] = field1D[i]
        res = result_counter.CountResults(arr, 5)        
        Application().Run(MyWindow(res))
    except:
        w = Window()
        l = Label()
        l.Content = "Error occured: see error.txt"
        with open("error.txt", 'w') as f:
            f.write( str("Unexpected error:" + str(sys.exc_info())))
        w.AddChild(l)
        w.ShowDialog()
    #f = Foo()
    #s = f.HelloWorld()
    #i = f.IntIncremented(10)
    
