import tkinter as tk
import numpy as np
import time

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Point Moving')
        self.cvs_map = tk.Canvas(self, width= 300, height= 300, relief= tk.SUNKEN, border= 1)

        btn_start = tk.Button(self, text= 'Start', width= 6,
                              command= self.btn_start_click)

        self.mypath = [(10, 10), (250, 60), (150, 150), (200, 250)]
        self.cvs_map.create_line(self.mypath, fill= 'blue', width= 3) #create an custom the line
        x0 = self.mypath[0][0]
        y0 = self.mypath[0][1]
        self.cvs_map.create_text(x0, y0 + 10, text='A')
        self.cvs_map.create_oval(x0 - 5, y0 - 5, x0 + 5, y0 + 5,
                             fill='green', outline='red' )

        x1 = self.mypath[1][0]
        y1 = self.mypath[1][1]
        self.cvs_map.create_text(x1, y1 + 10, text= 'B')

        x2 = self.mypath[2][0]
        y2 = self.mypath[2][1]
        self.cvs_map.create_text(x2 - 5, y2 + 10, text='C')

        x3 = self.mypath[3][0]
        y3 = self.mypath[3][1]
        self.cvs_map.create_text(x3 + 5, y3 + 5, text= 'D')

        

        # custom boder
        self.cvs_map.grid(row=0, column= 0, padx= 5, pady= 5)
        btn_start.grid(row = 0, column = 1, padx =5 , pady = 6, sticky= tk.NW) #NorthWest

    def btn_start_click(self):
        cvs_map_bg = self.cvs_map["background"] #mau nen map

        x0 = self.mypath[0][0]
        y0 = self.mypath[0][1]
        x1 = self.mypath[1][0]
        y1 = self.mypath[1][1]
        x2 = self.mypath[2][0]
        y2 = self.mypath[2][1]
        x3 = self.mypath[3][0]
        y3 = self.mypath[3][1]

        # chay doan 1
        d0 = np.sqrt((x1 - x0)**2 + (y1 - y0)**2)
        N0 = 10
        dt = 1.0/(N0 - 1)
        for i in range(0, N0):
            t = i*dt
            x = x0 + (x1 -x0)*t
            y = y0 + (y1 -y0)*t
            self.cvs_map.create_line(self.mypath, fill= 'blue', width= 3)
            self.cvs_map.create_oval(x-5, y-5, x+5, y+5,
                                     fill='green', outline='red')
            time.sleep(0.5)
            
            self.cvs_map.update()
            if i < N0 - 1:
                self.cvs_map.create_oval(x-5, y-5, x+5, y+5,
                                     fill=cvs_map_bg, outline=cvs_map_bg)
        
        # chay doan 2
        # d1 = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        N0 = 10
        dt = 1.0/(N0 - 1)
        for i in range(0, N0):
            t = i*dt
            x = x1 + (x2 -x1)*t
            y = y1 + (y2 -y1)*t
            self.cvs_map.create_line(self.mypath, fill= 'blue', width= 3)
            self.cvs_map.create_oval(x-5, y-5, x+5, y+5,
                                     fill='green', outline='red')
            time.sleep(0.5)
            
            self.cvs_map.update()
            if i < N0 - 1:
                self.cvs_map.create_oval(x-5, y-5, x+5, y+5,
                                     fill=cvs_map_bg, outline=cvs_map_bg)      

        # chay doan 3
        N0 = 10
        dt = 1.0/(N0 - 1)
        for i in range(0, N0):
            t = i*dt
            x = x2 + (x3 -x2)*t
            y = y2 + (y3 -y2)*t
            self.cvs_map.create_line(self.mypath, fill= 'blue', width= 3)
            self.cvs_map.create_oval(x-5, y-5, x+5, y+5,
                                     fill='green', outline='red')
            time.sleep(0.5)
            
            self.cvs_map.update()
            if i < N0 - 1:
                self.cvs_map.create_oval(x-5, y-5, x+5, y+5,
                                     fill=cvs_map_bg, outline=cvs_map_bg)             
                
        pass

if __name__== "__main__":
    app =App()
    app.mainloop()