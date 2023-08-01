import json

chemin = "database/"

def importdata(chemin : str, filename : str, name : str  = None):
    with open(f'{chemin}/{filename[:-5]}.json', 'r') as f:
        
        if name == None:
            return json.load(f)
        else :
            return json.load(f)[name]

class Check:
    def owner(id: str):
        with open('database/buyer-owner.json', 'r') as f:
            owner_file = json.load(f)
        for ownerid in owner_file['owner']:
            if ownerid == str(id):
                return True 
        
            