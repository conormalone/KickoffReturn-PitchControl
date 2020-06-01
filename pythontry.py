# -*- coding: utf-8 -*-
"""
Created on Thu May 14 20:32:20 2020

@author: conny
"""
import Metrica_IO as mio
import Metrica_Viz as mviz
import Metrica_Velocities as mvel

import myversion_Metrica_PitchControl as mympc
import numpy as np
from pandas import DataFrame, read_csv
import pandas as pd 

tracking_home = pd.read_csv('C:\\Users\\conny\\OneDrive\\Documents\\KickoffReturn-PitchControl\\PossTeams.csv')

tracking_away = pd.read_csv('C:\\Users\\conny\\OneDrive\\Documents\\KickoffReturn-PitchControl\\DefTeams.csv')

Player_Speed_DF = pd.read_csv('C:\\Users\\conny\\OneDrive\\Documents\\KickoffReturn-PitchControl\\speed_widedata.csv')

#PassEvents = events[events.Type == "PASS"]

#passeventlist = events["Start Time [s]" ][events["Start Time [s]"] > 3000 & events["Start Time [s]"] < 3011 ].index
mylist = []
for i in range(0,641):
    try:
        PPCF,xgrid,ygrid = mympc.generate_pitch_control_for_event(i, tracking_home, tracking_away, params, Player_Speed_DF, field_dimen = (106.,68.,), n_grid_cells_x = 50)
    except IndexError:
        pass
    #mylist.append(PPCF)
    np.savetxt(str(i)+'.csv', PPCF, delimiter=',')


#np.savetxt("test.txt",mylist, delimiter = ', ', fmt ='%12.8f')