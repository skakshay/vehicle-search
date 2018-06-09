A Django app for searching car models where the user is presented the suggestions based what she types. 

#### Requirements : 
Django==2.0.6

jQueryUI==1.12

#### Logic : 
An ajax get call is made when user types at least 2 characters. The server returns list of car models matching the search string in decreasing order of 'select_count'(refer model.py) which are then displayed using Autocomplete widget of jQueryUI. If a user selects a particular model another ajax post call is made on which the server increments the 'select_count' in database. 

### APIs : 
__'/'__ : 			renders the html where the user can search for the car. 

__'/search_model/'__ : 	returns the list of models matching the search string. 

__'/ajax/select_model/'__ :  update the select_count field in the database of the selected car. 
