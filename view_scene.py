import mujoco
import mujoco.viewer
import os

urdf_path = "/home/mailroom/trossen_arm_mujoco/trossen_arm_mujoco/assets/jony_sofi/jony_sofi.xml"

# Change working directory to the URDF's folder before loading
os.chdir(os.path.dirname(urdf_path))

model = mujoco.MjModel.from_xml_path(urdf_path)
data = mujoco.MjData(model)

with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running():
        mujoco.mj_step(model, data)