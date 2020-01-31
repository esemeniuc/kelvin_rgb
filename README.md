# kelvin_rgb

A python library for converting colour temperature (Kelvin) to RGB values

![alt text](https://github.com/esemeniuc/kelvin_rgb/blob/master/colour_temp.png "Colour Temperature")

Convert color from RGB to Kelvin and back

## Installation

```bash
pip install kelvin_rgb
```

## Usage

```python
import kelvin_rgb
r, g, b = kelvin_rgb.k_to_rgb(3500)
print(r,g,b) #outputs (255, 138, 195)
hex = kelvin_rgb.k_to_rgb_hex(3500)                                                                                          
print(hex) #outputs '#ff8ac3'
```
Note: The conversions use approximations and are suitable for photo-manipulation and other non-critical uses.

Accuracy is best between 1000K and 40000K.