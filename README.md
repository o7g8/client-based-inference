# Demo of a client-side inference

You need to serve it as HTTPS endpoint to make the user-device camera work.

## Prerequisites

- Download ngrok: 

```
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
unzip ngrok-stable-linux-amd64.zip -d ~
```

- In case you will serve the web-server with VSCode Live Server, fix the path to the certifcates and key files in the `.vscode/settings.json`.

## Start the HTTPS server serving the webpage with the model 

It can be served either or:

- Live Server VSCode extesion: Go Live, mthen run the `ngrok_https.sh` to forward the custom port (5500) to a firewall/proxy-friendly endpoint on ngrok.

- run `python3 py_serv_https.py` and then expose it via ngrok with `ngrok_https.sh`.

You can check the local serving is working with:

`wget https://localhost:5500 --no-check-certificate`

## Open the webpage with the browser

Open the browser with `https://<ngrok-endpoint>/` and open the page `index_video.html`.

