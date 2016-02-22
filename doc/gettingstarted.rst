Getting Started with the eBot
=============================

+---------+--------------+------------+-------+----------+-----------+
| Title   | Description  | Author(s)  | Tags  | Created  | Modified  |
+=========+==============+============+=======+==========+===========+
| Getting | Getting      | Abhishek   | eBot, | 20 Oct   | 18 Dec    |
| started | started with | Harsh      | SOAR  | 2014     | 2014      |
| guide   | the eBot     |            |       |          |           |
+---------+--------------+------------+-------+----------+-----------+

eBot Description
----------------

|solarized dualmode|

LED positions 

* 1- Bluetooth
* 2- MCU 
* 3- Charging

eBots are a robust, 3D-printed versatile STEM learning robotics platform
that provide modularity and customization options. eBots aim to bridge
the link between theory and practice by providing the ideal platform for
students to collaborate and use their combined knowledge to build the
best solution to a task. EdgeBotix wants to build the best supporting
community and provide resources for teaching, making it extremely easy
to integrate into the curriculum, something not seen in current
educational robots.

General Instructions
~~~~~~~~~~~~~~~~~~~~

Robot could be controlled using the python programming languages, using the
python libraries 

**Description of files** 

eBot.py – Contains the eBot API functions for controlling eBot 

Locator_EKF.py – used for estimations of the position of the eBot

Serial files: serialposix.py, serialutil.py, serialwin32.py – used for
the serial communication 

**Instruction for running the eBot**

1. Make sure the left most LED is blinking when the eBot is switched on 
2. Once the eBot is connected, the left most LED will become solid 
3. Right most LED is the charging LED, while charging it will show ORANGE, once
   fully charge kindly remove the charging cable. DO not overcharge it, it might
   damage the battery 
4. Do not manually move the eBot wheels, or force it to move with hand
5. In case you are using Odometery() make sure eBot is on ground and you do not
   move the eBot while it is connecting
6. In case you are using sonar sensors, make sure there is no obstacle up to 30
   cm in front of each sonars

Technical Specification
~~~~~~~~~~~~~~~~~~~~~~~

The following are detailed technical specifications of the eBots: 

* **Physical robot** 
    * 15 x 15 x 8 cm, ABS plastic housing with various colour options 
    * Tank drive (2 drive treads) 
        * Powered by 2 low current Tamiya DC brushed motors 
        * 150 RPM no load speed 
        * .2 m/s average speed 
* **Firmware** 
    * Powered by an ARM Cortex M0 microprocessor running at 48 MHz 
* **Sensors & other I/O** 
    * 6 Sonar range finders (15 cm to 3 m range) 
        * 1 Front facing 
        * 2 At 45° from front 
        * 2 Side facing 
        * 1 Back facing 
        * Within 20 cm dead zone requirement 
    * 6 DOF IMU (Accelerometer & Gyroscope) 
        * Raw acceleration data in x, y and z axis 
        * Raw euler angle (rotation) along x, y and z axis 
    * 2 Encoders, providing distance and velocity measurements for both treads
    * 2 LDRs
        * 1 Top facing 
        * 1 Front facing 
    * Onboard buzzer with a frequency range of 100 Hz to 10 KHz
* **Wireless communication** 
    * Bluetooth connectivity to host computer 
    * Each robot has unique serialized Bluetooth identifier, in accordance to 
      the serial number labeled on robot body 
* **Power** 
    * 2 Ah Li-Po battery providing 3+ hours of continuous runtime 
    * Mini USB charging port 
        * 1 Hour full charge time 
* **Software** 
    * eOS Running onboard eBots (an RTOS built on the mbed RTOS) 
* **Interface** 
    * Currently there are two interface with python language 
        * `Soar Interface <#soar>`__ 
        * `API interface <#api>`__

Pairing eBot
~~~~~~~~~~~~

-  eBot could be paired by entering the pairing code "0000". If you want
   the step by step guide of pairing with your system you can click
   `here <#pairing>`__.

Python Installation
~~~~~~~~~~~~~~~~~~~

Dependencies : 

* `Python 2.7 <https://www.python.org/download/releases/2.7.6/>`__

Windows Only: 

* `pywin32 x64 <http://sourceforge.net/projects/pywin32/files/pywin32/Build%20219/pywin32-219.win-amd64-py2.7.exe/download>`__
* `pywin32 x86 <http://sourceforge.net/projects/pywin32/files/pywin32/Build%20219/pywin32-219.win32-py2.7.exe/download>`__

Soar
----

This section assumes that you have Python 2.7 already installed. To
install Digital World Library, follow the steps according to your
platform:

**OS X and Linux:**

* Download SOAR-master.zip from the `github <https://github.com/EdgeBotix/SOAR>`__ 
* Open Terminal 
* Go the directory/folder where you save the file, e.g. if you save it to 
  Mac's default Downloads folder, then type :

::

        cd $HOME/Downloads

-  Unzip the file, e.g. type :

   ::

       tar SOAR-master.zip

-  Go to the SOAR-master folder, e.g. type:

   ::

          cd SOAR-master

-  Install the library by typing:

   ::

          sudo python setup.py install

**Windows:** 

* Download SOAR-master.zip from the
  `github <https://github.com/EdgeBotix/SOAR>`__ 
* Unzip the file 
* Open Command Prompt by typing "cmd" from the Start Menu
* Go the directory/folder where you have unzipped the file, e.g. type :

::

        cd C:\Downloads\SOAR-master\

-  Install the library by typing:

   ::

          python setup.py install

RUNNING SIMULATOR - SOAR
~~~~~~~~~~~~~~~~~~~~~~~~

After you have installed the Digital World Library, you can run the
simulator, called SOAR. To run it, follow the steps below:

**OS X and Linux:**

* Open Terminal
* Go to the SOAR-master folder
* Go to soar folder
* Run soar by typing:

::

      python runsoar.py

**Windows:**

* Open Command Prompt by typing "cmd" from the Start Menu
* Go to the folder where you store Digital World Library, e.g.:

::

        cd C:\Downloads\SOAR-master\

-  Go to "soar" folder:

   ::

          cd soar

-  Run soar by typing:

   ::

       python runsoar.py

USING SIMULATOR - SOAR
~~~~~~~~~~~~~~~~~~~~~~

1. Running the code and connect to eBot using wireless connection:

-  Run Soar
-  Click "Simulator" button to load any Python files for the Worlds
-  Click "Brain" button and choose the Python files containing your
   robot brain
-  Click "START" button to start connection with EBot

WORLD

Some World files for simulation has been created ans it is part of the
Digital Library Package. It is also included in this package under the
folder "worlds".

BRAIN

A simple Brain file has been included: brainfile.py.

API
---

The user can use the eBot directly by writing a simple python code by
calling the API's from the given list

you can download the API from
`here <https://github.com/EdgeBotix/eBot-API/>`__

**General**

* open() / connect(): Connects to the (first) eBot the computer is connected to
* close()/ disconnect(): Close the comport
* halt(): Halts the eBot, turns motors and LED off

**Outputs**

* led(bool): Turns led on, if input is 1, off if input is 0
* wheels(Ls,Rs): Controls the wheel speed using specified values
* buzzer(frequency, time): Plays the buzzer for given time at given frequency

**Sensors**

* robot\_uS(): Returns a tuple containing all 6 ultraSonic readings in meters
* light(): Returns a tupple containing 2 LDR readings from as 0 to 1, 1 being
  brightest
* obstacle(): Reads the obstacle in front of the front sonar sensor Returns 
  true if the vale is less than 250 mm
* acceleration(): Returns the absolute value of the X,Y, theta coordinates of
  the robot with reference to starting position

**Example**

.. code:: python

    from eBot import *
    from time import *
    eBot = eBot()
    eBot.connect()
    eBot.wheels(1,1) #full forward
    sleep(1)
    eBot.wheels(0,0) #Stop – can use halt as well
    sleep(0.5)
    eBot.led(1)
    eBot.wheels(-1,-1) #full backward
    sleep(1)
    eBot.halt()

Pairing
-------

**Windows**

1. Type add Bluetooth device in the start search box

2. A dialog window will open up as shown in figure 
   
   |Devices|

3. Select the eBotxxx (your eBot number) and press next

4. a new dialog window will open up as shown in figure and then we enter
   the device pairing code 
   
   |pairing_code|

5. the device pairing code is 0000, enter that and press next
   
   |code|

6. we would then get a window saying the device was successfully added.

**For Mac**

1. Click the Bluetooth Icon on upper right corner of a Mac system. 
   
   |mac|

2. Click on Open Bluetooth Preferences as shown

3. Look for eBotxxx (your eBot number) and pair it

4. If it is doesnt connect then click on options

5. Then enter the device pairing code as 0000 and click pair.

.. |solarized dualmode| image:: https://raw.githubusercontent.com/EdgeBotix/docs/master/images/eBot-topview.jpg
   :target: #features
.. |Devices| image:: https://raw.githubusercontent.com/EdgeBotix/docs/master/images/devices.PNG
.. |pairing_code| image:: https://raw.githubusercontent.com/EdgeBotix/docs/master/images/pairing_code.PNG
.. |code| image:: https://raw.githubusercontent.com/EdgeBotix/docs/master/images/code.PNG
.. |mac| image:: https://raw.githubusercontent.com/EdgeBotix/docs/master/images/mac.png

