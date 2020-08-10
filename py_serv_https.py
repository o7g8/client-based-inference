from http.server import HTTPServer, SimpleHTTPRequestHandler 
import ssl

def get_password():
    return "test"

ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ctx.load_cert_chain(
    "./https/localhost.pem",
    keyfile="./https/localhost.key", 
    password=get_password)
httpd = HTTPServer(('0.0.0.0', 5500), SimpleHTTPRequestHandler)
httpd.socket = ctx.wrap_socket(
    httpd.socket,
    server_side=True)
httpd.serve_forever()