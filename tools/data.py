import json
CREDIT = "made by 0xadn"
class importdata:
    def simple(chemin : str, filename : str, name : str  = None):
        with open(f'{chemin}/{filename}.json', 'r') as f:
                return json.load(f)[name]
    def list(chemin : str, filename : str, name : str  = None, number : int = None):
        with open(f'{chemin}/{filename}.json', 'r') as f:
                return json.load(f)[name][number]
    def tableau(chemin : str, filename : str, name_list : str  = None, name : str = None):
        with open(f'{chemin}/{filename}.json', 'r') as f:
                return json.load(f)[name_list][name]

class postdata:
    def simple(chemin : str, filename : str, name : str  = None, value: str  = None):
        with open(f'{chemin}/{filename}.json', 'r') as f:
                file =  json.load(f)
        file[name] = value

        with open(f'{chemin}/{filename}.json', 'w') as f:
            json.dump(file, f, indent= 2)
    def list(chemin : str, filename : str, name : str  = None, value: str  = None) :
        with open(f'{chemin}/{filename}.json', 'r') as f:
            file =  json.load(f)
        file[name].append(value)
        with open(f'{chemin}/{filename}.json', 'w') as f:
            json.dump(file, f, indent= 2)
    def tableau(chemin : str, filename : str, name_list : str  = None, name : str = None, value: str  = None):
        with open(f'{chemin}/{filename}.json', 'r') as f:
            file =  json.load(f)
        file[name_list][name] = value    
        with open(f'{chemin}/{filename}.json', 'w') as f:
                json.dump(file, f, indent= 2)