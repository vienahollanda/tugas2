## Tugas 2

### Viena Hollanda Koswara 
### 2106751253
### PBP A

#### - Link menuju ke [aplikasi katalog](https://tugas2viena.herokuapp.com/) yang telah dibuat.

### 1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`;

![User](https://user-images.githubusercontent.com/112618738/190313748-a0ba9c05-ed78-4c65-9091-f92463994b4e.png)


#### Untuk membuat sebuah request, langkah awal yang dilakukan adalah *user* akan membuat request ke *Django server*, setelah *middleware classes* memproses request yang dibuat, request akan diteruskan ke URL Router di `urls.py`. Ketika sudah mendapatkan *matching URL* berdasarkan request, *view function* atau fungsi yang sesuai di `views.py` yang bersesuaian akan dipanggil, dan jika fungsi ini sudah dieksekusi, waktunya untuk merespon request yang diberikan. Ketika responsnya adalah render, ia akan mencari HTML. Responsnya berisi HTML dan file statis lainnya yang akan diberikan ke *user*


### 2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
#### Kita menggunakan *virtual environment* untuk mengelola *Python packages* untuk setiap proyek yang berbeda agar menghindari adanya *package collision error* ketika kita meng-*install package* baru. Tanpa menggunakan *virtual environment* kita tetap bisa membuat aplikasi web berbasis Django.

### 3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
### - Membuat sebuah fungsi pada `views.py` yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.
#### Untuk bagian ini saya melakukan *import* terhadap class CatalogItem dari berkas `models.py`. Dalam berkas `views.py`, saya membuat sebuah fungsi dengan parameter request dan fungsi ini akan mengambil semua obyek data dari *instance* yang berada di class CatalogItem dan dimasukkan ke dalam sebuah variabel `context`. Fungsi yang ada di dalam `views.py` tersebut akan mengembalikan berkas `html` sesuai dengan data dari variable `context` dan `katalog.html`.


### - Membuat sebuah *routing* untuk memetakan fungsi yang telah kamu buat pada `views.py`
#### Di bagian ini, saya menambahkan *path url* yang bisa mengakses aplikasi yang dibuat di `urls.py` di folder `project_django`. Pada `urls.py` di folder `katalog`, saya melakukan *import* untuk fungsi yang sudah saya buat sebelumnya di `views.py`. Ketika *path url* yang baru saya buat untuk mengakses aplikasi ini diakses, fungsi yang sesuai pada `views.py` akan dipanggil dan mengembalikan respon yang diinginkan.


### - Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template.
#### Di bagian ketiga ini saya memodifikasi `Fill me!` dengan `{{nama}}` dan `{{NPM}}` yang berada di `katalog.html`. Lalu saya memasukkan beberapa data dari tabel yang berada di `models`. Dan data berhasil untuk dipetakan pada berkas `html`.


### - Melakukan *deployment* ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
#### Untuk melakukan ini, saya mengunggah file proyek Django yang telah diubah berdasarkan request yang diberikan ke *repository* yang telah saya buat sebelumya di Github dengan melakukan perintah `add`, `commit`, dan `push`.Lalu di Heroku, saya membuat aplikasi baru dengan nama `tugas2viena` dan menambahkan `HEROKU_APP_NAME` yang isinya nama dari aplikasi yang saya buat di Heroku dan `HEROKU_API_KEY` yang isinya API key dari akun saya pada `secrets`.Setelah melakukan langkah-langkah di atas, saya melakukan *deploy* kembali dengan menekan `re-run all jobs` pada *repository* yang sesuai di Github.


#### Dan aplikasi yang sudah saya buat bisa diakses melalui [tautan ini](https://tugas2viena.herokuapp.com/)


