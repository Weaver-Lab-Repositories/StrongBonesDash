from shiny import ui, render, App
from shinywidgets import render_widget
import pandas as pd
import ipython
import plotly
import plotly.express as px

import numpy as np
import matplotlib.pyplot as plt


app_ui = ui.page_fluid(
    ui.layout_sidebar(
        ui.sidebar(
            ui.h2("Page Charts"),
            ui.hr(),
            ui.input_slider(id="slider", label="Number of bins:", min=5, max=25, value=15)
        ),
            ui.output_plot(id="histogram")        
    )
)

def server(input, output, session):
    @output
    @render.plot
    def histogram():
        

        x = 100 + np.random.randn(500)
        plt.title("A histogram", size=20)
        plt.hist(x=x, bins=input.slider(), color="grey", ec="black")



app = App(ui=app_ui, server=server) 