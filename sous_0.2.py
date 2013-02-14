#-------------------------------------------------------------------------------
# Name:         Sous
# Version:      0.2
# Purpose:      Calculate basic task ordering/timing info for individual meals
#
# Author:       Dave
#
# Created:      11/02/2013
# Copyright:    (c) Dave 2013
# Licence:      <Hands off, you dirty hippies!>
#-------------------------------------------------------------------------------


from pprint import pprint       #Pretty Print
from data_structures import *   #Task & Meal classes, associated functions

##from apscheduler.scheduler import Scheduler
##from datetime import datetime, date, time, timedelta
##import time
##
##from pygraph.classes.graph import graph
##from pygraph.classes.digraph import digraph
##from pygraph.algorithms.searching import breadth_first_search

from kivy.app import App
from kivy.uix.widget import Widget

class PongGame(Widget):
    pass


class PongApp(App):
    def build(self):
        return PongGame()



def main():

    meals = []
    dir1 = "F:\Sous\meal1.json"
    dir2 = "F:\Sous\meal2.json"
    dir3 = "F:\Sous\meal3.json"
    meals.append(load_meal_from_file(dir1, printYN=True))
    meals.append(load_meal_from_file(dir2, True))
    meals.append(load_meal_from_file(dir3))

    pprint (meals[1].graph, width=40)
    pprint (meals[0].graph)

    print meals[2].to_string()
    pprint (meals[2].graph)



if __name__ == '__main__':
    main()
    PongApp().run()