#-------------------------------------------------------------------------------
# Name:        data_structures
# Purpose:     Contains Meal and Task classes, plus conversion functions
#
# Author:      Dave
#
# Created:     10/02/2013
# Copyright:   (c) Dave 2013
# Licence:     <Hands off, you dirty hippies!>
#-------------------------------------------------------------------------------

import json #For importing/exporting Json formatted objects

class CTask:
    """A task that forms a sequence of actions to make a meal"""
    UUID = 0
    name = ""
    desc = ""
    #maybe put these into a tuple or something? TODO
    time_total = 0  #total time of this task in seconds
    time_active = 0  #active time: how long the chef is working on this task
    time_passive = 0  #passive time: how long the chef is waiting for this task to complete
    depends_on = []
    dependents = []
    def __init__(self, UUID, name, desc, time_active, time_passive, depends_on, dependents):
        """init a task with values from file/DB"""
        self.UUID = UUID
        self.name = name
        self.desc = desc
        self.time_active = time_active
        self.time_passive = time_passive
        self.time_total = self.time_active + self.time_passive
        self.depends_on = depends_on
        self.dependents = dependents

    def to_string(self):
        output = ("Task \""+ self.name +"\" " + "has UUID: " + str(self.UUID) +" "+
        "and takes " + str(self.time_total) + " ("+str(self.time_active)+ "+" +
        str(self.time_passive)+")" + " seconds.")
        return output


#-------------------------------------------------------------------------------
class CMeal:
    """A meal, its description, ingredients and the tasks to make it"""
    UUID = 0
    name = ""
    desc = ""
    ingredients = []
    tasks = {}
    graph = {}
    def __init__(self, UUID, name, desc, ingredients, tasks):
        self.UUID = UUID
        self.name = name
        self.desc = desc#
        self.ingredients = ingredients
        self.tasks = tasks
        #fill up the ordered graph with tasks, connected via their dependencies
        self.graph = {}                         #self.graph is a dict
        for task in self.tasks:                 #for each task
            self.graph[task] = []               #its value in the dict is an empty array
            for dep in self.tasks[task].depends_on:
                self.graph[task].append(dep)    #add each dependency to that array

    def to_string(self):
        meal_str = ("Meal \""+ self.name +"\" "+
                    "has UUID: "+ str(self.UUID) +" "+
                    "and requires " + str(self.ingredients) + " to make.\n")
        tasks_str = "Tasks: \n"
        for task in self.tasks:
            tasks_str += ("* " + self.tasks[task].to_string() + "\n")
        output = meal_str + tasks_str
        return output



#-------------------------------------------------------------------------------
def Json_to_CTask(JTask):
    """Convert a JSON structure to a CTask"""
    aTask = CTask(JTask["UUID"], JTask["name"], JTask["desc"],
                  JTask["active_time"], JTask["passive_time"],
                  JTask["dependencies"], JTask["dependents"])
    #print aTask.to_string()
    return aTask


#-------------------------------------------------------------------------------
def Json_to_CMeal(JMeal):
    """Convert a JSON structure to a CMeal"""
    j_tasks = JMeal["tasks"]
    c_tasks = {}
    for task in j_tasks:
        c_tasks[task["UUID"]] = (Json_to_CTask(task))

    aMeal = CMeal(JMeal["UUID"], JMeal["name"], JMeal["desc"],
                  JMeal["ingredients"], c_tasks)
    return aMeal


#-------------------------------------------------------------------------------
def load_meal_from_file(dir, printYN = False):
    """Take a json object, parse it and convert it to a CMeal object"""
    file_directory = dir
    json_file = open(file_directory).read()
    json_data = json.loads(json_file)
    loaded_meal = Json_to_CMeal(json_data)
    if printYN:
        print loaded_meal.to_string()
    return loaded_meal


#-------------------------------------------------------------------------------
