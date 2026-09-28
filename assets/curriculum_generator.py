#!/usr/bin/env python3
import os
import json

SAMPLE_PRES_PATH = "/home/dpdp/target/classes/5-6-sinf/1-hafta/02-dars-ai-aktyor/prezentatsiya.html"
with open(SAMPLE_PRES_PATH, "r", encoding="utf-8") as f:
    sample_html = f.read()

s_start = sample_html.find('<div class="stage">') + len('<div class="stage">')
f_start = sample_html.find('<div class="bar">')
s_close = sample_html.rfind('</div>', 0, f_start)

BASE_HEADER = sample_html[:s_start]
BASE_FOOTER = sample_html[s_close:]

SAMPLE_WS_PATH = "/home/dpdp/target/classes/5-6-sinf/1-hafta/01-dars-ai-nima/varaqa.html"
with open(SAMPLE_WS_PATH, "r", encoding="utf-8") as f:
    sample_ws = f.read()

idx_bet1 = sample_ws.find('<!-- ================= BET 1 ================= -->')
HEAD_AND_CONTROLS = sample_ws[:idx_bet1]

idx_s1 = sample_ws.find('<section class="sec">', idx_bet1)
P1_MASTHEAD = sample_ws[idx_bet1:idx_s1]

idx_foot1 = sample_ws.find('<div class="foot">', idx_s1)
idx_bet2 = sample_ws.find('<!-- ================= BET 2 ================= -->', idx_foot1)
P1_FOOTER = sample_ws[idx_foot1:idx_bet2]

idx_s5 = sample_ws.find('<section class="sec">', idx_bet2)
P2_MASTHEAD = sample_ws[idx_bet2:idx_s5]

idx_foot2 = sample_ws.find('<div class="foot">', idx_s5)
idx_script = sample_ws.rfind('<script>', idx_foot2)
P2_FOOTER = sample_ws[idx_foot2:idx_script]
SCRIPT_TAIL = sample_ws[idx_script:]

def build_presentation(title, slides_html, notes_dict):
    t_start = BASE_HEADER.find('<title>')
    t_end = BASE_HEADER.find('</title>') + len('</title>')
    header = BASE_HEADER[:t_start] + f"<title>{title}</title>" + BASE_HEADER[t_end:]

    notes_json = json.dumps(notes_dict, ensure_ascii=False, indent=2)
    n_start = BASE_FOOTER.find('var NOTES = {')
    n_end = BASE_FOOTER.find('};', n_start) + 2
    footer = BASE_FOOTER[:n_start] + f"var NOTES = {notes_json};" + BASE_FOOTER[n_end:]

    footer = footer.replace('1 / 14', '1 / 10').replace('1 / 11', '1 / 10')
    return f"{header}\n{slides_html}\n{footer}"

def build_worksheet(cohort, week, num, t1, s1, k1, p1_content, t2, s2, p2_content, hw_body, crit_rows, next_lesson_title):
    if cohort == "5-6-sinf":
        uz_c, ru_c, en_c = "5-6-sinf", "5-6 класс", "grade 5-6"
    elif cohort == "7-8-sinf":
        uz_c, ru_c, en_c = "7-8-sinf", "7-8 класс", "grade 7-8"
    else:
        uz_c, ru_c, en_c = cohort, cohort, cohort

    m1 = P1_MASTHEAD
    m1 = m1.replace('5-6-sinf · 1-dars', f'{uz_c} · {num}-dars')
    m1 = m1.replace('5-6 класс · урок 1', f'{ru_c} · урок {num}')
    m1 = m1.replace('grade 5-6 · lesson 1', f'{en_c} · lesson {num}')

    old_h1 = '<h1><span lang="uz">Sun\'iy intellekt nima?</span><span lang="ru">Что такое искусственный интеллект?</span><span lang="en">What is artificial intelligence?</span></h1>'
    new_h1 = f'<h1><span lang="uz">{t1["uz"]}</span><span lang="ru">{t1["ru"]}</span><span lang="en">{t1["en"]}</span></h1>'
    m1 = m1.replace(old_h1, new_h1)

    old_sub = '<p class="sub"><span lang="uz">Bu varaqani dars davomida to\'ldirasiz. 2-bet — amaliy ishning natijasi, u baholanadi.</span><span lang="ru">Этот лист вы заполняете во время урока. Страница 2 — результат практической работы, она оценивается.</span><span lang="en">You fill this in during the lesson. Page 2 is the result of the practical work and it is graded.</span></p>'
    new_sub = f'<p class="sub"><span lang="uz">{s1["uz"]}</span><span lang="ru">{s1["ru"]}</span><span lang="en">{s1["en"]}</span></p>'
    m1 = m1.replace(old_sub, new_sub)

    old_key = '<p><span lang="uz">AI bilmaydi — u taxmin qiladi. Shuning uchun u haqiqatni ham, uydirmani ham bir xil ishonch bilan aytadi.</span><span lang="ru">ИИ не знает — он угадывает. Поэтому правду и выдумку он произносит с одинаковой уверенностью.</span><span lang="en">AI doesn\'t know — it guesses. That is why it states truth and invention with the same confidence.</span></p>'
    new_key = f'<p><span lang="uz">{k1["uz"]}</span><span lang="ru">{k1["ru"]}</span><span lang="en">{k1["en"]}</span></p>'
    m1 = m1.replace(old_key, new_key)

    f1 = P1_FOOTER.replace("1-dars", f"{num}-dars").replace("урок 1", f"урок {num}").replace("lesson 1", f"lesson {num}")

    m2 = P2_MASTHEAD
    old_p2_h1 = '<h1><span lang="uz">Yomon prompt · yaxshi prompt</span><span lang="ru">Слабый промпт · сильный промпт</span><span lang="en">Weak prompt · strong prompt</span></h1>'
    new_p2_h1 = f'<h1><span lang="uz">{t2["uz"]}</span><span lang="ru">{t2["ru"]}</span><span lang="en">{t2["en"]}</span></h1>'
    m2 = m2.replace(old_p2_h1, new_p2_h1)

    old_p2_sub = '<p class="sub"><span lang="uz">Bitta AI vositasini oching. Vosita nomi:</span><span lang="ru">Откройте один ИИ-инструмент. Название инструмента:</span><span lang="en">Open one AI tool. Tool name:</span> <span style="display:inline-block; width:50mm; border-bottom:1px solid var(--write)"></span></p>'
    new_p2_sub = f'<p class="sub"><span lang="uz">{s2["uz"]}</span><span lang="ru">{s2["ru"]}</span><span lang="en">{s2["en"]}</span> <span style="display:inline-block; width:50mm; border-bottom:1px solid var(--write)"></span></p>'
    m2 = m2.replace(old_p2_sub, new_p2_sub)

    f2 = P2_FOOTER
    old_next = '<span><span lang="uz">Keyingi dars: AI bilan samarali ishlash qoidalari</span><span lang="ru">Следующий урок: как эффективно работать с ИИ</span><span lang="en">Next lesson: how to work with AI effectively</span></span>'
    new_next = f'<span><span lang="uz">Keyingi dars: {next_lesson_title["uz"]}</span><span lang="ru">Следующий урок: {next_lesson_title["ru"]}</span><span lang="en">Next lesson: {next_lesson_title["en"]}</span></span>'
    f2 = f2.replace(old_next, new_next)

    sec09 = f"""
  <section class="sec">
    <div class="h"><span class="no">09</span><h2><span lang="uz">Uy vazifasi · keyingi darsga</span><span lang="ru">Домашнее задание · к следующему уроку</span><span lang="en">Homework · for next lesson</span></h2></div>
    <div class="hwgrid">
      <div style="display:grid; gap:8px">
        {hw_body}
      </div>
      <div class="crit">
        <span class="k"><span lang="uz">Baholash · 10 ball</span><span lang="ru">Оценка · 10 баллов</span><span lang="en">Grading · 10 points</span></span>
        {crit_rows}
      </div>
    </div>
  </section>
"""
    return f"{HEAD_AND_CONTROLS}{m1}\n{p1_content}\n{f1}{m2}\n{p2_content}\n{sec09}\n{f2}{SCRIPT_TAIL}"

print("curriculum_generator.py created successfully!")
