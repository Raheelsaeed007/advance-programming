# Creating a dictionary of film details
films=[{
    "Title":"Inception",
    "Director":"Christopher Nolan",
    "Release year": 2010
},
 {  "Title":"The Dark Knight",
    "Director":"Christopher Nolan",
    "Release year": 2008
},
 ]
# using for loop as required
for film in films:
    print("Title:", film["Title"])
    print("Director:",film["Director"])
    print("Release year:",film["Release year"])

