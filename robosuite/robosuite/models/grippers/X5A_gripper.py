"""
Gripper for X5A robot (has two fingers).
"""
import numpy as np

from robosuite.models.grippers.gripper_model import GripperModel
from robosuite.utils.mjcf_utils import xml_path_completion


class PandaGripperBase(GripperModel):
    """
    Gripper for X5A robot (has two fingers).

    Args:
        idn (int or str): Number or some other unique identification string for this gripper instance
    """

    def __init__(self, idn=0):
        super().__init__(xml_path_completion("grippers/X5A_gripper.xml"), idn=idn)

    def format_action(self, action):
        return action

    @property
    def init_qpos(self):
        # 设置夹爪的初始位置为稍微打开的状态
        # joint7: 0.01 (稍微打开)
        # joint8: 0.01 (稍微打开)
        return np.array([0.01, 0.01])

    @property
    def _important_geoms(self):
        return {
            "left_finger": ["finger1_collision", "finger1_pad_collision"],
            "right_finger": ["finger2_collision", "finger2_pad_collision"],
            "left_fingerpad": ["finger1_pad_collision"],
            "right_fingerpad": ["finger2_pad_collision"],
        }


class X5AGripper(PandaGripperBase):
    """
    X5A机器人的夹爪控制器，使用一个控制输入控制两个夹爪关节。
    """

    def format_action(self, action):
        """
        将连续动作映射到两个夹爪关节的输出
        -1 => 打开, 1 => 关闭

        Args:
            action (np.array): 夹爪特定动作

        Raises:
            AssertionError: [无效的动作维度]
        """
        assert len(action) == self.dof
        # 两个夹爪关节的方向:
        # joint7 (左指): 0->0.044 表示关闭 (轴方向为正)
        # joint8 (右指): 0->0.044 表示关闭 (轴方向为负)
        # 所以在控制时，两个关节的范围定义相同，但实际物理运动方向相反
        self.current_action = np.clip(
            self.current_action + np.array([1.0, 1.0]) * self.speed * np.sign(action), -1.0, 1.0
        )
        return self.current_action

    @property
    def speed(self):
        return 0.2

    @property
    def dof(self):
        return 1
