import requests, hashlib, re, os

class acgnZone:
    def __init__(self):
        self.session = requests.Session()
        self.isLogin = False
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0) Gecko/20190101 Firefox/77.0'
            }

    def login(self, usr, pw):
        if self.isLogin:
            print('Already login')
            return

        m = hashlib.md5()
        m.update(pw.encode("utf-8"))
        pw = m.hexdigest()

        headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
        headers.update(self.headers)
        data = {
            'email': usr,
            'password': pw
            }

        r = self.session.post('https://acgn.zone/user-login.htm', data=data, headers=headers)
        if re.search('用户名不存在', r.text):
            print('Not Loggin')
            return False
        elif re.search('登录成功', r.text):
            self.isLogin = True
            print('Loggin successful')
            return True
        return False

    def sign(self):
        if not self.isLogin:
            print('Not Loggin')
            return False

        r = self.session.post('https://acgn.zone/sg_sign.htm', headers=self.headers)
        if re.search('签过啦', r.text):
            print('Sign succeed')
            return True
        return False

if __name__ == '__main__':
    az = acgnZone()
    az.login(os.environ['USR'], os.environ['PASS'])
    az.sign()
