#imports
import os
import pickle
import random
from tkinter import ttk
import keyboard
import tkinter as tk
import time
global Cy_Warrior
global Space_Pilot
global Bio_Engineer
global Quantum_Hacker
global Infiltrator
from Classes import Cy_Warrior, Space_Pilot, Bio_Engineer, Quantum_Hacker, Infiltrator 
from weapons import *
from items import *



#creating the window
window = tk.Tk()
window.minsize(width=580,height=220)
window.maxsize(width=580,height=0)

#locations found markers
global Ignis_found, City_square_found, Black_Widow_Craft_Ales_found, The_Angelic_Shoe_found, The_Rainy_Tribute_found, Genius_in_a_Bottle_found, le_Talisman_found, The_Flying_Carpet_found
Ignis_found = False
City_square_found = False
Black_Widow_Craft_Ales_found = False
The_Angelic_Shoe_found = False
The_Rainy_Tribute_found = False
Genius_in_a_Bottle_found = False
le_Talisman_found = False
The_Flying_Carpet_found = False
Adventurers_Den_found = False


global load
load = False


global player_inv
inv_categories = ["weapons","armor","consumables","resouces","currency","misc"]
player_inv = {gpound:200,gcredit:2000}

#making a disabler
def disabler():
    global Locations_all
    global Locations_name
    for i in range(0,len(Locations_all)):
        Locations_all[i] = False
    for i in range(0,len(Locations_all)):
        pickle.dump(Locations_all[i],open(f"{Locations_name[i]}.p","wb"))
    # pickle.dump(Black_Widow_Craft_Ales,open("Black_Widow_Craft_Ales.p","wb"))
    # pickle.dump(The_Angelic_Shoe,open("The_Angelic_Shoe.p","wb"))
    # pickle.dump(The_Rainy_Tribute,open("The_Rainy_Tribute.p","wb"))
    # pickle.dump(Genius_in_a_Bottle,open("Genius_in_a_Bottle.p","wb"))
    # pickle.dump(le_Talisman,open("le_Talisman.p","wb"))
    # pickle.dump(The_Flying_Carpet,open("The_Flying_Carpet.p","wb"))
    # pickle.dump(City_square,open("City_square.p","wb"))
#function to get the text from the entry box
def get_entry_text():
    global selection
    selection = ""
    selection = txt_ent.get()
    #ret = txt_ent.cget('text')
    #selection = str(ret) #txt_ent.cget('text')
#function to print text to the text box
def printString(string):
    for char in string:
        txt.configure(text=txt.cget('text') + char)
        txt.update()
        time.sleep(.01)
def inv_print(string):
    pass
#function to clear the text box
def clear_txt_box():
    txt.configure(text="")
    txt.update()
    window.update()


#column and row values
CRV = 10


#configuring the window
button_labels = ["Inventory","Skills","Stats","Move","Attack","Astro","Ether","Nav Controls","Combat Functions","Comms","Resource Management","Environment","Misc","Action","Location","15","16","17","18","19","20","21","22","23","24"]
for i in range(0, CRV):
    window.columnconfigure(i, weight=1, minsize=1)
    window.rowconfigure(i, weight=1, minsize=1)


#creating the widgets
content = tk.Frame(window)       
txt_frm = tk.Frame(content, borderwidth=5, relief="raised", width=1680, height=100)
txt = tk.Label(txt_frm, text="", wraplength=560,justify="center")
btn_frm = tk.Frame(content, borderwidth=5, relief="raised", width=1680, height=100)
txt_ent = tk.Entry(content,borderwidth=5,relief="raised",width=93)



#button functions



#function to display the inventory
def inventory():
    global inventory_window, inv_tree
    texty =  txt.cget('text')
    inventory_window = tk.Tk()
    inventory_window.title("Inventory")

    #unpickling the items
    

    #inventory widgets
    inv_tree = ttk.Treeview(inventory_window,columns=("quantity"),selectmode="browse")
    inv_tree.heading("#0",text="Item")
    inv_tree.heading("quantity",text="Quantity")

    for i in range(0,len(inv_categories)):
        inv_tree.insert("", "end",id=inv_categories[i], text=inv_categories[i], values=(""), tags=(inv_categories[i]))

    

    for k in player_inv.keys():
        v = player_inv[k]
        t = k.type
        inv_tree.insert(str(k.type), "end", text=k.name, values=(v))
    
    ttk.Style(inv_tree).theme_use("clam")
    ttk.Style(inv_tree).configure("Treeview",background="black",foreground="green",fieldbackground="black")
    ttk.Style(inv_tree).configure("Treeview.Heading",background="black",foreground="green")


    inv_tree.tag_configure("weapons",background="red",foreground="black")
    inv_tree.tag_configure("armor",background="blue",foreground="red")
    inv_tree.tag_configure("consumables",background="yellow",foreground="red")
    inv_tree.tag_configure("resouces",background="purple",foreground="red")
    inv_tree.tag_configure("currency",background="orange",foreground="red")
    inv_tree.tag_configure("misc",background="darkslategrey",foreground="red")
    
    inv_tree.pack()



    fin = False
    while fin == False:
        texty =  txt.cget('text')
        clear_txt_box()
        inventory_window.wait_window(inventory_window)
        printString(texty)
        fin = True
        break












#function to display the skills
def skills():
    global skills_window
    texty = txt.cget('text')
    skills_window = tk.Tk()
    skills_window.title("Skills")
    fin = False
    while not fin:
        texty = txt.cget('text')
        clear_txt_box()
        skills_window.wait_window(skills_window)
        printString(texty)
        fin = True












#function to display the stats
def stats():
    global stats_window, player
    texty = txt.cget('text')
    stats_window = tk.Tk()
    stats_window.title("Stats")
    fin = False

    hp = tk.Label(stats_window ,text="HP: ")
    name = tk.Label(stats_window ,text="Name: "+str(player.name))
    melee = tk.Label(stats_window ,text="Melee: "+str(player.melee))
    ranged = tk.Label(stats_window ,text="Ranged: "+str(player.ranged))
    intelligence = tk.Label(stats_window ,text="Intelligence: "+str(player.intelligence))
    wisdom = tk.Label(stats_window ,text="Wisdom: "+str(player.wisdom))
    durrability = tk.Label(stats_window ,text="Durrability: "+str(player.durability))
    dexterity = tk.Label(stats_window ,text="Dexterity: "+str(player.dexterity))
    navigation = tk.Label(stats_window ,text="Navigation: "+str(player.navigation))

    hp.grid(row=0,column=0)
    name.grid(row=0,column=1)
    melee.grid(row=0,column=2)
    ranged.grid(row=1,column=0)
    intelligence.grid(row=1,column=1)
    wisdom.grid(row=1,column=2)
    durrability.grid(row=2,column=0)
    dexterity.grid(row=2,column=1)
    navigation.grid(row=2,column=2)

    while not fin:
        texty = txt.cget('text')
        clear_txt_box()
        stats_window.wait_window(stats_window)
        txt.configure(text=texty)
        fin = True












#function to move

def move():
    global move_window
    texty = txt.cget('text')
    move_window = tk.Tk()
    move_window.title("Move")
    move_window.tk_setPalette(background="black",foreground="green")

    global close
    close = True

    #unpickling the locations
    try:
        Black_Widow_Craft_Ales = pickle.load(open("Black_Widow_Craft_Ales.p","rb"))
        The_Angelic_Shoe = pickle.load(open("The_Angelic_Shoe.p","rb"))
        The_Rainy_Tribute = pickle.load(open("The_Rainy_Tribute.p","rb"))
        Genius_in_a_Bottle = pickle.load(open("Genius_in_a_Bottle.p","rb"))
        le_Talisman = pickle.load(open("le_Talisman.p","rb"))
        The_Flying_Carpet = pickle.load(open("The_Flying_Carpet.p","rb"))
        City_square = pickle.load(open("City_square.p","rb"))
        Adventurers_Den = pickle.load(open("Adventurers_Den.p","rb"))
    except:
        pass

    #move button functions
    def bwaf():
        disabler()
        global City_square
        City_square = True
        pickle.dump(City_square,open("City_square.p","wb"))
        clear_txt_box()
        move_window.destroy()
        text = "You walk to the Black Widow Craft Ales and enter the bar. The bartender greets you and asks what you would like to drink. What do you do?"
        printString(text)
        time.sleep(0.5)
        window.title("Tex-9__Ignis__Black Widow Craft Ales")
        window.update()
        global Black_Widow_Craft_Ales_found
        Black_Widow_Craft_Ales_found = True
        pickle.dump(Black_Widow_Craft_Ales_found,open("Black_Widow_Craft_Alesf.p","wb"))
        global close
        close = True

    def tasf():
        disabler()
        global City_square
        City_square = True
        pickle.dump(City_square,open("City_square.p","wb"))
        clear_txt_box()
        text = "You walk to The Angelic Shoe and enter the shop. The shopkeeper greets you and asks if you would like to buy anything. What do you do?"
        printString(text)
        time.sleep(0.5)
        move_window.destroy()
        window.title("Tex-9__Ignis__The Angelic Shoe")
        window.update()
        global The_Angelic_Shoe_found
        The_Angelic_Shoe_found = True
        pickle.dump(The_Angelic_Shoe_found,open("The_Angelic_Shoef.p","wb"))
        global close
        close = True

    def trtf():
        disabler()
        global City_square
        City_square = True
        pickle.dump(City_square,open("City_square.p","wb"))
        clear_txt_box()
        text = "You walk to The Rainy Tribute and enter the shop. The shopkeeper greets you and asks if you would like to buy anything. What do you do?"
        printString(text)
        time.sleep(0.5)
        move_window.destroy()
        window.title("Tex-9__Ignis__The Rainy Tribute")
        window.update()
        global The_Rainy_Tribute_found
        The_Rainy_Tribute_found = True
        pickle.dump(The_Rainy_Tribute_found,open("The_Rainy_Tributef.p","wb"))
        global close
        close = True

    def gibf():
        disabler()
        global City_square
        City_square = True
        pickle.dump(City_square,open("City_square.p","wb"))
        clear_txt_box()
        text = "You walk to Genius in a Bottle and enter the shop. The shopkeeper greets you and asks if you would like to buy anything. What do you do?"
        printString(text)
        time.sleep(0.5)
        move_window.destroy()
        window.title("Tex-9__Ignis__Genius in a Bottle")
        window.update()
        global Genius_in_a_Bottle_found
        Genius_in_a_Bottle_found = True
        pickle.dump(Genius_in_a_Bottle_found,open("Genius_in_a_Bottlef.p","wb"))
        global close
        close = True

    def ltf():
        disabler()
        global City_square
        City_square = True
        pickle.dump(City_square,open("City_square.p","wb"))
        clear_txt_box()
        text = "You walk to Le Talisman and enter the shop. The shopkeeper greets you and asks if you would like to buy anything. What do you do?"
        printString(text)
        time.sleep(0.5)
        move_window.destroy()
        window.title("Tex-9__Ignis__Le Talisman")
        window.update()
        global le_Talisman_found
        le_Talisman_found = True
        pickle.dump(le_Talisman_found,open("le_Talismanf.p","wb"))
        global close
        close = True

    def tfcf():
        disabler()
        global City_square
        City_square = True
        pickle.dump(City_square,open("City_square.p","wb"))
        clear_txt_box()
        text = "You walk to The Flying Carpet and enter the shop. The shopkeeper greets you and asks if you would like to buy anything. What do you do?"
        printString(text)
        time.sleep(3)
        move_window.destroy()
        window.title("Tex-9__Ignis__The Flying Carpet")
        window.update()
        global The_Flying_Carpet_found
        The_Flying_Carpet_found = True
        pickle.dump(The_Flying_Carpet_found,open("The_Flying_Carpetf.p","wb"))
        global close
        close = True

    City_square_Locations = [Black_Widow_Craft_Ales, The_Angelic_Shoe, The_Rainy_Tribute, Genius_in_a_Bottle, le_Talisman, The_Flying_Carpet, Adventurers_Den]

    def City_squaref():
        global City_square
        disabler()
        for i in range(0,len(City_square_Locations)):
            global Locations_name
            City_square_Locations[i] = True
            pickle.dump(City_square_Locations[i],open(f"{Locations_name[i]}.p","wb"))
        City_square = False
        pickle.dump(City_square,open("City_square.p","wb"))
        clear_txt_box()
        text = "You walk to the City Square and look around. You see a few shops and a bar. What do you do?"
        printString(text)
        time.sleep(0.5)
        move_window.destroy()
        window.title("Tex-9__Ignis__City Square")
        window.update()
        global City_square_found
        City_square_found = True
        pickle.dump(City_square_found,open("City_squaref.p","wb"))
        global close
        close = True
    
    def Adventurers_Denf():
        disabler()
        global City_square
        City_square = True
        pickle.dump(City_square,open("City_square.p","wb"))
        clear_txt_box()
        text = "You walk to the Adventurers Den and enter the den. You see a few adventurers and a shop. What do you do?"
        printString(text)
        time.sleep(0.5)
        move_window.destroy()
        window.title("Tex-9__Ignis__Adventurers Den")
        window.update()
        global Adventurers_Den_found
        Adventurers_Den_found = True
        pickle.dump(Adventurers_Den_found,open("Adventurers_Denf.p","wb"))
        global close
        close = True


    #move widgets
    north = tk.Button(move_window,text="North")
    south = tk.Button(move_window,text="South")
    east = tk.Button(move_window,text="East")
    west = tk.Button(move_window,text="West")
    north.grid(row=0,column=1)
    south.grid(row=2,column=1)
    east.grid(row=1,column=2)
    west.grid(row=1,column=0)
    if Black_Widow_Craft_Ales == True:
        bwa = tk.Button(move_window,text="Black Widow Craft Ales",command=bwaf)
        bwa.grid(row=3,column=0)
    if The_Angelic_Shoe == True:
        tas = tk.Button(move_window,text="The Angelic Shoe",command=tasf)
        tas.grid(row=3,column=1)
    if The_Rainy_Tribute == True:
        trt = tk.Button(move_window,text="The Rainy Tribute",command=trtf)
        trt.grid(row=3,column=2)
    if Genius_in_a_Bottle == True:
        gib = tk.Button(move_window,text="Genius in a Bottle",command=gibf)
        gib.grid(row=4,column=0)
    if le_Talisman == True:
        lt = tk.Button(move_window,text="Le Talisman",command=ltf)
        lt.grid(row=4,column=1)
    if The_Flying_Carpet == True:
        tfc = tk.Button(move_window,text="The Flying Carpet",command=tfcf)
        tfc.grid(row=4,column=2)
    if City_square == True:
        cs = tk.Button(move_window,text="City Square",command=City_squaref)
        cs.grid(row=3,column=1)
    if Adventurers_Den == True:
        ad = tk.Button(move_window,text="Adventurers Den",command=Adventurers_Denf)
        ad.grid(row=5,column=0)

    
    #fin = False
    while close == False:
        texty = txt.cget('text')
        clear_txt_box()
        move_window.wait_window(move_window)
        printString(texty)
        #fin = True












#function to attack
def attack():
    global attack_window
    texty = txt.cget('text')
    attack_window = tk.Tk()
    attack_window.title("Attack")
    fin = False
    while not fin:
        texty = txt.cget('text')
        clear_txt_box()
        attack_window.wait_window(attack_window)
        printString(texty)
        fin = True












#function to display the astro
def astro():
    global astro_window
    texty = txt.cget('text')
    astro_window = tk.Tk()
    astro_window.title("Astro")
    fin = False
    while not fin:
        texty = txt.cget('text')
        clear_txt_box()
        astro_window.wait_window(astro_window)
        printString(texty)
        fin = True












#function to display the ether
def ether():
    global ether_window
    texty = txt.cget('text')
    ether_window = tk.Tk()
    ether_window.title("Ether")
    fin = False
    while not fin:
        texty = txt.cget('text')
        clear_txt_box()
        ether_window.wait_window(ether_window)
        printString(texty)
        fin = True












#function to display the nav controls
def nav_controls():
    global nav_controls_window
    texty = txt.cget('text')
    nav_controls_window = tk.Tk()
    nav_controls_window.title("Nav Controls")
    fin = False
    while not fin:
        texty = txt.cget('text')
        clear_txt_box()
        nav_controls_window.wait_window(nav_controls_window)
        printString(texty)
        fin = True












#function to display the combat functions
def combat_functions():
    global combat_functions_window
    texty = txt.cget('text')
    combat_functions_window = tk.Tk()
    combat_functions_window.title("Combat Functions")
    fin = False
    while not fin:
        texty = txt.cget('text')
        clear_txt_box()
        combat_functions_window.wait_window(combat_functions_window)
        printString(texty)
        fin = True












#function to display the comms
def comms():
    global comms_window
    texty = txt.cget('text')
    comms_window = tk.Tk()
    comms_window.title("Comms")
    fin = False
    while not fin:
        texty = txt.cget('text')
        clear_txt_box()
        comms_window.wait_window(comms_window)
        printString(texty)
        fin = True












#function to display the resource management
def resource_management():
    global resource_management_window
    texty = txt.cget('text')
    resource_management_window = tk.Tk()
    resource_management_window.title("Resource Management")

    fin = False
    while not fin:
        texty = txt.cget('text')
        clear_txt_box()
        resource_management_window.wait_window(resource_management_window)
        printString(texty)
        fin = True
    










#function to display the environment
def environment():
    global environment_window
    texty = txt.cget('text')
    environment_window = tk.Tk()
    environment_window.title("Environment")
    fin = False
    while not fin:
        texty = txt.cget('text')
        clear_txt_box()
        environment_window.wait_window(environment_window)
        printString(texty)
        fin = True












#function to display the misc
def misc():
    global misc_window
    texty = txt.cget('text')
    misc_window = tk.Tk()
    misc_window.title("Misc")
    fin = False
    while not fin:
        texty = txt.cget('text')
        clear_txt_box()
        misc_window.wait_window(misc_window)
        printString(texty)
        fin = True












#function to display the Action
def action():
    global action_window
    texty = txt.cget('text')
    action_window = tk.Tk()
    action_window.title("Action")
    fin = False
    while not fin:
        texty = txt.cget('text')
        clear_txt_box()
        action_window.wait_window(action_window)
        printString(texty)
        fin = True












#function to display the location
#pointer
def location():
    global location_window, Ignis_found, City_square_found, Black_Widow_Craft_Ales_found, The_Angelic_Shoe_found, The_Rainy_Tribute_found, Genius_in_a_Bottle_found, le_Talisman_found, The_Flying_Carpet_found, Adventurers_Den_found
    texty = txt.cget('text')
    location_window = tk.Tk()
    location_window.title("Location")

    #unpickling the findings
    try:
        Ignis_found = pickle.load(open("Ignisf.p","rb"))
    except:
        pass

    try:
        City_square_found = pickle.load(open("City_squaref.p","rb"))
    except:
        pass

    try:
        Black_Widow_Craft_Ales_found = pickle.load(open("Black_Widow_Craft_Alesf.p","rb"))
    except:
        pass

    try:
        The_Angelic_Shoe_found = pickle.load(open("The_Angelic_Shoef.p","rb"))
    except:
        pass

    try:
        The_Rainy_Tribute_found = pickle.load(open("The_Rainy_Tributef.p","rb"))
    except:
        pass

    try:
        Genius_in_a_Bottle_found = pickle.load(open("Genius_in_a_Bottlef.p","rb"))
    except:
        pass

    try:
        le_Talisman_found = pickle.load(open("le_Talismanf.p","rb"))
    except:
        pass

    try:
        The_Flying_Carpet_found = pickle.load(open("The_Flying_Carpetf.p","rb"))
    except:
        pass

    try:
        Adventurers_Den_found = pickle.load(open("Adventurers_Denf.p","rb"))
    except:
        pass

    #location widgets
    location = ttk.Treeview(location_window)
    updater = tk.Button(location_window,text="Update",command=location)
    #location.column('test', width=100,anchor='center', stretch=tk.NO)
    #location.heading('test', text='Test')
    location.heading('#0', text='Location')
    location.tag_configure('Planet', background='red',foreground='white')
    location.tag_configure('Zone', background='blue',foreground='white')
    location.tag_configure('City', background='green',foreground='black')
    location.tag_configure('Area', background='yellow',foreground='black')
    location.tag_configure('Building', background='Black',foreground='green')
    location.tag_configure('Clicked', background='Purple',foreground='black')
    updater.pack()
    location.insert('',"end",'Planet',text="Tex-9",tags=('Planet'))
    
    
    if Ignis_found == True:
        location.insert('Planet',"end",'Ignis',text="Ignis",tags=('Zone'))

    if City_square_found == True:
        location.insert('Ignis',"end",'City Square',text="City Square",tags=('City'))

    if Black_Widow_Craft_Ales_found == True:
        location.insert('City Square',"end",'Black Widow Craft Ales',text="Black Widow Craft Ales",tags=('Building'))

    if The_Angelic_Shoe_found == True:
        location.insert('City Square',"end",'The Angelic Shoe',text="The Angelic Shoe",tags=('Building'))

    if The_Rainy_Tribute_found == True:
        location.insert('City Square',"end",'The Rainy Tribute',text="The Rainy Tribute",tags=('Building'))

    if Genius_in_a_Bottle_found == True:
        location.insert('City Square',"end",'Genius in a Bottle',text="Genius in a Bottle",tags=('Building'))

    if le_Talisman_found == True:
        location.insert('City Square',"end",'Le Talisman',text="Le Talisman",tags=('Building'))

    if The_Flying_Carpet_found == True:
        location.insert('City Square',"end",'The Flying Carpet',text="The Flying Carpet",tags=('Building'))

    if Adventurers_Den_found == True:
        location.insert('City Square',"end",'Adventurers Den',text="Adventurers Den",tags=('Building'))


    location.pack()

    fin = False
    while not fin:
        texty = txt.cget('text')
        clear_txt_box()
        location_window.wait_window(location_window)
        printString(texty)
        fin = True












#function to display the 15
def fifteen():
    global fifteen_window
    texty = txt.cget('text')
    fifteen_window = tk.Tk()
    fifteen_window.title("15")
    fin = False
    while not fin:
        texty = txt.cget('text')
        clear_txt_box()
        fifteen_window.wait_window(fifteen_window)
        printString(texty)
        fin = True












#function to display the 16
def sixteen():
    global sixteen_window
    texty = txt.cget('text')
    sixteen_window = tk.Tk()
    sixteen_window.title("16")
    fin = False
    while not fin:
        texty = txt.cget('text')
        clear_txt_box()
        sixteen_window.wait_window(sixteen_window)
        printString(texty)
        fin = True












#function to display the 17
def seventeen():
    global seventeen_window
    texty = txt.cget('text')
    seventeen_window = tk.Tk()
    seventeen_window.title("17")
    fin = False
    while not fin:
        texty = txt.cget('text')
        clear_txt_box()
        seventeen_window.wait_window(seventeen_window)
        printString(texty)
        fin = True












#function to display the 18
def eighteen():
    global eighteen_window
    texty = txt.cget('text')
    eighteen_window = tk.Tk()
    eighteen_window.title("18")
    fin = False
    while not fin:
        texty = txt.cget('text')
        clear_txt_box()
        eighteen_window.wait_window(eighteen_window)
        printString(texty)
        fin = True












#function to display the 19
def nineteen():
    global nineteen_window
    texty = txt.cget('text')
    nineteen_window = tk.Tk()
    nineteen_window.title("19")
    fin = False
    while not fin:
        texty = txt.cget('text')
        clear_txt_box()
        nineteen_window.wait_window(nineteen_window)
        printString(texty)
        fin = True












#function to display the 20
def twenty():
    global twenty_window
    texty = txt.cget('text')
    twenty_window = tk.Tk()
    twenty_window.title("20")
    fin = False
    while not fin:
        texty = txt.cget('text')
        clear_txt_box()
        twenty_window.wait_window(twenty_window)
        printString(texty)
        fin = True












#function to display the 21
def twentyone():
    global twentyone_window
    texty = txt.cget('text')
    twentyone_window = tk.Tk()
    twentyone_window.title("21")
    fin = False
    while not fin:
        texty = txt.cget('text')
        clear_txt_box()
        twentyone_window.wait_window(twentyone_window)
        printString(texty)
        fin = True












#function to display the 22
def twentytwo():
    global twentytwo_window
    texty = txt.cget('text')
    twentytwo_window = tk.Tk()
    twentytwo_window.title("22")
    fin = False
    while not fin:
        texty = txt.cget('text')
        clear_txt_box()
        twentytwo_window.wait_window(twentytwo_window)
        printString(texty)
        fin = True












#function to display the 23
def twentythree():
    global twentythree_window
    texty = txt.cget('text')
    twentythree_window = tk.Tk()
    twentythree_window.title("23")
    fin = False
    while not fin:
        texty = txt.cget('text')
        clear_txt_box()
        twentythree_window.wait_window(twentythree_window)
        printString(texty)
        fin = True












#function to display the 24
def twentyfour():
    global twentyfour_window
    texty = txt.cget('text')
    twentyfour_window = tk.Tk()
    twentyfour_window.title("24")
    fin = False
    while not fin:
        texty = txt.cget('text')
        clear_txt_box()
        twentyfour_window.wait_window(twentyfour_window)
        printString(texty)
        fin = True











    

#list of functions
functions = [inventory,skills,stats,move,attack,astro,ether,nav_controls,combat_functions,comms,resource_management,environment,misc,action,location,fifteen,sixteen,seventeen,eighteen,nineteen,twenty,twentyone,twentytwo,twentythree,twentyfour]














#formatting the buttons
x= -1
for i in range(0,5):
    btn_frm.columnconfigure(i, weight=1, minsize=1)
    btn_frm.rowconfigure(i, weight=1, minsize=1)
    
    for j in range(0, 5):
        button = tk.Button(
            master=btn_frm,
            relief=tk.RAISED,
            borderwidth=1,
            text="",
            command=functions[x+1]
        )
        x+=1
        button.grid(row=i, column=j, padx=5, pady=5)
        button.config(text=button_labels[x])













#placing the widgets
content.grid(column=0, row=0)
txt_frm.grid(column=0, row=0, columnspan=10,rowspan=5, sticky="nsew")
txt.pack(fill="x")
txt_ent.grid(column=0,row=5,sticky="n")
btn_frm.grid(column=0,row=6,columnspan=10,rowspan=4,sticky="nsew")













#load save
def load_save():
    global load
    load = True
    global Ignis_found, City_square_found, Black_Widow_Craft_Ales_found, The_Angelic_Shoe_found, The_Rainy_Tribute_found, Genius_in_a_Bottle_found, le_Talisman_found, The_Flying_Carpet_found, Adventurers_Den_found
    global player
    global Locations_all
    global Locations_name
    for i in Locations_all:
        try:
            Locations_all[i] = pickle.load(open(f"{Locations_name[i]}.p","rb"))
        except:
            pass
    try:
        Ignis_found = pickle.load(open("Ignisf.p","rb"))
        City_square_found = pickle.load(open("City_squaref.p","rb"))
        Black_Widow_Craft_Ales_found = pickle.load(open("Black_Widow_Craft_Alesf.p","rb"))
        The_Angelic_Shoe_found = pickle.load(open("The_Angelic_Shoef.p","rb"))
        The_Rainy_Tribute_found = pickle.load(open("The_Rainy_Tributef.p","rb"))
        Genius_in_a_Bottle_found = pickle.load(open("Genius_in_a_Bottlef.p","rb"))
        le_Talisman_found = pickle.load(open("le_Talismanf.p","rb"))
        The_Flying_Carpet_found = pickle.load(open("The_Flying_Carpetf.p","rb"))
        Adventurers_Den_found = pickle.load(open("Adventurers_Denf.p","rb"))
        player = pickle.load(open("player.p","rb"))

    except:
        load = False
    start()
    











#save game
def save_game():
    global Ignis_found, City_square_found, Black_Widow_Craft_Ales_found, The_Angelic_Shoe_found, The_Rainy_Tribute_found, Genius_in_a_Bottle_found, le_Talisman_found, The_Flying_Carpet_found, Adventurers_Den_found
    global player
    #pickleing markers
    pickle.dump(Ignis_found,open("Ignisf.p","wb"))
    pickle.dump(City_square_found,open("City_squaref.p","wb"))
    pickle.dump(Black_Widow_Craft_Ales_found,open("Black_Widow_Craft_Alesf.p","wb"))
    pickle.dump(The_Angelic_Shoe_found,open("The_Angelic_Shoef.p","wb"))
    pickle.dump(The_Rainy_Tribute_found,open("The_Rainy_Tributef.p","wb"))
    pickle.dump(Genius_in_a_Bottle_found,open("Genius_in_a_Bottlef.p","wb"))
    pickle.dump(le_Talisman_found,open("le_Talismanf.p","wb"))
    pickle.dump(The_Flying_Carpet_found,open("The_Flying_Carpetf.p","wb"))
    pickle.dump(Adventurers_Den_found,open("Adventurers_Denff.p","wb"))
    
    try:
        pickle.dump(player,open("player.p","wb"))
    except:
        pass
    clear_txt_box()
    text = "Your game has been saved"
    printString(text)
    time.sleep(1)
    clear_txt_box()
    text = "Goodbye"
    printString(text)
    time.sleep(0.5)
    exit()












#ask the player if they want to load a save
def Query():
    text = "Do you want to load a save?"
    printString(text)
    answer = False
    while answer == False:
        window.update()
        get_entry_text()
        if selection == "1":
            txt_ent.delete(0,tk.END)
            load_save()
        if selection == "2":
            txt_ent.delete(0,tk.END)
            start()












# Function to start the game
def start():
    window.title("Adventure begins")
    clear_txt_box()
    global text
    text = "Welcome to the planet Tex-9. I'll run you through a few things; first of all my name is Rex Langer and i'm a sophisticated travel A.I., secondly, as you may have already noticed this planet is orbiting a dual star system and has 12 sister planets, third, your sole aim on this planet is to conquer it and colonize it and finally"
    printString(text)
    time.sleep(0.5)
    text = " don't die."
    printString(text)
    time.sleep(2.5)
    get_entry_text()
    if load == False:
        select_class()
    else:
        game()












# Function to prompt the user to select a class
def select_class():
    # Display class options to the user
    clear_txt_box()
    window.title("Select your Class")
    text = "1 " + "Cy_Warrior" + "\n"
    printString(text)
    text = "2 " + "Space_Pilot" + "\n"
    printString(text)
    text = "3 " + "Bio_Engineer" + "\n"
    printString(text)
    text = "4 " + "Quantum_Hacker" + "\n"
    printString(text)
    text = "5 " + "Infiltrator" + "\n"
    printString(text)
    text = "Pick a class from above using the numbers before."
    printString(text)
    

    
    answer = False
    # Loop until a valid class is selected
    while answer == False:
        window.update()
        get_entry_text()
        if selection in ["1", "2", "3", "4", "5",1,2,3,4,5]:
            answer = True
            clear_txt_box()
            txt_ent.delete(0, tk.END)
            text = "You have selected class " + selection
            printString(text)
    
    
    #player creation
    global namer
    namer = random.randint(0,9)
    Names_cywarrior = ["Issa","Hora","Kek","Vena","Nix","Astartus","Asardin","Nirmal","Anskar","Eirforað"]
    Names_spacepilot = ["Satet","Ganmaes","Galmami","Dobrur","Murboic","Giggamri","Lolger","Ludit","Kirgod","Fodgrear"]
    Names_bioengineer = ["Enusim","Iphiar","Asuless","Aprix","Amazz","Ebaris","Orokey","Farass","Alin","Emidel"]
    Names_quantumhacker = ["Paragon","Umbra","Azrael","Tyran","Primrose","Rose","Asp","Zot","Vex","Dawn"]
    Names_infiltrator = ["Guarde","Mongrel","Shank","Lore","Raine","Nightshade","Nil","Thorne","Mockingbird","Lynch"]
    global meleer, ranger, inteller, wisdomer, durabilityer, dexterityer, navigationer
    meleer = random.randint(11,20)
    ranger = random.randint(11,20)
    inteller = random.randint(11,20)
    wisdomer = random.randint(11,20)
    durabilityer = random.randint(11,20)
    dexterityer = random.randint(11,20)
    navigationer = random.randint(11,20)
    global player
    global load
    if load == False:
        if selection == "1":
            global player
            player = Cy_Warrior(Names_cywarrior[namer],meleer+5,ranger+1,inteller,wisdomer+3,durabilityer+2,dexterityer+1,navigationer)
            playerp = pickle.dump(player,open("player.p","wb"))
        elif selection == "2":
            player = Space_Pilot(Names_spacepilot[namer],meleer,ranger+1,inteller+2,wisdomer+1,durabilityer,dexterityer+3,navigationer+5)
            playerp = pickle.dump(player,open("player.p","wb"))
        elif selection == "3":
            player = Bio_Engineer(Names_bioengineer[namer],meleer,ranger+2,inteller+5,wisdomer+1,durabilityer+1,dexterityer+2,navigationer+1)
            playerp = pickle.dump(player,open("player.p","wb"))
        elif selection == "4":
            player = Quantum_Hacker(Names_quantumhacker[namer],meleer,ranger+2,inteller+5,wisdomer+3,durabilityer,dexterityer+2,navigationer)
            playerp = pickle.dump(player,open("player.p","wb"))
        elif selection == "5":
            player = Infiltrator(Names_infiltrator[namer],meleer+2,ranger+2,inteller+2,wisdomer,durabilityer,dexterityer+5,navigationer+1)
            playerp = pickle.dump(player,open("player.p","wb"))
    else:
        playerp = pickle.load(open("player.p","rb"))
        player = playerp
    
    time.sleep(3)
    game()  # Start the game












# Function to handle the main game logic
def game():
    clear_txt_box()
    window.title("Tex-9__Ignis")
    global Ignis_found
    Ignis_found = True
    pickle.dump(Ignis_found,open("Ignisfs.p","wb"))

    # Display welcome message
    text = "welcome to the wide world"
    printString(text)
    time.sleep(2)
    clear_txt_box()
    
    # Display initial game scenario
    # print("name: "+player.name)
    # try:
    #     print("melee: "+ str(player.melee))
    #     print("ranged: "+ str(player.ranged))
    #     print("intelligence: "+ str(player.intelligence))
    #     print("wisdom: "+ str(player.wisdom))
    #     print("durability: "+ str(player.durability))
    #     print("dexterity: "+ str(player.dexterity))
    #     print("navigation: "+ str(player.navigation))
    # except:
    #     pass
    text = "You find yourself in a city square, the suns are shining and the people are going about their business. You see a few shops and a bar. There's a sign pointing toward the Adventurers Den. What do you do?"
    global City_square_found
    City_square_found = True
    disabler()
    pickle.dump(City_square_found,open("City_squaref.p","wb"))
    printString(text)
    time.sleep(1)
    global Black_Widow_Craft_Ales, The_Angelic_Shoe, The_Rainy_Tribute, Genius_in_a_Bottle, le_Talisman, The_Flying_Carpet, Adventurers_Den, City_square
    Black_Widow_Craft_Ales = True
    The_Angelic_Shoe = True
    The_Rainy_Tribute = True
    Genius_in_a_Bottle = True
    le_Talisman = True
    The_Flying_Carpet = True
    Adventurers_Den = True
    City_square = False
    pickle.dump(City_square,open("City_square.p","wb"))
    pickle.dump(Black_Widow_Craft_Ales,open("Black_Widow_Craft_Ales.p","wb"))
    pickle.dump(The_Angelic_Shoe,open("The_Angelic_Shoe.p","wb"))
    pickle.dump(The_Rainy_Tribute,open("The_Rainy_Tribute.p","wb"))
    pickle.dump(Genius_in_a_Bottle,open("Genius_in_a_Bottle.p","wb"))
    pickle.dump(le_Talisman,open("le_Talisman.p","wb"))
    pickle.dump(The_Flying_Carpet,open("The_Flying_Carpet.p","wb"))
    pickle.dump(Adventurers_Den,open("Adventurers_Den.p","wb"))
    answer = False
    while answer == False:
        get_entry_text()
        window.update()
        if selection == "1":
            txt_ent.delete(0, tk.END)
            end()
        else:
            pass
    #Coming soon













def end():
    clear_txt_box()
    text = "The end of the game"
    printString(text)
    time.sleep(1)
    text = "\n Do you want to save?"
    printString(text)
    time.sleep(1)
    answer = False
    while answer == False:
        get_entry_text()
        window.update()
        if selection == "1":
            save_game()
            txt_ent.delete(0,tk.END)
            clear_txt_box()
        if selection == "2":
            delete_save()
            clear_txt_box()


def delete_save():
    try:
        os.remove("player.p")
        os.remove("Ignis.p")
        os.remove("City_square.p")
        os.remove("Black_Widow_Craft_Ales.p")
        os.remove("The_Angelic_Shoe.p")
        os.remove("The_Rainy_Tribute.p")
        os.remove("Genius_in_a_Bottle.p")
        os.remove("le_Talisman.p")
        os.remove("The_Flying_Carpet.p")
        os.remove("Adventurers_Den.p")
        print("Save deleted")
    except:
        pass
    text = "Save deleted"
    printString(text)
    time.sleep(1)
    clear_txt_box()
    text = "Goodbye"
    printString(text)
    time.sleep(1)
    exit()











#locations
global Locations_all
global Locations_name
global City_square
global Black_Widow_Craft_Ales
global The_Angelic_Shoe
global The_Rainy_Tribute
global Genius_in_a_Bottle
global le_Talisman
global The_Flying_Carpet
global Adventurers_Den
global Etherpoint
global The_Pearly_Forests
global Mather_Island
global Selene
global Prodigy
global Terminus_Eternity
global Revelation_Colony
global Helios_Colony
global Icihala
City_square = False
Black_Widow_Craft_Ales = False
The_Angelic_Shoe = False
The_Rainy_Tribute = False
Genius_in_a_Bottle = False
le_Talisman = False
The_Flying_Carpet = False
Adventurers_Den = False
Etherpoint = False
The_Pearly_Forests = False
Mather_Island = False
Selene = False
Prodigy = False
Terminus_Eternity = False
Revelation_Colony = False
Helios_Colony = False
Icihala = False
Locations_all=[City_square, Black_Widow_Craft_Ales, The_Angelic_Shoe, The_Rainy_Tribute, Genius_in_a_Bottle, le_Talisman, The_Flying_Carpet, Adventurers_Den, Etherpoint, The_Pearly_Forests, Mather_Island, Selene, Prodigy, Terminus_Eternity, Revelation_Colony, Helios_Colony, Icihala]
Locations_name=["City_square","Black_Widow_Craft_Ales", "The_Angelic_Shoe", "The_Rainy_Tribute", "Genius_in_a_Bottle", "le_Talisman", "The_Flying_Carpet", "Adventurers_Den", "Etherpoint", "The_Pearly_Forests", "Mather_Island", "Selene", "Prodigy", "Terminus_Eternity", "Revelation_Colony", "Helios_Colony", "Icihala"]

for i in range(0,len(Locations_all)):
    try:
        pickle.dump(Locations_all[i],open(f"{Locations_name[i]}.p","wb"))
    except:
        pass










# Entry point of the script
if __name__ == "__main__":
    Query()
    
    


window.mainloop()  # Start the Tkinter main loop