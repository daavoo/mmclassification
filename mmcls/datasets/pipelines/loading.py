from mmcv import LoadImageFromFile

from ..builder import PIPELINES

PIPELINES.register_module(LoadImageFromFile)
