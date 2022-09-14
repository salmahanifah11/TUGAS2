Link aplikasi heroku : https://pbp-tugas-app.herokuapp.com/katalog/


##### 1. Penjelasan bagan request client pada web aplikasi berbasis Django
Bagan request client
![request_client](https://user-images.githubusercontent.com/112617784/190215583-bbe601c4-6086-4f58-a99f-35cd0ace45d7.png)

Request datang dari permintaan user/client melalui browser pada web server. Web tersebut tersambung pada URL yang kemudian akan tertuju pada urls.py. Lalu, urls.py akan memilih mengenai fungsi pada VIEWS atau views.py yang akan digunakan. View akan meminta data pada MODEL atau models.py yang mengakses data dari database serta kemudian memilih template html yang berfungsi untuk menampilkan halaman atau tampilan web pada browser client.

urls.py, views.py, models.py, serta html saling berkaitan dalam menjalankan web aplikasi berbasis Django. urls.py memiliki code yang akan menentukan path yang tersambung pada views.py. Views.py akan mengambil data pada models.py lalu melakukan mapping terhadap data tersebut agar dapat muncul di halaman HTML.

##### 2. Kenapa menggunakan virtual environment? Apakah dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual environment digunakan agar proses development tidak saling bentrok atau bertabrakan antar satu proyek dengan proyek lainnya. Virtual environment juga digunakan untuk membentuk suatu development environment sehingga dapat menjalankan proyek dengan versi python maupun dependencies yang berbeda-beda dalam satu hardware (laptop/PC).

Membuat aplikasi web berbasis Django tanpa menggunakan virtual environment tetap bisa dilakukan namun, tentunya tidak akan mendapat benefit yang sama baiknya dengan menggunakan virtual environment.

#### 3. Jelaskan bagaimana cara mengimplementasikan poin 1 sampai 4
Memulai proses dengan menjalankan virtual environment pada direktori repositori yang dituju kemudian menginstall segala dependencies yang terdaftar pada requirements.txt. Lalu menjalankan perintah makemigrations dan migrate untuk mempersiapkan serta menerapkan skema model, kemudian menjalankan perintah loaddata json untuk memasukkan data tersebut ke dalam database Django lokal.

Untuk melakukan routing terhadap views, masukkan path views pada urls.py. Lalu import class model dari models.py pada views.py untuk pengambilan data dari database. Masukkan variabel nama dan student ID untuk melengkapi code dan tambahkan variabel context untuk me-return fungsi render sehingga dapat muncul pada halaman HTML. Update code pada katalog.html dengan menambahkan variabel sesuai dengan yang ada pada class models.py. Lakukan add, push, commit.

Terakhir adalah deployment dengan membuat aplikasi baru pada web heroku. Lalu menambahkan secret key pada repositori proyek dengan memasukkan API key akun heroku serta nama aplikasi yang telah dibuat. Re-run workflow pada github hingga aplikasi web muncul dengan baik.