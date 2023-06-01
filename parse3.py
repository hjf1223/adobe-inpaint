from requests_toolbelt.multipart import decoder
import requests
from requests.structures import CaseInsensitiveDict as CaseInsensitiveDict
import cgi  

def getFileName(headers):

    value, params = cgi.parse_header(headers[b"Content-Disposition"].decode("utf-8"))
    fileName =params.get("name")
    
    
    match headers[b"Content-Type"]:
        case b"image/jpeg":
            fileName = fileName+".jpg"
        case b"image/png":
            fileName = fileName+".png"
        case b"application/json":
            fileName = fileName+".json"
    
    # if headers["Content-Type"] == 'image/jpeg':
    #     fileName = fileName+".jpg"
    
    # if headers["Content-Type"] == 'image/png':
    #     fileName = fileName+".png"
        
    # if headers["Content-Type"] == 'application/json':
    #     fileName = fileName+".json"
        
    return fileName

def parseMultipart(bodyFile,boundary):
    f = open(bodyFile,mode="rb")
    data = f.read()
    f.close()

    # print(b'\r\n\r\n' in data)
    r = requests.models.Response()
    r._content = data
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "multipart/form-data; boundary=" + boundary
    r.headers = headers
    # r.encoding = "ISO-8859-1"

    multipart_data = decoder.MultipartDecoder.from_response(r, encoding='utf-8')

    for part in multipart_data.parts:
        fileName = bodyFile + '-' + getFileName(part.headers)
        file = open(fileName, 'wb')
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