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
  { "Title":"Sholay",
    "Director":"Ramesh Sippy",
    "Release year": 1975
}]

for film in films:
    print("Title:", film["Title"])
    print("Director:",film["Director"])
    print("Release year:",film["Release year"])

