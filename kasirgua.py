import tkinter as tk
from tkinter import messagebox, ttk

# Data barang disimpan dalam dict (nama: harga)
barang_data = {}

# Data keranjang belanja (list of tuple)
keranjang = []

# Fungsi tambah barang ke daftar
def tambah_barang():
    nama = entry_nama_barang.get()
    try:
        harga = int(entry_harga_barang.get())
    except ValueError:
        messagebox.showerror("Error", "Harga harus berupa angka!")
        return
    if nama and harga > 0:
        barang_data[nama] = harga
        update_combobox()
        entry_nama_barang.delete(0, tk.END)
        entry_harga_barang.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Isi nama dan harga dengan benar!")

# Update dropdown barang
def update_combobox():
    combo_barang['values'] = list(barang_data.keys())

# Tambah ke keranjang
def tambah_ke_keranjang():
    barang = combo_barang.get()
    if not barang or barang not in barang_data:
        messagebox.showwarning("Pilih Barang", "Pilih barang dari daftar!")
        return
    try:
        jumlah = int(entry_jumlah.get())
    except ValueError:
        messagebox.showerror("Error", "Jumlah harus angka!")
        return
    if jumlah > 0:
        harga = barang_data[barang]
        total = harga * jumlah
        keranjang.append((barang, harga, jumlah, total))
        listbox_keranjang.insert(tk.END, f"{barang} x{jumlah} - Rp{total}")
        entry_jumlah.delete(0, tk.END)

# Cetak struk
def cetak_struk():
    if not keranjang:
        messagebox.showinfo("Kosong", "Keranjang masih kosong!")
        return
    total_belanja = sum(item[3] for item in keranjang)
    struk = "\n--- STRUK BELANJA ---\n"
    for barang, harga, jumlah, total in keranjang:
        struk += f"{barang} ({jumlah} x {harga}) = Rp{total}\n"
    struk += f"\nTotal Bayar: Rp{total_belanja}\n"
    messagebox.showinfo("Struk Belanja", struk)

# Reset transaksi
def reset_transaksi():
    keranjang.clear()
    listbox_keranjang.delete(0, tk.END)

# GUI
root = tk.Tk()
root.title("Aplikasi Kasir - Toko Sembako")

# Frame tambah barang
frame_tambah = tk.LabelFrame(root, text="Tambah Barang Baru")
frame_tambah.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

tk.Label(frame_tambah, text="Nama Barang:").grid(row=0, column=0)
entry_nama_barang = tk.Entry(frame_tambah)
entry_nama_barang.grid(row=0, column=1)

tk.Label(frame_tambah, text="Harga (Rp):").grid(row=1, column=0)
entry_harga_barang = tk.Entry(frame_tambah)
entry_harga_barang.grid(row=1, column=1)

btn_tambah_barang = tk.Button(frame_tambah, text="Tambah Barang", command=tambah_barang)
btn_tambah_barang.grid(row=2, column=0, columnspan=2, pady=5)

# Frame transaksi
frame_transaksi = tk.LabelFrame(root, text="Transaksi")
frame_transaksi.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

tk.Label(frame_transaksi, text="Pilih Barang:").grid(row=0, column=0)
combo_barang = ttk.Combobox(frame_transaksi, state="readonly")
combo_barang.grid(row=0, column=1)

tk.Label(frame_transaksi, text="Jumlah:").grid(row=1, column=0)
entry_jumlah = tk.Entry(frame_transaksi)
entry_jumlah.grid(row=1, column=1)

btn_tambah_keranjang = tk.Button(frame_transaksi, text="Tambah ke Keranjang", command=tambah_ke_keranjang)
btn_tambah_keranjang.grid(row=2, column=0, columnspan=2, pady=5)

# Keranjang
listbox_keranjang = tk.Listbox(root, width=40)
listbox_keranjang.grid(row=2, column=0, padx=10, pady=10)

# Tombol aksi
frame_aksi = tk.Frame(root)
frame_aksi.grid(row=3, column=0, pady=10)

btn_struk = tk.Button(frame_aksi, text="🧾 Cetak Struk", command=cetak_struk)
btn_struk.grid(row=0, column=0, padx=5)

btn_reset = tk.Button(frame_aksi, text="🔁 Reset", command=reset_transaksi)
btn_reset.grid(row=0, column=1, padx=5)

root.mainloop()

