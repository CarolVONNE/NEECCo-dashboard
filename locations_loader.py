import os
import json

class LocationsLoader:
    """
    Helper class to read the locations of the data files to be used 
    in the dashboard.
    Expected format of the locations file is a csv file with 
    'name', 'type', 'link' as headers.
    """
    def __init__(self, file_location='locations.json'):
        self.file_location = file_location
        self.locations = self.load_locations(file_location)
    
    def load_locations(self, file_location):
        assert os.path.exists(file_location), "The locations file is not found."
        # load the file
        with open(file_location, 'r') as fIn:
            locations = json.load(fIn)
        print("Locations loaded.")
        return locations

    def get_link(self, name):
        print(f'Accessing: {name}')
        return self.locations[name]

