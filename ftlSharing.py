import ftplib

HOSTNAME = "ftp.dlptest.com"
USERNAME = "dlpuser"
PASSWORD = "rNrKYTX9g7z3RgJRmxWuGHbeu"

ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)

ftp_server.encoding = "utf-8"

filename = "text.txt"

with open(filename, "rb") as file :
    ftp_server.storbinary(f"STOR (filename)", file)

ftp_server.dir()

with open(filename, "wb") as file :
    ftp_server.retrbinary(f"STOR (filename)", file)

file = open(filename, "r")
print('File Content:', file.read())

ftp_server.quit()