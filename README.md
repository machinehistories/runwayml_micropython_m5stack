# runwayml_micropython_m5stack 
using http requests with m5stack to communicate with ![Test Image 3](https://github.com/machinehistories/runwayml_micropython_m5stack/blob/master/runway.jpg)

# example using http get with RunwayML classification models
![Test Image 4](https://github.com/machinehistories/runwayml_micropython_m5stack/blob/master/apple_image.jpg)
![Test Image 4](https://github.com/machinehistories/runwayml_micropython_m5stack/blob/master/Screenshot%20from%202020-02-23%2019-55-19.png)

this example uses the big gan model to identify items and stream the text descriptions to the screen of the M5Stack using http get and json. the M5Stack responds by graphically representing the identified object as well as changing the color of the leds to a color matching the identified object. this example can be customized to use the identification value from RunwayML to trigger and control various hardwares such as motors, LEDs, and sound on the M5Stack.

# example using http post with RunwayML to explore latent space

this example sends vectors to RunwayML and allows you to interact and select different categories from which to draw
