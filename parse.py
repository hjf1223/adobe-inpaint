from requests_toolbelt.multipart import decoder
import requests
from requests.structures import CaseInsensitiveDict as CaseInsensitiveDict
import cgi  

def getFileName(headers):
    value, params = cgi.parse_header(headers["Content-Disposition"])
    fileName =params.get("name")
        
    if headers["Content-Type"] == 'image/jpeg':
        fileName = fileName+".jpg"
    
    if headers["Content-Type"] == 'image/png':
        fileName = fileName+".png"
        
    if headers["Content-Type"] == 'application/json':
        fileName = fileName+".json"

    return fileName

def parseMultipart(bodyFile,boundary):
    f = open(bodyFile, "r")
    data = f.read()
    f.close()

    r = requests.models.Response()
    r._content = data
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "multipart/form-data; boundary=" + boundary
    r.headers = headers
    r.encoding = "utf-8"

    multipart_data = decoder.MultipartDecoder.from_response(r)

    for part in multipart_data.parts:
        fileName = bodyFile + '-' + getFileName(part.headers)
        file = open(fileName, 'w')
        file.write(part.content)
        file.close()

        #print(part.content)  # Alternatively, part.text if you want unicode
        #print(part.headers)

parseMultipart("fish/spl-request-fish","----WebKitFormBoundary0G3RxyYNw6RvAqWk")
parseMultipart("fish/spl-response-fish","R8K6Z1DwjOWSmd3o3Ryxbxga")
print("parse fish done.")

parseMultipart("stone/spl-request-stone","----WebKitFormBoundary8u1CUPnRUreHEQeQ")
parseMultipart("stone/spl-response-stone","uB5VkwqxZcrlXg4jxMOBLIOc")
print("parse stone done.")