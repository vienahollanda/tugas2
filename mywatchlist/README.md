## Tugas 3

### Viena Hollanda K
### 2106751253
### PBP A

### Mengakses tiga URL di poin 6 menggunakan Postman dan menangkap hasil *screenshot*-nya.

![IMG_2685](https://user-images.githubusercontent.com/112618738/191655725-ce839ad7-4bff-4765-b29b-90e84648e006.jpg)
![IMG_2683](https://user-images.githubusercontent.com/112618738/191655830-3d282b3b-4399-4a14-847a-c012616f94ae.jpg)
![IMG_2684](https://user-images.githubusercontent.com/112618738/191655877-e41229c4-bd10-4927-a0c9-0e23d62bd63b.jpg)


### 1. Jelaskan perbedaan antara JSON, XML, dan HTML!
#### JSON menyimpan elemennya secara efisien akan tetapi tidak rapi untuk dilihat. Sedangkan XML menyimpan elemen-elemen nya dengan cara yang terstruktur, mudah dibaca oleh manusia dan mesin, akan tetapi kurang efisien. Nama dari file JSON akan diakhiri dengan ekstensi .json. Sedangkan, file XML akan diakhiri dengan ekstensi .xml.JSON digunakan untuk mengirimkan data dengan cara data diuraikan dan dikirimkan melalui internet. Sedangkan, XML memiliki data yang lebih terstruktur dan pengguna dapat menggunakannya untuk menambahkan catatan. Kode JSON juga lebih ringkas karena tidak memerlukan tag pembuka dan penutup sehingga kodenya juga lebih mudah dipahami.
#### HTML lebih berfokus pada pada bagaimana format tampilan dari data, sedangkan XML lebih berfokus pada struktur dan konteksnya. XML dan HTML dibuat untuk tujuan yang berbeda dan keduanya saling melengkapi. Sebuah file HTML tersusun atas tag-tag yang mengatur bagaimana data dalam file itu akan ditampilkan, tetapi tidak ada informasi mengenai isi dari data tersebut. Didalam file XML, kandungan informasi berbentuk format yang terstruktur. Dengan XML data dan tampilannya dibuat terpisah.

### 2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
#### Kita memerlukan Data delivery dalam pengimplementasian sebuah platform karena pada umunya,  akan ada pertukaran data setiap waktu di antara pengguna yang satu dan yang lainnya dalam penggunaan sebuah platform. Salah satu contoh adalah CRUD (Create, Read, Update, Delete) Process. 

### 3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
#### Pertama, membuat aplikasi baru pada proyek Django Tugas 2 di terminal dengan menuliskan perintah `py manage.py startapp mywatchlist.` Setelah itu, menambahkan mywatchlist ke INSTALLED_APPS di `settings.py` project_django sehingga pengguna dapat mengakses http://localhost:8000/mywatchlist dan melakukan routing dari urls yang ada di project_django dengan menambahkan kode ini `path('mywatchlist/', include('mywatchlist.urls'))`. Lalu, menambahkan `urls.py` di dalam app mywatchlist dan melakukan routing lagi di dalamnya. 
#### Selanjutnya, membuat class `WatchListMovies` yang merepresentasikan sebuah data model watchlist model dengan menambahkan atribut-atributnya yang berada di dalam class ini. Atribut yang ada di dalam class ini: 
#### Atribut watched yang mendeskripsikan film tersebut sudah ditonton atau belum. Untuk membuatnya, digunakan field boolean karena di sini hanya bisa 2 pilihan, antara sudah ditonton (true) atau belum ditonton (false). Kode: `watched = models.BooleanField()`
#### Atribut title yang mendeskripsikan judul film. Untuk ini, saya menggunakan field char yang di-limit sebanyak 255 karakter. Kode: `title = models.CharField(max_length=255)`
#### Atribut rating untuk mendeskripsikan rating film dalam *range* 1 sampai 5. Untuk ini, digunakan field integer yang dibatasi nilainya dari 1-5 memakai validator. Kode: `rating_validator = [MaxValueValidator(5), MinValueValidator(1)]`. dan `rating = models.IntegerField(rating_validator)`
#### Atribut release_date untuk mendeskripsikan kapan film tersebut dirilis. Di bagian ini, digunakan field Date (di json formatnya yyyy-mm-dd). kode: `release_date = models.DateField()`
#### Dan yang terakhir adalah atribut review untuk mendeskripsikan *feedback* dari film . Untuk membuat ini, digunakan text field. Kode: `review = models.TextField(default='-')`.

### Link untuk ke aplikasi yang dibuat:

#### [Tipe HTML](https://tugas2viena.herokuapp.com/mywatchlist/html/)
#### [Tipe XML](https://tugas2viena.herokuapp.com/mywatchlist/xml/)
#### [Tipe JSON](https://tugas2viena.herokuapp.com/mywatchlist/json/)
