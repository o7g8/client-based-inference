# Demo of a client-side inference

Demonstration of a client-side inference using (Tensorflow.js)[https://www.tensorflow.org/js] and (MobileNet)[https://github.com/tensorflow/tfjs-examples/tree/master/mobilenet]. The JS code is based on the tutorial (Realtime object detection with MobileNet - ML with Tensorflow.js #5)[https://www.youtube.com/watch?v=QUmuxu6pJD0].

## Prerequisites

- A laptop or a phone with a camera and a modern web-browser.

- Download ngrok: 

```
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
unzip ngrok-stable-linux-amd64.zip -d ~
```

- In case you will serve the web-server with VSCode Live Server, fix the path to the certifcates and key files in the `.vscode/settings.json`.

## Start the HTTPS server serving the webpage with the model 

To make user-device camera work the pages need to be served over HTTPS. It can be using one of the approaches below:

- Live Server VSCode extesion: Go Live.

- run `python3 py_serv_https.py`.

Check the local HTTPS serving with:

`wget https://localhost:5500 --no-check-certificate`

(Optional): in case your users are behind firewall/proxy you may need to expose the custom port (5500) to a firewall/proxy-friendly endpoint on ngrok:

`./ngrok_https.sh`

## Open the webpage with the browser

Open the browser with `https://<your-machine>:5500` (or `https://<ngrok-endpoint>/`) and open the page `index_video.html`.
