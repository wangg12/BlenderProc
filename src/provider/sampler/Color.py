import mathutils
import random

from src.main.Provider import Provider


class Color(Provider):
    """ Uniformly samples a 4-dimensional RGBA vector.

    **Configuration**:

    .. csv-table::
       :header: "Parameter", "Description"

       "min", "A list of four values, describing the minimum values for R, G, B and A components. Range: [0; 1]. Type: list."
       "max", "A list of four values, describing the maximum values for R, G, B and A components. Range: [0; 1]. Type: list."
       "grey", "Sample grey values only. Type: bool. Default: False"

    """

    def __init__(self, config):
        Provider.__init__(self, config)

    def run(self):
        """ Samples a RGBA vector uniformly for each component.

        :return: RGBA vector. Type: mathutils.Vector
        """
        # minimum values vector
        min = self.config.get_vector4d("min")
        # maximum values vector
        max = self.config.get_vector4d("max")
        # sample only grey values
        grey = self.config.get_bool("grey", False)

        color = mathutils.Vector([0, 0, 0, 0])
        for i in range(4):
            if all([0 <= min[i] <= 1, 0 <= max[i] <= 1]):
                if grey and 0 < i < 3:
                    color[i] = color[i-1]
                else:
                    color[i] = random.uniform(min[i], max[i])
            else:
                raise RuntimeError("min and max vectors must be composed of values in [0, 1] range!")

        return color