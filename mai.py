clientes = 'miguel, leronado,'

def create_client(client_name):
    global clientes
    if client_name not in clientes:
        clientes += client_name
        _add_comma()
    else:
        print('Client already in the clients\' list')


def list_clients():
    global clientes
    print(clientes)


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you to like to do today ?')
    print('[C]reate client')
    print('[D]elete client')


def _add_comma():
    global clientes
    clientes += ',' 


if __name__ == '__main__':
    _print_welcome()
    command = input()
    if command == 'C':
        client_name = input('What is the client name? ')
        create_client(client_name)
        list_clients()
    elif command == 'D':
        pass
    else:
        print('Invalid command')
