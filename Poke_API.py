import requests 
import time


def get_poke_info(poke):
    #   Gets all of the information about a specified pokemon 
    """
    :param name: Pokemon Name
    :returns: Dictionary of Pokemon Info, if successful. Won't return anything if unsuccessful 
    """
    print("Getting Pokemon Info.....")
    pokemon = poke.lower()
    time.sleep(1)
    resp_msg = requests.get('https://pokeapi.co/api/v2/pokemon/' + pokemon) 
    if resp_msg.status_code == 200:
        print('Success!',"\n")
        return resp_msg.json()
    else:
        print('Action Failed. Response code:', resp_msg.status_code)
        return