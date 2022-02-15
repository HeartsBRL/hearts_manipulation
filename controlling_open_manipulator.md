# Controlling open manipulator

You can controll open manipulator with either arduino or ROS. 

## Arduino 

Open manipulator with Arduino gives you a chance to work with a better GUI and you can make it to do some fancy stuffs in a short period of time which will 
require a lot of effort from ROS (unless and untill you have spent a lot of time on ROS).

You can refer to [official website](https://emanual.robotis.com/docs/en/platform/openmanipulator_x/quick_start_guide/#install-ros-on-pc) and select Arduino to 
cross check or for reference. The below steps are just explained version of official website with my personal experience. 

### Setup Arduino IDE for OpenCR

For reference check the [official page](https://emanual.robotis.com/docs/en/parts/controller/opencr10/#install-on-linux) 

#### Before installing Arduino IDE:

Make your system to upload code to OpenCr without root permission 

```
wget https://raw.githubusercontent.com/ROBOTIS-GIT/OpenCR/master/99-opencr-cdc.rules
sudo cp ./99-opencr-cdc.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules
sudo udevadm trigger
```

Since the OpenCR libraries is built for 32 bit platform, 64 bit PC needs the 32 bit compiler relevants for the ArduinoIDE.

```
sudo apt-get install libncurses5-dev:i386
```
**NOTE**: In the case you already have Arduino in your system it is worth trying this step without uninstalling Arduino IDE. However I am not certain if that will
work.

#### Download Arduino IDE 

Download Arduino IDE from the [official site](https://www.arduino.cc/en/Main/Software)

Then run the installation script:

```
cd Downloads/arduino-1.8.18/
./install.sh
```
Your location of Arduino Download might be different.

Now, set Arduino IDE's path as absolute path. This is done by making changes to bashrc script and sourcing it:

Open bashrc script (i am using nano to do it)

```
sudo nano ~/.bashrc 
```

Then add the following line in the bashrc script that is opened in terminal

```
export PATH=$PATH:$HOME/tools/arduino-1.6.4
```

In order to close nano press ctrl+x and then type y when it ask to save the file and then press enter.

Now source the file 

```
source ~/.bashrc
```

It is recomended to open a new tab after sourcing bashrc.

Follow the instructions given on [these page](https://emanual.robotis.com/docs/en/parts/controller/opencr10/#install-on-linux) ater this steps for arduino setup.

#### Installing Processor

Processor is the main gui were you can see the state of the manipulator and also control it.

Download processing using [this link]( https://processing.org/download/).

Now check the downloaded file for a file named as "processing". and launch the same file with terminal. In my system it was something like this:

```
/home/hearts/Downloads/processing-4.0b2/processing
```
Follow the instruction on [this page](https://emanual.robotis.com/docs/en/platform/openmanipulator_x/quick_start_guide/#install-ros-on-pc) for initiating processing for open manipulator.

### Introduction to the Interface

After launching the processing you will see two windows one of them will show you the state of the manipulator and the other one will show the controll pannel. 

At the very top of controll interface you will see 4 sections which are discussed below:

#### Joint space
![Screenshot from 2022-02-15 15-58-30](https://user-images.githubusercontent.com/50763982/154103049-a439ff97-e625-4566-9b37-8cfb044fb96f.png)

Selecting Controller ON will enable immediate use of BASIC and ORIGIN options which are two stable states of the manipulator. Before selecting basic do not forget to support the manipulator otherwise it may trip.

Changing joint angle of any knob between 1-4 will set that joint at that same angle. The gripper can only act either in Gripper Open or Close state. 




