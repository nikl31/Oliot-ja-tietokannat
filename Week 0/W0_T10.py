word = input("Insert word: ")
search = input("Insert search term: ")

if search in word:
    print(f"Search term '{search}' do appear in word '{word}'")
else:
    print(f"Search term '{search}' doesn't appears in word '{word}'")