# import modules that I'm using
# from lmfit import minimize, Parameters, Minimizer
import classifier
import pandas as pd
import seaborn as sns
import scipy as sc
import numpy as np
from tkinter import *
import tkinter
import tkinter.ttk
import matplotlib.pyplot as pltlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
matplotlib.use('TKAgg')
# import matplotlib.pyplot as pltlib
# lmfit is imported becuase parameters are allowed to depend on each other along with bounds, etc.

# Make object for application


class App_Window(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):

        button = tkinter.ttk.Button(
            self, text="Open File", command=self.OnButtonClick)
        button.pack(side=tkinter.TOP)

        button = tkinter.ttk.Button(
            self, text="Quit", command=self.quit)
        button.pack(side=tkinter.TOP)

        self.input = tkinter.ttk.Entry(self)
        self.input.pack(side=tkinter.TOP)

        # self.canvasFig = pltlib.figure(1)
        Fig = matplotlib.figure.Figure(figsize=(10, 8), dpi=100)
        self.FigSubPlot = Fig.add_subplot(1, 1, 1)

        x = []
        y = []

        self.FigSubPlot.scatter(x, y)
        self.canvas = FigureCanvasTkAgg(
            Fig, master=self)
        self.setAxes()

        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        self.canvas._tkcanvas.pack(
            side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        self.resizable(True, False)
        self.update()

    def setAxes(self):
        ax = self.canvas.figure.axes[0]
        ax.set_xlim(-0.1, 1.1)
        ax.set_ylim(-0.1, 1.1)

    # def refreshFigure(self, x, y):
    #     self.FigSubPlot.clear()
    #     self.FigSubPlot.scatter(x, y)
    #     ax = self.canvas.figure.axes[0]
    #     self.setAxes()
    #     self.canvas.draw()

    def OnButtonClick(self):
        [a, b] = list(map(int, self.input.get().split(' ')))
        self.FigSubPlot.clear()

        c = classifier.Classifier(a, b)
        x, y = c.getAllSamples()
        self.FigSubPlot.scatter(x, y, c='b')

        c = classifier.Classifier(a, b)
        x, y = c.getAllSamples()
        self.FigSubPlot.scatter(x, y, c='k')

        ax = self.canvas.figure.axes[0]
        self.setAxes()
        self.canvas.draw()
        # self.refreshFigure(x, y)


if __name__ == "__main__":
    MainWindow = App_Window(None)
    MainWindow.mainloop()
