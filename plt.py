import base64
import io
import matplotlib.pyplot as plt

plt.rcParams['axes.unicode_minus'] = False
plt.xlabel("used time")
plt.ylabel("failure time")
plt.xticks([])
plt.yticks([])
plt.show()
# 转为base64
buffer = io.BytesIO()
plt.savefig(buffer, format='png')
# 直接读取二进制，转换base64
base64_png = base64.b64encode(buffer.getvalue())

print(base64_png)