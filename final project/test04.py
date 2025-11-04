# ✅ 1) ข้อมูลตัวอย่าง (คุณกรอกเองได้เลย)
# ตัวอย่าง: ราคาปิด Close ของย้อนหลัง 7 วัน
prices = [150, 152, 151, 153, 155, 156, 158]  # <-- คุณแก้ตรงนี้ได้เลย

# ✅ 2) สร้าง X = 1, 2, 3, ... จากจำนวนวันที่มีข้อมูล
days = list(range(1, len(prices) + 1))

# ✅ 3) คำนวณค่า a และ b ด้วยสูตร Linear Regression
n = len(days)
sum_x = sum(days)
sum_y = sum(prices)
sum_xy = sum([x*y for x, y in zip(days, prices)])
sum_x2 = sum([x**2 for x in days])

# slope (b) และ intercept (a)
b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
a = (sum_y - b * sum_x) / n

print("ค่าคงที่ a =", a)
print("ความชัน b =", b)

# ✅ 4) ทำนายราคาวันถัดไป
next_day = n + 1
predicted_price = a + b * next_day
print("⛅ ราคาที่ทำนายวันถัดไป =", predicted_price)

# ✅ 5) วาดกราฟจริง + เส้นแนวโน้ม
import matplotlib.pyplot as plt

# สร้างเส้นตรงจาก a + b*x
trend_line = [a + b * x for x in days]

plt.plot(days, prices, marker='o', label='Actual Price')        # จุดจริง
plt.plot(days, trend_line, label='Linear Regression Line')      # เส้นทำนาย
plt.scatter(next_day, predicted_price, color='red', label='Next Day Prediction')  # จุดทำนาย

plt.xlabel('Day (Time)')
plt.ylabel('Stock Price')
plt.title('Stock Price Prediction with Linear Regression')
plt.legend()
plt.show()
