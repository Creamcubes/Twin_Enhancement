import mujoco

print("MuJoCo version:", mujoco.mj_versionString())
print(mujoco.__file__)
import numpy as np
import robosuite as suite
robot = "X5A"#"Panda"
# create environment instance
env = suite.make(
    env_name="Stack", # try with other tasks like "Stack" and "Door"
    robots="X5A",  # try with other robots like "Sawyer" and "Jaco"   #"Panda"   "X5A"
    has_renderer=True,
    has_offscreen_renderer=False,
    use_camera_obs=False,
)

env.reset()

for i in range(1000):
    random_number = np.random.normal()
    #print(f'shape:{env.action_spec[0].shape}')
    #action = np.random.randn(*env.action_spec[0].shape) * 0.1
    action = np.array([1,1,1,0,0,0,0])
    #action = np.random.randn(6) * 0.1
    #print(f'action:{action}')
    obs, reward, done, info = env.step(action)  # take action in the environment
    env.render()  # render on display



#相比Panda作修改：部分文件中7维数据改为6维
#如C:\Users\86136\anaconda3\envs\robosuite\Lib\site-packages\robosuite\robots\robot.py line258:        
        # if len(self.sim.data.qpos[self._ref_joint_pos_indexes])==7:
        #     self.sim.data.qpos[self._ref_joint_pos_indexes] = init_qpos
        # if len(self.sim.data.qpos[self._ref_joint_pos_indexes])==6:
        #     self.sim.data.qpos[self._ref_joint_pos_indexes] = init_qpos[:6]
#ValueError: No "site" with name robot0_right_center exists. Available "site" names = ('table_top', 'robot0_ee', 'robot0_ee_x', 'robot0_ee_z', 'robot0_ee_y', 'gripper0_right_ft_frame', 'gripper0_right_grip_site', 'gripper0_right_ee_x', 'gripper0_right_ee_y', 'gripper0_right_ee_z', 'gripper0_right_grip_site_cylinder', 'cubeA_default_site', 'cubeB_default_site').
#C:\Users\86136\anaconda3\envs\robosuite\Lib\site-packages\robosuite\robots\fixed_base_robot.py line152
            #applied_action = np.clip(applied_action, applied_action_low, applied_action_high)
            #applied_action = np.clip(applied_action, applied_action*0-1, applied_action*0+1)