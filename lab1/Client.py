import os
import sys
from HDFSClient import HDFSClient

class Client:
    remote_path = ''
    list_command = ['ls', 'lls', 'cd', 'lcd', 'put', 'get', 'mkdir', 'delete', 'append']
    def __init__(self, url='localhost', port='50070', username='default'):
        self.url = url
        self.port = port
        self.username = username
        self.local_path = os.getcwd()
        self.remote_path = '/'
        self.hdfs = HDFSClient(self.url, self.username, self.remote_path)
    def input_command(self, text):
        return input(text + '>')
    def verification(self, path, dir):
        if os.path.exists(path):
            if os.path.isfile(path) and dir == 1:
                return "You are trying to get a file instead of directory." \
                       " Maybe you want to load file to server? (put <path to file>)"
            elif os.path.isfile(path) and dir == 0:
                return True
            elif not os.path.isfile(path) and dir == 0:
                return "You are trying to get directory instead of a file." \
                       " Maybe you want to change your directory? (cd <path to directory>)"
            else:
                return True
        else:
            return "Given path does not exist. Please, check the path."
    def process_ls(self):
        for i in self.hdfs.list_dir():
            print(i['pathSuffix'])
    def process_lls(self):
        for i in os.listdir(self.local_path):
            print(i)
    def process_cd(self, path=''):
        list_dir = self.hdfs.process_cd(path)
        if isinstance(list_dir, str):
            print(list_dir)
            return
        for i in list_dir:
            print(i['pathSuffix'])
    def process_lcd(self, path=''):
        if path.count("..") > 0:
            path = os.getcwd()
            self.process_lcd(path[:path.rfind("\\") + 1])
        else:
            if path.count("\\") > 0:
                res_path = path
                revision = self.verification(res_path, 1)
                if revision:
                    os.chdir(res_path)
                    self.local_path = res_path
            elif path.count("\\") == 0:
                res_path = self.local_path + '/' + path
                revision = self.verification(res_path, 1)
                if revision:
                    os.chdir(res_path)
                    self.local_path = res_path
    def process_put(self, name):
        self.hdfs.process_put_file(self.local_path + os.sep + name, name)
    def process_get(self, name):
        self.hdfs.process_open_file(name, self.local_path + os.sep + name)
    def process_mkdir(self, folder):
        print(self.hdfs.process_mkdir(folder))
    def process_delete(self, folder):
        print(self.hdfs.process_delete(folder))
    def process_append(self, localfile, name):
        self.hdfs.process_append(localfile, name)
    def get_command(self):
        command = self.input_command('')
        if command != 'exit':
            input_list = command.split(' ')
            temp = input_list[0].lower()
            self.dispatch(temp, input_list)
        else:
            sys.exit()
    def dispatch(self, value, input_list):
        if value in self.list_command:
            method_name = 'process_' + str(value)
            method = getattr(self, method_name)
            if (value == 'ls') or (value == 'lls'):
                return method()
            elif value != 'append':
                if len(input_list) == 2:
                    return method(input_list[1])
            else:
                if len(input_list) == 3:
                    return method(input_list[1], input_list[2])
            return method()


