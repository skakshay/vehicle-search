A Django app for searching car models where the user is presented the suggestions based what she types. 

#### Requirements : 
Django==2.0.6

jQueryUI==1.12

#### Logic : 
An ajax get call is made when user types at least 2 characters. The server returns list of car models matching the search string in decreasing order of 'select_count'(refer model.py) which are then displayed using Autocomplete widget of jQueryUI. If a user selects a particular model another ajax post call is made on which the server increments the 'select_count' in database. 

Also first run the `populate_db.py`, so that it populates the db with the `query_result.csv` . 

### APIs : 
`'/'` : 			renders the html where the user can search for the car. 

`'/search_model/'` : 	returns the list of models matching the search string. 

`'/ajax/select_model/'` :  update the select_count field in the database of the selected car. 
