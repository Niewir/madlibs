# need to take user inputs for the strings that will fill in each blank space
# need to have a text for the inputs to be embedded within
# need to know how to put strings together with concatenation

name = input("Enter a name: ")
adjective = input("Enter an adjective: ")
verb1 = input("Enter a verb ending in -er: ")
verb2 = input("Enter a verb: ")
animal = input("Enter an animal: ")
verb3 = input("Enter a verb ending in -ing: ")

def story():
    print(f"\nHello {name}, I heard you're a really {adjective} {verb1}. ",
          f"\nYou don't even know how to {verb2} without asking someone for help... ",
          f"\nEven your pet {animal} knows you suck at {verb3}. Crazy...\n")

    return 'Thanks for trying my program!'

print(story())