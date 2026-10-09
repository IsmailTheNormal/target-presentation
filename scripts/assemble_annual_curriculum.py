#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assemble the complete 36-week Annual Curriculum Data (scripts/annual_curriculum_data.py).
Combines weeks 1-5 from index.html (COURSE_DATA) with weeks 6-36 from cohort modules,
and integrates the official 108 Vibecoding master lessons from assets/reja_vibecoding.docx.
"""

import json
import re
import os
import sys

from cohort_10_11_data import WEEKS_10_11_PLANNED
from cohort_9_data import WEEKS_9_PLANNED
from cohort_7_8_data import WEEKS_7_8_PLANNED
from cohort_5_6_data import WEEKS_5_6_PLANNED

def load_existing_course_data():
    with open('index.html', 'r', encoding='utf-8') as f:
        text = f.read()
    m = re.search(r'window\.COURSE_DATA\s*=\s*(\[.*?\]);\s*</script>', text, re.DOTALL)
    if not m:
        raise ValueError("COURSE_DATA not found in index.html")
    return json.loads(m.group(1))

# Load the 108 lessons from vibecoding docx dump
with open('scripts/vibecoding_108_dump.json', 'r', encoding='utf-8') as f:
    dump = json.load(f)

vibecoding_108 = [x for x in dump if x['lesson_num'].isdigit()]

QUARTERS = [
    {
        "id": 1,
        "name": {
            "uz": "1-Chorak: Prompt Engineering, AI Dizayn va Kiberxavfsizlik",
            "ru": "1-я Четверть: Prompt Engineering, AI Дизайн и Кибербезопасность",
            "en": "Quarter 1: Prompt Engineering, AI Design and CyberSecurity"
        },
        "weeks": list(range(1, 10)),
        "weeks_str": "1–9-haftalar (9 hafta)",
        "focus": {
            "uz": "AI modellari asoslari, zamonaviy veb, kiber-gigiyena, xavfsiz API va boshlang'ich laboratoriyalar",
            "ru": "Основы AI моделей, современный веб, кибер-гигиена, безопасные API и базовые лаборатории",
            "en": "AI fundamentals, modern web, cyber-hygiene, secure APIs, and foundational laboratories"
        }
    },
    {
        "id": 2,
        "name": {
            "uz": "2-Chorak: Agentik Dasturlash va Avtonom Tizimlar",
            "ru": "2-я Четверть: Агентное Программирование и Автономные Системы",
            "en": "Quarter 2: Agentic Programming and Autonomous Systems"
        },
        "weeks": list(range(10, 19)),
        "weeks_str": "10–18-haftalar (9 hafta)",
        "focus": {
            "uz": "ReAct tsikllari, Tool calling, avtonom kod yozuvchi agentlar, multi-agent tizimlari va Scratch ilg'or mantig'i",
            "ru": "Циклы ReAct, Tool calling, кодовые агенты, мультиагентные системы и продвинутая логика Scratch",
            "en": "ReAct loops, Tool calling, autonomous coding agents, multi-agent systems, and advanced game logic"
        }
    },
    {
        "id": 3,
        "name": {
            "uz": "3-Chorak: AI Avtomatlashtirish, n8n, Make va MCP",
            "ru": "3-я Четверть: AI Автоматизация, n8n, Make и MCP",
            "en": "Quarter 3: AI Automation, n8n, Make, and Model Context Protocol (MCP)"
        },
        "weeks": list(range(19, 28)),
        "weeks_str": "19–27-haftalar (9 hafta)",
        "focus": {
            "uz": "Biznes jarayonlarni avtomatlashtirish, n8n workflow dvigateli, shaxsiy MCP serverlar va 3D grafika",
            "ru": "Автоматизация бизнес-процессов, движок n8n, кастомные MCP серверы и 3D графика",
            "en": "Business automation pipelines, n8n workflows, custom MCP servers, and 3D visual environments"
        }
    },
    {
        "id": 4,
        "name": {
            "uz": "4-Chorak: Amaliyot, Startap va Yakuniy Capstone Loyiha",
            "ru": "4-я Четверть: Практика, Стартап и Финальный Capstone Проект",
            "en": "Quarter 4: Industry Practice, Startup Incubator, and Final Capstone Project"
        },
        "weeks": list(range(28, 37)),
        "weeks_str": "28–36-haftalar (9 hafta)",
        "focus": {
            "uz": "PRD dan boshlab prodactiongacha bo'lgan to'liq SaaS/o'yin/loyiha sikli, jamoaviy muhandislik va Grand Demo Day",
            "ru": "Полный цикл от PRD до продакшна: SaaS/игры, командная разработка и финальный Grand Demo Day",
            "en": "Full production lifecycle from PRD to launch: SaaS, games, team engineering, and Grand Demo Day"
        }
    }
]

PLANNED_MAP = {
    "10-11-sinf": WEEKS_10_11_PLANNED,
    "9-sinf": WEEKS_9_PLANNED,
    "7-8-sinf": WEEKS_7_8_PLANNED,
    "5-6-sinf": WEEKS_5_6_PLANNED
}

HOURS_MAP = {
    "10-11-sinf": 5,
    "9-sinf": 5,
    "7-8-sinf": 5,
    "5-6-sinf": 6
}

def get_quarter_for_week(w_num):
    if 1 <= w_num <= 9:
        return 1
    elif 10 <= w_num <= 18:
        return 2
    elif 19 <= w_num <= 27:
        return 3
    else:
        return 4

def assemble():
    raw_cohorts = load_existing_course_data()
    annual_cohorts = []

    for cohort in raw_cohorts:
        cid = cohort['id']
        cohort_hours = HOURS_MAP.get(cid, 5)
        planned_weeks = PLANNED_MAP.get(cid, {})

        all_weeks = []
        # Weeks 1-5 from existing course data
        for w_idx, w in enumerate(cohort['weeks'], 1):
            w_copy = dict(w)
            w_copy['week_num'] = w_idx
            w_copy['quarter'] = get_quarter_for_week(w_idx)
            w_copy['quarter_info'] = QUARTERS[w_copy['quarter'] - 1]
            w_copy['hours'] = len(w.get('lessons', []))
            w_copy['status'] = "done"  # Completed with real materials
            all_weeks.append(w_copy)

        # Weeks 6-36 from planned database
        for w_num in range(6, 37):
            q_num = get_quarter_for_week(w_num)
            q_info = QUARTERS[q_num - 1]
            plan = planned_weeks.get(w_num, {
                "title": {"uz": f"{w_num}-hafta mavzusi", "ru": f"Тема {w_num}-й недели", "en": f"Week {w_num} Topic"},
                "type": {"uz": "Amaliy", "ru": "Практика", "en": "Practical"},
                "skills": {"uz": "O'quv ko'nikmalari", "ru": "Учебные навыки", "en": "Core skills"},
                "deliverable": {"uz": "Topshiriq natijasi", "ru": "Результат", "en": "Deliverable"},
                "tools": "VS Code"
            })

            # Form synthetic lessons list for uniform interface
            lessons_list = []
            for l_sub in range(1, cohort_hours + 1):
                lessons_list.append({
                    "id": f"w{w_num}-l{l_sub}",
                    "num": f"{w_num:02d}.{l_sub}",
                    "title": plan["title"],
                    "lede": plan["skills"],
                    "type": plan["type"],
                    "skills": plan["skills"],
                    "deliverable": plan["deliverable"],
                    "tools": plan["tools"],
                    "planned": True
                })

            w_obj = {
                "id": f"{w_num}-hafta",
                "week_num": w_num,
                "quarter": q_num,
                "quarter_info": q_info,
                "title": {
                    "uz": f"{w_num}-hafta: {plan['title']['uz']}",
                    "ru": f"{w_num}-я неделя: {plan['title']['ru']}",
                    "en": f"Week {w_num}: {plan['title']['en']}"
                },
                "hours": cohort_hours,
                "status": "planned",
                "plan": plan,
                "lessons": lessons_list
            }
            all_weeks.append(w_obj)

        total_hours = sum(w['hours'] for w in all_weeks)
        annual_cohorts.append({
            "id": cid,
            "title": cohort['title'],
            "badge": cohort.get('badge', ''),
            "icon": cohort.get('icon', '📌'),
            "desc": cohort['desc'],
            "weekly_hours": cohort_hours,
            "total_annual_hours": total_hours,
            "total_weeks": len(all_weeks),
            "weeks": all_weeks
        })

    # Write JSON data file
    with open('scripts/annual_curriculum_data.json', 'w', encoding='utf-8') as f:
        json.dump({
            "quarters": QUARTERS,
            "vibecoding_108": vibecoding_108,
            "cohorts": annual_cohorts
        }, f, ensure_ascii=False, indent=2)

    # Write clean Python loader module
    py_content = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Target International School — Yillik Taqvim-Mavzu Rejasi (36 Hafta / 4 Chorak)
Rasmiy yagona ma'lumotlar bazasi (annual_curriculum_data.py).
"""

import json
import os

_DATA_FILE = os.path.join(os.path.dirname(__file__), 'annual_curriculum_data.json')
with open(_DATA_FILE, 'r', encoding='utf-8') as f:
    _d = json.load(f)

QUARTERS_INFO = _d['quarters']
VIBECODING_108_MASTER = _d['vibecoding_108']
ANNUAL_COHORTS_DATA = _d['cohorts']
'''

    with open('scripts/annual_curriculum_data.py', 'w', encoding='utf-8') as f:
        f.write(py_content)


    print(f"Successfully assembled annual curriculum data for {len(annual_cohorts)} cohorts.")
    for c in annual_cohorts:
        done_weeks = sum(1 for w in c['weeks'] if w['status'] == 'done')
        planned_weeks = sum(1 for w in c['weeks'] if w['status'] == 'planned')
        print(f" - {c['id']}: {len(c['weeks'])} weeks ({done_weeks} done, {planned_weeks} planned), {c['total_annual_hours']} total hours.")
    print(f"Vibecoding 108 Master lessons: {len(vibecoding_108)} lessons.")

if __name__ == '__main__':
    assemble()
