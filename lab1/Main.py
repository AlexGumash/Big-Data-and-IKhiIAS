import sys

from Client import Client
if __name__ == "__main__":
    if len(sys.argv) == 4:
        client = Client(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3])
    else:
        client = Client(
            'localhost',
            '50070',
            'default')
    while True:
        command = client.get_command()


