import numpy as np
import robosuite as suite
from robosuite.models.robots import Robot
from robosuite.models.arenas import TableArena
from robosuite.models.objects import BoxObject
from robosuite.models.tasks import Task
from robosuite.utils.placement_samplers import UniformRandomSampler
from robosuite.controllers import load_composite_controller_config

# 加载自定义机器人
class Arx5x5(Robot):
    def __init__(self, idn=0):
        # 加载 URDF 文件，确保路径正确
        super().__init__(robot_type="Arx5x5", idn=idn, urdf_file="/home/zz/Desktop/robosuite_env/models/X5.urdf")

# 创建环境
def create_environment():
    # 定义机器人
    robots = [Arx5x5()]

    # 定义工作台
    arena = TableArena(table_full_size=(0.8, 0.8, 0.05), table_friction=(0.001, 0.001, 0.001))

    # 定义方块对象
    obj1 = BoxObject(
        name="block1",
        size_min=[0.02, 0.02, 0.02],
        size_max=[0.02, 0.02, 0.02],
        rgba=[1, 0, 0, 1]  # 红色
    )
    obj2 = BoxObject(
        name="block2",
        size_min=[0.02, 0.02, 0.02],
        size_max=[0.02, 0.02, 0.02],
        rgba=[0, 0, 1, 1]  # 蓝色
    )

    # 随机放置方块
    placement_initializer = UniformRandomSampler(
        name="ObjectSampler",
        x_range=[-0.1, 0.1],
        y_range=[-0.1, 0.1],
        z_range=[0.02, 0.02],
        rotation=[0, 0, 0],
        ensure_object_boundary_in_range=True,
        ensure_valid_placement=True
    )
    placement_initializer.setup(obj1, obj2)

    # 创建任务
    task = Task(
        robots=robots,
        objects=[obj1, obj2],
        arena=arena,
        placement_initializer=placement_initializer
    )

    # 创建环境
    env = suite.make(
        env_name="Stack",
        robots=robots,
        controller_configs=load_composite_controller_config(default_controller="OSC_POSE"),
        has_renderer=True,
        has_offscreen_renderer=False,
        use_camera_obs=False,
        task=task
    )
    return env

# 主程序
if __name__ == "__main__":
    env = create_environment()
    obs = env.reset()
    for _ in range(1000):
        action = np.random.randn(*env.action_spec[0].shape) * 0.1  # 随机动作
        obs, reward, done, _ = env.step(action)
        env.render()
