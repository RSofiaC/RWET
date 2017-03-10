#
# Worksheet #4
#
# This worksheet is also a Python program. Your task is to read the 
# task descriptions below and then write one or more Python statements to
# carry out the tasks. There's a Python "print" statement before each
# task that will display the expected output for that task; you can use
# this to ensure that your statements are correct.
#
# In this worksheet, some of the tasks will throw an error that causes
# the program to stop running, and skip the remaining tasks. Because of
# this, you'll have to complete the tasks in the given order!

print "\n------"
print "Task 1: Making a web request"
print 'Expected output: {"ping": "ok"}'

# Task 1: There is a web API (which I made specifically for this worksheet!)
# available at the following URL:
#   http://blooming-shelf-7827.herokuapp.com
# Modify the value of the variable "url" below so that it makes a request to
# the "/ping" path of this web API.

import urllib
url = "http://blooming-shelf-7827.herokuapp.com/ping" # <-- modify this
response = urllib.urlopen(url).read()
print response

#------------------------------------------------------------------------

print "\n------"
print "Task 2: Parsing JSON"
print "Expected output: <type 'dict'>"

# Task 2: The web API also supports a path called "/kittens", which returns
# a list of kittens in JSON format. Add a function call to the line below
# so that the variable "data" is a Python dictionary containing the data from
# the response. (I've taken the liberty of importing the Python library that
# contains the function you'll want to use.)

import json
url = "http://blooming-shelf-7827.herokuapp.com/kittens"
response = urllib.urlopen(url).read()
data = response.read() # <-- add a function call here!
print type(data)

#------------------------------------------------------------------------

print "\n------"
print "Task 3: Manipulating URLs, part one"
print 'Expected output: ["results"]'

# Task 3: You may have noticed that the previous response actually returned
# an error! That's because this particular API requires that you supply an
# API key. The API key must be supplied as a parameter on the query string.
# Modify the variable "url" below so that it has a query string with one
# parameter, "api_key", whose value is "abc123".

url = "http://blooming-shelf-7827.herokuapp.com/kittens" # <-- modify this
response = urllib.urlopen(url).read()
# uncomment the following line if you want to see what the response looks like
#print response
data = json.loads(response)
print data.keys()

#------------------------------------------------------------------------

print "\n------"
print "Task 4: Working with web API data"
print "Expected output: 3"

# Task 4: A request to "/kittens" (with the appropriate API key) returns a
# list of kittens. Modify the expression following "print" below so that the
# number of kittens in the response is displayed. (Use the value of "url"
# from the previous task.)

response = urllib.urlopen(url).read()
# uncomment the following line if you want to see what the response looks like
#print response
data = json.loads(response)
print data # <-- modify this!

#------------------------------------------------------------------------

print "\n------"
print "Task 5: Working with embedded data structures"
print "Expected output:"
print "  McFluff the Crime Kitten"
print "  Scratch"
print "  Her Majesty Queen Esmerelda Poopbutt"

# Task 5: Use the variable "data" from the previous task. Modify the two
# expressions indicated below so that the names of each of the kittens are
# displayed. (Take a good look at the data structure returned from the 
# response. What kind of data structure is it? What other kinds of data
# structures does it contain?)

kitten_list = [] # <-- modify this! Hint: the value for a key in "data"
for kitten in kitten_list:
	print "" # <-- modify this too! Hint: "kitten" is a dictionary

#------------------------------------------------------------------------

print "\n------"
print "Task 6: Manipulating URLs, part two"
print "Expected output:"
print "  McFluff the Crime Kitten"
print "  Her Majesty Queen Esmerelda Poopbutt"
print "  Scratch"

# Task 6: This API also allows you to specify a sort order for the kittens
# returned in the data. To take advantage of this functionality, include a key
# in the query string, "sort", whose value is the data field that you want to
# sort by (e.g., "name", "weeks_old", "weight_kg", etc.). Modify the dictionary
# inside the call to urllib.urlencode below so that the for loop prints the
# names of the kittens in (ascending) order by weight. (Hint: don't forget
# to include your API key!)

base_url = "http://blooming-shelf-7827.herokuapp.com/kittens?"
params = urllib.urlencode({}) # <-- modify this dictionary
url = base_url + params
response = urllib.urlopen(url).read()
data = json.loads(response)
for kitten in data['results']:
	print kitten['name']

#------------------------------------------------------------------------

print "\n------"
print "Task 7: Working with embedded data structures, part two"
print "Expected output:"
print "  salmon"
print "  duck"
print "  chicken"

# Task 7: Use the variable "url" from the previous task. The value for each
# kitten's "favorite_foods" key is a list of strings. Change the indicated
# expression below so that the code prints out the first favorite food for
# each kitten.

response = urllib.urlopen(url).read()
data = json.loads(response)
for kitten in data['results']:
	print "" # <-- modify this expression!

#------------------------------------------------------------------------

print "\n------"
print "Task 8: Working with embedded data structures, part three (advanced!)"
print "Expected output: 7.3"

# Task 8: Write a list comprehension in the indicated space that returns a
# list of the values for the "weight_kg" field in each kitten record.
# The resulting expression will pring out the sum of their weights. (Use the
# value of "url" from the previous task.)

response = urllib.urlopen(url).read()
data = json.loads(response)
print sum([]) # <-- change [] to a list comprehension
