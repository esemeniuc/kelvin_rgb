import math
from typing import Tuple

#  Neil Bartlett
#  neilbartlett.com
#  2015-01-22
#
#  Copyright [2015] [Neil Bartlett] for Javascript source
#  Copyright Eric Semeniuc
#
# Color Temperature is the color due to black body radiation at a given
# temperature. The temperature is given in Kelvin. The concept is widely used
# in photography and in tools such as f.lux.
#
# The function here converts a given color temperature into a near equivalent
# in the RGB colorspace. The function is based on a curve fit on standard sparse
# set of Kelvin to RGB mappings.
#
# NOTE The approximations used are suitable for photo-manipulation and other
# non-critical uses. They are not suitable for medical or other high accuracy
# use cases.
#
# Accuracy is best between 1000K and 40000K.
#
# See http://github.com/neilbartlett/color-temperature for further details.

'''
 A more accurate version algorithm based on a different curve fit to the
 original RGB to Kelvin data.
 Input: color temperature in degrees Kelvin
 Output: tuple of red, green and blue components of the Kelvin temperature
'''

def __clamp(value: float, min_val: int = 0, max_val: int = 255) -> int:
    # use rounding to better represent values between max and min
    return int(round(max(min(value, max_val), min_val)))

# see http://www.zombieprototypes.com/?p=210 for plot and calculation of coefficients
def color_temp_to_rgb(kelvin: int) -> Tuple[int, int, int]:
    temperature = kelvin / 100.0

    if temperature < 66.0:
        red = 255
    else:
        # a + b x + c Log[x] /.
        # {a -> 351.97690566805693`,
        # b -> 0.114206453784165`,
        # c -> -40.25366309332127
        # x -> (kelvin/100) - 55}
        red = temperature - 55.0
        red = 351.97690566805693 + 0.114206453784165 * red - 40.25366309332127 * math.log(red)

    # Calculate green
    if temperature < 66.0:
        # a + b x + c Log[x] /.
        # {a -> -155.25485562709179`,
        # b -> -0.44596950469579133`,
        # c -> 104.49216199393888`,
        # x -> (kelvin/100) - 2}
        green = temperature - 2
        green = -155.25485562709179 - 0.44596950469579133 * green + 104.49216199393888 * math.log(green)
    else:
        # a + b x + c Log[x] /.
        # {a -> 325.4494125711974`,
        # b -> 0.07943456536662342`,
        # c -> -28.0852963507957`,
        # x -> (kelvin/100) - 50}
        green = temperature - 50.0
        green = 325.4494125711974 + 0.07943456536662342 * green - 28.0852963507957 * math.log(green)

    # Calculate blue
    if temperature >= 66.0:
        blue = 255
    elif temperature <= 20.0:
        blue = 0
    else:
        # a + b x + c Log[x] /.
        # {a -> -254.76935184120902`,
        # b -> 0.8274096064007395`,
        # c -> 115.67994401066147`,
        # x -> kelvin/100 - 10}
        blue = temperature - 10
        blue = -254.76935184120902 + 0.8274096064007395 * blue + 115.67994401066147 * math.log(blue)

    return __clamp(red, 0, 255), __clamp(blue, 0, 255), __.clamp(green, 0, 255)
