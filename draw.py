# 导入库
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 读取数据
data = pd.read_excel('data.xlsx')


# 数据计算
# radius为要绘制的扇形半径，即plt.bar()的参数height
# 64为中心空心圆环的半径，需要减去
radius = data['长度'] - 64
# n为扇形个数，即国家数，本例中为33，在分别求左右半圆的个数时会用到
n = radius.count()

# 判断n的奇偶性
# 本例中n为奇数，为使此绘图脚本更具通用性，应针对n的奇偶性分别判断，此处略
# 本例中含有33个国家，33为奇数，为了制图美观，使得左半圆和右半圆之间刚好被一条垂直直线平分，
# 将左半圆放置前16个国家，右半圆放置后17个国家，即int(n/2)和int(n/2)+1。
# 如果n为偶数，则左半圆和右半圆扇形数量相同，直接n/2即可。

# 取radius前一半的数据，即前16个国家的扇形半径
radius1 = radius[:int(n/2)]
# 取radius后一半的数据，即后17个国家的扇形半径
radius2 = radius[int(n/2):]

# theta为每个扇形的起始角度，即plt.bar()的参数x，x坐标(极坐标下即为扇形的起始角度)
# 左半圆每个扇形的起始角度，即把左半圆的pi分成16份，从0到pi，间隔pi/16
theta1 = np.arange(0, np.pi, np.pi / int(n/2))
# 右半圆每个扇形的起始角度，先把右半圆的pi分成17份，位置从0到pi，间隔pi/17，再加上左半圆的角度偏移pi，即从pi到2pi，间隔pi/17
theta2 = np.arange(0, np.pi, np.pi / (int(n/2)+1)) + np.pi

# width为每个扇形的宽度，即plt.bar()的参数width(极坐标下即为扇形的角度)
# 左半圆每个扇形的角度，即把pi分成16份
width1 = np.pi / int(n/2)
# 右半圆每个扇形的角度，即把pi分成17份
width2 = np.pi / (int(n/2)+1)

# color 为每个扇形的填充颜色，从人民日报原图中取色得到
color = data['颜色']
# 左半圆每个扇形的颜色值，即color中第1个到第16个值
color1 = color[:int(n/2)]
# 右半圆每个扇形的颜色值，即color中第17个到第33个值
color2 = color[int(n/2):]


# 绘制扇形
# 设置画布大小和分辨率
# 画布大小单位为英寸，1英寸=2.54厘米；分辨率若用于打印则为300，屏幕显示则为72
fig = plt.figure(figsize=(30, 30), dpi=300)

# 启用极坐标
ax = fig.add_subplot(projection='polar')
# 设置极坐标0°位置为'N'
ax.set_theta_zero_location('N')

# 绘制左半圆
ax.bar(x=theta1, height=radius1, width=width1,
       color=color1, edgecolor=color1, linewidth=0.15,
       align='edge', bottom=64)

# 绘制右半圆
ax.bar(x=theta2, height=radius2, width=width2,
       color=color2, edgecolor=color2, linewidth=0.15,
       align='edge', bottom=64)
# 参数解释：
# edgecolor: 用填充形状的颜色作为边框颜色
# linewidth: 设置边框宽度。如果不画边框，扇形会出现白边
# align: 从指定角度开始绘图。设置为'edge'可从0度开始(默认值'center’会居中)
# bottom: 条形的起始位置，也是y轴的起始坐标，即中心空心圆环的半径

# 绘制中心的两个半透明圆
# 内圆起始角度为0，角度2pi，半径122，白色，透明度0.15(内圆的透明度会叠加外圆的透明度)
ax.bar(x=0, height=122, width=2*np.pi,
       color='white', alpha=0.15)
# 外圆起始角度为0，角度2pi，半径162，白色，透明度0.1
ax.bar(x=0, height=162, width=2*np.pi,
       color='white', alpha=0.1)


# 显示图形
# 关闭边框显示
plt.axis('off')
# 当画布尺寸较大时，可关闭显示图形，直接输出png图片，否则无响应
# plt.show()

# 保存图片
# transparent参数可生成背景透明的png
plt.savefig('COVID-19.png', transparent=True)
