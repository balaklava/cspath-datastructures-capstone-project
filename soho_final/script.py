from trie import Trie
from data import *
from welcome import *
from hashmap import HashMap
from linkedlist import LinkedList

######################################
# helper functions

def linked_list_len(ll):
    counter = 0
    item = ll.get_head_node()
    while item is not None:
        counter = counter + 1
        item = item.get_next_node()
    return counter


def print_restaurants_ll(restaurants):
    item = restaurants.get_head_node()
    while item is not None:
        d = item.get_value()
        print("\n------------------")
        for key in d:
            if key == "price" or key == "rating":
                 value = d[key] + "/5"
                 print("%s: %s" % (key, value))
            else:
                 print("%s: %s" % (key, d[key]))
        item = item.get_next_node()


def print_user_choice(choice):
    print("The only option with those beginning letters is %s. "
          "Do you want to look at %s restaurants?" % (choice.title(), choice.title()))
    user_respond = str(input("Enter 'y' for yes and 'n' for no. ")).lower()
    return user_respond

#####################################
# main script


# Printing the Welcome Message
print_welcome()


# Creating a hashmap object with linked list using restaurant type data
hash_map_types = HashMap(20)
for t in types:
    # if the key is the first time
    if hash_map_types.retrieve(t[0]) == None:
        ll = LinkedList(t)
        hash_map_types.assign(t[0], ll)
    # if the key was seen already
    else:
        ll_tmp = hash_map_types.retrieve(t[0])
        ll_tmp.insert_beginning(t)


# Creating a hashmap object with linked list using restaurant data
hash_map_rest = HashMap(20)
for r in restaurant_data:
    key = r[0]
    d = {"name": r[1], "price": r[2], "rating": r[3], "address": r[4]}
    # the key is seen the first time
    if hash_map_rest.retrieve(key) == None:
        ll = LinkedList(d)
        hash_map_rest.assign(key, ll)
    # the key is seen not the first time
    else:
        ll_tmp = hash_map_rest.retrieve(key)
        ll_tmp.insert_beginning(d)


# User interaction code
while True:

    options_len = None
    while options_len is None:
        user_input = str(input("\nWhat type of food would you like to eat?\nType "
                               "the beginning of that food type and press enter to see if it's here.\n")).lower()
        options = hash_map_types.retrieve(user_input[0])
        try:
            options_len = linked_list_len(options)
        except:
            print("The is not restaurant type starting with '%s'. Try again." % user_input)

    options_len = linked_list_len(options)
    len_user_input = len(user_input)

    if options.get_head_node().get_value() != None:
        # if there are several options of the restaurant types given user input
        if options_len > 1:
            if len_user_input == 1:
                print("With those beginning letters, your choices are ", options.stringify_list())
            else:
                opt = options.get_head_node()
                while opt is not None:
                    opt_value = opt.get_value()
                    if opt_value[0:len_user_input] == user_input:
                        choice = opt_value
                        user_respond = print_user_choice(choice)
                        if user_respond == "y":
                            restaurants = hash_map_rest.retrieve(choice)
                            print_restaurants_ll(restaurants)
                            continue_input = str(input("Do you want to find other restaurants? "
                                                        "Enter 'y' for yes and enter 'n' for no. \n"))
                            if continue_input == "n":
                                exit()
                    opt = opt.get_next_node()
        # if there is one option of the restaurant types given user input
        elif options_len == 1:
            choice = options.get_head_node().get_value()
            user_respond = print_user_choice(choice)
            if user_respond == "y":
                restaurants = hash_map_rest.retrieve(choice)
                print_restaurants_ll(restaurants)
                continue_input = str(input("Do you want to find other restaurants? "
                                            "Enter 'y' for yes and enter 'n' for no. \n"))
                if continue_input == "n":
                    exit()








