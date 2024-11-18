from mmseg.datasets.builder import DATASETS
from .custom import CustomDataset

@DATASETS.register_module()
class ScoliosisDataset():
    METAINFO = dict(
        classes=('Spine'),
        palette=([255, 0, 0])
    )
    
    def __init__(self, **kwargs):
        super(ScoliosisDataset, self).__init__(
            img_suffix='.png',
            seg_map_suffix='.png',
            reduce_zero_label=True,
            **kwargs)