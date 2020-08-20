# automated_filter_wheel
This project is an automated filter wheel mounted on a Thorlab microsope, using a TinyG board to control the rotation of the filter wheel.

## Connecting to TinyG Board
Before using this code to communicate with the TinyG board, it's better we test the connection between our computer and TingG board is fine by using another software called [coolterm](https://github.com/synthetos/TinyG/wiki/Connecting-TinyG).



## TinyG Board Configuration
There are some default configurations you don't need to worry too much about, and one special configuration specific configured to this project.

default configuration

    $1ma=0    Maps motor 1 to the X axis
    $2ma=1    Maps motor 2 to the Y axis
    $3ma=2    Maps motor 3 to the Z axis
    $4ma=1    Maps motor 4 to the Y axis
In my case, I wired my motor to motor 1(marked on the board), so all the configuration I care about is $1**=**

special configuration

    $1tr=360
After setting the Travel per Revolution of the motor you're using to 360, the code will work fine, since the code will translate amount traveled into angle to desired filter internally.

After setting the special configuration, the code will work fine as expected.