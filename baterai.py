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

# Cetak informasi baterai
print(f"Level Baterai: {level}%")
print(f"Status Baterai: {status}")
print(f"Kesehatan Baterai: {health}")
