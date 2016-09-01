import list_serial_ports as s
from serial import SerialException

def choose_port():
    """ Provides a simple menu for selecting a serial port

        :raises SerialException:
            If no ports are found
        :returns:
            The selected port
    """
    ports = s.list_serial_ports()
    if not ports:
        raise SerialException("No open serial ports could be found. Check the connections.")

    print("The following ports were detected:")
    for index, port in enumerate(ports, start=1):
        print('PORT', str(index) + ":", port)

    while True:
        print('Choose a port (type the number, e.g. 1)')
        try:
            selected = int(input('PORT '))
            if not (1 <= selected <= len(ports)):
                raise ValueError()
            break
        except ValueError:
            print("You must enter a valid number")
    return ports[selected - 1]

if __name__ == '__main__':
    choose_port()
