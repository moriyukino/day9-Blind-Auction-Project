programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}
#print(programming_dictionary["Function"])

programming_dictionary["Loop"] = "The action of doing something over and over again."

enpty_dictionary = {}

# Wipe an existing dictionary

#作成した辞書を丸ごと削除する
# programing_dictionary = {}
#print(# programing_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
#print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])