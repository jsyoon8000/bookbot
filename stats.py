def count_words(string):
    new_list = string.split()
    count = len(new_list)
    print(f'Found {count} total words')

def count_chars(string):
    dict_count = {}

    for letter in string:
        if letter.lower() in dict_count:
            dict_count[letter.lower()] += 1
        else:
            dict_count[letter.lower()] = 1
    
    sorted_dict = sorted(dict_count.items(), key=lambda x:x[1],reverse=True)

    print(f'''
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
{count_words(string)}
--------- Character Count -------
    ''')
    for char in sorted_dict:
        if char[0].isalpha() == True:
            print(f'{char[0]}: {char[1]}')
    print("============= END ===============")