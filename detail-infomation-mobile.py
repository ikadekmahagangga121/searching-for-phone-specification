import subprocess

# Jalankan perintah ADB untuk mendapatkan informasi perangkat
output = subprocess.check_output(["adb", "shell", "getprop"]).decode().strip()

# Cari baris dengan nama perangkat
device_name = [line for line in output.split('\n') if 'ro.product.model' in line][0]
device_name = device_name.split(':')[1].strip()

# Cari baris dengan nama produsen
manufacturer = [line for line in output.split('\n') if 'ro.product.manufacturer' in line][0]
manufacturer = manufacturer.split(':')[1].strip()

# Cari baris dengan versi Android
android_version = [line for line in output.split('\n') if 'ro.build.version.release' in line][0]
android_version = android_version.split(':')[1].strip()

# Cari baris dengan resolusi layar
display_resolution = [line for line in output.split('\n') if 'ro.sf.lcd_density' in line][0]
display_resolution = display_resolution.split(':')[1].strip()

# Cari baris dengan ukuran layar
display_size = [line for line in output.split('\n') if 'ro.product.display_size' in line][0]
display_size = display_size.split(':')[1].strip()

# Cari baris dengan jumlah memori RAM
ram_size = [line for line in output.split('\n') if 'ro.product.ram' in line][0]
ram_size = ram_size.split(':')[1].strip()

# Cari baris dengan jumlah memori internal
storage_size = [line for line in output.split('\n') if 'ro.product.internal' in line][0]
storage_size = storage_size.split(':')[1].strip()

# Cetak informasi perangkat
print(f"Nama Perangkat: {device_name}")
print(f"Produsen: {manufacturer}")
print(f"Versi Android: {android_version}")
print(f"Resolusi Layar: {display_resolution}")
print(f"Ukuran Layar: {display_size}")
print(f"RAM: {ram_size}")
print(f"Memori Internal: {storage_size}")
