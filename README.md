# E-ink-Home-assistant-Display
Setting up a sensor and weatherman for home assistant and a e-ink esp32 display
First I want to thank Madelna and DeastinY for thier projects providing solid base for my project.

* https://github.com/Madelena/esphome-weatherman-dashboard
* https://github.com/DeastinY/esphome-waveshare-e-paper-dashboard

Also thank you to MallocArray for their Air Gradient esphome code
* https://github.com/MallocArray/airgradient_esphome

This is a repo for my project for a more modular/drop in setup for a E-Ink Display dashboard
This dashboard currently shows sensor readings from a air-gradient pro and an Air GRadient Open Air for indoor and outdoor readings
The weather is done with the built in weather sensor in Home assistant.

![IMG_8724](https://github.com/user-attachments/assets/78ac15a6-40f2-4a48-946d-a7e5e5d0cf35)


The code is designed for a waveshare 7.5in E-ink display using a waveshare esp32 e-ink display driver
Currently as of 7/12/2024 it only has todays weather but the code is setup to easily add a 5 day forecast just need to setup the display to show it.

the automation is to run a python script put into a folder called python_scripts
the python script pulls data from the forecast get forecast and splits the data for the different values of condition, tempurature and humidity.
It then saves the data into text inputs for the custom sensors to pull.

configuration.yaml has the text-inputs and the sensors and sets the sensors data based on the text inputs.
