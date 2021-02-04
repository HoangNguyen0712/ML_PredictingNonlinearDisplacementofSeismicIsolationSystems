# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 21:44:21 2020

@author: USER
"""

import PySimpleGUI as sg
import numpy as np
from pickle import load

# ADD TITLE COLOUR ,title_color='white'
sg.theme('DefaultNoMoreNagging')	# Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Developed by Hoang D. Nguyen, Nhan D. Dao, and Myoungsu Shin')],
            [sg.Text('Ulsan National Institute of Science and Technology (UNIST)')],
            [sg.Text('Ulsan, South Korea')],
            [sg.Text('Email: nguyenhoangkt712@unist.ac.kr')],
            #[sg.Text('Input parameters')],
            [sg.Frame(layout=[
            [sg.Text('SM-1s',size=(10, 1)),sg.InputText(key='-f1-'),sg.Text('g')],
            [sg.Text('SM-2s',size=(10, 1)), sg.InputText(key='-f2-'),sg.Text('g')],
            [sg.Text('SM-3s',size=(10, 1)), sg.InputText(key='-f3-'),sg.Text('g')],
            [sg.Text('SM-4s',size=(10, 1)), sg.InputText(key='-f4-'),sg.Text('g')],
            [sg.Text('SM-5s',size=(10, 1)), sg.InputText(key='-f5-'),sg.Text('g')],
            [sg.Text('K1/Kd',size=(10, 1)), sg.InputText(key='-f6-'),sg.Text('--')],
            [sg.Text('fd',size=(10, 1)), sg.InputText(key='-f7-'),sg.Text('--')],
            [sg.Text('Td',size=(10, 1)),sg.InputText(key='-f8-'),sg.Text('s')]],title='Input parameters')],
            [sg.Frame(layout=[   
            [sg.Text('Maximum Displacement',size=(22, 1)), sg.InputText(key='-OP-',size=(30, 1)),sg.Text('m')]],title='Output')],
            [sg.Button('Predict'),sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Predicting Maximum Displacement of Seismic Isolation Systems', layout)

filename = 'BestModel_RF_Final.sav'
loaded_model = load(open(filename, 'rb'))
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':	# if user closes window or clicks cancel
        break
    #window['-OP-'].update('Please fill all the input parameters')
    if event == 'Predict':
        #window['-OP-'].update(values[0])
        #break
        if values['-f1-'] == '' or values['-f2-'] == '' or values['-f3-'] == '' or values['-f4-'] == '' or values['-f5-'] == '' or values['-f6-'] == '' or values['-f7-'] == '' or values['-f8-'] == '':

            window['-OP-'].update('Please fill all the input parameters')

        else:

            x_test=np.array([[float(values['-f1-'])*9.81,float(values['-f2-'])*9.81, float(values['-f3-'])*9.81,float(values['-f4-'])*9.81,float(values['-f5-'])*9.81,values['-f6-'],values['-f7-'],values['-f8-']]])
            y_pred_disp = loaded_model.predict(x_test)
            window['-OP-'].update(np.round((y_pred_disp[0]),4))

window.close()
