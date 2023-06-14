def my_content(john):
    john = open('data.txt', 'r')
    new_john = john.read()

    print(new_john)

my_content("john")