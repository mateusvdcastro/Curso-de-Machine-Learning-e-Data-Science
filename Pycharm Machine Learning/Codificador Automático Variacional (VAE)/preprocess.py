class MinMaxNormaliser:
    """ MinMaxNormaliser applies min max normalisation to an array """

    def __init__(self, min_val, max_val):
        self.min = min_val
        self.max_val = max_val

        def normalise(self, array):
            norm_array = (array - array.min()) / (array.max() - array.min())
            norm_array = norm_array * (self.max - self.min) + self.min
            return norm_array

        def denormalise(self, norm_array, original_min, original_max):
            array = (norm_array - self.min) / (self.max - self.min)
            array = array * (original_max - original_min) + original_min
            return array