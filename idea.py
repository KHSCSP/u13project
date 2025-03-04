# this is NOT the assignment
# this is an idea of a 'challenge' *after* you complete the assignment


options = '''
\nHere are your options:
(act) to show all activities
(solo) to show all solo activities
(acc) to show all accessible activities
(cat) to get a category of activities
-----
(meme) to show all memes
(link) to show all memes with a url
(large) to show all large memes
(favs) to get all memes of your favorite category
(q) or (quit) to quit
'''

choice = 'jjj'
while choice[0].lower() != 'q':
    print(options)
    choice = input()
