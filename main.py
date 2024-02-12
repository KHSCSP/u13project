import setup

# note:
# the activities are random
# you will get different results each time you run

# ----------- activities -----------
print("\n--- part 1, (random) activities ---")
activities = setup.get_activities(10)
print("all activities\n", activities)
# ^^^ you may want to comment that line out, too much info
# notice the keys for each item


# display the type of data of 'activities'
# display the first item in 'activities'
# display type of data of the first item in 'activities'



print("\none participant...")
# write a function that receives the list of activities and returns a list of activities with one participant
# this will require you to iterate through the list (use a loop)
# and look at the value (use a conditional and [] or .get())
# display your list




print("\nmusic...")
# write a function that receives the list of activities and returns a list of activities that have 'music' in the description
# this is similar to the above, but may require 'in'
# display your list




print("\naccessible...")
# write a function that receives the list of activities and returns a list of the most accessible
# accessibility < 0.1
# this time each item in the list should be a tuple
# (activity, accessiblility)
# display your list
  



print("\nwith link")
# write a function that receives the list of activities and returns a list of activities that have a link
# this time the list should be a tuple (activity, link)
# display your list




# ----------- memes -----------
print("\n--- part 2, memes ---")
# memes = setup.get_memes()
# print("all memes\n", memes)
# ^^^ when ready, uncomment those two lines ^^^

# explore the type of data, how many items in your data, the first item in the data, and the type of data for the first item



print("\nlarge memes...")
# write a function that receives the list of memes and returns a list of memes which are >= 1000 pixels wide
# the list should be a tuple with 4 items
# (name, url, width, height)
# or a dictionary with 4 key-value pairs
# {'name'='', 'url'='', 'width'='', height=''}
# display your new data



print("\nspecific memes...")
# write a function that receives the list of memes, a string (such as 'cat') and returns a list with that string in the name
# the list should be a tuple
# (name, link)
# or a dictionary
# {'name'='', 'link'=''}
# display your new data





# ---- optional challenge ----
# display the image for one of your memes 
# from PIL import Image

# addr = "TODO use one of your urls"

# img = Image.open(requests.get(addr, stream = True).raw)
# img.show()

