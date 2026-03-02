import re
from collections import defaultdict

def fix_urdf(input_path, output_path):
    with open(input_path, 'r') as f:
        content = f.read()

    # Fix duplicate link names
    name_counts = defaultdict(int)
    name_seen = defaultdict(int)
    for match in re.finditer(r'<link name="([^"]+)"', content):
        name_counts[match.group(1)] += 1

    def replace_link(match):
        name = match.group(1)
        if name_counts[name] > 1:
            new_name = f"{name}_{name_seen[name]:03d}"
            name_seen[name] += 1
            return f'<link name="{new_name}"'
        return match.group(0)

    content = re.sub(r'<link name="([^"]+)"', replace_link, content)

    # Fix duplicate visual/collision geom names
    geom_counts = defaultdict(int)
    geom_seen = defaultdict(int)
    for match in re.finditer(r'(?<=name=")([^"]+_(?:visual|collision))(?=")', content):
        geom_counts[match.group(1)] += 1

    def replace_geom(match):
        name = match.group(1)
        if geom_counts.get(name, 0) > 1:
            new_name = f"{name}_{geom_seen[name]:03d}"
            geom_seen[name] += 1
            return new_name
        return name

    content = re.sub(r'(?<=name=")([^"]+_(?:visual|collision))(?=")', replace_geom, content)

    with open(output_path, 'w') as f:
        f.write(content)

    print("Fixed duplicate link and geom names.")

fix_urdf("/home/mailroom/trossen_arm_mujoco/jony_sofi/Gazebo/JONY_SOFI/JONY_SOFI.urdf", 
         "/home/mailroom/trossen_arm_mujoco/jony_sofi/Gazebo/JONY_SOFI/JONY_SOFI_fixed.urdf")