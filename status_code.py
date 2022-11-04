import csv
import sys
import os
import requests


def main():
    args = sys.argv[1:]
    if len(args) > 0:
        filename = args[0]
        delimiter = args[1]
        odomain = args[2]
        ndomain = args[3]
        user = args[4]
        password = args[5]
        openFile(filename, delimiter, odomain, ndomain, user, password)


def openFile(filename, delimiter, odomain, ndomain, user, password):
    fs = open("output.csv", "w+", encoding="utf-8", newline='')
    output = csv.writer(fs)

    pathname = os.path.abspath(filename)
    print(pathname)

    with open(pathname, 'r', encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=delimiter)
        header = next(reader)
        header.append("RM status code")
        header.append("RM URL")
        output.writerow(header)
        content = header.index("Content Type")
        suffixes = (".pdf", ".jpg", ".png", ".bmp") 
        for row in reader:
            if "text/html" in row[content] and not row[0].endswith(suffixes):
                newURL = row[0].replace(odomain, ndomain)
                response = getStatus(newURL, user, password)
                row.append(response[0])
                row.append(response[1])
                output.writerow(row)

    fs.close()


def getStatus(newURL, user, password):
    session = requests.Session()
    if user != "" and password != "":
        session.auth = (user, password)

    try:
        headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'Accept':
            'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-US,en;q=0.9,pt;q=0.8,pt-PT;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br'
        }
        r = session.get(newURL.strip(), headers=headers, allow_redirects=False)
        return ([r.status_code, newURL.strip()])

    except:
        return (["Error", newURL])

if __name__ == "__main__":
    main()