from compressor.filters import FilterBase

class NewlineNormalizerFilter(FilterBase):
    def input(self, **kwargs):
        return self.content.replace("\r\n", "\n").replace("\r", "\n")