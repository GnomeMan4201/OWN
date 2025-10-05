import base64


def obfuscate_http(payload):
    headers, body = payload.split("\r\n\r\n", 1)
    encoded = base64.b64encode(body.encode()).decode()
    obfuscated = headers + "\r\nX-Encoded: true\r\n\r\n" + encoded
    return obfuscated


def demo():
    p = "POST /login HTTP/1.1\r\nHost: target.com\r\n\r\nusername=admin&password=secret"
    print(obfuscate_http(p))


if __name__ == "__main__":
    demo()
