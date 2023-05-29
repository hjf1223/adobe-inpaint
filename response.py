from http.client import HTTPResponse
from io import BytesIO
class FakeSocket:
    def __init__(self, response_str):
        self._file = BytesIO(response_str.encode())
    def makefile(self, *args, **kwargs):
        return self._file
def create_response(content_type, body):
    content_length = len(body)
    response_str = f"HTTP/1.1 200 OK\r
" \
                   f"Content-Type: {content_type}\r
" \
                   f"Content-Length: {content_length}\r
" \
                   "\r
" \
                   f"{body}"
    
    fake_socket = FakeSocket(response_str)
    response = HTTPResponse(fake_socket)
    response.begin()
    return response