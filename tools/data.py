import json

class data:
    def simple(chemin : str, filename : str, name : str  = None):
        with open(f'{chemin}/{filename}.json', 'r') as f:
            if name == None:
                return json.load(f)
            else :
                return json.load(f)[name]
    def list(chemin : str, filename : str, name : str  = None, number : int = None):
        with open(f'{chemin}/{filename}.json', 'r') as f:
            if name == None:
                return json.load(f)
            else :
                return json.load(f)[name][number]
    def tableau(chemin : str, filename : str, name_list : str  = None, name : str = None):
        with open(f'{chemin}/{filename}.json', 'r') as f:
            if name_list == None:
                return json.load(f)
            else :
                return json.load(f)[name_list][name]