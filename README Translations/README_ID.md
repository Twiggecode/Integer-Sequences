<!-- Do not translate this -->
<details>
<summary>
<strong> Read this guide in other languages </strong>
</summary>
    <ul>
        <li><a href="./README.md"> English </a></li>
        <li><a href="./README Translations\README_KR.md"> Korean </a></li>
        <li><a href="./README Translations\README_ES.md"> Spanish </a></li>
        <li><a href="./README Translations\README_RO.md"> Romanian </a></li>
        <li><a href="./README Translations\README_PT.md"> Portuguese </a></li>
    </ul>
</details>
<!-- Do not translate this -->

# Urutan Bilangan Bulat

## Pengenalan Proyek

Ini adalah proyek sumber terbuka yang relatif mudah dan ramah pemula yang merupakan pilihan yang sangat baik untuk berkontribusi bagi yang ingin memberikan kontribusi sumber terbuka pertama mereka. Walau demikian, semua bebas untuk berkontribusi.

Tujuan dari proyek ini adalah untuk menciptakan sebuah basis data algoritma menggunakan bahasa pemrograman pilihan Anda, dimana setiap algoritma akan mengembalikan elemen ke-n dari salah satu urutan bilangan bulat terkemuka pada pranala wikipedia berikut. https://en.wikipedia.org/wiki/List_of_integer_sequences

Pranala wikipedia ini mengandung daftar berbagai urutan bilangan bulat terkemuka, seperti bilangan prima, urutan Kolakoski, bilangan Motzkin, bilangan Lucas dan seterusnya...

'n' merepresentasikan bilangan bulat yang dimasukkan oleh pengguna. Sebagai contoh, apabila pengguna memasukkan bilangan bulat '2', maka algoritma Anda harus mengembalikan elemen ketiga dari urutan tersebut (karena pengindeksan dimulai pada 0, elemen pertama dari urutan adalah n=0, elemen kedua adalah n=1 dan seterusnya).

Apabila seseorang perlu mengimplementasikan salah satu urutan bilangan bulat tidak terkenal yang terdaftar di halaman wikipedia tersebut dalam program mereka, besar kemungkinan algoritma tersebut harus dikembangkan dari awal untuk menemukan elemen ke-n dari urutan yang diinginkan, karena tidak ada kode untuk menghasilkan urutan tidak terkenal tersebut di internet.

Saya ingin melengkapi basis data algoritma di dalam proyek ini agar orang lain dapat dengan mudah menggunakan algoritma dalam basis data saya dibandingkan harus menghabiskan waktu mengembangkan algoritma mereka sendiri. Siapapun bebas untuk menggunakan kode di proyek ini dalam perangkat lunak mereka. Tidak dibutuhkan permintaan izin karena proyek ini menggunakan lisensi Unlicense.

## Bagaimana Cara Berkontribusi

Lihat pranala wikipedia https://en.wikipedia.org/wiki/List_of_integer_sequences

Lihat daftar urutan bilangan bulat dan kembangkan sebuah algoritma dalam bahasa pemrograman apa saja untuk mengembalikan elemen ke-n dari urutan tersebut. Pengindeksan dimulai dari 0, sehingga apabila pengguna memasukkan n=0, ini akan mengembalikan elemen pertama dari urutan tersebut, n=1 akan mengembalikan elemen kedua dan seterusnya. Lihat _repository_ proyek untuk memastikan kode untuk urutan bilangan bulat pilihan Anda belum ditambahkan ke proyek dalam bahasa pemrograman pilihan Anda.

Sebagai contoh, bila seseorang sudah membuat algoritma Python untuk bilangan Bell dan menambahkannya ke proyek ini, Anda tetap dapat membuat sebuah algoritma untuk bilangan Bell dalam bahasa lain, hanya tidak dengan Python.

Bila tidak ada kode untuk sebuah urutan bilangan spesifik di dalam _repository_ proyek, Anda dapat membuat kode untuk urutan bilangant ersebut di bahasa pemrograman apapun yang Anda mau.

Anda dapat melihat dan menggunakan kode yang sudah ada di dalam _repository_ proyek untuk memandu dan membantu pengembangan algoritma Anda sendiri.

Setelah Anda senang dengan kode yang telah Anda kembangkan, ajukan sebuah _pull request_ menggunakan templat _pull request_, dan juga perbarui daftar pelacakan. Kemudian saya akan tinjau kode Anda untuk memastikan semua berjalan sesuai ekspektasi, dan lalu menambahkannya ke _repository_ proyek. Apabila kode Anda menghasilkan keluaran yang tepat, kode tersebut akan selalu ditambahkan ke _repository_ proyek, tanpa memperhatikan standar pengkodean / kualitas kode, dan tanpa memperhatikan kecepatan dari kodenya.

Anda juga dapat memodifikasi dan memperbaiki kode yang ada di dalam proyek. Ajukan sebuah _pull request_ dan saya akan tinjau perubahan Anda. Sebagai contoh, Anda dapat memperbaiki kecepatan dari kode atau meningkatkan standar pengkodean dengan menambahkan kode, spasi, merubah nama variabel, dan seterusnya.

## Bagaimana Cara Mengajukan _Pull Request_

Karena proyek ini ditargetkan untuk pemula, saya ingin menjelaskan dengan singkat cara yang paling mudah untuk mengajukan sebuah _pull request_ untuk mereka yang tidak mengetahui caranya.

Buka _repository_ saya dan klik "Fork". Ini akan menciptakan sebuah salinan cabang dari _repository_ tersebut.

Tambahan kode Anda ke salinan cabang Anda.

Kembali ke _repository_ saya dan klik "Submit pull request". Klik "Compare across forks". Pilih salinan cabang dari _repository_ Anda sebagai _head_ dan _repository_ saya sebagai _base_.

Klik "Submit a pull request" dan tinggalkan sebuah komentar bermakna menjelaskan kode yang Anda ingin tambahkan ke proyek.

Secara alternatif, Anda dapat menggunakan perintah _git_ berikut:

<!-- Alternatively, you can use the following git commands: -->

1. Untuk meng-klon _repository_ ke sistem lokal Anda, gunakan

`git clone repo-link folder_name`

2. Untuk _stage_ file yang Anda ubah, gunakan

`git add file-name`

3. Dalam kasus Anda telah merubah banyak file dan ingin _stage_ mereka semua bersamaan, gunakan

`git add .`

4. Untuk _commit_ terhadap perubahan tersebut, gunakan

`git commit -m "Fixed Issue #issue_number"`

5. Untuk _push_ perubahan tersebut, gunakan

`git push origin Branch-name`
