"""
X5A robot base.
"""
import numpy as np

from robosuite.models.bases.mount_model import MountModel
from robosuite.utils.mjcf_utils import xml_path_completion


class X5A_base(MountModel):
    """
    Base for X5A robot.

    Args:
        idn (int or str): Number or some other unique identification string for this mount instance
    """

    def __init__(self, idn=0):
        super().__init__(xml_path_completion("bases/X5A_base.xml"), idn=idn)

    @property
    def naming_prefix(self):
        return "X5A_base{}_".format(self.idn)

    @property
    def top_offset(self):
        return np.array((0, 0, 0.0605))  # 从URDF中获取的joint1的z偏移

    @property
    def horizontal_radius(self):
        # 根据机械臂的工作空间设置
        return 0.5 