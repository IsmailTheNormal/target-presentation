#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Target International School — Vibecoding Dars Portali Generator
Generates root index.html with interactive class/week/lesson navigation,
path routing, live search, and dark/light trilingual theme.
"""

import os
import re
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CLASSES_DIR = os.path.join(BASE_DIR, "classes")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# Cohorts specification
COHORTS = [
    {
        "id": "10-11-sinf",
        "title": {
            "uz": "10–11-sinf: Senior AI & Muhandislik",
            "ru": "10–11 классы: Senior AI и Инженерия",
            "en": "Grades 10–11: Senior AI & Engineering"
        },
        "desc": {
            "uz": "LLM ichki mexanikasi, Tool calling, RAG vektor qidiruv, Multi-Agent tizimlar va AI kiberxavfsizligi",
            "ru": "Внутренняя механика LLM, Tool calling, RAG векторный поиск, Мультиагентные системы и безопасность ИИ",
            "en": "LLM internal mechanics, Tool calling, RAG vector search, Multi-Agent systems & AI cybersecurity"
        },
        "badge": "Senior Track",
        "icon": "🎓",
        "weeks_meta": {
            "1-hafta": {"uz": "1-hafta: Vibecoding asoslari, HTML/CSS va Freelance", "ru": "1-неделя: Основы Vibecoding, HTML/CSS и Фриланс", "en": "Week 1: Vibecoding Basics, HTML/CSS & Freelance"},
            "2-hafta": {"uz": "2-hafta: API, Ma'lumotlar, Kiberxavfsizlik va Agentic AI", "ru": "2-неделя: API, Данные, Кибербезопасность и Agentic AI", "en": "Week 2: API, Data, Cybersecurity & Agentic AI"},
            "3-hafta": {"uz": "3-hafta: LLM Mexanikasi, Tool Calling va RAG", "ru": "3-неделя: Механика LLM, Tool Calling и RAG", "en": "Week 3: LLM Mechanics, Tool Calling & RAG"},
            "4-hafta": {"uz": "4-hafta: Chuqur RAG, Vektor Qidiruv va Prompt Injection", "ru": "4-неделя: Глубокий RAG, Векторный поиск и Prompt Injection", "en": "Week 4: Deep RAG, Vector Search & Prompt Injection"}
        }
    },
    {
        "id": "9-sinf",
        "title": {
            "uz": "9-sinf: Junior Vibecoders & DevOps",
            "ru": "9 класс: Junior Vibecoders и DevOps",
            "en": "Grade 9: Junior Vibecoders & DevOps"
        },
        "desc": {
            "uz": "AI Streaming, Git & GitHub, Pull Request, CI/CD avtomatlashtirish, SemVer va AI Bug Hunter",
            "ru": "AI Streaming, Git & GitHub, Pull Request, CI/CD автоматизация, SemVer и AI Bug Hunter",
            "en": "AI Streaming, Git & GitHub, Pull Request, CI/CD automation, SemVer & AI Bug Hunter"
        },
        "badge": "DevOps Track",
        "icon": "🚀",
        "weeks_meta": {
            "1-hafta": {"uz": "1-hafta: Vibecoding, HTML/CSS va Loyiha Deploy", "ru": "1-неделя: Vibecoding, HTML/CSS и Деплой", "en": "Week 1: Vibecoding, HTML/CSS & Deploy"},
            "2-hafta": {"uz": "2-hafta: REST API, JSON, Auth va AI Bug Hunter", "ru": "2-неделя: REST API, JSON, Auth и AI Bug Hunter", "en": "Week 2: REST API, JSON, Auth & AI Bug Hunter"},
            "3-hafta": {"uz": "3-hafta: Git, GitHub, PR, CI/CD va Open Source", "ru": "3-неделя: Git, GitHub, PR, CI/CD и Open Source", "en": "Week 3: Git, GitHub, PR, CI/CD & Open Source"}
        }
    },
    {
        "id": "7-8-sinf",
        "title": {
            "uz": "7–8-sinf: Game Dev & Interaktiv Veb",
            "ru": "7–8 классы: Game Dev и Интерактивный Веб",
            "en": "Grades 7–8: Game Dev & Interactive Web"
        },
        "desc": {
            "uz": "JavaScript hodisalari, Canvas 2D dvigateli, O'yin fizikasi, Web Audio API, Partikllar va Game Jam",
            "ru": "События JavaScript, движок Canvas 2D, физика игр, Web Audio API, частицы и Game Jam",
            "en": "JavaScript events, Canvas 2D game engine, physics, Web Audio API, particles & Game Jam"
        },
        "badge": "Game Dev Track",
        "icon": "🎮",
        "weeks_meta": {
            "1-hafta": {"uz": "1-hafta: Sun'iy intellekt va birinchi veb sahifa", "ru": "1-неделя: Искусственный интеллект и первая веб-страница", "en": "Week 1: Artificial Intelligence & First Web Page"},
            "2-hafta": {"uz": "2-hafta: Interaktivlik, JavaScript va Mini-o'yin", "ru": "2-неделя: Интерактивность, JavaScript и Мини-игра", "en": "Week 2: Interactivity, JavaScript & Mini-Game"},
            "3-hafta": {"uz": "3-hafta: Canvas 2D O'yin Tsikli, Fizika va Boss Jangi", "ru": "3-неделя: Canvas 2D Игровой цикл, Физика и Босс", "en": "Week 3: Canvas 2D Game Loop, Physics & Boss Battle"},
            "4-hafta": {"uz": "4-hafta: Audio API, Partikllar, Mobil Joystik va Game Jam", "ru": "4-неделя: Audio API, Частицы, Мобильный джойстик и Game Jam", "en": "Week 4: Audio API, Particles, Mobile Joystick & Game Jam"}
        }
    },
    {
        "id": "5-6-sinf",
        "title": {
            "uz": "5–6-sinf: Junior Creators & Kiber-O'yinlar",
            "ru": "5–6 классы: Junior Creators и Киберигры",
            "en": "Grades 5–6: Junior Creators & Cyber Games"
        },
        "desc": {
            "uz": "AI ijodkorlik (hikoya, audio, multfilm), 3D o'yin dunyosi, Game Loop mexanikasi va Level Editor",
            "ru": "Творчество с ИИ (истории, звук, мультфильмы), 3D игровой мир, Game Loop механика и Редактор уровней",
            "en": "AI Creativity (stories, voice, animation), 3D game world, Game Loop mechanics & Level Editor"
        },
        "badge": "Creators Track",
        "icon": "👾",
        "weeks_meta": {
            "1-hafta": {"uz": "1-hafta: AI Sehrli Olam: Aktyor, Ertakchi va Rassom", "ru": "1-неделя: Волшебный мир ИИ: Актер, Сказочник и Художник", "en": "Week 1: AI Magic World: Actor, Storyteller & Artist"},
            "2-hafta": {"uz": "2-hafta: O'yin Dunyosi: 3D, SFX, Aqlli NPC va UI", "ru": "2-неделя: Игровой мир: 3D, SFX, Умные NPC и UI", "en": "Week 2: Game World: 3D, SFX, Smart NPCs & UI"},
            "3-hafta": {"uz": "3-hafta: Kiber-Yuguruvchi: Mexanika, Tikanlar va Boss", "ru": "3-неделя: Кибер-Бегун: Механика, Шипы и Босс", "en": "Week 3: Cyber Runner: Mechanics, Traps & Boss"},
            "4-hafta": {"uz": "4-hafta: Dushman AI Ta'qibi va O'z Levelingni Qur", "ru": "4-неделя: Преследование Вражеского ИИ и Свой уровень", "en": "Week 4: Enemy AI Pursuit & Build Your Level"}
        }
    }
]

def load_logos():
    light_logo = ""
    dark_logo = ""
    light_path = os.path.join(ASSETS_DIR, "logo-light.txt")
    dark_path = os.path.join(ASSETS_DIR, "logo-dark.txt")
    if os.path.exists(light_path):
        with open(light_path, "r", encoding="utf-8") as f:
            light_logo = f.read().strip()
    if os.path.exists(dark_path):
        with open(dark_path, "r", encoding="utf-8") as f:
            dark_logo = f.read().strip()
    return light_logo, dark_logo

def parse_lesson(sinf_id, week_id, lesson_id, lesson_path):
    p_path = os.path.join(lesson_path, "prezentatsiya.html")
    v_path = os.path.join(lesson_path, "varaqa.html")
    has_p = os.path.exists(p_path)
    has_v = os.path.exists(v_path)
    
    # Check interactive subproject
    interactive_url = None
    interactive_name = None
    for sub in ["lab", "arena", "game", "editor", "aha"]:
        sub_idx = os.path.join(lesson_path, sub, "index.html")
        if os.path.exists(sub_idx):
            interactive_url = f"classes/{sinf_id}/{week_id}/{lesson_id}/{sub}/index.html"
            sub_names = {
                "lab": {"uz": "Interaktiv Lab", "ru": "Интерактивная Лаба", "en": "Interactive Lab"},
                "arena": {"uz": "Kiber-Arena", "ru": "Кибер-Арена", "en": "Cyber Arena"},
                "game": {"uz": "Jonli O'yin", "ru": "Живая Игра", "en": "Live Game"},
                "editor": {"uz": "Level Redaktor", "ru": "Редактор Уровней", "en": "Level Editor"},
                "aha": {"uz": "Interaktiv Lab", "ru": "Интерактивная Лаба", "en": "Interactive Lab"}
            }
            interactive_name = sub_names.get(sub, {"uz": "Interaktiv Loyiha", "ru": "Интерактивный Проект", "en": "Interactive Project"})
            break

    # Extract lesson number from folder name
    num_match = re.match(r"^(\d+)", lesson_id)
    lesson_num = num_match.group(1) if num_match else "00"

    title = {"uz": "", "ru": "", "en": ""}
    lede = {"uz": "", "ru": "", "en": ""}

    # Parse HTML for Title and Lede
    source_file = p_path if has_p else (v_path if has_v else None)
    if source_file:
        try:
            with open(source_file, "r", encoding="utf-8") as f:
                content = f.read()

                # Extract H1
                m = re.search(r"<h1([^>]*)>(.*?)</h1>", content, re.DOTALL | re.IGNORECASE)
                if m:
                    attrs = m.group(1)
                    body = m.group(2)
                    ru_m = re.search(r"data-ru=[\"\x27](.*?)[\"\x27]", attrs + body)
                    en_m = re.search(r"data-en=[\"\x27](.*?)[\"\x27]", attrs + body)
                    clean_uz = re.sub(r"<[^>]+>", " ", body).strip()
                    clean_uz = re.sub(r"\s+", " ", clean_uz)
                    title["uz"] = clean_uz
                    title["ru"] = ru_m.group(1) if ru_m else clean_uz
                    title["en"] = en_m.group(1) if en_m else clean_uz

                # Extract Lede
                lm = re.search(r"<p[^>]*class=[\"\x27][^\"\x27]*lede[^\"\x27]*[\"\x27][^>]*>(.*?)</p>", content, re.DOTALL | re.IGNORECASE)
                if lm:
                    body = lm.group(1)
                    ru_lm = re.search(r"data-ru=[\"\x27](.*?)[\"\x27]", body)
                    en_lm = re.search(r"data-en=[\"\x27](.*?)[\"\x27]", body)
                    clean_uz = re.sub(r"<[^>]+>", " ", body).strip()
                    clean_uz = re.sub(r"\s+", " ", clean_uz)
                    lede["uz"] = clean_uz
                    lede["ru"] = ru_lm.group(1) if ru_lm else clean_uz
                    lede["en"] = en_lm.group(1) if en_lm else clean_uz
        except Exception as e:
            print(f"Error parsing {source_file}: {e}")

    # Fallbacks if title not found
    if not title["uz"]:
        clean_name = " ".join(lesson_id.split("-")[2:]).title()
        title["uz"] = f"{lesson_num}-dars: {clean_name}"
        title["ru"] = title["uz"]
        title["en"] = title["uz"]

    return {
        "id": lesson_id,
        "num": lesson_num,
        "title": title,
        "lede": lede,
        "has_p": has_p,
        "p_url": f"classes/{sinf_id}/{week_id}/{lesson_id}/prezentatsiya.html" if has_p else None,
        "has_v": has_v,
        "v_url": f"classes/{sinf_id}/{week_id}/{lesson_id}/varaqa.html" if has_v else None,
        "interactive_url": interactive_url,
        "interactive_name": interactive_name
    }

def build_data():
    dataset = []
    total_lessons = 0

    for cohort in COHORTS:
        c_id = cohort["id"]
        c_path = os.path.join(CLASSES_DIR, c_id)
        if not os.path.isdir(c_path):
            continue

        c_data = {
            "id": c_id,
            "title": cohort["title"],
            "desc": cohort["desc"],
            "badge": cohort["badge"],
            "icon": cohort["icon"],
            "weeks": []
        }

        # Scan weeks in order
        week_dirs = [w for w in sorted(os.listdir(c_path)) if os.path.isdir(os.path.join(c_path, w)) and w != "game"]
        for w_id in week_dirs:
            w_path = os.path.join(c_path, w_id)
            w_meta = cohort["weeks_meta"].get(w_id, {
                "uz": f"{w_id.replace('-', ' ').title()}",
                "ru": f"{w_id.replace('-', ' ').title()}",
                "en": f"{w_id.replace('-', ' ').title()}"
            })

            w_data = {
                "id": w_id,
                "title": w_meta,
                "lessons": []
            }

            lesson_dirs = [l for l in sorted(os.listdir(w_path)) if os.path.isdir(os.path.join(w_path, l)) and l != "eski-duel-dars"]
            for l_id in lesson_dirs:
                l_path = os.path.join(w_path, l_id)
                lesson_info = parse_lesson(c_id, w_id, l_id, l_path)
                w_data["lessons"].append(lesson_info)
                total_lessons += 1

            c_data["weeks"].append(w_data)

        dataset.append(c_data)

    print(f"Data compiled: {len(dataset)} cohorts, {total_lessons} total lessons.")
    return dataset

def generate_index_html():
    dataset = build_data()
    light_logo, dark_logo = load_logos()
    data_json = json.dumps(dataset, ensure_ascii=False)

    html_template = f'''<!DOCTYPE html>
<html lang="uz" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Target International School — Vibecoding Dars Portali</title>
  <link rel="icon" type="image/png" href="assets/target-logo.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@600;700;800&family=Source+Sans+3:wght@400;600;700&family=JetBrains+Mono:wght@400;600;700&display=swap">
  
  <style>
    /* ============================================================
       TARGET INTERNATIONAL SCHOOL — Vibecoding Portali Dizayn Tizimi
       Navy #00214A · Qizil #FF1100 · Dark/Light Mavzusi
       ============================================================ */
    :root {{
      --bg: #F4F7FC;
      --panel: #FFFFFF;
      --panel-2: #E8EEF8;
      --card-hover: #F0F4FA;
      --ink: #00214A;
      --ink-2: #46587A;
      --ink-3: #7588A3;
      --rule: #D1DCEB;
      --accent: #FF1100;
      --accent-ink: #C21000;
      --accent-soft: #FFE6E3;
      --ok: #0B6B4F;
      --ok-soft: #DDF0E8;
      --shadow-sm: 0 2px 8px rgba(0, 33, 74, 0.05);
      --shadow-md: 0 8px 24px rgba(0, 33, 74, 0.08);
      --shadow-lg: 0 16px 40px rgba(0, 33, 74, 0.12);
      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 20px;
    }}

    @media (prefers-color-scheme: dark) {{
      :root:not([data-theme="light"]) {{
        --bg: #061530;
        --panel: #0E2249;
        --panel-2: #16305A;
        --card-hover: #153266;
        --ink: #E9EFF8;
        --ink-2: #A2B4CE;
        --ink-3: #70859F;
        --rule: #1E3A63;
        --accent: #FF3B26;
        --accent-ink: #FF7563;
        --accent-soft: #3B140F;
        --ok: #7FD3B2;
        --ok-soft: #0F2E26;
        --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.3);
        --shadow-md: 0 8px 24px rgba(0, 0, 0, 0.4);
        --shadow-lg: 0 16px 40px rgba(0, 0, 0, 0.6);
      }}
    }}

    :root[data-theme="dark"] {{
      --bg: #061530;
      --panel: #0E2249;
      --panel-2: #16305A;
      --card-hover: #153266;
      --ink: #E9EFF8;
      --ink-2: #A2B4CE;
      --ink-3: #70859F;
      --rule: #1E3A63;
      --accent: #FF3B26;
      --accent-ink: #FF7563;
      --accent-soft: #3B140F;
      --ok: #7FD3B2;
      --ok-soft: #0F2E26;
      --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.3);
      --shadow-md: 0 8px 24px rgba(0, 0, 0, 0.4);
      --shadow-lg: 0 16px 40px rgba(0, 0, 0, 0.6);
    }}

    :root[data-theme="light"] {{
      --bg: #F4F7FC;
      --panel: #FFFFFF;
      --panel-2: #E8EEF8;
      --card-hover: #F0F4FA;
      --ink: #00214A;
      --ink-2: #46587A;
      --ink-3: #7588A3;
      --rule: #D1DCEB;
      --accent: #FF1100;
      --accent-ink: #C21000;
      --accent-soft: #FFE6E3;
      --ok: #0B6B4F;
      --ok-soft: #DDF0E8;
      --shadow-sm: 0 2px 8px rgba(0, 33, 74, 0.05);
      --shadow-md: 0 8px 24px rgba(0, 33, 74, 0.08);
      --shadow-lg: 0 16px 40px rgba(0, 33, 74, 0.12);
    }}

    /* Global Resets & Typography */
    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: "Source Sans 3", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: var(--bg);
      color: var(--ink);
      line-height: 1.5;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      -webkit-font-smoothing: antialiased;
      transition: background 0.25s ease, color 0.25s ease;
    }}

    /* Scrollbars */
    * {{ scrollbar-width: thin; scrollbar-color: var(--rule) transparent; }}
    ::-webkit-scrollbar {{ width: 8px; height: 8px; }}
    ::-webkit-scrollbar-track {{ background: transparent; }}
    ::-webkit-scrollbar-thumb {{ background: var(--rule); border-radius: 99px; }}
    ::-webkit-scrollbar-thumb:hover {{ background: var(--ink-3); }}

    /* Brand Top Rule */
    .brandrule {{
      height: 4px;
      width: 100%;
      background: linear-gradient(to right, var(--ink) 0 64%, var(--accent) 64% 100%);
      position: sticky;
      top: 0;
      z-index: 1000;
    }}

    /* Brandmark Logolar */
    .brandmark {{
      display: inline-block;
      line-height: 0;
      max-width: 190px;
    }}
    .brandmark img {{
      display: block;
      width: 100%;
      height: auto;
    }}
    .brandmark .on-dark {{ display: none; }}
    @media (prefers-color-scheme: dark) {{
      :root:not([data-theme="light"]) .brandmark .on-light {{ display: none; }}
      :root:not([data-theme="light"]) .brandmark .on-dark {{ display: block; }}
    }}
    :root[data-theme="dark"] .brandmark .on-light {{ display: none; }}
    :root[data-theme="dark"] .brandmark .on-dark {{ display: block; }}

    /* Layout Containers */
    .container {{
      width: 100%;
      max-width: 1360px;
      margin: 0 auto;
      padding: 0 clamp(16px, 3vw, 36px);
    }}

    /* Header */
    header.site-header {{
      background: var(--panel);
      border-bottom: 1px solid var(--rule);
      box-shadow: var(--shadow-sm);
      position: sticky;
      top: 4px;
      z-index: 990;
      backdrop-filter: blur(12px);
    }}
    .header-inner {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 20px;
      padding: 14px 0;
      flex-wrap: wrap;
    }}
    .brand-section {{
      display: flex;
      align-items: center;
      gap: 18px;
      text-decoration: none;
      color: inherit;
    }}
    .header-text {{
      display: flex;
      flex-direction: column;
    }}
    .header-text h1 {{
      font-family: "Manrope", sans-serif;
      font-weight: 800;
      font-size: 19px;
      letter-spacing: -0.02em;
      color: var(--ink);
      line-height: 1.2;
    }}
    .header-text p {{
      font-size: 13px;
      color: var(--ink-2);
      font-weight: 500;
    }}

    /* Controls: Search, Lang, Theme */
    .header-controls {{
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }}

    .search-box {{
      position: relative;
      min-width: 260px;
    }}
    .search-box input {{
      width: 100%;
      padding: 9px 14px 9px 36px;
      font-family: inherit;
      font-size: 14px;
      background: var(--bg);
      border: 1px solid var(--rule);
      border-radius: var(--radius-sm);
      color: var(--ink);
      outline: none;
      transition: all 0.2s ease;
    }}
    .search-box input:focus {{
      border-color: var(--accent);
      box-shadow: 0 0 0 3px var(--accent-soft);
    }}
    .search-box svg {{
      position: absolute;
      left: 11px;
      top: 50%;
      transform: translateY(-50%);
      width: 16px;
      height: 16px;
      stroke: var(--ink-3);
      pointer-events: none;
    }}

    .btn-group {{
      display: inline-flex;
      background: var(--bg);
      border: 1px solid var(--rule);
      border-radius: var(--radius-sm);
      padding: 2px;
      gap: 2px;
    }}
    .btn-group button {{
      background: transparent;
      border: 0;
      color: var(--ink-2);
      font-family: "JetBrains Mono", monospace;
      font-size: 12px;
      font-weight: 600;
      padding: 5px 10px;
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .btn-group button.active, .btn-group button:hover {{
      background: var(--panel);
      color: var(--accent-ink);
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }}

    .theme-toggle {{
      background: var(--bg);
      border: 1px solid var(--rule);
      color: var(--ink-2);
      padding: 7px 11px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      font-size: 14px;
      display: flex;
      align-items: center;
      gap: 6px;
      font-family: inherit;
      font-weight: 600;
      transition: all 0.15s ease;
    }}
    .theme-toggle:hover {{
      color: var(--ink);
      border-color: var(--ink-3);
    }}

    /* Main Content Area */
    main.portal-main {{
      flex: 1;
      padding: 32px 0 64px;
    }}

    /* Breadcrumbs & Active Path Bar */
    .path-banner {{
      background: var(--panel);
      border: 1px solid var(--rule);
      border-radius: var(--radius-md);
      padding: 14px 20px;
      margin-bottom: 28px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      box-shadow: var(--shadow-sm);
      flex-wrap: wrap;
    }}
    .breadcrumbs {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 14px;
      color: var(--ink-2);
      font-weight: 600;
    }}
    .breadcrumbs a, .breadcrumbs span.crumb-btn {{
      color: var(--ink-2);
      text-decoration: none;
      cursor: pointer;
      transition: color 0.15s;
    }}
    .breadcrumbs a:hover, .breadcrumbs span.crumb-btn:hover {{
      color: var(--accent-ink);
    }}
    .breadcrumbs .crumb-sep {{
      color: var(--ink-3);
      font-size: 12px;
    }}
    .breadcrumbs .crumb-current {{
      color: var(--ink);
      font-weight: 700;
    }}

    .path-slug {{
      font-family: "JetBrains Mono", monospace;
      font-size: 12px;
      padding: 4px 10px;
      background: var(--bg);
      border: 1px solid var(--rule);
      border-radius: 6px;
      color: var(--ink-3);
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .copy-slug-btn {{
      background: none;
      border: none;
      cursor: pointer;
      color: var(--accent-ink);
      font-size: 11px;
      font-family: inherit;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}
    .copy-slug-btn:hover {{
      text-decoration: underline;
    }}

    /* Step Section Headers */
    .step-header {{
      margin-bottom: 20px;
      display: flex;
      align-items: flex-end;
      justify-content: space-between;
      gap: 16px;
      border-bottom: 2px solid var(--rule);
      padding-bottom: 12px;
    }}
    .step-title-group {{
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}
    .step-badge {{
      font-family: "JetBrains Mono", monospace;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--accent-ink);
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }}
    .step-badge::after {{
      content: "";
      width: 24px;
      height: 2px;
      background: var(--accent);
    }}
    .step-heading {{
      font-family: "Manrope", sans-serif;
      font-weight: 800;
      font-size: clamp(22px, 2.5vw, 28px);
      color: var(--ink);
      letter-spacing: -0.02em;
    }}
    .step-desc {{
      font-size: 14px;
      color: var(--ink-2);
    }}

    /* Step 1: Cohort Cards Grid */
    .cohort-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(290px, 1fr));
      gap: 20px;
      margin-bottom: 36px;
    }}
    .cohort-card {{
      background: var(--panel);
      border: 2px solid var(--rule);
      border-radius: var(--radius-lg);
      padding: 24px;
      cursor: pointer;
      transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 16px;
      position: relative;
      overflow: hidden;
      box-shadow: var(--shadow-sm);
    }}
    .cohort-card:hover {{
      border-color: var(--accent);
      transform: translateY(-4px);
      box-shadow: var(--shadow-md);
    }}
    .cohort-card.selected {{
      border-color: var(--accent);
      background: var(--card-hover);
      box-shadow: var(--shadow-md);
    }}
    .cohort-card.selected::before {{
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 5px;
      background: linear-gradient(to right, var(--ink) 0 64%, var(--accent) 64% 100%);
    }}
    .cohort-card-top {{
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}
    .cohort-icon {{
      font-size: 32px;
    }}
    .cohort-track-badge {{
      font-family: "JetBrains Mono", monospace;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      padding: 4px 10px;
      border-radius: 99px;
      background: var(--panel-2);
      color: var(--accent-ink);
      letter-spacing: 0.05em;
    }}
    .cohort-card-title {{
      font-family: "Manrope", sans-serif;
      font-size: 20px;
      font-weight: 800;
      color: var(--ink);
      line-height: 1.3;
    }}
    .cohort-card-desc {{
      font-size: 14px;
      color: var(--ink-2);
      line-height: 1.5;
    }}
    .cohort-card-footer {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 13px;
      color: var(--ink-3);
      font-weight: 600;
      border-top: 1px solid var(--rule);
      padding-top: 14px;
    }}
    .select-arrow {{
      color: var(--accent);
      font-size: 18px;
      transition: transform 0.2s;
    }}
    .cohort-card:hover .select-arrow {{
      transform: translateX(4px);
    }}

    /* Step 2: Week Navigation Tabs */
    .week-nav-container {{
      background: var(--panel);
      border: 1px solid var(--rule);
      border-radius: var(--radius-md);
      padding: 12px 16px;
      margin-bottom: 28px;
      box-shadow: var(--shadow-sm);
    }}
    .week-nav {{
      display: flex;
      gap: 10px;
      overflow-x: auto;
      scrollbar-width: none;
      padding-bottom: 2px;
    }}
    .week-nav::-webkit-scrollbar {{ display: none; }}
    .week-pill {{
      background: var(--bg);
      border: 1px solid var(--rule);
      color: var(--ink-2);
      padding: 10px 18px;
      border-radius: 10px;
      font-family: "Manrope", sans-serif;
      font-weight: 700;
      font-size: 14px;
      white-space: nowrap;
      cursor: pointer;
      transition: all 0.18s ease;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .week-pill:hover {{
      border-color: var(--accent);
      color: var(--ink);
    }}
    .week-pill.active {{
      background: var(--ink);
      border-color: var(--ink);
      color: var(--bg);
      box-shadow: var(--shadow-sm);
    }}
    .week-pill.active .week-count {{
      background: var(--bg);
      color: var(--ink);
    }}
    .week-count {{
      font-family: "JetBrains Mono", monospace;
      font-size: 11px;
      background: rgba(255,255,255,0.2);
      padding: 2px 7px;
      border-radius: 99px;
    }}
    .week-pill:not(.active) .week-count {{
      background: var(--panel-2);
      color: var(--accent-ink);
    }}

    /* Step 3: Lessons Grid */
    .lessons-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
      gap: 24px;
    }}
    .lesson-card {{
      background: var(--panel);
      border: 1px solid var(--rule);
      border-radius: var(--radius-lg);
      padding: 24px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 18px;
      box-shadow: var(--shadow-sm);
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
    }}
    .lesson-card:hover {{
      border-color: var(--accent);
      box-shadow: var(--shadow-md);
      transform: translateY(-3px);
    }}
    .lesson-card.highlighted {{
      border-color: var(--accent);
      box-shadow: 0 0 0 3px var(--accent-soft), var(--shadow-lg);
    }}
    .lesson-card-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
    }}
    .lesson-num-badge {{
      font-family: "JetBrains Mono", monospace;
      font-size: 12px;
      font-weight: 700;
      background: var(--panel-2);
      color: var(--accent-ink);
      padding: 4px 10px;
      border-radius: 6px;
      border: 1px solid var(--rule);
    }}
    .lesson-week-tag {{
      font-family: "JetBrains Mono", monospace;
      font-size: 11px;
      color: var(--ink-3);
      font-weight: 600;
    }}
    .lesson-title {{
      font-family: "Manrope", sans-serif;
      font-weight: 800;
      font-size: 18px;
      line-height: 1.35;
      color: var(--ink);
    }}
    .lesson-lede {{
      font-size: 14px;
      color: var(--ink-2);
      line-height: 1.5;
      display: -webkit-box;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }}

    /* Action Buttons within Card */
    .lesson-actions {{
      display: flex;
      flex-direction: column;
      gap: 8px;
      border-top: 1px solid var(--rule);
      padding-top: 16px;
    }}
    .action-row {{
      display: flex;
      gap: 8px;
      width: 100%;
    }}
    .btn-action {{
      flex: 1;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 7px;
      padding: 9px 12px;
      font-family: "Manrope", sans-serif;
      font-size: 13px;
      font-weight: 700;
      text-decoration: none;
      border-radius: var(--radius-sm);
      transition: all 0.15s ease;
      cursor: pointer;
    }}
    .btn-primary {{
      background: var(--ink);
      color: var(--bg);
      border: 1px solid var(--ink);
    }}
    .btn-primary:hover {{
      background: var(--accent);
      border-color: var(--accent);
      color: #FFFFFF;
    }}
    .btn-secondary {{
      background: var(--panel-2);
      color: var(--ink);
      border: 1px solid var(--rule);
    }}
    .btn-secondary:hover {{
      background: var(--card-hover);
      border-color: var(--ink-3);
    }}
    .btn-lab {{
      background: linear-gradient(135deg, #10b981 0%, #059669 100%);
      color: #FFFFFF;
      border: none;
    }}
    .btn-lab:hover {{
      opacity: 0.92;
      box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
    }}
    .btn-link-copy {{
      background: transparent;
      border: 1px solid var(--rule);
      color: var(--ink-3);
      padding: 6px 10px;
      border-radius: var(--radius-sm);
      font-size: 11px;
      font-family: "JetBrains Mono", monospace;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 5px;
      transition: all 0.15s ease;
    }}
    .btn-link-copy:hover {{
      color: var(--ink);
      border-color: var(--ink-2);
    }}

    /* Live Search Results View */
    .search-summary {{
      margin-bottom: 24px;
      font-size: 16px;
      color: var(--ink-2);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}
    .clear-search-btn {{
      background: none;
      border: none;
      color: var(--accent-ink);
      font-weight: 700;
      cursor: pointer;
      font-family: inherit;
    }}

    /* Toast Notification */
    .toast {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: var(--ink);
      color: var(--bg);
      padding: 12px 20px;
      border-radius: var(--radius-sm);
      font-size: 14px;
      font-weight: 600;
      box-shadow: var(--shadow-lg);
      transform: translateY(100px);
      opacity: 0;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      z-index: 2000;
      border-left: 4px solid var(--accent);
    }}
    .toast.show {{
      transform: translateY(0);
      opacity: 1;
    }}

    /* Footer */
    footer.site-footer {{
      background: var(--panel);
      border-top: 1px solid var(--rule);
      padding: 32px 0;
      margin-top: auto;
      font-size: 13px;
      color: var(--ink-2);
    }}
    .footer-inner {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 20px;
      flex-wrap: wrap;
    }}
    .footer-links {{
      display: flex;
      gap: 16px;
    }}
    .footer-links a {{
      color: var(--ink-2);
      text-decoration: none;
      font-weight: 600;
    }}
    .footer-links a:hover {{
      color: var(--accent-ink);
    }}

    /* Empty state */
    .empty-state {{
      text-align: center;
      padding: 60px 20px;
      background: var(--panel);
      border: 1px dashed var(--rule);
      border-radius: var(--radius-lg);
      grid-column: 1 / -1;
    }}
    .empty-state h3 {{
      font-family: "Manrope", sans-serif;
      font-size: 20px;
      color: var(--ink);
      margin-bottom: 8px;
    }}
    .empty-state p {{
      color: var(--ink-2);
    }}

    @media (max-width: 768px) {{
      .lessons-grid {{
        grid-template-columns: 1fr;
      }}
      .search-box {{
        min-width: 100%;
        order: 3;
      }}
      .path-banner {{
        flex-direction: column;
        align-items: flex-start;
      }}
    }}
  </style>
</head>
<body>
  <!-- Brand Rule -->
  <div class="brandrule"></div>

  <!-- Header -->
  <header class="site-header">
    <div class="container header-inner">
      <a href="#/" class="brand-section" onclick="window.navigateToCohort(null); return false;">
        <span class="brandmark">
          <img class="on-light" src="{light_logo}" alt="Target Logo">
          <img class="on-dark" src="{dark_logo}" alt="Target Logo">
        </span>
        <div class="header-text">
          <h1 data-ru="Портал Уроков Vibecoding" data-en="Vibecoding Course Portal">Vibecoding Dars Portali</h1>
          <p data-ru="Target International School · 5–11 классы" data-en="Target International School · Grades 5–11">Target International School · 5–11-sinflar</p>
        </div>
      </a>

      <div class="header-controls">
        <div class="search-box">
          <svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
          </svg>
          <input type="text" id="searchInput" placeholder="Dars yoki mavzuni qidirish..." data-ru-ph="Поиск урока или темы..." data-en-ph="Search lesson or topic...">
        </div>

        <div class="btn-group" id="langSwitcher">
          <button type="button" data-lang="uz" class="active">UZ</button>
          <button type="button" data-lang="ru">RU</button>
          <button type="button" data-lang="en">EN</button>
        </div>

        <button type="button" class="theme-toggle" id="themeToggle" title="Mavzuni almashtirish">
          <span id="themeIcon">🌙</span>
        </button>
      </div>
    </div>
  </header>

  <!-- Main Portal -->
  <main class="portal-main">
    <div class="container">
      
      <!-- Path & Breadcrumb Banner -->
      <section class="path-banner" id="pathBanner">
        <div class="breadcrumbs" id="breadcrumbTrail">
          <span class="crumb-btn" onclick="window.navigateToCohort(null)">🏠 <span data-ru="Главная" data-en="Home">Bosh sahifa</span></span>
        </div>
        <div class="path-slug">
          <span>PATH:</span>
          <strong id="currentPathDisplay">/</strong>
          <button type="button" class="copy-slug-btn" id="copyPathBtn" title="Havolani nusxalash" data-ru="Копировать URL" data-en="Copy URL">Nusxa olish</button>
        </div>
      </section>

      <!-- Search Results Area (Hidden by default) -->
      <section id="searchResultsSection" style="display: none; margin-bottom: 36px;">
        <div class="search-summary">
          <div><span data-ru="Результаты поиска для:" data-en="Search results for:">Qidiruv natijalari:</span> <b id="searchQueryText"></b> (<span id="searchResultCount">0</span>)</div>
          <button type="button" class="clear-search-btn" id="clearSearchBtn" data-ru="Очистить поиск" data-en="Clear search">✕ Qidiruvni tozalash</button>
        </div>
        <div class="lessons-grid" id="searchResultsGrid"></div>
      </section>

      <!-- Standard Step-by-Step Flow -->
      <div id="standardFlow">
        
        <!-- Step 1: Select Cohort -->
        <section id="cohortSection">
          <div class="step-header">
            <div class="step-title-group">
              <div class="step-badge">1-BOSQICH · STEP 1</div>
              <h2 class="step-heading" data-ru="Выберите класс (когорту)" data-en="Select Class Cohort">Sinfni (Kohortani) Tanlang</h2>
              <p class="step-desc" data-ru="Каждая когорта имеет специализированный трек обучения" data-en="Each cohort follows a specialized engineering track">Har bir kohorta o'ziga xos amaliy dasturga ega</p>
            </div>
          </div>
          <div class="cohort-grid" id="cohortsGrid"></div>
        </section>

        <!-- Step 2 & 3: Weeks & Lessons (Visible when a cohort is active) -->
        <section id="lessonsSection" style="display: none;">
          <div class="step-header">
            <div class="step-title-group">
              <div class="step-badge">2 & 3-BOSQICH · STEPS 2 & 3</div>
              <h2 class="step-heading" id="selectedCohortTitle">Darslar Ro'yxati</h2>
              <p class="step-desc" id="selectedCohortDesc"></p>
            </div>
          </div>

          <!-- Week selector tabs -->
          <div class="week-nav-container">
            <div class="week-nav" id="weekTabs"></div>
          </div>

          <!-- Lessons Grid -->
          <div class="lessons-grid" id="lessonsGrid"></div>
        </section>

      </div>

    </div>
  </main>

  <!-- Toast notification -->
  <div class="toast" id="toast">Havola buferga nusxalandi!</div>

  <!-- Footer -->
  <footer class="site-footer">
    <div class="container footer-inner">
      <div>
        <strong>Target International School</strong> · Yunusobod Filiali · IT Ta'lim Dasturi
      </div>
      <div class="footer-links">
        <span data-ru="Преподаватель:" data-en="Teacher:">O'qituvchi:</span> <strong>Ismoiljon Usmonov</strong>
        <span>·</span>
        <span>24 dars/hafta</span>
        <span>·</span>
        <span>108 darslik reja</span>
      </div>
    </div>
  </footer>

  <!-- Raw Embedded JSON Data -->
  <script>
    window.COURSE_DATA = {data_json};
  </script>

  <!-- Interactive Logic & Router -->
  <script>
    (function() {{
      var currentLang = localStorage.getItem('vc-lang') || 'uz';
      var currentTheme = localStorage.getItem('vc-theme') || 'dark';
      var activeCohortId = null;
      var activeWeekId = null;
      var activeLessonId = null;

      // Apply initial theme
      function applyTheme(theme) {{
        currentTheme = theme;
        if (theme === 'auto') {{
          document.documentElement.removeAttribute('data-theme');
        }} else {{
          document.documentElement.setAttribute('data-theme', theme);
        }}
        localStorage.setItem('vc-theme', theme);
        var icon = document.getElementById('themeIcon');
        if (icon) {{
          icon.textContent = theme === 'dark' ? '☀️' : '🌙';
        }}
      }}
      applyTheme(currentTheme);

      // Theme toggle button
      document.getElementById('themeToggle').addEventListener('click', function() {{
        var next = (currentTheme === 'dark') ? 'light' : 'dark';
        applyTheme(next);
      }});

      // Language Switcher
      function applyLang(lang) {{
        currentLang = lang;
        document.documentElement.setAttribute('data-lang', lang);
        localStorage.setItem('vc-lang', lang);

        // Update active class in button group
        var btns = document.querySelectorAll('#langSwitcher button');
        btns.forEach(function(b) {{
          b.classList.toggle('active', b.getAttribute('data-lang') === lang);
        }});

        // Update static elements with data-ru / data-en
        document.querySelectorAll('[data-' + lang + ']').forEach(function(el) {{
          var trans = el.getAttribute('data-' + lang);
          if (trans) el.textContent = trans;
        }});

        // Update placeholder
        var searchInp = document.getElementById('searchInput');
        if (searchInp) {{
          var ph = searchInp.getAttribute('data-' + lang + '-ph') || searchInp.getAttribute('placeholder');
          searchInp.setAttribute('placeholder', ph);
        }}

        // Re-render UI
        renderCohorts();
        if (activeCohortId) {{
          renderCohortDetails(activeCohortId, activeWeekId, activeLessonId);
        }}
        renderBreadcrumbs();
      }}

      document.querySelectorAll('#langSwitcher button').forEach(function(btn) {{
        btn.addEventListener('click', function() {{
          applyLang(this.getAttribute('data-lang'));
        }});
      }});

      // Toast Helper
      function showToast(msg) {{
        var t = document.getElementById('toast');
        t.textContent = msg;
        t.classList.add('show');
        setTimeout(function() {{
          t.classList.remove('show');
        }}, 2400);
      }}

      // Path display & clipboard
      function updatePathDisplay(path) {{
        document.getElementById('currentPathDisplay').textContent = path;
      }}

      document.getElementById('copyPathBtn').addEventListener('click', function() {{
        var fullUrl = window.location.href;
        navigator.clipboard.writeText(fullUrl).then(function() {{
          showToast(currentLang === 'ru' ? 'Ссылка скопирована!' : (currentLang === 'en' ? 'Link copied!' : 'Havola nusxalandi!'));
        }});
      }});

      // Render Step 1: Cohorts Grid
      function renderCohorts() {{
        var grid = document.getElementById('cohortsGrid');
        grid.innerHTML = '';

        window.COURSE_DATA.forEach(function(c) {{
          var card = document.createElement('div');
          card.className = 'cohort-card' + (c.id === activeCohortId ? ' selected' : '');
          card.onclick = function() {{
            window.navigateToCohort(c.id);
          }};

          var titleText = c.title[currentLang] || c.title.uz;
          var descText = c.desc[currentLang] || c.desc.uz;

          // Count total lessons
          var lessonCount = 0;
          c.weeks.forEach(function(w) {{ lessonCount += w.lessons.length; }});

          card.innerHTML = `
            <div class="cohort-card-top">
              <span class="cohort-icon">${{c.icon}}</span>
              <span class="cohort-track-badge">${{c.badge}}</span>
            </div>
            <div>
              <h3 class="cohort-card-title">${{titleText}}</h3>
              <p class="cohort-card-desc">${{descText}}</p>
            </div>
            <div class="cohort-card-footer">
              <span><b>${{c.weeks.length}}</b> ${{currentLang === 'ru' ? 'недели' : (currentLang === 'en' ? 'weeks' : 'hafta')}} · <b>${{lessonCount}}</b> ${{currentLang === 'ru' ? 'уроков' : (currentLang === 'en' ? 'lessons' : 'dars')}}</span>
              <span class="select-arrow">→</span>
            </div>
          `;
          grid.appendChild(card);
        }});
      }}

      // Render Step 2 & 3: Weeks and Lessons
      function renderCohortDetails(cohortId, weekId, highlightLessonId) {{
        var cohort = window.COURSE_DATA.find(function(c) {{ return c.id === cohortId; }});
        if (!cohort) return;

        var lessonsSec = document.getElementById('lessonsSection');
        lessonsSec.style.display = 'block';

        // Title and description
        document.getElementById('selectedCohortTitle').textContent = cohort.title[currentLang] || cohort.title.uz;
        document.getElementById('selectedCohortDesc').textContent = cohort.desc[currentLang] || cohort.desc.uz;

        // Render Week tabs
        var tabsCont = document.getElementById('weekTabs');
        tabsCont.innerHTML = '';

        // "All weeks" pill
        var allPill = document.createElement('button');
        allPill.type = 'button';
        allPill.className = 'week-pill' + (!weekId ? ' active' : '');
        var totalLessons = 0;
        cohort.weeks.forEach(function(w) {{ totalLessons += w.lessons.length; }});
        allPill.innerHTML = `<span>${{currentLang === 'ru' ? 'Все недели' : (currentLang === 'en' ? 'All Weeks' : 'Barcha haftalar')}}</span><span class="week-count">${{totalLessons}}</span>`;
        allPill.onclick = function() {{
          window.navigateToWeek(cohortId, null);
        }};
        tabsCont.appendChild(allPill);

        cohort.weeks.forEach(function(w) {{
          var pill = document.createElement('button');
          pill.type = 'button';
          pill.className = 'week-pill' + (w.id === weekId ? ' active' : '');
          var wTitle = w.title[currentLang] || w.title.uz;
          pill.innerHTML = `<span>${{wTitle}}</span><span class="week-count">${{w.lessons.length}}</span>`;
          pill.onclick = function() {{
            window.navigateToWeek(cohortId, w.id);
          }};
          tabsCont.appendChild(pill);
        }});

        // Render Lessons
        var lGrid = document.getElementById('lessonsGrid');
        lGrid.innerHTML = '';

        var weeksToShow = weekId ? cohort.weeks.filter(function(w) {{ return w.id === weekId; }}) : cohort.weeks;
        var renderedCount = 0;

        weeksToShow.forEach(function(w) {{
          w.lessons.forEach(function(les) {{
            renderedCount++;
            var card = document.createElement('div');
            card.id = 'lesson-' + les.id;
            card.className = 'lesson-card' + (les.id === highlightLessonId ? ' highlighted' : '');

            var lTitle = les.title[currentLang] || les.title.uz;
            var lLede = les.lede[currentLang] || les.lede.uz;
            var wTitle = w.title[currentLang] || w.title.uz;

            var presBtn = les.has_p ? `<a href="${{les.p_url}}" target="_blank" class="btn-action btn-primary">🖥️ ${{currentLang === 'ru' ? 'Презентация' : (currentLang === 'en' ? 'Presentation' : 'Prezentatsiya')}}</a>` : '';
            var varBtn = les.has_v ? `<a href="${{les.v_url}}" target="_blank" class="btn-action btn-secondary">📄 ${{currentLang === 'ru' ? 'Рабочий лист' : (currentLang === 'en' ? 'Worksheet' : 'Ishchi varaqa')}}</a>` : '';
            var labBtn = '';
            if (les.interactive_url) {{
              var labName = les.interactive_name ? (les.interactive_name[currentLang] || les.interactive_name.uz) : 'Lab / Arena';
              labBtn = `<a href="${{les.interactive_url}}" target="_blank" class="btn-action btn-lab">🧪 ${{labName}}</a>`;
            }}

            var lessonPath = '#/' + cohortId + '/' + w.id + '/' + les.id;

            card.innerHTML = `
              <div class="lesson-card-header">
                <span class="lesson-num-badge">${{les.num}}-dars</span>
                <span class="lesson-week-tag">${{w.id}}</span>
              </div>
              <div>
                <h3 class="lesson-title">${{lTitle}}</h3>
                ${{lLede ? `<p class="lesson-lede" style="margin-top:8px;">${{lLede}}</p>` : ''}}
              </div>
              <div class="lesson-actions">
                <div class="action-row">
                  ${{presBtn}}
                  ${{varBtn}}
                </div>
                ${{labBtn ? `<div class="action-row">${{labBtn}}</div>` : ''}}
                <div style="display:flex; justify-content:flex-end;">
                  <button type="button" class="btn-link-copy" onclick="window.copyLessonLink('${{cohortId}}', '${{w.id}}', '${{les.id}}')">
                    🔗 ${{currentLang === 'ru' ? 'Ссылка' : (currentLang === 'en' ? 'Permalink' : 'Havola')}}
                  </button>
                </div>
              </div>
            `;
            lGrid.appendChild(card);
          }});
        }});

        if (renderedCount === 0) {{
          lGrid.innerHTML = `
            <div class="empty-state">
              <h3>${{currentLang === 'ru' ? 'Уроки пока не добавлены' : (currentLang === 'en' ? 'No lessons yet' : 'Darslar hali yuklanmadi')}}</h3>
              <p>${{currentLang === 'ru' ? 'Для этой недели материал в разработке' : (currentLang === 'en' ? 'Materials for this week are in progress' : 'Bu hafta uchun materiallar tez orada qo\\'shiladi')}}</p>
            </div>
          `;
        }}

        // If highlightLessonId specified, scroll to it
        if (highlightLessonId) {{
          setTimeout(function() {{
            var el = document.getElementById('lesson-' + highlightLessonId);
            if (el) {{
              el.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
            }}
          }}, 100);
        }}
      }}

      // Breadcrumb builder
      function renderBreadcrumbs() {{
        var bc = document.getElementById('breadcrumbTrail');
        var homeLabel = currentLang === 'ru' ? 'Главная' : (currentLang === 'en' ? 'Home' : 'Bosh sahifa');
        
        var html = `<span class="crumb-btn" onclick="window.navigateToCohort(null)">🏠 ${{homeLabel}}</span>`;

        if (activeCohortId) {{
          var cohort = window.COURSE_DATA.find(function(c) {{ return c.id === activeCohortId; }});
          var cTitle = cohort ? (cohort.title[currentLang] || cohort.title.uz) : activeCohortId;
          html += ` <span class="crumb-sep">/</span> <span class="crumb-btn" onclick="window.navigateToCohort('${{activeCohortId}}')">${{cTitle}}</span>`;

          if (activeWeekId) {{
            html += ` <span class="crumb-sep">/</span> <span class="crumb-btn" onclick="window.navigateToWeek('${{activeCohortId}}', '${{activeWeekId}}')">${{activeWeekId}}</span>`;
          }}

          if (activeLessonId) {{
            html += ` <span class="crumb-sep">/</span> <span class="crumb-current">${{activeLessonId}}</span>`;
          }}
        }}

        bc.innerHTML = html;
      }}

      // Router & Deep Linking
      function handleRoute() {{
        var hash = window.location.hash || '#/';
        // strip leading #/ or #
        var path = hash.replace(/^#\\/?/, '');
        var segments = path ? path.split('/').filter(Boolean) : [];

        var cohortId = segments[0] || null;
        var weekId = segments[1] || null;
        var lessonId = segments[2] || null;

        activeCohortId = cohortId;
        activeWeekId = weekId;
        activeLessonId = lessonId;

        // Update path slug display
        updatePathDisplay('/' + (segments.join('/')));

        renderCohorts();

        var lessonsSec = document.getElementById('lessonsSection');
        if (activeCohortId) {{
          renderCohortDetails(activeCohortId, activeWeekId, activeLessonId);
          lessonsSec.style.display = 'block';
        }} else {{
          lessonsSec.style.display = 'none';
        }}

        renderBreadcrumbs();
      }}

      window.addEventListener('hashchange', handleRoute);

      // Navigation API
      window.navigateToCohort = function(cId) {{
        if (!cId) {{
          window.location.hash = '#/';
        }} else {{
          window.location.hash = '#/' + cId;
        }}
      }};

      window.navigateToWeek = function(cId, wId) {{
        if (!wId) {{
          window.location.hash = '#/' + cId;
        }} else {{
          window.location.hash = '#/' + cId + '/' + wId;
        }}
      }};

      window.copyLessonLink = function(cId, wId, lId) {{
        var url = window.location.origin + window.location.pathname + '#/' + cId + '/' + wId + '/' + lId;
        navigator.clipboard.writeText(url).then(function() {{
          showToast(currentLang === 'ru' ? 'Прямая ссылка скопирована!' : (currentLang === 'en' ? 'Direct link copied!' : 'Darsning to\\'g\\'ridan-to\\'g\\'ri havolasi nusxalandi!'));
        }});
      }};

      // Search functionality
      var searchInput = document.getElementById('searchInput');
      var searchSection = document.getElementById('searchResultsSection');
      var standardFlow = document.getElementById('standardFlow');
      var searchResultsGrid = document.getElementById('searchResultsGrid');
      var searchQueryText = document.getElementById('searchQueryText');
      var searchResultCount = document.getElementById('searchResultCount');
      var clearSearchBtn = document.getElementById('clearSearchBtn');

      function performSearch(query) {{
        var q = (query || '').trim().toLowerCase();
        if (!q) {{
          searchSection.style.display = 'none';
          standardFlow.style.display = 'block';
          return;
        }}

        searchSection.style.display = 'block';
        standardFlow.style.display = 'none';
        searchQueryText.textContent = query;

        var matches = [];
        window.COURSE_DATA.forEach(function(c) {{
          c.weeks.forEach(function(w) {{
            w.lessons.forEach(function(l) {{
              var uzT = (l.title.uz || '').toLowerCase();
              var ruT = (l.title.ru || '').toLowerCase();
              var enT = (l.title.en || '').toLowerCase();
              var uzL = (l.lede.uz || '').toLowerCase();
              var ruL = (l.lede.ru || '').toLowerCase();
              var enL = (l.lede.en || '').toLowerCase();
              var idS = l.id.toLowerCase();
              var numS = l.num;

              if (uzT.includes(q) || ruT.includes(q) || enT.includes(q) ||
                  uzL.includes(q) || ruL.includes(q) || enL.includes(q) ||
                  idS.includes(q) || numS === q) {{
                matches.push({{ cohort: c, week: w, lesson: l }});
              }}
            }});
          }});
        }});

        searchResultCount.textContent = matches.length;
        searchResultsGrid.innerHTML = '';

        if (matches.length === 0) {{
          searchResultsGrid.innerHTML = `
            <div class="empty-state">
              <h3>${{currentLang === 'ru' ? 'Ничего не найдено' : (currentLang === 'en' ? 'No results found' : 'Hech narsa topilmadi')}}</h3>
              <p>${{currentLang === 'ru' ? 'Попробуйте изменить поисковый запрос' : (currentLang === 'en' ? 'Try adjusting your search query' : 'Boshqa so\\'z yoki dars raqami bilan qidirib ko\\'ring')}}</p>
            </div>
          `;
          return;
        }}

        matches.forEach(function(item) {{
          var c = item.cohort;
          var w = item.week;
          var les = item.lesson;

          var card = document.createElement('div');
          card.className = 'lesson-card';

          var lTitle = les.title[currentLang] || les.title.uz;
          var lLede = les.lede[currentLang] || les.lede.uz;
          var cTitle = c.title[currentLang] || c.title.uz;

          var presBtn = les.has_p ? `<a href="${{les.p_url}}" target="_blank" class="btn-action btn-primary">🖥️ Prezentatsiya</a>` : '';
          var varBtn = les.has_v ? `<a href="${{les.v_url}}" target="_blank" class="btn-action btn-secondary">📄 Ishchi varaqa</a>` : '';
          var labBtn = les.interactive_url ? `<a href="${{les.interactive_url}}" target="_blank" class="btn-action btn-lab">🧪 Interaktiv Lab</a>` : '';

          card.innerHTML = `
            <div class="lesson-card-header">
              <span class="lesson-num-badge">${{c.badge}} · ${{les.num}}-dars</span>
              <span class="lesson-week-tag">${{w.id}}</span>
            </div>
            <div>
              <h3 class="lesson-title">${{lTitle}}</h3>
              ${{lLede ? `<p class="lesson-lede" style="margin-top:8px;">${{lLede}}</p>` : ''}}
            </div>
            <div class="lesson-actions">
              <div class="action-row">
                ${{presBtn}}
                ${{varBtn}}
              </div>
              ${{labBtn ? `<div class="action-row">${{labBtn}}</div>` : ''}}
              <div style="display:flex; justify-content:space-between; align-items:center;">
                <span style="font-size:12px; color:var(--ink-3); font-weight:600;">${{cTitle}}</span>
                <button type="button" class="btn-link-copy" onclick="window.copyLessonLink('${{c.id}}', '${{w.id}}', '${{les.id}}')">
                  🔗 Havola
                </button>
              </div>
            </div>
          `;
          searchResultsGrid.appendChild(card);
        }});
      }}

      searchInput.addEventListener('input', function(e) {{
        performSearch(e.target.value);
      }});

      clearSearchBtn.addEventListener('click', function() {{
        searchInput.value = '';
        performSearch('');
      }});

      // Initial boot
      applyLang(currentLang);
      handleRoute();

    }})();
  </script>
</body>
</html>
'''

    out_file = os.path.join(BASE_DIR, "index.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html_template)

    print(f"Successfully generated {out_file} ({len(html_template)} bytes)")

if __name__ == "__main__":
    generate_index_html()
