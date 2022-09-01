import socket;

def escanear(ip, puerto):
    """
    Crea un socket, intenta conectarse a la IP y al puerto dados, y si
    tiene éxito, imprime un mensaje, de lo contrario, imprime un mensaje de error.
    
    :param ip: La dirección IP del host que desea escanear
    :param puerto: The port to scan
    """
    Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

    try:
        Socket.settimeout(1);
        Socket.connect((ip, puerto));
        Socket.send(b'hola mundo');      
        print("El puerto {} está abierto".format(puerto));

    except Exception as e:
        print(f"E: {e}");
    finally:
        Socket.close();


'''
def escanearHost(ip):
    """
    Crea un socket, establece un tiempo de espera y luego intenta conectarse al socket. Si
    se puede conectar, imprime que el puerto esta abierto
    
    :param ip: La dirección IP del host que desea escanear
    """
    for puerto in range(135,140):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        
        try:
            socket.setdefaulttimeout(2);
            resultado = s.connect_ex((ip, puerto));
            if (resultado == 0):
                print(f"El puerto {puerto} está abierto");
            s.close();

        except Exception as e:
            print(f"E: {e}");
'''



if __name__ == '__main__':

    addressIP = socket.gethostbyname(input("Ingrese su dirección IP: "));
    print(f"\nEscaneando objetivo {addressIP}\n");

    puertos = [80, 8080, 21, 3306, 443, 135];
    for puerto in puertos:
        escanear(addressIP, puerto);

    #escanearHost(addressIP);