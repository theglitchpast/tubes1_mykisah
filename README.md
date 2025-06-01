<div align="center">
  <h1>💎 Greedy Algorithms in Etimo Diamonds Game</h1>
  <h3>Tugas Besar 1 IF2211 Strategi Algoritma</h3>
  <p>by My Kisah</p>
  <img src="img/kucing.jpeg" alt="kucing" width="350"/>
  <br/>
  <br/>
</div>

> 🎓 Latar Belakang Proyek: Kami membuat algoritma greedy pada bot game Etimo Diamonds sebagai bagian dari tugas besar mata kuliah Strategi Algoritma pada semester empat di Program Studi Teknik Informatika ITERA.

## 📝 Description

Diamonds adalah sebuah tantangan pemrograman yang mempertemukan bot buatan Anda dengan bot dari pemain lain. Setiap pemain akan memiliki sebuah bot dengan tujuan untuk mengumpulkan sebanyak mungkin diamond menggunakan algoritma greedy.

## 🚨 Implementasi Algoritma

Kami akhirnya memutuskan untuk mengkombinasikan beberapa solusi. Jadi strategi kami adalah Greedy by Density diamond di sekitar base dengan kalkulasi waktu apakah cukup untuk mengambil dan pulang ke base. Bot kami juga bisa melakukan tackle jika bot musuh berada dekat dengan bot kami. Tapi fokus utama bot kami adalah mengumpulkan diamond dan memaksimalkan score yang bisa didapatkan.

## 📁 Project Structure

```bash
tubes1_mykisah
├── doc
│   └── My Kisah.pdf
├── src
│   ├── game
│   │   ├── logic
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── maling_pro_player.py
│   │   │   └── random.py
│   │   ├── __init__.py
│   │   ├── api.py
│   │   ├── board_handler.py
│   │   ├── bot_handler.py
│   │   ├── models.py
│   │   └── util.py
│   ├── decode.py
│   ├── main.py
│   ├── requirements.txt
│   ├── run-bots.bat
│   ├── run-bots.sh
├── img
│   └── kucing.jpeg
├── .gitignore
└── README.md
```

## 🔨 Dependencies

1. Game Engine

   • Node.js (https://nodejs.org/en)

   • Docker desktop (https://www.docker.com/products/docker-desktop/)

   • Yarn

2. Bot Engine

   • Python

## 💻 Configuration Guide

### 💎 Game Engine Setup:

1. Clone repository ke file lokal Anda dan pastikan semua dependensi sudah terpasang di perangkat Anda. Akses repository [di sini](https://github.com/haziqam/tubes1-IF2211-game-engine/releases/tag/v1.1.0).
2. Ekstrak file zip, lalu masuk ke folder hasil ekstraksi dan buka terminal.
3. Masuk ke direktori root proyek dengan menjalankan `cd tubes1-IF2110-game-engine-1.1.0` di terminal.
4. Instal dependensi dengan menjalankan perintah `yarn` di terminal.
5. Konfigurasi environment variables dengan menjalankan script `./scripts/copy-env.bat`.
6. Setup database lokal (buka aplikasi Docker desktop terlebih dahulu, lalu jalankan perintah berikut di terminal) `compose up -d database`.
7. Jalankan script berikut untuk Windows `./scripts/setup-db-prisma.bat`.
8. Lakukan build dengan perintah `npm run build`.

### 🤖 Bot Engine Setup:

1. Clone repository ini ke file lokal Anda dan pastikan semua dependensi sudah terpasang di perangkat Anda. Akses repository [di sini](https://github.com/theglitchpast/tubes1_mykisah).

## 🏃‍♂️ How to Run

1. Ubah direktori terminal ke direktori root file game engine dengan menjalankan perintah `cd tubes1-IF2110-game-engine-1.1.0` di terminal.
2. Jalankan game engine dengan perintah `npm run start` dan pastikan game engine berjalan di (http://localhost:8082/).
3. Ubah direktori terminal ke file bot engine dengan menjalankan perintah `cd tubes1_mykisah\src`.
4. Untuk menjalankan bot, eksekusi logika dengan perintah `python main.py --logic MalingProPlayer --email=test@email.com --name=stima --password=123456 --team etimo`.
5. Untuk Windows, Anda juga dapat menjalankan bot dengan perintah `./run-bots.bat` dan untuk Linux dapat menjalankan bot dengan perintah `./run-bots.sh`.

## 🔬 Contributors

| Nama                | NIM       | Instagram                                                 |
| ------------------- | --------- | --------------------------------------------------------- |
| Andika Dinata       | 123140096 | [theglithcpast](https://www.instagram.com/theglitchpast/) |
| Agus Subekti        | 123140104 | [asubekk\_](https://www.instagram.com/asubekk_/)          |
| Satria Lemana Putra | 123140088 | [putra373.\_](https://www.instagram.com/putra373._/)      |
