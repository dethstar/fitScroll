fitScroll
=========
>Most technologic work is done so the user does less. We believe doing less and less will be harmful in the long run, like in that movie Wall-e.
fitScroll is a tool in the works to help those who use a PC for long time involve in greater physical activity.

>This will be achieved by using bike pedals to scroll content (be it a book, a document, or a webpage).

>It's going to be supported in both Windows and Linux.
No support for OS X is planned, althought if you're using Xorg, it *might* be compatible.


##How to use
* [Circuit](#Circuit)
* [Arduino](#Arduino)
* [Linux](#Linux)
* [Windows](#Windows)

###*The following how-to assumes you have every requirement for your system installed [Windows](requirementsWindows.md)|[Linux](requirementsLinux.md).<br>It also assumes you have cloned the repo.
####<a name="Circuit"></a>Circuit
1. Obtain 2 opto interrupters itr8102, those are our cheap sensors.
2. Make a circuit like the one in the [figure]().


####<a name="Arduino"></a>Arduino
1. Connect your Arduino device to your computer and fire up the Arduino software
2. Copy the fitScroll.ino file content into the Arduino software
3. You could change the pins to be used, default are pin 7 and pin 8, to do so change the value of the variables ban and ban2 respectively.
4. Click the load button and upload the code to your Arduino device 
5. Connect the [circuit](#Circuit) to the pins you picked and feed the circuit with the Arduino 5v output pin, you should make sure to also connect a ground pin.

####<a name="Linux"></a>Linux
1. Plug your Arduino board and look at the part highlighted in [this picture]() in the Arduino software running on your machine.
2. Go into the ```src``` folder and run<br>
```
sudo python read.py dID
 ``` Where dID is what it says on the Arduino software. E.g ACM0<br>
3. Ready, hop on your bike and scroll.

####<a name="Windows"></a>Windows
1. Plug your Arduino board and look at the part highlighted in [this picture]() in the Arduino software running on your machine, if it says ```COM3``` go to next step, else [do this](#fixcom3) and then come back.
2. Go into the ```src``` folder and run the ready.py script<br>
3. Ready, hop on your bike and scroll.

####<a name="fixcome3"></a>Windows fix
Change line 10 and change ```device="COM3"``` to ```device="dID"``` where dID is whatever it says on the Arduino software instead of COM3 
##License

Creative Commons License<br>
This work is licensed under a Creative Commons Attribution-NonCommercial 3.0 Unported License. To read more you can go to:[http://creativecommons.org/licenses/by-nc/3.0/deed.en_US](http://creativecommons.org/licenses/by-nc/3.0/deed.en_US)