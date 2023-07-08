import psutil

battery = psutil.sensors_battery()

print(f"Status: {battery.power_plugged}")
print(f"Persentase Kesehatan: {battery.percent}%")
print(f"Waktu Penuh: {battery.secsleft / 3600:.2f} jam")
print(f"Kapasitas Maksimum: {battery.max:.2f} Wh")
print(f"Kapasitas Saat Ini: {battery.current:.2f} Wh")
