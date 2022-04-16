#   LAB 8 PYTHON 
#   -----------------------------------------------------------------
#   -----------------------------------------------------------------
#   PROGRAM DESCRIPTION: This lab is designed to create a GUI page of
#   the POKEAPI and allow the user to input a certain pokemon, and 
#   their results will show up on the GUI information page after 
#   getting the results from the PokeAPI.
#   -----------------------------------------------------------------
#   -----------------------------------------------------------------
#   USAGE: python Lab8_PokeGUI.py
#
#   -----------------------------------------------------------------
#   -----------------------------------------------------------------
#
#   DUE DATE: MONDAY APRIL 18TH, 2022
#
#   -----------------------------------------------------------------
#   -----------------------------------------------------------------
#   HISTORY:
#       DATE        AUTHOR      Description
#       2022-04-11  N.KAPSHEY   Initial Creation
#
#   _________________________________________________________________
#   

from tkinter import *
from tkinter import ttk
from Poke_API import get_poke_info

def main():
    
    #   Initialize the Window
    root = Tk()
    root.title("The Poke View 3000")
    root.iconbitmap("poke.ico")
    
    #   Create the Window frame
    frm_user_input = ttk.Frame(root)
    frm_user_input.grid(row=0, column=0, columnspan=2, padx = 10, pady = 10)
    root.geometry('450x450')
    
    frm_info = ttk.LabelFrame(root, text='Info')
    frm_info.grid(row=1, column=0, padx = 10, pady = 10)
    
    frm_stats = ttk.LabelFrame(root, text='Stats')
    frm_stats.grid(row=1, column=1, padx = 10, pady = 10)
    
    #   Create the input areas
    lbl_name = ttk.Label(frm_user_input, text='Pokemon Name:')
    lbl_name.grid(row = 0, column = 0, padx = 10, pady = 10)
    
    ent_name = ttk.Entry(frm_user_input) 
    ent_name.grid(row = 0, column = 1, pady = 10)
    
    def btn_get_info_click():
        #   Get the info of the Pokemon frm PokeAPI
        pokemon_name = ent_name.get()
        pokemon_name.lower()
        print (pokemon_name)
        poke_dict = get_poke_info(pokemon_name)
        if poke_dict:
            lbl_height_val['text'] = str(poke_dict['height']) + " dm"
            types_list = (t['type']['name']for t in poke_dict['types'])
            lbl_type_val['text'] = ', '.join(types_list)
            lbl_weight_val['text'] = str(poke_dict['weight']) + " hg"
            prg_hp['value'] = poke_dict['stats'][0]['base_stat']
            prg_attack['value'] = poke_dict['stats'][1]['base_stat']
            prg_defense['value'] = poke_dict['stats'][2]['base_stat']
            prg_sA['value'] = poke_dict['stats'][3]['base_stat']
            prg_sD['value'] = poke_dict['stats'][4]['base_stat']
            prg_speed['value'] = poke_dict['stats'][5]['base_stat']
            
    btn_get_info = ttk.Button(frm_user_input, text = 'Get Info', command = btn_get_info_click)
    btn_get_info.grid(row = 0, column = 2, padx = 10, pady = 10)

    #   Populate the INFO, TYPE, widgets in the info frame
    lbl_height = ttk.Label(frm_info, text = 'Height:')
    lbl_height.grid(row = 1, column=1, padx = 5, pady = 10, sticky = E)
    lbl_height_val = ttk.Label(frm_info, text = '')
    lbl_height_val.grid(row = 1, column=2, padx = 5, pady = 10)
   
    lbl_type = ttk.Label(frm_info, text = 'Type: ')
    lbl_type.grid(row = 2, column=1, padx = 5, pady = 10, sticky = E)
    lbl_type_val = ttk.Label(frm_info, text = '')
    lbl_type_val.grid(row = 2, column=2, padx = 5, pady = 10)
    
    lbl_weight = ttk.Label(frm_info, text = 'Weight: ')
    lbl_weight.grid(row = 3, column=1, padx = 5, pady = 10, sticky = E)
    lbl_weight_val = ttk.Label(frm_info, text = '')
    lbl_weight_val.grid(row = 3, column=2, padx = 5, pady = 10)
    
    #   Calculate the widgets for the other stat grid
    lbl_hp = ttk.Label(frm_stats, text = 'HP: ')
    lbl_hp.grid(row = 1, column = 1, padx = 5, pady = 10, sticky = E)
    prg_hp = ttk.Progressbar(frm_stats, length=200, maximum = 255)
    prg_hp.grid(row = 1, column = 2, padx = 5, pady = 10)
    
    lbl_attack = ttk.Label(frm_stats, text = 'Attack: ')
    lbl_attack.grid(row = 2, column = 1, padx = 5, pady = 10, sticky = E)
    prg_attack = ttk.Progressbar(frm_stats, length=200, maximum = 255)
    prg_attack.grid(row = 2, column = 2, padx = 5, pady = 10)
    
    lbl_defense = ttk.Label(frm_stats, text = 'Defense: ')
    lbl_defense.grid(row = 3, column = 1, padx = 5, pady = 10, sticky = E)
    prg_defense = ttk.Progressbar(frm_stats, length=200, maximum = 255)
    prg_defense.grid(row = 3, column = 2, padx = 5, pady = 10)
    
    lbl_sA = ttk.Label(frm_stats, text = 'Speed Attack: ')
    lbl_sA.grid(row = 4, column = 1, padx = 5, pady = 10, sticky = E)
    prg_sA = ttk.Progressbar(frm_stats, length=200, maximum = 255)
    prg_sA.grid(row = 4, column = 2, padx = 5, pady = 10)
    
    lbl_sD = ttk.Label(frm_stats, text = 'Speed Defense: ')
    lbl_sD.grid(row = 5, column = 1, padx = 5, pady = 10, sticky = E)
    prg_sD = ttk.Progressbar(frm_stats, length=200, maximum = 255)
    prg_sD.grid(row = 5, column = 2, padx = 5, pady = 10)
    
    lbl_speed = ttk.Label(frm_stats, text = 'Speed: ')
    lbl_speed.grid(row = 6, column = 1, padx = 5, pady = 10, sticky = E)
    prg_speed = ttk.Progressbar(frm_stats, length=200, maximum = 255)
    prg_speed.grid(row = 6, column = 2, padx = 5, pady = 10)
    
    root.mainloop()


    pass 


main()