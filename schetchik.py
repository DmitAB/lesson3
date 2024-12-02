calls = 0

def count_calls():
    global calls
    calls = calls +1
    return calls

def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()

def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()


    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()
        continue
    if string in list_to_search:
        string = True
    else:
        string = False

    return string

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(string_info('BoBiK'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))
print(is_contains('BobiK', ['recycling', 'cyclic', 'bobik']))# No matches
print(calls)




