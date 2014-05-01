'''
Created on Apr 28, 2014

@author: sgk
'''
import tkinter

class Ui(tkinter.Frame):
    '''
    classdocs
    '''


    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.createWidgets(master)
        self.pack()
        
    def createWidgets(self, master=None):
        self.canvas = tkinter.Canvas(master, width = 300, height =200 )
        
        self.line_horizontal(0, 300, 25)
        self.line_vertical(1, 0, 60)
        self.line_vertical(60, 0, 60)
        
        self.canvas.create_text(10, 10, anchor = 'nw', state = 'normal', text = "Stuff")
        
        self.canvas.pack()

        self.entry_url = tkinter.Entry(master, background = 'white', width = 50)
        self.entry_url.insert(0, "Enter a url: example.com")
        self.entry_url.pack()
        
    # TODO pass canvas in as param
    def line_horizontal(self, orig_x, distal_x, y):
        self.canvas.create_line(orig_x, y, distal_x, y)
        
    # TODO pass canvas in as param
    def line_vertical(self, x, orig_y, distal_y):
        self.canvas.create_line(x, orig_y, x, distal_y)
        
    def print_table_row( self, line ):
        pass
    
    def autoClearEntry( self ):
        pass
    
    def addNewUrlEntry( self ):
        pass

if __name__ == '__main__':
    root = tkinter.Tk()
    app = Ui(master=root)
    app.mainloop()
    
    