import psutil

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

if plugged:
    print("Baterai sedang diisi daya.")
else:
    print("Baterai tidak diisi daya.")

if percent <= 20:
    print(f"Kesehatan baterai saat ini adalah {percent}%, baterai perlu diisi segera.")
elif 20 < percent <= 50:
    print(f"Kesehatan baterai saat ini adalah {percent}%, baterai masih cukup.")
elif 50 < percent <= 80:
    print(f"Kesehatan baterai saat ini adalah {percent}%, baterai baik-baik saja.")
else:
    print(f"Kesehatan baterai saat ini adalah {percent}%, baterai sudah sangat sehat.")
