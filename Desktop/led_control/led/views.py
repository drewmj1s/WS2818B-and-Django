from __future__ import unicode_literals
from django.shortcuts import render
from rpi_ws281x import *
import RPi.GPIO as GPIO
import time
import random
import math
import thread
from math import sqrt
from . models import Pattern
from . forms import PatternForm


on = False
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
LED_COUNT = 150
DATA_OUTPUT_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0

COLORS = []

strip = Adafruit_NeoPixel(LED_COUNT, DATA_OUTPUT_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)

strip.begin()



def rand_color():
    r = random.randint(0, 250)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def bubbleSort(arr):
    '''I am using the bubble sort formula from this useful site https://www.geeksforgeeks.org/bubble-sort/
        I don't implement it in this program because it doesn't make sense to sort by red unless that's the desired output,
        but feel free to edit to sort by whatever color pattern you want and implement it to reflect onto the strip.''' 
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                

def perfect_square(num_leds): #this returns the closest square root below the given number, in the case that you were to layout your strip in a square as I did, it makes it easier to find values for particular patterns.
    if sqrt(float(num_leds)) % 1 == 0:
        return sqrt(num_leds)
    return perfect_square(float(num_leds) - 1)


def hex_to_rgb(value):
    """Return (red, green, blue) for the color given as #rrggbb."""
    '''I got this from https://stackoverflow.com/questions/214359/converting-hex-color-to-rgb-and-vice-versa'''
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def displayLights(pattern_speed, pattern_color, pattern_name, pattern_baf, pattern_leds):
    r,g,b = hex_to_rgb(pattern_color)
    #print ('{0} {1} {2}'.format(r,g,b))
    pattern_leds = perfect_square(pattern_leds)
    #print(pattern_leds)
    brightness = 1
    global on
    on = True
    while on == True:
        
        if r<=15:
            if r == 15:
                r = 255
            else:
                r = r*16
        if g<=16:
            if g == 15:
                g = 255
            else:
                g = g*16
        if b<=16:
            if b == 15:
                b = 255
            else:
                b = b*16
        red = r
        green = g
        blue = b
        #print ('{0} {1} {2}'.format(red,green,blue))
        speed = pow(10,(float(pattern_speed))*-1)
        for x in range(0, LED_COUNT):
            if(float(x)<=pattern_leds or float(x)>(pattern_leds*pattern_leds)-pattern_leds):
                strip.setPixelColor((x), Color(red, green, blue))
            if(float(x)%pattern_leds==0 or float(x)%pattern_leds==1):
                strip.setPixelColor((x), Color(red, green, blue))
            '''strip.setPixelColor(x-1,Color(0,0,0))
            strip.setPixelColor((x), Color(red, green, blue))'''

            time.sleep(speed)
            strip.show()

        if(pattern_baf=="True"):
            for y in range(0, LED_COUNT):
                strip.setPixelColor(LED_COUNT-y+1, Color(0,0,0))
                strip.setPixelColor(LED_COUNT-y, Color(red,green,blue))
                time.sleep(speed)
                strip.show()
        #speed = speed*1.01
        del COLORS[:]
        #red, green, blue = rand_color()

def home(request):
    all_patterns = Pattern.objects.order_by('speed_var')
    form = PatternForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PatternForm()
    context = {
        'all_patterns' : all_patterns, 'form' : form
    }
    return render(request, 'home.html', context)



def on_page(request, pattern_speed, pattern_color, pattern_name, pattern_baf, pattern_leds):
    
    thread.start_new_thread(displayLights, (pattern_speed, pattern_color, pattern_name, pattern_baf, pattern_leds))
    all_patterns = Pattern.objects.order_by('speed_var')
    form = PatternForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PatternForm()
    context = {
        'all_patterns' : all_patterns,
        'form' : form,
        'pattern_name': pattern_name,
        'pattern_baf': pattern_baf,
        'pattern_leds': pattern_leds,
        'pattern_speed': pattern_speed,
        'pattern_color': pattern_color,
    }
    return render(request, 'on_page.html', context)


def offFunc():
    for position in range(0, LED_COUNT):
        strip.setPixelColor(position, Color(0, 0, 0))
        strip.show()
        time.sleep(0.0000001)
def turnOff(request):
    global on
    on = False
    for x in range(10):
        offFunc()
    all_patterns = Pattern.objects.order_by('speed_var')
    form = PatternForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PatternForm()
    context = {
        'all_patterns' : all_patterns,
        'form' : form,
    }
    return render(request, 'off_page.html', context)


