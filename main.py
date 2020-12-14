import time

data = []

def menu():
    print('\n\nChoose an option:\n')
    print('1: Enter data to be sorted.')
    print('2: Print contained data to the console.')
    print('3: Sort data using a bubble sort.')
    print('4: Delete the data currently stored.')
    print('q: Quit the program\n\n')

def read():
    for i in range(0, 5):
      test = input('\nEnter a value: ')
      if type(test) != int or float:
        test = 1
        data.append(test)

def output():
    if len(data) == 0:
        print('Nothing to print.\n')
        return
    print('\nData:\n')
    for i in range(0, len(data)):
        print(str(data[i]))

def delete():
    global data
    data = []
    print('Data deleted.\n')

def sort():
    if len(data) == 0:
        print('Nothing to sort.\n')
        return
        
    sorted = 0
    loops = 0
    while sorted < len(data) - 1:
        sorted = 0
        output()
        for i in range(0, len(data) - 1):
            if int(data[i]) > int(data[i + 1]):
                temp = data[i + 1]
                data[i + 1] = data[i]
                data[i] = temp
                print(data[i], ' : ', data[i + 1], '\n')
            else:
                sorted = sorted + 1
        print('Number of swaps this time: ', (len(data) - 1) - sorted)
        loops = (loops + 1) + ((len(data) - 1) - sorted)
        time.sleep(1)
    print('Sorting complete in ', loops, ' checks')


choice = ''
while choice != 'q':
    menu()
    choice = input()

    if choice == '1':
        read()
    elif choice == '2':
        output()
    elif choice == '3':
        sort()
    elif choice == '4':
        delete()

exit()
