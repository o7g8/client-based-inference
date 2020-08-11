# Serving HTTPS

The VSCode settings `../.vscode` are inspired by the guide <https://gist.github.com/prof3ssorSt3v3/edb2632a362b3731274cfab84e9973f9>

The key and certificate files are created following the same guide:

```
openssl genrsa -aes256 -out localhost.key 2048
openssl req -days 3650 -new -newkey rsa:2048 -key localhost.key -x509 -out localhost.pem
```

The included private key has password `test`. You are welcome to generate your own files and use your own password.