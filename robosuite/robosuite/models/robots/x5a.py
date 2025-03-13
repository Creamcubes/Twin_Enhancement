import os
import numpy as np
from robosuite.models.robots.robot_model import RobotModel
from robosuite.utils.mjcf_utils import xml_path_completion
ROBOTS = {

    "X5A": X5A,  # 注册自定义机器人模型
}
class X5A(RobotModel):
    """
    Custom X5A robot arm.
    """
    def __init__(self):
        # URDF 文件路径
        urdf_path = os.path.join(os.path.dirname(__file__), "X5A.urdf")
        
        # 调用父类构造函数
        super().__init__(urdf_path, name="x5a")

    def _get_controller_config(self):
        """
        返回控制器配置。
        """
        return {
            "type": "OSC_POSE",  # 使用 OSC（操作空间控制）
            "interpolation": "linear",
            "impedance_mode": "fixed",
            "kp": 150,
            "damping_ratio": 1,
        }

    @property
    def dof(self):
        """
        返回机械臂的自由度数。
        """
        return 8  # 根据 URDF 文件中的关节数量设置

    @property
    def gripper_joints(self):
        """
        返回夹爪关节名称。
        """
        return ["joint7", "joint8"]  # 根据 URDF 文件中的夹爪关节设置

    @property
    def default_gripper(self):
        """
        返回默认夹爪。
        """
        return "X5AGripper"  # 如果需要自定义夹爪，可以在这里定义

    @property
    def default_controller_config(self):
        """
        返回默认控制器配置。
        """
        return self._get_controller_config()

    @property
    def init_qpos(self):
        """
        返回初始关节位置。
        """
        return np.array([0, 0, 0, 0, 0, 0, 0, 0])  # 根据机械臂的自由度设置