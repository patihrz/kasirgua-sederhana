# Modern GUI version using customtkinter
import customtkinter as ctk
from tkinter import messagebox

# Inisialisasi
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("🧾 Kasir Toko Sembako - Modern UI")
app.geometry("600x600")

barang_data = {}
keranjang = []

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
        entry_nama_barang.delete(0, ctk.END)
        entry_harga_barang.delete(0, ctk.END)
    else:
        messagebox.showerror("Error", "Isi nama dan harga dengan benar!")

def update_combobox():
    combo_barang.configure(values=list(barang_data.keys()))

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
        listbox_keranjang.insert("end", f"{barang} x{jumlah} - Rp{total}")
        entry_jumlah.delete(0, ctk.END)

def cetak_struk():
    if not keranjang:
        messagebox.showinfo("Kosong", "Keranjang masih kosong!")
        return
    total_belanja = sum(item[3] for item in keranjang)
    struk = "--- STRUK BELANJA ---\n"
    for barang, harga, jumlah, total in keranjang:
        struk += f"{barang} ({jumlah} x {harga}) = Rp{total}\n"
    struk += f"\nTotal Bayar: Rp{total_belanja}\n"
    messagebox.showinfo("Struk Belanja", struk)

def reset_transaksi():
    keranjang.clear()
    listbox_keranjang.delete(0, "end")

# Frame Tambah Barang
frame_barang = ctk.CTkFrame(app)
frame_barang.pack(pady=10, padx=10, fill="x")

ctk.CTkLabel(frame_barang, text="Tambah Barang Baru", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=5)
entry_nama_barang = ctk.CTkEntry(frame_barang, placeholder_text="Nama Barang")
entry_nama_barang.pack(padx=10, pady=5)
entry_harga_barang = ctk.CTkEntry(frame_barang, placeholder_text="Harga (Rp)")
entry_harga_barang.pack(padx=10, pady=5)
btn_tambah = ctk.CTkButton(frame_barang, text="Tambah Barang", command=tambah_barang)
btn_tambah.pack(pady=5)

# Frame Transaksi
frame_transaksi = ctk.CTkFrame(app)
frame_transaksi.pack(pady=10, padx=10, fill="x")

ctk.CTkLabel(frame_transaksi, text="Transaksi", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=5)
combo_barang = ctk.CTkComboBox(frame_transaksi, values=[])
combo_barang.pack(pady=5)
entry_jumlah = ctk.CTkEntry(frame_transaksi, placeholder_text="Jumlah")
entry_jumlah.pack(pady=5)
btn_keranjang = ctk.CTkButton(frame_transaksi, text="Tambah ke Keranjang", command=tambah_ke_keranjang)
btn_keranjang.pack(pady=5)

# Keranjang
ctk.CTkLabel(app, text="🛒 Keranjang Belanja", font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)
listbox_keranjang = ctk.CTkTextbox(app, width=500, height=150)
listbox_keranjang.pack(pady=5)

# Tombol Aksi
frame_aksi = ctk.CTkFrame(app)
frame_aksi.pack(pady=10)

btn_cetak = ctk.CTkButton(frame_aksi, text="🧾 Cetak Struk", command=cetak_struk)
btn_cetak.grid(row=0, column=0, padx=10)
btn_reset = ctk.CTkButton(frame_aksi, text="🔁 Reset", command=reset_transaksi)
btn_reset.grid(row=0, column=1, padx=10)

app.mainloop()

