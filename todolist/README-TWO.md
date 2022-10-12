### Tugas 6 PBP
### Viena Hollanda K
### 2106751253

#### 1. Jelaskan perbedaan antara *asynchronous programming* dengan *synchronous programming*.
##### Dengan menggunakan *asynchronous programming*, program tetap bisa bersifat *responsive* terhadap *event* lain yang mungkin saja terjadi ketika sedang menjalankan tugas dan tidak perlu menunggu hingga tugas yang sedang dijalankan selesai. Karena hal ini, *asynchronous programming* memungkinkan sebuah program untuk menerima beberapa *request* di waktu yang bersamaaan sehingga bisa menyelesaikan lebih banyak tugas dalam waktu yang lebih singkat. 
##### Dalam *synchronous programming*, ketika program sedang menjalankan tugas, program ini tidak dapat menangani *event* lain yang mungkin saja terjadi dan harus menunggu hingga tugas yang sedang dijalankan selesai untuk menjalankan tugas selanjutnya. Program tidak dapat menangani *event* lain yang terjadi, ketika sedang menjalankan suatu tugas.

#### 2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma *Event-Driven Programming*. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
##### *Event-Driven Programming* merupakan sebuah paradigma pemrograman komputer, di mana *control flow* dari program bergantung dengan adanya kejadian dari sebuah *event* yang dimonitor oleh *event listener*. Ketika *event listener* mendeteksi adanya kejadian dari *event* yang didefinisikan, *event handler* terhadap *event* ini akan dijalankan dan memanggil *function* atau *method* yang dipicu berdasarkan tipe *event* yang terjadi.
##### Contoh penerapannya pada tugas ini, ada pada kode yang mendefinisikan *button close* di modal untuk tambah task. Kodenya: `<button aria-label="Close" class="btn-close" data-bs-dismiss="modal" onclick="resetForm();"type="button"></button>`. Di kode tersebut, terdapat atribut `onclick="resetForm()` yang berarti fungsi `resetForm()` akan dipanggil jika *button close* ditekan dan menjalankan barisan kode di dalam fungsi tersebut.

#### 3. Jelaskan penerapan *asynchronous programming* pada AJAX.
##### Dalam menerapkan *asynchronous programming* pada AJAX, kita bisa memanfaatkan fungsi `setTimeout()`. Contoh kode: `setTimeout(functionRef, delay)`, untuk parameter kedua akan diisi dengan durasi waktu dalam satuan *milliseconds* (*timer*), dan parameter pertama akan diisi dengan fungsi yang akan dieksekusi ketika *timer* berakhir. Contoh kode: 
##### `console.log('i need u');`
##### `setTimeout(() => { console.log('Javascript')},100) // tunda selama 100 miliseconds`
##### `console.log('where are you?');`
##### Sebelum fungsi pada parameter 1 dijalankan, akan ada waktu penundaan selama 100 *milliseconds*. Ketika proses yang sedang dieksekusi melebihi batas waktu pada *timer*, sembari menunggu proses ini selesai, javascript akan memanggil fungsi di parameter 1 untuk mengeksekusi perintah selanjutnya.

#### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
##### a. Mengubah tugas 4 yang telah dibuat sebelumnya menjadi menggunakan AJAX.
##### b. Buatlah sebuah tombol Add Task yang membuka sebuah modal dengan form untuk menambahkan task.
