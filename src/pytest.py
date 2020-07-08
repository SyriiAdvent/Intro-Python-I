 # create a Statement that will print out words that start with 's'
my_str = 'Print only the words that start with s in this sentence'

for word in my_str.split(" "):
    if word[0] == 's' and len(word) > 1:
        print(word)

print('\n ***** \n')

# Print every word that has even letters
my_even_string = 'Print every word in this sentence that has an even number of letters'

for word in my_even_string.split(" "):
    if len(word) % 2 == 0:
        print(f"{word}: Even!")