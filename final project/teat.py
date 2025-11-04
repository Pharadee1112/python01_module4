# ===============================
# Linear Regression หุ้นไทย - ใช้ได้จริง
# ===============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import yfinance as yf

# ===============================
# 🔹 เลือกแหล่งข้อมูล
# ===============================
use_api = True  # True = ดึงจาก API, False = ใช้ไฟล์ CSV
symbol = "PTT.BK"  # รหัสหุ้นไทย เช่น PTT.BK, AOT.BK, CPALL.BK

if use_api:
    data = yf.download(symbol, start="2023-01-01", end="2025-01-01")
else:
    data = pd.read_csv("PTT_data.csv")  # ไฟล์ CSV ที่ดาวน์โหลดจาก SET
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)

# ===============================
# 🔹 เตรียมข้อมูล
# ===============================
data['Day'] = np.arange(len(data))          # ตัวแปรอิสระ = วัน
X = data[['Day']]                           # Feature
y = data['Close']                           # Target

# ===============================
# 🔹 สร้างและฝึกโมเดล Linear Regression
# ===============================
model = LinearRegression()
model.fit(X, y)

# ===============================
# 🔹 ทำนายค่าและเก็บใน DataFrame
# ===============================
data['Predicted'] = model.predict(X)

# ===============================
# 🔹 ประเมินโมเดล
# ===============================
mse = mean_squared_error(y, data['Predicted'])
r2 = r2_score(y, data['Predicted'])
print(f"Mean Squared Error: {mse:.2f}")
print(f"R2 Score: {r2:.2f}")

# ===============================
# 🔹 แสดงกราฟ
# ===============================
plt.figure(figsize=(12,6))
sns.lineplot(data=data, x='Date', y='Close', label='Actual Price')
sns.lineplot(data=data, x='Date', y='Predicted', label='Predicted Trend', color='red')
plt.title(f"{symbol} Stock Price Trend Prediction")
plt.xlabel("Date")
plt.ylabel("Price (THB)")
plt.legend()
plt.show()
# ===============================
# Linear Regression หุ้นไทย - ใช้ได้จริง
# ===============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import yfinance as yf

# ===============================
# 🔹 เลือกแหล่งข้อมูล
# ===============================
use_api = True  # True = ดึงจาก API, False = ใช้ไฟล์ CSV
symbol = "PTT.BK"  # รหัสหุ้นไทย เช่น PTT.BK, AOT.BK, CPALL.BK

if use_api:
    data = yf.download(symbol, start="2023-01-01", end="2025-01-01")
else:
    data = pd.read_csv("PTT_data.csv")  # ไฟล์ CSV ที่ดาวน์โหลดจาก SET
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)

# ===============================
# 🔹 เตรียมข้อมูล
# ===============================
data['Day'] = np.arange(len(data))          # ตัวแปรอิสระ = วัน
X = data[['Day']]                           # Feature
y = data['Close']                           # Target

# ===============================
# 🔹 สร้างและฝึกโมเดล Linear Regression
# ===============================
model = LinearRegression()
model.fit(X, y)

# ===============================
# 🔹 ทำนายค่าและเก็บใน DataFrame
# ===============================
data['Predicted'] = model.predict(X)

# ===============================
# 🔹 ประเมินโมเดล
# ===============================
mse = mean_squared_error(y, data['Predicted'])
r2 = r2_score(y, data['Predicted'])
print(f"Mean Squared Error: {mse:.2f}")
print(f"R2 Score: {r2:.2f}")

# ===============================
# 🔹 แสดงกราฟ
# ===============================
plt.figure(figsize=(12,6))
sns.lineplot(data=data, x='Date', y='Close', label='Actual Price')
sns.lineplot(data=data, x='Date', y='Predicted', label='Predicted Trend', color='red')
plt.title(f"{symbol} Stock Price Trend Prediction")
plt.xlabel("Date")
plt.ylabel("Price (THB)")
plt.legend()
plt.show()
