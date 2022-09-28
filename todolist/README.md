link apllikasi heroku: https://pbp-tugas-app.herokuapp.com/todolist/

### 1.  Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

### 2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Ya, bisa. Langsung masukkan {{form}} di dalam <form> pada template html yang dituju, hal tersebut akan membuat form input tidak terbungkus dengan <tr>, <div>, ataupun <p> sehingga web akan menampilkan tempat input form yang cenderung menyamping (apabila terdapat 2 atau lebih input variabel).

### 3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Jalankan environment pada commandprompt lalu membuat aplikasi baru dengan manage.py startapp bernama todolist serta menambahkan app tersebut pada INSTALLED_APP yang ada pada settings.py. Membuat sebuah class pada models.py yang berisikan empat variabel, yakni usernames, date, title, dan description dengan fieldtype masing-masing yang berbeda. Membuat sebuah file baru bernama forms.py yang akan meng-import class dari models.py, lalu membentuk class baru dengan ModelForm yang tersambung pada class models.py.

Buat sebuah fungsi baru pada views.py untuk me-return render dari sebuah parameter requet dengan bentuk html, lalu membuat folder templates yang akan berisikan code html dengan menambahkan beberapa fitur (salah satunya button yang akan tersambung pada fungsi di views.py). Membentuk beberapa fungsi baru pada views.py, seperti fungsi register, login, logout, hingga fungsi untuk membuat form. Bentuk file html register, login sesuai dengan template yang telah diberikan dan file html createtask yang akan berisikan tabel form untuk meminta input user. Sambungkan setiap fungsi pada views.py dengan file html melalui render.

Merestriksi halaman utama todolist dengan menambahkan @login_required(login_url='') agar halaman hanay dapat diakses setelah user login serta membuat atau menambahkan cookie dengan menambahkan data last_login dan menampilkannya ke halaman utama todolist.

Pada urls.py, import setiap fungsi pada views.py, lalu masukan path pada urlpatterns sesuai dengan fungsinya masing-masing. Untuk dapat mengakses django admin, lakukan perintah createsuperstar pada commandprompt dan buatlah akun, kemudian pada file admin.py masukkan admin.site.register(<model>) agar form yang di=input user dapat masuk pada django admin.