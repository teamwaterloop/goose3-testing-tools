'''
@file graphing.py
@brief Graphs sensor data for various functions from input file using plotly.

@author Ibrahim Irfan
@date December 9, 2017
@bugs No known bugs.
'''

import os
import plotly
from plotly.graph_objs import Scatter, Layout

# graph the data parsed from input file
def graph(data, outputFolder):
    # different graph for every function
    for function in data:
        # initialize x data (just 1,2, 3 ... numParams)
        xData = []
        numParams = len(data[functionName])
        for i in range(1, numParams): 
            xData.append(i)

        # plot the function values with plotly
        plotly.offline.plot({
            "data": [Scatter(x=xData, y=data[function])],
            "layout": Layout(title="Sensor Data for " + function),
        }, filename=outputFolder + function + ".html", image="png", image_filename=function)


fileName = raw_input("Input file (including path and extension): ")

with open(fileName, 'rb') as fileIn:
    data = {}

    # for every line in file
    for line in fileIn:
        # get each comma delimited argument
        params = line.strip("\n").split(", ")
        numParams = int(params[1]) 
        functionName = params[0]

        # new data entry for this function
        if (functionName not in data):
            data[functionName] = []

        # add parameters to data
        for i in range(2, numParams + 2):
            param = params[i]
            data[functionName].append(int(param))

    # end of file
    else: 
        print data
        # get output folder from user and error check
        outputFolder = raw_input("Done reading file. Output folder (empty for current directory): ")
        if outputFolder != '':
            if outputFolder[-1] != "/":
                outputFolder += "/"

            # create folder if not exists 
            if not os.path.exists(outputFolder):
                os.makedirs(outputFolder)
        
        graph(data, outputFolder)

