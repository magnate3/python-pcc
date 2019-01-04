import socket, pickle

HOST = '172.16.1.254'
PORT = 50005
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
arr = ('192.168.0.1', '192.168.0.4')
s.send(pickle.dumps(arr))

data = s.recv(4096)
data_arr = pickle.loads(data)
s.close()
print 'Received', repr(data_arr)
