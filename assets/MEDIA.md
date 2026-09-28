# Meme va GIF — qo'yish qoidasi

MP4 va rasmlar `assets/` papkasida. Slaydda ishlatish:

```html
<div class="media" data-gif="rolando-ronaldo.mp4"></div>
```

`.mp4` `.webm` `.mov` → `<video>`: ovozsiz, cheksiz takrorlanadi, o'zi ishga
tushadi. `.gif` `.png` `.jpg` → `<img>`. `data-gif` yozilmagan `.media`
bloki umuman ko'rinmaydi.

## Qachon qo'yiladi — MUHIM

Meme bezak emas, u **hazilning tugatuvchi zarbasi**. Shuning uchun:

- **Faqat kulgi nuqtasida.** Slaydda hazil bo'lmasa, meme ham bo'lmaydi.
  Hazilsiz meme — o'rinsiz meme.
- **Darsiga ikkitadan ko'p emas.** Har slaydda meme bo'lsa, hech biri
  ishlamay qoladi.
- **Jiddiy slaydda hech qachon:** qoidalar, xulosa, uy vazifasi,
  ta'rif, ogohlantirish. Bu yerlarda meme darsning ma'nosini yo'q qiladi.
- **Ko'rsatishdan oldin ko'ring.** Meme sinfga mos ekaniga o'zingiz
  ishonch hosil qiling — nomiga qarab ishonmang.

## Hozir qo'yilgan joylar

| Fayl | Nima ko'rinadi | Qayerda | Nega o'sha yerda |
|---|---|---|---|
| `rolando-ronaldo.mp4` | Ronaldo ishonqiramay tikiladi | 11-sinf 2-raund natijasi · 7–8 2-o'yin | AI soxta narsani jiddiy yuz bilan uydirgani ma'lum bo'ladigan payt |
| `the-weeknd-weekend.mp4` | The Weeknd g'alaba bilan kuladi | ikkala darsning finali | chempion e'lon qilinadi |

## Ishlatilmayotgan

| Fayl | Nima ko'rinadi | Qachon kerak bo'lishi mumkin |
|---|---|---|
| `speed-...-shaking-his-head.mp4` | bosh chayqaydi, "yo'q-e" | juftlik shartni butunlay buzganda |
| `bye-im-out.mp4` | yigit ketib qoladi | prompt shu qadar yomonki, AI javob bermaganda |
| `001.mp4` | divanda charchagan qarash | uzun debug sessiyasidan keyin |

## Diqqat

Fayllar HTML ichiga ham joylashtirilgan, shuning uchun artifact havolasida
ham ishlaydi. Yangi meme qo'shsangiz ayting — qayta joylashtirish kerak.
