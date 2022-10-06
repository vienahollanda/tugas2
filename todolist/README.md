# Tugas 4

## Viena Hollanda Koswara
## 2106751253
## PBP A

### 1. Apa kegunaan `{% csrf_token %}` pada elemen `<form>?` Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>?`
#### CSRF adalah singkatan dari *Cross Site Request Forgery* yang merupakan sebuah serangan eksploitasi web yang membuat pengguna tanpa sadar mengirimkan suatu *request* ke website yang sedang digunakan saat itu, tapi seringkali pengguna tidak sadar bila serangan ini terjadi. CSRF Token dapat mencegah hal ini terjadi yang membuat pelaku tidak mungkin bisa melakukan permintaan HTTP yang secara sepenuhnya cocok untuk diumpankan ke pengguna karena `{% csrf_token %}` membuat sebuah nilai token pada server ketika melakukan *rendering* sebuah halaman dan memastikan untuk melakukan pengecekan kembali terhadap token ini ketika ada *request* yang dilakukan. Hal ini membuat pelaku tidak dapat memprediksi nilai dari token CSRF pengguna sehingga *request* dengan semua parameter yang diperlukan aplikasi untuk memenuhi *request* tersebut tidak dapat dibuat. Jika kita tidak menggunakan kode tersebut, maka akan muncul *error* ketika ingin melakukan *submit* pada `form` karena nilai CSRF Token pada `server` berbeda dengan yang dimiliki oleh `form`.
 
### 2. Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan *generator* seperti `{{ form.as_table }})`? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.
#### Betul, kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan *generator* seperti `{{ form.as_table }})` dengan cara menggunakan tag dasar. Sebuah form dalam berkas HTML harus berada di dalam tag form, yang diawali dengan `<form>` dan diakhiri dengan `</form>`. Tag ini memiliki beberapa atribut, yaitu `action` dan `method`. `action` berfungsi untuk menjelaskan kemana data form akan dikirimkan, dan `method` berfungsi untuk menjelaskan bagaimana data isian dari form akan dikirim oleh *web browser*. Nilai dari `method` bisa berupa `get` atau `post`. jika kita mengisi atribut tersebut dengan `get`, maka isian form akan terlihat pada *url browser*, `post` biasanya digunakan untuk data yang lebih sensitif dan level privasi yang tinggi, seperti *password*.
#### Adapun tag lainnya yang digunakan, yaitu `tag<input>`, `tag<textarea>`, dan `tag<select>`. Setiap tag input di dalam form harus ditambahkan atribut name yang menjadi *variable form* agar dapat diproses oleh *web server*.
  
### 3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
#### User akan melakukan input data di form yang tertera di berkas create-task.html. Ketika `title` dan `description` sudah diisi pada form dan user memencet tombol `Tambah Task`, request dalam bentuk POST akan dikirimkan dan juga isi dari formnya. Jika isi data di form valid, maka akan diambil isi dari `title` dan `description`. Setelah itu, akan dibuat data baru buat dimasukkan ke database dengan input field-fieldnya merupakan sesuatu yang diisi oleh user, `description` dan `title` berdasarkan apa yang diisi di form oleh user, dan tanggalnya adalah tanggal ketika task itu pertama kali dibuat. Sesudah data ditambahkan ke dalam database, maka akan ditampilkan di berkas todolist.html, tapi task yang ditampilkan ini merupakan task yang dimiliki oleh seorang user yang sedang melakukan `log in`, bukan semua task dari semua user.
  
### 4.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
#### a. Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.
##### Untuk bagian registrasi, dilakukan import untuk `UserCreationForm` yang akan membuat user, fungsi `messages`untuk memberikan pesan, dan fungsi `redirect` untuk melakukan pengarahan ulang halaman. Kemudian, membuat fungsi `register` dalam views.py yang nantinya fungsi ini akan membuat formulir registrasi dan menghasilkan akun user yang baru selesai dibuat. Setelah itu, membuat berkas HTML di folder `templates` milik `todolist` dengan nama `register.html`. Lalu, melakukan routing di urls.py milik `todolist` sehingga ketika kita memasukkan link untuk mengakses aplikasi `todolist`, fungsi registrasi akan dipanggil yang akan menampilkan halaman registrasi.
##### Untuk bagian login, dilakukan import authenticate untuk memproses username dan password ketika user melakukan login, dan juga import login untuk menjalankan proses login di views.py. Dan membuat fungsi dengan nama `login_user` untuk *handle* eksekusi yang akan dilakukan ketika user melakukan *log in*. Setelah itu, membuat berkas HTML dengan nama login.html pada folder templates milik todolist. Lalu, melakukan routing di urls.py milik todolist supaya ketika kita memasukkan link untuk mengakses aplikasi `todolist` akan memanggil fungsi login akan dipanggil yang akan menampilkan halaman login.
##### Untuk bagian logout , dilakukan import fungsi logout dan membuat fungsi dengan nama `logout_user` di views.py. Dan tambahkan tombol `logout`ke dalam todolist.html. Lalu, melakukan routing di urls.py milik todolist supaya ketika kita memasukkan link untuk mengakses aplikasi `todolist` akan memanggil fungsi logout yang akan melakukan proses logout user dari akun yang dimilikinya.

#### b. Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.
##### Di bagian ini, dibuat fungsi di dalam views.py yang akan melakukan render pada halaman utama. Di fungsi ini, dibuat variabel context yang akan melakukan passing data task yang berhubungan dengan user, username dari user, dan data dari tanggal terakhir user melakukan login. Lalu, membuat berkas todolist.html yang akan menampilkan field-field yang diinginkan.

#### c. Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task.

  
### Akses menuju aplikasi `todolist` ada [di sini.](https://tugas2viena.herokuapp.com/todolist/login/)
 
 
### Tugas 5

#### 1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
##### Inline CSS adalah kode CSS yang ditulis langsung pada atribut elemen HTML. Setiap elemen HTML memiliki atribut style, di situ lah inline CSS ditulis.  Inline CSS digunakan hanya untuk mengubah satu elemen saja. Kekurangan: cara ini kurang efisien karena hanya bisa diterapkan pada satu elemen HTML sehingga kurang cocok untuk website dengan baris coding yang banyak. Kelebihan: memudahkan dalam perbaikan atribut HTML, membantu saat pengujian dan melihat perubahan pada satu elemen saja.

##### Kode CSS akan ditulis di dalam tag <style> lokasinya berada pada bagian atas header file HTML. Internal CSS dapat digunakan untuk membuat tampilan pada satu halaman website dan tidak digunakan pada halaman website yang lain. Perubahan pada Internal CSS hanya berlaku pada satu halaman saja. Kekurangan: performa website menjadi lebih lambat karena setiap halaman memiliki CSS sendiri, kurang efisien jika ingin digunakan di beberapa halaman website yang sama karena kode harus dituliskan ulang di setiap halaman, dan ukuran file menjadi lebih besar karena setiap halaman memiliki CSS sendiri. Kelebihan: mudah dalam melakukan editing tiap halaman website, tidak perlu melakukan upload file CSS karena masuk dalam file HTML, dan mudah saat memperbaiki error pada CSS website.

 ##### Eksternal CSS adalah kode CSS yang ditulis secara terpisah dengan kode HTML, kodenya ditulis di dalam file khusus yang berekstensi .css. Dan ada dua cara untuk menghubungkan file yang berisi kode CSS dengan HTML, yaitu dengan menggunakan <link> (biasa dituliskan pada bagian <head>, jadi setiap halaman website dilakukan pemanggilan file .css.) atau @import. File CSS dapat digunakan di beberapa halaman website sekaligus, jadi perubahan yang dilakukan akan terlihat tidak hanya di satu halaman saja. Kelebihan: ukuran file HTML menjadi lebih kecil, penulisan kode HTML menjadi lebih rapi, melakukan loading website menjadi lebih cepat, dan file CSS bisa digunakan untuk beberapa halaman website berbeda. Kekurangan: tidak cocok untuk halaman website yang membutuhkan halaman custom dan halaman website rawan berantakan saat file CSS gagal load dengan sempurna sehingga tampilan website juga berantakan.

 #### 2. Jelaskan tag HTML5 yang kamu ketahui.
 ##### <nav> untuk mendefinisikan navigasi pada halaman.
 ##### <!DOCTYPE html> untuk mendeklarasikan tipe dari dokumen yang akan dibuat kepada browser.
 ##### <figure> untuk mendefinisikan gambar yang ada pada artikel
 ##### <canvas> Elemen ini memberi ruang gambar dalam JavaScript di halaman web. 
 ##### <video> yang berfungsi untuk menambahkan video ke halaman web.
 ##### <audio> yang berfungsi untuk menambahkan audio ke halaman web.
 
 #### 3. Jelaskan tipe-tipe CSS selector yang kamu ketahui.
 ##### Type Selector - Selektor ini akan memilih elemen berdasarkan nama tag.
 ##### Class Selector - Selektor class adalah selektor yang memilih elemen berdasarkan nama class yang diberikan. Selektor class dibuat dengan tanda titik        di depannya pada file CSS.
 ##### ID Selector - Selektor ID penerapannya hampir sama dengan Class Selector. Bedanya, ID bersifat unik karena hanya boleh digunakan oleh satu elemen          saja. Selektor ID ditandai dengan tanda pagar (#) di depannya saat menulikannya di kode CSS.
 ##### Attribute Selector - Selektor atribut adalah selektor yang memilik elemen berdasarkan atribut. Selektor ini hampir sama seperti selektor Tag.
 ##### Universal Selectors - Selektor ini digunakan untuk memilih setiap single element dari tipe element apapun. Artinya, penyeleksian berlaku secara      keseluruhan untuk semua single element. Penggunaan Universal Selector pada kode CSS ditandai dengan karakter arterisk (*) yang dapat digunakan secara berdiri sendiri ataupun digabungkan dengan tipe selektor lainnya, tergantung kebutuhan.

 #### 4. Kustomisasi templat (login, register, create-task)
 ##### Langkah pertama, saya menambahkan 2 barisan kode pada aplikasi todolist supaya komponen - komponen pada Bootstrap bisa digunakan untuk mengubah tampilan halaman web. Kodenya adalah:
##### a. `<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">`
 
 ##### b. `<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>`
 ##### Setelah itu, saya memakai komponen-komponen yang ada pada Bootsrap untuk memperindah tampilan halaman website saya, seperti *button*, *margin* dan *padding*, dan *cards*, dan komponen yang lainnya.
 
 #### 5. Kustomisasi halaman utama todo list menggunakan cards. (Satu card mengandung satu task).
 
 #### 4. Membuat keempat halaman yang dikustomisasi menjadi *responsive*.
 ##### Menambahkan responsive viewport meta tag di bagian <head> pada berkas base.html. Kodenya adalah: `<meta name="viewport" content="width=device-width, initial-scale=1.0">.` Setelah itu membuat *media query* pada `file .css` untuk mengubah *stylesheet* berdasarkan lebar dan tinggi yang ditentukan, hal ini berguna jika kita ingin membuat *layout* halaman web kita *responsive* dengan menyesuaikan tampilannya berdasarkan ukuran layar perangkat yang digunakan.
 



