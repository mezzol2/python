#Did the cat throw up on the floor and you stepped in it?
def gibberish():
    exit("You entered some gibberish.  Please try again.")

def puke_test():
    puke = input("Is there cat throw up on the floor? (y/n)\n").lower()
    if puke == 'n':
        print("Of course not. The cat is a perfect baby angel.")
    elif puke == 'y':
        step = input("Did you step in it? (y/n)\n").lower()
        if step == 'y':
            print('Seems like you were asking for it. Sounds like a personal problem.')
        elif step == 'n':
            print('Very good.  Time to clean up after the perfect babes. <3')
        else:
            gibberish()
    else:
        gibberish()


cat = input('Do you have a cat? (y/n)\n').lower()

if cat == 'n':
    exit("The fuck are you doing with your life?  Go get a little baby!")
elif cat == 'y':
    puke_test()
else:
    gibberish()