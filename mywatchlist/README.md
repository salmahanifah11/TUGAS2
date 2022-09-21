link aplikasi heroku: https://pbp-tugas-app.herokuapp.com/mywatchlist/

#### Jelaskan perbedaan antara JSON, XML, dan HTML!
JSON (JavaScript Object Notation) didesain menjadi self-describing sehingga JSON mudah dimengerti dan dapat digunakan untuk menyimpan dan mengirimkan data. JSON memiliki format berupa text kode sehingga JSON banyak terdapat di banyak bahasa pemrograman.

XML (eXtensible Markup Language) didesain menjadi self-descriptive sehingga informasi yang disampaikan dari data dapat mudah dimengerti. XML merupakan sebuah informasi yang dibungkus di dalam tag dengan struktur tree. Struktur tersebut dimulai dari root, branch, hingga berakhir pada leaves sehingga XML seringkali digunakan sebagai tempat untuk menyimpan dan mengirimkan data.

HTML (HyperText Markup Language) merupakan sebuah markup language yang didesain untuk membuat dan atau menampilkan web pages. HTML menampilkan data dan mendeskripsikan struktur dari sebuah webpage namun, HTML merupakan sebuah bahasa yang telah ditentukan dengan implikasinya sendiri.

#### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery merupakan sebuah proses mentransfer data dari suatu platform menuju ke suatu profil atau platform lainnya. Dalam Django, dimungkinkan bagi kita untuk mengirimkan data dari suatu stack ke stack lainnya, data-data tersebut dapat berbentuk dalam berbagai format, seperti JSON, XML, HTML, dan lainnya sehingga data delivery sangat diperlukan dalam mengimplementasikan sebuah platform.

#### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Diawali dengan mengaktifkan environment pada command prompt direktori yang dituju lalu menjalankan perintah startapp untuk membuat aplikasi baru bernama mywatchlist dan memasukkannya pada “INSTALLED APPS” yang ada pada settings.py django-app.
Mengisi file models.py pada folder mywatchlist dengan membentuk sebuah class baru yang berisi variabel-variabel yang akan dimasukkan pada web page lalu melakukan migration serta migrate. Membentuk sebuah file data json yang berisi data-data dengan variabel yang sesuai seperti yang tertera pada models.py dan lalu load data tersebut agar masuk ke dalam database django lokal.

Membuat sebuah fungsi pada file views.py yang akan me-return render dari sebuah parameter request dan html. Lalu membuat folder templates yang akan berisikan code html dengan template yang telah diberikan pada lab sebelumnya. Membuat file baru bernama urls.py yang berisikan URL path untuk platform dan menambahkan path file urls.py yang terdapat pada project_django.
Import models ke dalam views.py serta menambahkan kode yang akan berfungsi untuk memanggil fungsi query ke model database dan menyimpannya ke dalam sebuah variabel. Lalu mengedit file html yang telah dibuat sebelumnya dengan mengisikan baris sesuai dengan variabel yang diinginkan.

Untuk melakukan data delivery pada XML dan JSON, membuat fungsi yang menerima parameter request pada views.py (baik XML maupun JSON) lalu menambahkan import HttpResponse dan Serializer. Masukkan suatu variabel yang berisikan hasil query dari class dan tambahkan return function berupa HTTPresponse berisi parameter data hasil query yang sudah diserialisasikan menjadi XML ataupun JSON. Lalu, import fungsi yang telah dibuat pada file urls.py dan tambahkan path urlnya. Jalankan proyek dengan memberikan perintah runserver.

Terakhir adalah melakukan deployment aplikasi pada heroku dengan memasukkan API key dan nama aplikasi pada secret repositori github yang digunakan (sudah dilakukan pada tugas 2 minggu lalu).


#### Screenshot URL dengan postman
![2022-09-22](https://user-images.githubusercontent.com/112617784/191607788-0791e760-12ca-438f-aa24-f2ac520ec2be.png)
![2022-09-22 (1)](https://user-images.githubusercontent.com/112617784/191621288-99b40073-636b-4b0d-8b0c-d97be3ddd018.png)
