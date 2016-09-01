import serial
import sys
import os
import json
import argparse
from time import sleep
from initialize_connection import initialize_connection
from choose_port import choose_port

home = os.path.dirname(os.path.abspath(__file__))
settings_path = os.path.join(home, 'settings.json')
settings = dict()

def sendLine(line):
    connection.write(line.encode('ascii') + '\r\n'.encode('ascii'))

def sendFile(file):
    print('NOTICE - transmission has begun')
    script = open(file)
    for line in script:
        line = line.rstrip('\n') # remove line ending
        sleep(0.03) # NXT needs to keep up
        sendLine(line)
    script.close()
    print('SUCCESS - script transmitted')

def readOutput():
    while True:
        output = connection.readline()
        output = output.decode('ascii')
        if output == '':
            break
        print(output, end="")
        connection.flush()

def configure():
    init_dict = dict()
    init_dict['port'] = choose_port()
    with open(settings_path, 'w') as dump_file:
        json.dump(init_dict, dump_file, indent=4)

def main():
    global settings
    if not os.path.exists(settings_path):
        configure()
    with open(settings_path) as file:
        settings = json.load(file)

    global connection
    connection = initialize_connection(settings['port'], 38400) # do not change baud rate
    sendFile(args.file)
    print('NOTICE - the following output was generated during execution')
    print()
    readOutput()
    connection.close() # cleaning up

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', nargs='?', help='shorthand property to simply transmit and execute a file')
    parser.add_argument('-r','--reset', help='reset the configuration', action='store_true')
    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.print_help()
    if args.reset:
        print('create new configuration')
        configure()
        main()
    if args.file:
        main()
    else:
        print("?")
