import subprocess

# Jalankan perintah ADB untuk mendapatkan informasi baterai
output = subprocess.check_output(["adb", "shell", "dumpsys", "battery"]).decode().strip()

# Cari baris dengan persentase baterai
level = [line for line in output.split('\n') if 'level' in line][0]
level = int(level.split(':')[1].strip())

# Cari baris dengan status baterai
status = [line for line in output.split('\n') if 'status' in line][0]
status = status.split(':')[1].strip()

# Cari baris dengan kesehatan baterai
health = [line for line in output.split('\n') if 'health' in line][0]
health = health.split(':')[1].strip()

# Cari baris dengan kapasitas baterai saat ini
capacity = [line for line in output.split('\n') if 'capacity' in line][0]
capacity = int(capacity.split(':')[1].strip())

# Cari baris dengan tegangan baterai
voltage = [line for line in output.split('\n') if 'voltage' in line][0]
voltage = int(voltage.split(':')[1].strip())

# Cari baris dengan suhu baterai
temperature = [line for line in output.split('\n') if 'temperature' in line][0]
temperature = float(temperature.split(':')[1].strip()) / 10.0

# Cetak informasi baterai
print(f"Level Baterai: {level}%")
print(f"Status Baterai: {status}")
print(f"Kesehatan Baterai: {health}")
print(f"Kapasitas Baterai Saat Ini: {capacity} mAh")
print(f"Tegangan Baterai: {voltage / 1000.0} V")
print(f"Suhu Baterai: {temperature} °C")
