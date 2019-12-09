def open_print_txt_file(file_name):
    try:
        opened_file = open(file_name, 'r')
        lines = opened_file.readlines()
        for line in lines:
            print(line.strip())

        opened_file.close() # Closes the file, so it can be saved without conflict

    except FileNotFoundError as errmssg: # The 'as errmssg' captures the original message
        print('Check file name &/or path - File cannot be found')
        print(errmssg) # Printing original message

# Using with is better than open() and close ()
def open_print_close(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line.strip('\n'))

    except FileNotFoundError as error:
        print('Check your file')
        print(error)

    finally:
        print('Execution done!')

def open_write_txt(file,item):
    try:
        with open(file, 'a') as file_to_write:
            file_to_write.write(item + '\n')

    except FileNotFoundError as error:
        print('Check your file')
        print(error)

    finally:
        print('Execution done!')

open_write_txt('order2.txt', 'Cupcake')
open_write_txt('order2.txt', 'Benedict eggs')
open_write_txt('order2.txt', 'Beans on toast')
open_write_txt('order2.txt', 'OJ with carrots')

# open_print_txt_file('order2.txt')


# open_print_txt_file('order.txt')
# open_print_txt_file('order2.txt')
