from urllib.parse import urlparse
import socket


def check(inpVar, column_list):
    name = column_list[0]
    list = column_list[1]
    boolvar = False
    for i in list:
        for j in i:
            if j == inpVar:
                print("It ", name, " was blocked ")
                boolvar = True
                break
        if boolvar:
            break
    if not boolvar:
        print("It ", name, " not found")
    return boolvar


urls = []
domain = []
IPs = []
ip = ""
bvar = True
site_info = [['URL', urls], ['domain', domain], ['IP', IPs]]

buf = open("D:/register.txt", "r", encoding='utf-8').readlines()
for i in buf:
    line = i[0:len(i) - 2].split(";")  # избавляемся от /n
    urls.append(line[1].split(','))
    domain.append(line[2].split(','))
    IPs.append(line[3].split(','))


input_URL = input("input your ULR with with a space at the end: ")[0:-1]
if check(input_URL, site_info[0]):
    domain = urlparse(input_URL).netloc
    if domain[0:3] == "www":
        domain = domain[4:]
    if check(domain, site_info[1]):
        try:
            ip = socket.gethostbyname(domain)
        except socket.error:
            print("this IP not exist")
            bvar = False
        if bvar:
            check(ip, site_info[2])









