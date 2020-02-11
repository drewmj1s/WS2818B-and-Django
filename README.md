# WS2818B-and-Django
Control a WS2818B led strip with a site made with the Django framework. Will work on pc as well as mobile. The site is coded to use input from GPIO pins from a Raspberry Pi, and I used the model 4b to provide sufficient power for the strip.

## The purpose
The purpose of this project was to make an easy-to-use user interface for applying patterns to a WS2818B led strip given certain parameters.

## TO USE
The product itself is pretty simple to use after you've gone through the setup.
Once you've cloned the repository, navigate into the folder that was downloaded, should be led_control, from a terminal.
To run the site, use the command ```python manage.py runserver```.
You should see output that says that the site is being hosted on the URL localhost:xxxx, where xxxx is a port number, likely 8080.
If your terminal supports it, you may click the link to that URL.
If your terminal does not support it, you may go into your browser and type in localhost:xxxx, the port number it gives.
If you haven't done so already, you will want to connect some jumper wires to the WS2818B from your Raspberry Pi.
> While the Raspberry Pi is off, connect a jumper wire from a 5 Volt pin on the RPi to the red cable on the WS2818B
> Connect another jumper wire from a Ground pin on the RPi to the black cable on the WS2818B
> Finally, connect a last jumper wire from GPIO pin 18 to the green cable on the WS2818B

You can change the GPIO pin that the output is being read from if you prefer in led_control/led/views.py on line 18 that says DATA_OUTPUT_PIN = 18. Be aware of what the certain pins do before changing or connecting anything.

FINALLY, you can now use the site to add primitive patterns to the database which can be triggered at the bottom of the page with their own respective buttons.

### Things that could be added
I've thought about plenty of patterns that could be added as an "advanced patterns" setting, or as a set of defaults, but because of a lack of time I will not be implementing this. There are some unintuitive and some downright wrong methods of approach used here, however if they weren't
