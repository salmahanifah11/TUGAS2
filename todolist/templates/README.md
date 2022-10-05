link apllikasi heroku: https://pbp-tugas-app.herokuapp.com/todolist/

### 1. Apaperbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
Inline CSS merupakan suatu cara penulisan styling CSS yang dilakukan langsung dalam tag elemen yang bersangkutan. Hal ini membuat stylingnya spesifik pada satu elemen dan tidak dependen dengan styling lainnya. Contoh penulisan inline CSS adalah < p style="color:blue;text-align:center;">Hello World</ p >

Internal CSS merupakan suatu cara penulisan CSS yang berada langsung di dalam file HTML sehingga styling CSS tersebut hanya berlaku pada file HTML tersebut saja. Contoh penulisan internal CSS adalah < style > body {backgorund-color} < /style>

Eksternal CSS merupakan suatu cara penulisan CSS pada file yang terpisah dari HTML, yakni menggunakan file CSS. Untuk mengaplikasikan CSS tersebut pada file HTML gunakan tag < link rel="stylesheet" href="mystyle.css" >. File yang dituliskan dalam href adalah nama file .css yang telah dibuat. Isi dari file CSS eksternal akan mengubah styling untuk semua file .html.

### 2. Jelaskan tag HTML5 yang kamu ketahui.
< h1>, < h2>, < h3> merupakan tag heading dengan ukuran yang berbeda-beda.
< body> merupakan tag yang berisi data yang ingin ditampilkan di website.
< form> merupakan tag untuk membuat form.
< input> merupakan tag untuk menerima input dari user.
< style> merupakan tag untuk melakukan styling CSS.
Dan masih banyak tag lainnya.

### 3. Jelaskan tipe-tipe CSS selector yang kamu ketahui.
Terdapat beberapa tipe selector CSS, antara lain:

Tag : disebut juga type selector, memilih elemen berdasarkan tag, seperti tag p, button, table, dan lainnya.
p {
    insert code here
}

Class : memilih elemen berdasarkan nama class yang sudah diberikan.
.nama-class {
    insert code here
}

ID : memilih elemen berdasarkan id-nya.
#nama-id {
    insert code here
}

Atribut : memilih elemen berdasarkan attribut dari sebuah tag. Misal tag input memiliki beberapa tipe, salah satunya adalah text.
input[ type=text] {
    insert code here
}

Universal : sesuai dengan namanya, selektor ini berlaku untuk semua atribut.
* {
    insert code here
}

Pseudo : a. pseudo-class : untuk state element, seperti saat di click, hover, dan lainnya.
a:hover {
    insert code here
}

Pseudo-element : untuk element semu di HTML , misal seperti elemen di dalam elemen.
p span{
    insert code here
}
potongan kode diatas berarti styling akan berpengaruh pada elemen span yang berada di dalam tag p.

### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Melakukan penginstallan bootstrap dengan menambahkan link dan script pada base html. Lalu modifikasi setiap halaman pada login, register, halaman utama todolist, dan halaman create-task sesuai keinginan. Saya melakukan modifikasi dengan menambahhkan navbar, memberi warna, dan merapihkan content tulisan. Hal tersebut saya lakukan dengan internal CSS, yakni melakukan styling pada file HTML secara langsung. Code untuk menaplikasikan modifikasi tersebut tersebar banyak di internet.
Kemudian, membuat card untuk setiap task menggunakan class=card pada file todolist.html dan menyesuaikan layout sesuai dengan keinginan. Saya juga menambahkan fitur delete task, yang diimplementasikan dengan memmbuat fungsi baru pada views.py dan menambahkan path pada urls.py, lalu memanggil url fungsi tersebut pada file todolist.html.
Setelah selesai, pastikan bahwa web tersebut responsif (saat di zoom, maka tampilan web akan mengikuti bentuk dan ukurannya) Kemudian melakukan deployment ke heroku app.