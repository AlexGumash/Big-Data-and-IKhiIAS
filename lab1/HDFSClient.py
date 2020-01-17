import requests
import io
import shutil

class HDFSClient(object):
    DEFAULT_PORT = 50070
    WEBHDFS_PATH = '/webhdfs/v1'
    def __init__(self, host='localhost', user_name='Default', remote_path='/'):
        self.host = host
        self.user_name = user_name
        self.remote_path = remote_path
    def get_request(self, op, path='/', stream=None):
        return requests.get("http://{}:{}{}{}?user.name={}&op={}".format(
            self.host, self.DEFAULT_PORT, self.WEBHDFS_PATH, path, self.user_name, op), stream=stream)
    def put_request(self, op, folder='', path='/', data=None):
        return requests.put("http://{}:{}{}{}?user.name={}&op={}".format(
            self.host, self.DEFAULT_PORT, self.WEBHDFS_PATH, path + folder, self.user_name, op), data=data)
    def delete_request(self, op, folder, path='/'):
        return requests.delete("http://{}:{}{}{}?user.name={}&op={}".format(
            self.host, self.DEFAULT_PORT, self.WEBHDFS_PATH, path + folder, self.user_name, op))
    def post_request(self, op, folder='', path='/', data=None):
        return requests.post("http://{}:{}{}{}?user.name={}&op={}".format(
            self.host, self.DEFAULT_PORT, self.WEBHDFS_PATH, path + folder, self.user_name, op), data=data)
    def list_dir(self):
        dir_list = self.get_request('LISTSTATUS', self.remote_path).json()['FileStatuses']['FileStatus']
        return dir_list
    def process_cd(self, folder):
        if folder.count('..') > 0:
            if self.remote_path == '/':
                return 'It\'s root path'
            folder = self.remote_path
            folder = folder[:folder.rfind('/')]
            self.remote_path = folder[:folder.rfind('/') + 1]
            self.remote_path = self.remote_path[:folder.rfind('/')]
            folder = ''
        if folder.count('.') == 1:
            return 'This is file'
        if self.remote_path == '':
            a = self.get_request('LISTSTATUS', self.remote_path + '/').json()
        else:
            a = self.get_request('LISTSTATUS', self.remote_path + folder).json()
        if a.get('RemoteException'):
            return 'Wrong dir'
        self.remote_path = self.remote_path + folder + '/'
        return self.list_dir()
    def process_mkdir(self, folder):
        if isinstance(folder, str) and (folder != ''):
            return self.put_request('MKDIRS', folder, self.remote_path).json()['boolean']
        else:
            return 'Something went wrong'
    def process_delete(self, folder):
        if isinstance(folder, str) and (folder != ''):
            return self.delete_request('DELETE', folder, self.remote_path).json()['boolean']
        else:
            return 'Something went wrong'
    def process_put_file(self, localsrc, dest):
        try:
            with io.open(localsrc, 'rb') as f:
                self.create(self.remote_path + dest, f)
        except IOError:
            print('No such file')
    def process_open_file(self, name, path):
        r = self.get_request('OPEN', self.remote_path + name, stream=True)
        with io.open(path, 'wb') as fdst:
            shutil.copyfileobj(r.raw, fdst)
    def create(self, path, data):
        self.put_request('CREATE', '', path=path, data=data)
    def append(self, path, data):
        self.post_request('APPEND', '', path=path, data=data)
    def process_append(self, localfile, name):
        try:
            with io.open(localfile, 'rb') as f:
                self.append(self.remote_path + name, f)
        except IOError as e:
            print(e)


