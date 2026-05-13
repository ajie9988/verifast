# 📖 Panduan Penggunaan Verifast

Verifast adalah library Python sederhana namun kuat untuk memvalidasi nomor telepon dan email lintas negara. Library ini didesain untuk mudah digunakan dan mudah diperluas.

## 🚀 Instalasi

Untuk saat ini, Anda dapat menginstal library ini secara lokal dari folder proyek:

```bash
pip install -e .
```

---

## 📞 Validasi Nomor Telepon

Verifast menggunakan aturan spesifik per negara untuk memastikan nomor telepon valid dan berada dalam format yang benar.

### 1. Validasi Dasar
Fungsi `validate_phone` mengembalikan tuple `(is_valid, result)`. Jika valid, `result` adalah nomor yang sudah dinormalisasi. Jika tidak valid, `result` adalah pesan error.

```python
from verifast import validate_phone

# Validasi nomor Indonesia
is_valid, result = validate_phone("08123456789", "id")
if is_valid:
    print(f"Valid! Format internasional: {result}")
else:
    print(f"Gagal: {result}")
```

### 2. Normalisasi Saja
Jika Anda hanya ingin mengubah format lokal ke internasional tanpa validasi ketat:

```python
from verifast import normalize_phone

# Mengubah 0812... menjadi +62812...
normalized = normalize_phone("08123456789", "id")
print(normalized) # +628123456789
```

### 3. Cek Negara yang Didukung
```python
from verifast import get_supported_countries

print(get_supported_countries()) # ['id', 'us', 'in', 'cn', 'de']
```

---

## 📧 Validasi Email

### 1. Validasi Standar
```python
from verifast import validate_email

is_valid, result = validate_email("user@example.com")
```

### 2. Memblokir Email Sekali Pakai (Disposable)
Gunakan opsi `block_disposable=True` untuk menolak email dari penyedia seperti `tempmail.com`.

```python
is_valid, result = validate_email("test@tempmail.com", block_disposable=True)
if not is_valid:
    print("Email ini tidak diperbolehkan!")
```

---

## 🛠 Menambah Dukungan Negara Baru

Anda bisa menambah negara baru tanpa mengubah kode program. Cukup buat file JSON di folder `verifast/data/`.

Contoh `verifast/data/my.json` (Malaysia):
```json
{
    "country_name": "Malaysia",
    "country_code": "60",
    "phone_pattern": "^(\\+60|60|0)(1[0-9]{8,9})$",
    "example": "+60123456789",
    "min_length": 9,
    "max_length": 10
}
```

---

## 🧪 Menjalankan Unit Test

Kami menggunakan `pytest` untuk pengujian:

```bash
pytest tests/
```


## 📤 Return Values

Semua fungsi validasi mengembalikan **tuple** `(is_valid, result)`:

| Kondisi | `is_valid` | `result` |
|---------|------------|----------|
| Valid | `True` | Data yang sudah dinormalisasi |
| Tidak valid | `False` | Pesan error (string) |

### Contoh handling:
```python
is_valid, result = validate_phone("08123456789", "id")

if is_valid:
    # result berisi nomor yang sudah dinormalisasi
    send_otp(result)
else:
    # result berisi pesan error
    print(f"Error: {result}")

## 🔢 Versi & Perubahan (SemVer)

Proyek ini mengikuti [Semantic Versioning (SemVer)](https://semver.org/lang/id/). Format versi adalah `MAJOR.MINOR.PATCH`:

- **MAJOR**: Perubahan besar yang tidak kompatibel dengan versi sebelumnya (breaking changes).
- **MINOR**: Penambahan fitur baru yang tetap kompatibel dengan versi sebelumnya.
- **PATCH**: Perbaikan bug yang tetap kompatibel dengan versi sebelumnya.

Anda dapat mengecek versi library di dalam kode:
```python
import verifast
print(verifast.__version__)
```

Detail perubahan dapat dilihat di file [CHANGELOG.md](CHANGELOG.md).