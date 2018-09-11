First time connecting with a new computer:
(connect ethernet cable to tiago)

```
ssh root@10.68.0.1 (if using different tiago, use ifconfig to find xx.xx.x)
cd ../etc
nano hosts
```
add this line to the file (near the other similar lines):
```
10.68.0.xxx hostname
```
(if you need to find your host name, on your computer it is in ```/etc/hostname``` )
(to find your ip, type in ```ifconfig```)

Save the file.

Now on your computer, go to ```etc/hosts```, and add the line:
```
10.68.0.1 tiago-25c
```

Save the file.

Now you are set up to connect :) 

In every new terminal you want to connect to tiago (and use ros), type:
```
export ROS_IP=10.68.0.xxx
export ROS_MASTER_URI=http://10.68.0.1:11311/
```


When running our manipulation code, remember to source your terminal so catkin stuff works e.g.:
```
source ./devel/setup.bash
```
when in tiago_public_ws
