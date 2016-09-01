import serial

def initialize_connection(port, baud):
    """ Establishes a connection via a given serial port

        :raises SerialException:
            If the requested connection could not be established
        :returns:
            A handle for the requested port
    """
    connection = serial.Serial(port, baud)
    if connection.isOpen():
         print('SUCCESS - connection with', connection.name, 'established.')
    else:
        raise SerialException('ERROR - connection with', connection.name, 'could not be established.')
    return connection

if __name__ == '__main__':
    initialize_connection()
