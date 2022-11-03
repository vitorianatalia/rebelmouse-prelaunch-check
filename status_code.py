import csv
import sys
import os
import requests

def main():
    args = sys.argv[1:]
    if len(args)>0:
        filename = args[0]
        delimiter = args[1]
        odomain = args[2]
        ndomain = args[3]
        user = args[4]
        password = args[5]
        openFile(filename, delimiter, odomain, ndomain, user, password)


def openFile(filename, delimiter, odomain, ndomain, user, password):    
    file = open("addressList.txt", "w+", encoding="utf-8")

    pathname = os.path.abspath(filename)
    print(pathname)

    with open(pathname, 'r', encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=delimiter)
        header = next(reader)
        content= header.index("Content Type")
        for row in reader:
            if "text/html" in row[content]:
                file.write(row[0].replace(odomain, ndomain))
                file.write("\n")
    file.close()
    getStatusCode(user, password)


def getStatusCode(user, password):
    sf = open("success.txt", "w+", encoding="utf-8")
    ff = open("otherstatus.txt", "w+", encoding="utf-8")

    file = open("addressList.txt", "r+", encoding="utf-8")
    session = requests.Session()
    if user != "" and password != "":
        session.auth = (user, password)

    for line in file:
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36', 
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-US,en;q=0.9,pt;q=0.8,pt-PT;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br'}
            r = session.get(line.strip(), headers=headers, allow_redirects=False)    
            if r.status_code == 200:
                sf.write(str(r.status_code) + " | " + line.strip() + "\n")
            else:
                ff.write(str(r.status_code) + " | " + line.strip() + "\n")
            
        except:
            ff.write(line + " | " + "Error - not able to process" + "\n")

    sf.close()
    ff.close()
    file.close()
    os.remove("addressList.txt")


if __name__ == "__main__":
    main()