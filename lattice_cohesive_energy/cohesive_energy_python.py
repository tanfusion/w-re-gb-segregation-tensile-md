# 计算金属内聚能随晶格常数变化曲线
# 自动调用lammps脚本，计算
import numpy as np
import subprocess
import re
import random
import matplotlib
matplotlib.use('TkAgg')  # 设置后端为 'Agg'
import matplotlib.pyplot as plt

# 晶格常数计算范围
lattice_constants = np.arange(3, 3.5, 0.01)
cohesive_energies = []

# === 打开输出文件 ===
output_file = "cohesive_energy_data.txt"
with open(output_file, 'w', encoding='utf-8') as f:
    f.write("# Lattice_Constant(Angstrom)\tCohesive_Energy(eV)\n")  # 写入表头

for lattice_constant in lattice_constants:
    random_number = 12345  # random.randint(1,1000)
    command_line = f'lmp -var latconst {lattice_constant} -var seed {random_number} < in.cohesive_energy.txt'
    subprocess.run(command_line, shell=True)

    energy_value = None
    with open('log.lammps', 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith('%%'):
                energy_match = re.search(r'(?<=ecoh = )-?\d+\.\d+', line)
                if energy_match:
                    energy_value = float(energy_match.group())
                    cohesive_energies.append(energy_value)
                    # === 写入数据到文件 ===
                    with open(output_file, 'a') as f:
                        f.write(f"{lattice_constant:.5f}\t{energy_value:.8f}\n")
                    break

# 绘制晶格常数和内聚能的关系图
plt.plot(lattice_constants, cohesive_energies, '-*r')
plt.xlabel('Lattice Constant')
plt.ylabel('Cohesive Energy')
plt.title('Lattice Constant and Cohesive Energy')
plt.grid(True)

# 找到最小内聚能对应的晶格常数
min_energy_index = np.argmin(cohesive_energies)
stable_latconst = lattice_constants[min_energy_index]
stable_cohenergy = cohesive_energies[min_energy_index]

# 在图形的右上角添加文本标签
plt.legend([f'stable_cohenergy = {stable_cohenergy:.2f}\nstable_latconst = {stable_latconst:.2f}'], loc='upper right')

plt.savefig('cohesive_energy_plot.png')  # 将图形保存为文件
plt.show()

# === 在数据文件中末尾添加稳定点信息 ===
with open(output_file, 'a', encoding='utf-8') as f:
    f.write("\n# ===== 稳定点信息 =====\n")
    f.write(f"# 最小内聚能: {stable_cohenergy:.6f} eV\n")
    f.write(f"# 对应晶格常数: {stable_latconst:.6f} Å\n")

#  在屏幕上输出最小内聚能和对应的晶格常数
print('=======================================')
print(f'stable_cohenergy = {stable_cohenergy}')
print(f'stable_latconst = {stable_latconst}')
print(f"数据已保存至: {output_file}")