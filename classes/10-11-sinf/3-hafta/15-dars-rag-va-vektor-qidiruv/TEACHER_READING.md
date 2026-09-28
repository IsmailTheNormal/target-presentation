# O'qituvchi uchun Qo'llanma — 15-Dars: RAG va Vektor Qidiruv

## 1. Darsning Pedagogik Maqsadi
O'quvchilarga nega bugungi kunda oddiy prompt yoki Fine-Tuning korporativ tizimlarda yetarli emasligini, matnlarni qanday qilib semantik vektor fazosiga aylantirish (Embeddings) va Kosinus o'xshashlik orqali millionlab hujjatlar orasidan kerakli faktni 5 millisekundda topish mumkinligini amaliy laboratoriya bilan tushuntirish.

## 2. Dars Vaqti Taqsimoti (40 daqiqa)
- **0–3 daq:** Tashkiliy qism. Fine-tuning va RAG taqqoslovi.
- **3–13 daq:** Nazariya: Text Embeddings, Vektor fazosi va Kosinus o'xshashlik formulasi.
- **13–23 daq:** Arxitektura: Chunking strategiyalari (Fixed vs Recursive), HNSW graflari va Vektor bazalar (Pinecone, Qdrant, pgvector).
- **23–33 daq:** Amaliyot: `lab/index.html` da so'rovlar yuborish, kosinus ballarini o'lchash va ish varaqasiga yozish.
- **33–37 daq:** Xatolar tahlili: "Lost in the middle" va bo'laklarni to'g'ri joylashtirish.
- **37–40 daq:** Xulosa va 10 ballik mezon bo'yicha baholash.

## 3. O'quvchilarga beriladigan savollar
1. "Nega oddiy Google qidiruvida 'qizil olma sotib olish' desak, 'qimmat meva xaridi' sahifasini topa olmaydi, ammo vektor qidiruv topa oladi?"
2. "Agar hujjatni juda katta (2000 token) qilib bo'lsak nima bo'ladi? Juda kichik (20 token) bo'lsak-chi?"
3. "Nega kosinus o'xshashlik formulasida vektor uzunligiga (normaga) bo'lamiz?"
