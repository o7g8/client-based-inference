# Demo of a client-side inference

Demonstration of a client-side inference using [Tensorflow.js](https://www.tensorflow.org/js) and [MobileNet](https://github.com/tensorflow/tfjs-examples/tree/master/mobilenet).

The JS code is based on the tutorial [Realtime object detection with MobileNet - ML with Tensorflow.js #5](https://www.youtube.com/watch?v=QUmuxu6pJD0).

## Prerequisites

- A server: local machine, Cloud VM, or a device with installed Python 3.

- A laptop or a phone with a camera and a modern web-browser.

- (Optional) In case your users are behind firewall/proxy blocking non-standrad ports, download [ngrok](https://ngrok.com/): 

```
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
unzip ngrok-stable-linux-amd64.zip -d ~
```

ngrok requires a (free) account to serve HTTPS endpoints, therefore create the account on <https://ngrok.com> and run `ngrok authtoken <token>`according to <https://dashboard.ngrok.com/get-started/setup>.

- In case you will serve the web-server with VSCode [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer), fix the path to the certifcates and key files in the `.vscode/settings.json`.

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


## Greengrass deployment

Based on [New – AWS IoT Greengrass Adds Container Support and Management of Data Streams at the Edge](https://aws.amazon.com/blogs/aws/new-aws-iot-greengrass-adds-docker-support-and-streams-management-at-the-edge/).

Use your own Greengrass host or deploy an EC2 with installed Greengrass using the [CloudFormation template](https://us-west-2.console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?stackName=awsiotworkshop&templateURL=https://s3-us-west-2.amazonaws.com/iotworkshop/ec2-cf-fast-2020.json) taken from <http://iot.awsworkshops.com>.

### Create the Docker container

Build the container `gg-demo/client-inference` with the HTTPS server and the pages:

`./docker_build.sh`

Test the container working locally:

```
docker run -p 6600:5500 gg-client-inference:latest
wget https://localhost:6600 --no-check-certificate
```

### Deploy the container to ECR

Create the ECR repository `gg-client-inference` and follow the Push command guidance available in the AWS Console.

### Deploy the container to Greengrass

Allow Greengras core access docker compose file on S3 and pull the image from the ECR repository by add following managed policies to the Greengrass Core role:

- `AmazonS3ReadOnlyAccess`
- `AmazonEC2ContainerRegistryReadOnly`

You can of course create narrowed down policies scoped to the given S3 destination and following the [Amazon ECR Repository Policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-policies.html)


- Upload the `docker-compose.yml` to S3.

- On the Greengrass device:

```
sudo mkdir /greengrass/compose
chown ggc_user:docker /greengrass/compose
```

- Add Greengrass user into docker group:

`usermod -a -G docker ggc_user`

Alternatively you can create a dedicated Linux-user for the given contaier, make it a member of a the Docker group and specify the user in the Docker Connector properties below.

- Install `docker-compose` (see <https://docs.docker.com/compose/install/>):

```
sudo curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```

- AWS Console -> Greengrass -> Groups -> <Your group> ->  Add a connector -> Docker Application Deployment:

    - Docker Compose file in S3: point to the uploaded `docker-compose.yml` on S3.

    - Set the path for the local Compose file:

    `/greengrass/compose`

- AWS Console: deploy the Greengras group again and check the Greengrass log if there were any errors:

`tail /greengrass/ggc/var/log/user/<your-region>/aws/DockerApplicationDeployment.log`

You should see something similar to:

```
Creating greengrassdockerapplicationdeployment_web_1 ... done
[2020-08-11T13:39:04.909Z][ERROR]-
[2020-08-11T13:39:04.909Z][INFO]-docker_runner.py:125,Compose up successfull with following output
```

- Check the container running on the Greengrass machine:

```
netstat -nlt | grep 6600
wget https://localhost:6600 --no-check-certificate
```
