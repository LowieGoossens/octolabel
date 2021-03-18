import requests




if __name__ == '__main__':
    url = 'http://192.168.133.210:8765/api/print/namebadge'
    myobj = {'first': 'Printername', 'last': 'Filename', 'company': ' '}

    x = requests.get(url, data=myobj)

    print(x.text)
