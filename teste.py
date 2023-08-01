import json

def list_json(chemin : str, filename : str, name_list : str  = None, name : str = None):
        with open(f'{chemin}/{filename}.json', 'r') as f:
            if name_list == None:
                return json.load(f)
            else :
                return json.load(f)[name_list][name]
print(list_json(chemin='database/', filename='payement', name_list='paypal', name='link' ))