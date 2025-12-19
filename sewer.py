import socket, time

newbies = []

main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
main_socket.bind(("localhost", 10000))
main_socket.setblocking(False)
main_socket.listen(5)

print('сокет создан')
while True:
    try:
        newbie, message = main_socket.accept()
        print(f"подключился {message}")
        main_socket.setblocking(False)
        newbies.append(newbie)
    except BlockingIOError:
        pass

    for m in newbies:
        try:
            receiver = m.recv(1024).decode()
            print(f"получено {receiver}")
        except: pass
    time.sleep(1)