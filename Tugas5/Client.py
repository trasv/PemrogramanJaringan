import socket
import json

TARGET_IP = "127.0.0.1"
TARGET_PORT = 8889


class ChatClient:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (TARGET_IP, TARGET_PORT)
        self.sock.connect(self.server_address)
        self.tokenid = ""

    def proses(self, data):
        j = data.split(" ")
        try:
            command = j[0].strip()
            if (command == 'login'):
                username = j[1].strip()
                password = j[2].strip()
                return self.login(username, password)
            elif (command == 'send'):
                usernameto = j[1].strip()
                message = ""
                for i in range(2, len(j)):
                    message = message + ' ' + j[i].strip()
                return self.sendmessage(usernameto, message)
            elif (command == 'inbox'):
                return self.inbox()
            elif (command == 'show'):
                return self.showUser()
            elif (command == 'logout'):
                return self.logout()
            else:
                return "*Maaf, command tidak benar"
        except IndexError:
            return "-Maaf, command tidak benar"

    def sendstring(self, string):
        try:
            self.sock.sendall(string.encode())
            receivemsg = ""
            while True:
                data = self.sock.recv(64)
                # print("diterima dari server",data)
                if (data):
                    receivemsg = "{}{}".format(receivemsg,
                                               data.decode())  # data harus didecode agar dapat di operasikan dalam bentuk string
                    if receivemsg[-4:] == '\r\n\r\n':
                        # print("end of string")
                        return json.loads(receivemsg)
        except:
            self.sock.close()
            return {'status': 'ERROR', 'message': 'Gagal'}

    def login(self, username, password):
        string = "auth {} {}".format(username, password)
        result = self.sendstring(string)
        if result['status'] == 'OK':
            self.tokenid = result['tokenid']
            # print(self.tokenid)
            return "Welcome {}, Token: {}".format(username, self.tokenid)
        else:
            return "Error, {}".format(result['message'])

    def logout(self):
        if (self.tokenid == ""):
            return "User not Logged In"
        string = "logout {}".format(self.tokenid)
        result = self.sendstring(string)
        if result['status'] == 'OK':
            self.tokenid = ""
            return "{}".format(result['message'])
        else:
            return "Error, {}".format(result['message'])

    def sendmessage(self, usernameto, message):
        if (self.tokenid == ""):
            return "Error, not authorized"
        string = "send {} {} {}".format(self.tokenid, usernameto, message)
        # print("Sending Message to", usernameto)
        result = self.sendstring(string)
        if result['status'] == 'OK':
            return "Message sent to {}".format(usernameto)
        else:
            return "Error, {}".format(result['message'])

    def inbox(self):
        if (self.tokenid == ""):
            return "Error, not authorized"
        string = "inbox {}".format(self.tokenid)
        result = self.sendstring(string)
        if result['status'] == 'OK':
            return "{}".format(json.dumps(result['messages'], indent=4))
        else:
            return "Error, {}".format(result['message'])

    def showUser(self):
        if (self.tokenid == ""):
            return "Error, not authorized"
        string = "showUser {}".format(self.tokenid)
        result = self.sendstring(string)
        if result['status'] == 'OK':
            return "{}".format(json.dumps(result['messages'], indent=4))
        else:
            return "Error, {}".format(result['message'])


if __name__ == "__main__":
    cc = ChatClient()
    while True:
        cmdline = input("Enter Command: ")
        print(cc.proses(cmdline))
