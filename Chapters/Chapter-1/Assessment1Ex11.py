# Creating tuple with values
Year= (2017,2003,2011,2005,1987,2009,2020,2018,2009)

# Access value at index-3
value_index= Year[-3]
print("Value at index-3:",value_index)

# Reversing the tuple
reversed_year = tuple(reversed(Year))
print("Original tuple:", Year)
print("Reversed tuple:", reversed_year)

# counting number of times 2009 in the tuple
count= Year.count(2009)
print("Number of times 2009 is in the tuple:", count)

# Getting the index value
index= Year.index(2018)
print("Index of 2018:", index)

# length of tuple
length= len(Year)
print("Length of the tuple:", length)