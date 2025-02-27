# E-ink-Home-assistant-Display
Setting up a sensor and weatherman for home assistant and a e-ink esp32 display
First I want to thank Madelna and DeastinY for thier projects providing solid base for my project.

* https://github.com/Madelena/esphome-weatherman-dashboard
* https://github.com/DeastinY/esphome-waveshare-e-paper-dashboard

Also thank you to MallocArray for their Air Gradient esphome code
* https://github.com/MallocArray/airgradient_esphome


Items used for this project:
* Frame https://www.amazon.com/dp/B06Y26G4K5?ref=ppx_yo2ov_dt_b_product_details&th=1
* E-ink Display https://www.amazon.com/dp/B075R4QY3L?psc=1&ref=ppx_yo2ov_dt_b_product_details
* ESP32 waveshare e-ink driver https://www.amazon.com/dp/B07M5CNP3B?psc=1&ref=ppx_yo2ov_dt_b_product_details


Fonts used:
* https://fonts.google.com/specimen/Roboto
* https://github.com/Templarian/MaterialDesign-Webfont

This is a repo for my project for a more modular/drop in setup for a E-Ink Display dashboard
This dashboard currently shows sensor readings from a air-gradient pro and an Air GRadient Open Air for indoor and outdoor readings
The weather is done with the built in weather sensor in Home assistant.


![IMG_8810](https://github.com/user-attachments/assets/b73ab4a8-73db-4e13-b028-a60b08eaa4f6)


The code is designed for a waveshare 7.5in E-ink display using a waveshare esp32 e-ink display driver


the automation is to run a python script put into a folder called python_scripts
the python script pulls data from the forecast get forecast and splits the data for the different values of condition, tempurature and humidity.
It then saves the data into text inputs for the custom sensors to pull.

configuration.yaml has the text-inputs and the sensors and sets the sensors data based on the text inputs.
