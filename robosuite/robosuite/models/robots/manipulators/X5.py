import numpy as np
from robosuite.models.robots.manipulators.manipulator_model import ManipulatorModel
from robosuite.utils.mjcf_utils import xml_path_completion

class X5(ManipulatorModel):
    """
    X5是一个自定义机械臂
    
    Args:
        idn (int or str): 该机器人实例的唯一ID
    """
    
    arms = ["right"]  # 设置机械臂名称，如果是单臂，通常命名为"right"
    
    def __init__(self, idn=0):
        super().__init__(xml_path_completion("robots/X5/X5.xml"), idn=idn)
        
        # 可以设置关节阻尼等参数
        # self.set_joint_attribute(attrib="damping", values=np.array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]))
    
    @property
    def default_base(self):
        return "RethinkMount"  # 可以根据需要选择适合的基座
    
    @property
    def default_gripper(self):
        return {"right": "Robotiq85Gripper"}  # 选择合适的夹爪，或者设为None
    
    @property
    def default_controller_config(self):
        return {"right": "default_X5"}  # 需要为X5创建对应的控制器配置
    
    @property
    def init_qpos(self):
        # 设置初始关节角度，需要与您的机械臂关节数量匹配
        return np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    
    @property
    def base_xpos_offset(self):
        # 设置基座位置偏移
        return {
            "bins": (-0.5, -0.1, 0),
            "empty": (-0.6, 0, 0),
            "table": lambda table_length: (-0.16 - table_length / 2, 0, 0),
        }
    
    @property
    def top_offset(self):
        return np.array((0, 0, 1.0))
    
    @property
    def _horizontal_radius(self):
        return 0.5
    
    @property
    def arm_type(self):
        return "single"