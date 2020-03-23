from handler import Handle
import json
import logging

p = Handle()

class Machine:
    def proses(self,string_to_process):
        s = string_to_process
        cstring = s.split(" ")
        try:
            command = cstring[0].strip()
            if (command=='add'):
                filename = cstring[1].strip()
                file = cstring[2].strip()
                print("Adding",filename)
                p.add_file(filename,file.encode())
                return "File Added"

            elif (command=='get'):
                filename = cstring[1].strip()
                print("Retrieving", filename)
                hasil = p.get_file(filename)
                return hasil

            elif (command=='list'):
                logging.info("list")
                data = {}
                data['files'] = []
                hasil = p.list_file()
                for filename in hasil:
                    data['files'].append({"filename":filename})
                return json.dumps(data, indent=4)
            else:
                return "ERRCMD"
        except:
            return "ERROR"


if __name__=='__main__':
    machine = Machine()