# import numpy as np #ใช้เป็น array เเทน เพื่อขยายไม่ได้
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression

# x = [1, 2, 3, 4, 5, 6, 7]
# y = [25, 30, 35, 40, 45, 50, 55]

# plt.scatter(x,y)

# model = LinearRegression()

# x = np.array(x)
# y = np.array(y)

# x = x.reshape(-1, 1)

# model.fit(x, y)


# import สำหรับ plot graph
import matplotlib.pyplot as plt

# 1. ข้อมูลราคา (mock data)
prices = [100, 102, 101, 105, 107, 110, 108]

# 2. function หา slope ของ linear trend แบบง่าย
def simple_linear_regression(y_values):
    n = len(y_values)
    x_values = list(range(n))  # ใช้ index แทนเวลา
    sum_x = 0
    sum_y = 0
    sum_xy = 0
    sum_x2 = 0
    
    for i in range(n):
        sum_x += x_values[i]
        sum_y += y_values[i]
        sum_xy += x_values[i] * y_values[i]
        sum_x2 += x_values[i] * x_values[i]
    
    # formula slope: m = (N*Σxy - Σx*Σy) / (N*Σx² - (Σx)²)
    numerator = n * sum_xy - sum_x * sum_y
    denominator = n * sum_x2 - sum_x * sum_x
    
    if denominator != 0:
        slope = numerator / denominator
    else:
        slope = 0  # ป้องกันหารด้วย 0
    
    return slope

# 3. ใช้ function หา slope
trend_slope = simple_linear_regression(prices)

# 4. ตัดสินแนวโน้ม
if trend_slope > 0:
    trend = "Uptrend"
elif trend_slope < 0:
    trend = "Downtrend"
else:
    trend = "No trend"

print("Slope:", trend_slope)
print("Trend:", trend)

# 5. plot graph
plt.plot(prices, marker='o', label='Price')
plt.title("Stock Price Trend")
plt.xlabel("Time")
plt.ylabel("Price")
plt.grid(True)
plt.legend()
plt.show()
