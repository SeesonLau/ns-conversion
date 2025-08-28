# Make widgets a proper Python package
from .conversion_widget import ConversionWidget
from .addition_widget import AdditionWidget
from .encode_widget import EncodeWidget
from .decode_widget import DecodeWidget

__all__ = ['ConversionWidget', 'AdditionWidget', 'EncodeWidget', 'DecodeWidget']
