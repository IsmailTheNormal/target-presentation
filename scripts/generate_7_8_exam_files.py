#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator for Grade 7-8 Lesson 28 (Midterm Review & Exam Simulator)
Generates:
1. classes/7-8-sinf/8-hafta/28-dars-katta-takrorlash-va-oraliq-nazorat/test.html
2. classes/7-8-sinf/8-hafta/28-dars-katta-takrorlash-va-oraliq-nazorat/google_form.gs
Teacher: Ismoiljon Usmonov · Target International School
"""

import os
import json
from scripts.generate_cohort_docx_tests import randomize_bilingual_options
from scripts.test_data_7_8 import QUESTIONS_7_8_UZ, QUESTIONS_7_8_RU

# English translations for the 25 questions, options, and explanations
QUESTIONS_7_8_EN = [
    # Q1: LLM
    {
        "text": "According to Lesson 1, how do Large Language Models (LLMs) assist us in programming?",
        "topic": "Lesson 01: LLM & Artificial Intelligence",
        "expl": "LLMs interpret natural language prompts and swiftly generate functional code for HTML, CSS, and JavaScript.",
        "a_orig": "They just play computer games on our behalf.",
        "b_orig": "They understand requirements in our prompts and rapidly generate HTML, CSS, and JavaScript code.",
        "c_orig": "They delete all system files from the computer.",
        "d_orig": "They clean dust from the computer monitor.",
        "e_orig": "They function solely as a basic calculator."
    },
    # Q2: Prompt Structure
    {
        "text": "In Lesson 2 ('AI Duel'), what prompt structure produces the highest quality code?",
        "topic": "Lesson 02: Prompt Engineering Structure",
        "expl": "A high-quality prompt clearly specifies the program's purpose, technologies, and required UI components.",
        "a_orig": "Leaving AI with no instructions and expecting miracles.",
        "b_orig": "Writing only a single ambiguous keyword.",
        "c_orig": "Clearly defining what the program should do, which languages to use, and which buttons are required.",
        "d_orig": "Writing prompts exclusively in black text.",
        "e_orig": "Sending only funny stickers and emojis to the AI."
    },
    # Q3: SVG Vectors
    {
        "text": "What is the primary advantage of the SVG (Scalable Vector Graphics) format learned in Lesson 3?",
        "topic": "Lesson 03: SVG Vector Graphics",
        "expl": "SVG is built using mathematical coordinates and formulas, so it never blurs or loses quality at any display resolution.",
        "a_orig": "It cannot be opened inside a web browser.",
        "b_orig": "Because it consists of vector coordinates, it never blurs and stays crisp at any display magnification.",
        "c_orig": "It can only be rendered in solid black.",
        "d_orig": "It occupies 10 gigabytes on disk.",
        "e_orig": "It is used exclusively for playing audio music."
    },
    # Q4: Semantic HTML <main>
    {
        "text": "In Lesson 5, which semantic HTML tag is used to wrap the central primary content of a webpage?",
        "topic": "Lesson 05: Semantic HTML (<main> tag)",
        "expl": "The <main> tag designates the unique, primary content of a webpage, distinct from headers, navbars, and footers.",
        "a_orig": "<marquee>",
        "b_orig": "<main>",
        "c_orig": "<sound>",
        "d_orig": "<secret>",
        "e_orig": "<game>"
    },
    # Q5: Flexbox justify-content
    {
        "text": "In Lesson 7, which CSS property is used in Flexbox to center elements along the main (horizontal) axis?",
        "topic": "Lesson 07: Flexbox & justify-content",
        "expl": "justify-content: center aligns flex items along the main horizontal axis, while align-items centers vertically.",
        "a_orig": "color: blue;",
        "b_orig": "justify-content: center;",
        "c_orig": "font-size: 100px;",
        "d_orig": "background: red;",
        "e_orig": "margin: -9999px;"
    },
    # Q6: addEventListener
    {
        "text": "In Lesson 8, how do we track and respond to button clicks using JavaScript?",
        "topic": "Lesson 08: addEventListener & Clicks",
        "expl": "btn.addEventListener('click', fn) listens for mouse click events and executes the assigned handler function.",
        "a_orig": "btn.listen('music')",
        "b_orig": "btn.addEventListener('click', () => { ... })",
        "c_orig": "btn.destroyComputer()",
        "d_orig": "btn.shutdownNow()",
        "e_orig": "btn.sleep(1000)"
    },
    # Q7: Cyber Reaction Time
    {
        "text": "In Lesson 9 ('Cyber Reaction'), what does reaction time measured in milliseconds (ms) represent?",
        "topic": "Lesson 09: Cyber Reaction & Milliseconds",
        "expl": "Reaction time measures the duration from when the screen turns green until the player clicks the button.",
        "a_orig": "The size of the computer screen in inches.",
        "b_orig": "The speed at which the user presses the button as soon as the screen turns green.",
        "c_orig": "The level of room brightness.",
        "d_orig": "How fast the laptop battery charges.",
        "e_orig": "Internet download speed in megabits."
    },
    # Q8: DevTools Console
    {
        "text": "In Lesson 10, where do developers check for JavaScript code errors and console.log outputs in the browser?",
        "topic": "Lesson 10: DevTools Console",
        "expl": "Browser DevTools (F12) Console displays error stack traces, warnings, and console.log output.",
        "a_orig": "Inside the browser address bar.",
        "b_orig": "In the DevTools Console (F12 / Inspect -> Console).",
        "c_orig": "On the computer keyboard.",
        "d_orig": "Inside a paper notebook.",
        "e_orig": "In the computer mouse settings."
    },
    # Q9: LocalStorage Persistence
    {
        "text": "In Lesson 11, when do game high scores saved to LocalStorage get erased?",
        "topic": "Lesson 11: LocalStorage Persistence",
        "expl": "LocalStorage retains data even when pages reload or browsers close; it remains until explicitly cleared.",
        "a_orig": "Immediately when the web page is reloaded.",
        "b_orig": "LocalStorage does not erase on page reload or browser restart; it persists indefinitely.",
        "c_orig": "Every 5 seconds automatically.",
        "d_orig": "Whenever the user presses the spacebar.",
        "e_orig": "Whenever a game character jumps."
    },
    # Q10: Vercel Deploy & HTTPS
    {
        "text": "In Lesson 12, what is the main benefit of deploying web projects to Vercel?",
        "topic": "Lesson 12: Vercel Deploy & HTTPS",
        "expl": "Vercel deploys web projects online with public HTTPS links and QR codes accessible from any device worldwide.",
        "a_orig": "It deletes project code permanently.",
        "b_orig": "It provides a public 24/7 web link (with HTTPS and QR code) accessible to anyone in the world.",
        "c_orig": "It turns the computer into a game console.",
        "d_orig": "It turns off the computer screen.",
        "e_orig": "It sends physical paper letters to friends."
    },
    # Q11: HTML5 Canvas
    {
        "text": "In Lesson 13, which HTML5 element is used as the drawing surface for 2D games via JavaScript?",
        "topic": "Lesson 13: HTML5 Canvas",
        "expl": "The <canvas> element provides a pixel-based surface where JavaScript draws shapes, sprites, and animations.",
        "a_orig": "<paint>",
        "b_orig": "<canvas>",
        "c_orig": "<draw>",
        "d_orig": "<screen>",
        "e_orig": "<pixel>"
    },
    # Q12: requestAnimationFrame & 60 FPS
    {
        "text": "In Lesson 13, which modern browser function synchronizes game rendering to achieve smooth 60 FPS?",
        "topic": "Lesson 13: requestAnimationFrame & 60 FPS",
        "expl": "requestAnimationFrame synchronizes frame execution with monitor refresh rate (60 FPS) and pauses when tabs are inactive.",
        "a_orig": "setInterval(fn, 1000)",
        "b_orig": "requestAnimationFrame(gameLoop)",
        "c_orig": "wait(5000)",
        "d_orig": "sleep(60)",
        "e_orig": "delayForever()"
    },
    # Q13: Array Push
    {
        "text": "In Lesson 14, which JavaScript array method appends newly spawned enemies to the enemies array?",
        "topic": "Lesson 14: Array Method (push)",
        "expl": "The .push() method appends new elements to the end of a JavaScript array.",
        "a_orig": "enemies.delete()",
        "b_orig": "enemies.push(newEnemy)",
        "c_orig": "enemies.stop()",
        "d_orig": "enemies.clearAll()",
        "e_orig": "enemies.explode()"
    },
    # Q14: Gravity Physics
    {
        "text": "In Lesson 15, how does gravity pull a jumping character back down toward the ground?",
        "topic": "Lesson 15: Game Physics & Gravity",
        "expl": "Gravity constantly adds downward acceleration: in each frame, vy += gravity pulls the character downward.",
        "a_orig": "vy = -100 (sending the hero flying off the screen).",
        "b_orig": "In each frame, gravity is added to vertical speed (vy += gravity), pulling the hero back down.",
        "c_orig": "The hero floats indefinitely in the sky without moving.",
        "d_orig": "The character completely disappears from the game screen.",
        "e_orig": "The screen turns off completely."
    },
    # Q15: Collision Detection
    {
        "text": "In Lesson 15, what is the term for calculating whether two game rectangles or boxes overlap?",
        "topic": "Lesson 15: Collision (AABB)",
        "expl": "AABB (Axis-Aligned Bounding Box) collision detection checks whether coordinates of two boxes intersect.",
        "a_orig": "Internet disconnection.",
        "b_orig": "Collision Detection (e.g. AABB bounding box algorithm).",
        "c_orig": "Font enlargement.",
        "d_orig": "Screen brightness dimming.",
        "e_orig": "Speaker volume change."
    },
    # Q16: Web Audio API
    {
        "text": "In Lesson 17, which built-in browser technology synthesizes retro jump and hit sounds without external MP3 files?",
        "topic": "Lesson 17: Web Audio API",
        "expl": "Web Audio API's AudioContext and OscillatorNode mathematically synthesize sound waves directly inside the browser.",
        "a_orig": "Microphone recording software.",
        "b_orig": "Web Audio API (AudioContext, OscillatorNode).",
        "c_orig": "VLC Media Player application.",
        "d_orig": "An external physical cassette player.",
        "e_orig": "Desktop wallpaper settings."
    },
    # Q17: Camera Scrolling
    {
        "text": "In Lesson 18, why does the camera follow the character when running across a wide world map?",
        "topic": "Lesson 18: Camera Viewport Scrolling",
        "expl": "The camera shifts the drawing viewport offset (cameraX = player.x - screenWidth/2) so the player stays visible.",
        "a_orig": "To delete all trees and obstacles.",
        "b_orig": "To keep the character inside view while revealing distant sections of the expanding game world.",
        "c_orig": "To turn the entire game screen completely black.",
        "d_orig": "To force the browser window to close immediately.",
        "e_orig": "To invert all canvas colors randomly."
    },
    # Q18: Touch Events
    {
        "text": "In Lesson 19, which event fires the instant a player touches a smartphone touchscreen?",
        "topic": "Lesson 19: Mobile Touch Events",
        "expl": "The 'touchstart' event fires when a finger makes contact with a touch surface, followed by touchmove and touchend.",
        "a_orig": "clickMouseRight",
        "b_orig": "touchstart",
        "c_orig": "keyboardEnter",
        "d_orig": "wheelRotate",
        "e_orig": "doubleClickOnly"
    },
    # Q19: FUT OVR Formula
    {
        "text": "In Lesson 21 ('FUT Card Studio'), what does a player card's OVR rating represent?",
        "topic": "Lesson 21: FUT OVR Overall Rating",
        "expl": "OVR represents a weighted composite calculation combining PAC, SHO, PAS, DRI, DEF, and PHY stats into an overall score.",
        "a_orig": "The player's shoe size.",
        "b_orig": "The weighted composite rating calculated from PAC, SHO, PAS, DRI, DEF, and PHY stats.",
        "c_orig": "The player's shirt color in hex code.",
        "d_orig": "The date when the game was purchased.",
        "e_orig": "The brightness level of the computer monitor."
    },
    # Q20: FUT Chemistry Graph
    {
        "text": "In Lesson 22 ('FUT Squad Builder'), how does having teammates from the same club affect team chemistry?",
        "topic": "Lesson 22: FUT Chemistry Graph",
        "expl": "Shared club, league, or nationality creates graph edges that boost individual chemistry up to 3 points per card (33 max).",
        "a_orig": "Card chemistry immediately drops to 0.",
        "b_orig": "A green chemistry link forms, adding bonus synergy points (+1, +2, or +3 per player).",
        "c_orig": "Cards instantly disappear from the pitch.",
        "d_orig": "All player stats drop to zero.",
        "e_orig": "The screen turns entirely green and locks up."
    },
    # Q21: EA 5% Coin Sink Tax
    {
        "text": "In Lesson 24, why does the FUT Transfer Market deduct a 5% transaction tax from every card sale?",
        "topic": "Lesson 24: FUT 5% Tax & Virtual Economy",
        "expl": "The 5% EA tax acts as a Coin Sink, removing excess virtual currency from circulation to prevent market hyperinflation.",
        "a_orig": "To purchase real paper tickets for players.",
        "b_orig": "To serve as a Coin Sink that destroys excess currency, preventing virtual economy hyperinflation.",
        "c_orig": "To arbitrarily punish winning players.",
        "d_orig": "To delete random cards from accounts.",
        "e_orig": "To make all cards cost zero coins."
    },
    # Q22: Target Jarvis Speech API
    {
        "text": "In Lesson 25 ('Target Jarvis'), which modern browser API converts spoken voice input into text?",
        "topic": "Lesson 25: Target Jarvis & Speech API",
        "expl": "The Web Speech API (SpeechRecognition) performs browser-native Speech-to-Text conversion.",
        "a_orig": "AudioBluetoothAdapter",
        "b_orig": "Web Speech API (SpeechRecognition)",
        "c_orig": "FileSystemAccessAPI",
        "d_orig": "CanvasRenderingContext2D",
        "e_orig": "LocalStorageSaveAPI"
    },
    # Q23: Computer Vision Motion Detector
    {
        "text": "In Lesson 26 ('Cyber Eye'), how does the webcam motion detector sense movement in the room?",
        "topic": "Lesson 26: Frame Differencing Motion Detection",
        "expl": "Frame Differencing compares pixel color values between consecutive video frames to detect changes above a threshold.",
        "a_orig": "By measuring air pressure in the room.",
        "b_orig": "By comparing pixel differences between consecutive video frames (Frame Differencing).",
        "c_orig": "By measuring room temperature with a thermometer.",
        "d_orig": "By calculating the weight of the webcam.",
        "e_orig": "By tracking internet Wi-Fi bandwidth."
    },
    # Q24: Biometric Face ID
    {
        "text": "In Lesson 27, which biometric landmarks does Face ID use to recognize an individual?",
        "topic": "Lesson 27: Biometric Face ID Landmarks",
        "expl": "Face ID maps 68 invariant anatomical skull landmarks (eye sockets, nose bridge, jawline) and checks Liveness with EAR.",
        "a_orig": "Daily hairstyle, beard length, and cosmetic lipstick color.",
        "b_orig": "68 invariant anatomical skull landmarks (IPD eye spacing, eye socket geometry, nose bridge, and EAR blink liveness).",
        "c_orig": "The color of the player's headphones.",
        "d_orig": "The brand logo printed on their hoodie.",
        "e_orig": "The size of their smartphone case."
    },
    # Q25: Vibecoder Engineering Mindset
    {
        "text": "In summary, what is the core engineering philosophy of a Grade 7–8 Vibecoder?",
        "topic": "Summary: Grade 7–8 Vibecoder Engineering Mindset",
        "expl": "A true Vibecoder doesn't just copy prompts—they master architecture, debug errors, build real products, and protect security.",
        "a_orig": "Mindlessly clicking without understanding how software works.",
        "b_orig": "Not merely copying AI prompts, but mastering architecture, debugging logic, building real projects, and understanding cyber systems.",
        "c_orig": "Only playing games instead of coding.",
        "d_orig": "Refusing to learn how loops and functions operate.",
        "e_orig": "Closing code editors and memorizing definitions without practice."
    }
]

def main():
    print("Generating Grade 7-8 Lesson 28 Exam Materials...")
    
    # Randomize with seed 708 (matches docx exactly)
    randomized_uz_ru = randomize_bilingual_options(QUESTIONS_7_8_UZ, QUESTIONS_7_8_RU, seed=708)
    
    # Now build the 25 items matching the docx randomization
    # We map each question to its corresponding English version and shuffled choices
    final_questions = []
    
    letters = ["a", "b", "c", "d", "e"]
    
    for idx, q_bilingual in enumerate(randomized_uz_ru):
        en_meta = QUESTIONS_7_8_EN[idx]
        
        # In the original QUESTIONS_7_8_UZ[idx], the correct answer was 'B'.
        # In en_meta, b_orig is the correct answer.
        # Let's map uz/ru choices to en_choices:
        orig_uz_q = QUESTIONS_7_8_UZ[idx]
        
        # Build mapping from uz text to en text
        uz_to_en = {
            orig_uz_q['a']: en_meta['a_orig'],
            orig_uz_q['b']: en_meta['b_orig'],
            orig_uz_q['c']: en_meta['c_orig'],
            orig_uz_q['d']: en_meta['d_orig'],
            orig_uz_q['e']: en_meta['e_orig']
        }
        
        item = {
            "num": idx + 1,
            "topic_uz": q_bilingual["topic_uz"],
            "topic_ru": q_bilingual["topic_ru"],
            "topic_en": en_meta["topic"],
            "text_uz": q_bilingual["text_uz"],
            "text_ru": q_bilingual["text_ru"],
            "text_en": en_meta["text"],
            "expl_uz": q_bilingual["expl_uz"],
            "expl_ru": q_bilingual["expl_ru"],
            "expl_en": en_meta["expl"],
            "correct": q_bilingual["correct"],  # A, B, C, D, or E
            "choices": []
        }
        
        for l in letters:
            uz_choice = q_bilingual[l + "_uz"]
            ru_choice = q_bilingual[l + "_ru"]
            en_choice = uz_to_en.get(uz_choice, uz_choice)
            is_correct = (l == q_bilingual["correct"].lower())
            
            item["choices"].append({
                "letter": l.upper(),
                "text_uz": uz_choice,
                "text_ru": ru_choice,
                "text_en": en_choice,
                "is_correct": is_correct
            })
            
        final_questions.append(item)
        
    print(f"Generated {len(final_questions)} paired questions with seed 708.")
    
    # 1. Build test.html
    generate_test_html(final_questions)
    
    # 2. Build google_form.gs
    generate_google_form_gs(final_questions)

def generate_test_html(questions):
    filepath = "classes/7-8-sinf/8-hafta/28-dars-katta-takrorlash-va-oraliq-nazorat/test.html"
    
    # Build HTML cards
    cards_html = []
    
    for q in questions:
        num = q["num"]
        card_id = f"card_q{num}"
        feedback_id = f"feedback_q{num}"
        status_id = f"status_q{num}"
        
        choices_html = []
        for c_idx, c in enumerate(q["choices"]):
            correct_attr = "true" if c["is_correct"] else "false"
            c_html = f'''        <label class="choice-card" data-correct="{correct_attr}" onclick="selectChoice('q{num}', {c_idx})">
          <span class="choice-letter">{c["letter"]}</span>
          <span class="choice-text" data-ru="{escape_html(c["text_ru"])}" data-en="{escape_html(c["text_en"])}">{escape_html(c["text_uz"])}</span>
        </label>'''
            choices_html.append(c_html)
            
        choices_block = "\n".join(choices_html)
        
        card = f'''    <!-- Question {num} -->
    <div class="question-card" id="{card_id}" data-points="1">
      <div class="q-header">
        <span class="q-badge" data-ru="ВОПРОС {num} · 1 БАЛЛ" data-en="QUESTION {num} · 1 POINT">SAVOL {num} · 1 BALL</span>
        <span class="q-topic" data-ru="{escape_html(q["topic_ru"])}" data-en="{escape_html(q["topic_en"])}">{escape_html(q["topic_uz"])}</span>
        <span class="q-status" id="{status_id}"></span>
      </div>
      <div class="q-title" data-ru="{escape_html(q["text_ru"])}" data-en="{escape_html(q["text_en"])}">{escape_html(q["text_uz"])}</div>

      <div class="choices-list">
{choices_block}
      </div>

      <div class="feedback-box" id="{feedback_id}" style="display:none;"
        data-corr-uz="{escape_html("To'g'ri! " + q["expl_uz"])}"
        data-corr-ru="{escape_html("Верно! " + q["expl_ru"])}"
        data-corr-en="{escape_html("Correct! " + q["expl_en"])}"
        data-inc-uz="{escape_html("Xato. To'g'ri javob: " + q["correct"] + ". " + q["expl_uz"])}"
        data-inc-ru="{escape_html("Неверно. Правильный ответ: " + q["correct"] + ". " + q["expl_ru"])}"
        data-inc-en="{escape_html("Incorrect. Correct answer is " + q["correct"] + ". " + q["expl_en"])}">
      </div>
    </div>'''
        cards_html.append(card)

    all_cards = "\n\n".join(cards_html)
    
    html_content = f'''<!DOCTYPE html>
<html lang="uz" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title data-ru="7–8-Класс: 28-Урок Большое повторение и рубежный контроль — Кибер-Тест" data-en="Grade 7–8: Lesson 28 Comprehensive Review & Midterm Exam — Cyber-Quiz">7–8-Sinf: 28-Dars Katta Takrorlash va Oraliq Nazorat — Kiber-Test</title>
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@600;700;800&family=Source+Sans+3:wght@400;600;700&family=JetBrains+Mono:wght@400;600;700&display=swap">

<style>
:root {{
  --bg: #07152D;
  --panel: #0E2246;
  --panel-2: #142E5C;
  --panel-hover: #19386D;
  --ink: #F0F4FA;
  --ink-2: #A5B6D0;
  --ink-3: #6C819F;
  --rule: #1B355A;
  --rule-light: rgba(255, 255, 255, 0.08);
  --accent: #00F0FF;
  --accent-ink: #38BDF8;
  --accent-soft: rgba(0, 240, 255, 0.12);
  --blue-soft: #12284E;
  --green: #10B981;
  --green-soft: rgba(16, 185, 129, 0.12);
  --green-border: rgba(16, 185, 129, 0.4);
  --red: #EF4444;
  --red-soft: rgba(239, 68, 68, 0.12);
  --red-border: rgba(239, 68, 68, 0.4);
  --glass-bg: rgba(14, 34, 70, 0.88);
  --glass-border: rgba(255, 255, 255, 0.12);
  --radius-sm: 8px;
  --radius-md: 14px;
  --radius-lg: 20px;
  --shadow-sm: 0 4px 12px rgba(0, 0, 0, 0.25);
  --shadow-lg: 0 16px 40px rgba(0, 0, 0, 0.45);
}}

:root[data-theme="light"] {{
  --bg: #F8FAFD;
  --panel: #FFFFFF;
  --panel-2: #EDF2F9;
  --panel-hover: #E3EAF5;
  --ink: #00214A;
  --ink-2: #384A68;
  --ink-3: #7586A2;
  --rule: #DCE4EF;
  --rule-light: rgba(0, 33, 74, 0.06);
  --accent: #0284C7;
  --accent-ink: #0369A1;
  --accent-soft: #E0F2FE;
  --blue-soft: #EBF2FE;
  --green: #0B6B4F;
  --green-soft: #DDF0E8;
  --green-border: rgba(11, 107, 79, 0.35);
  --red: #C21000;
  --red-soft: #FFEAE6;
  --red-border: rgba(194, 16, 0, 0.35);
  --glass-bg: rgba(255, 255, 255, 0.92);
  --glass-border: rgba(0, 33, 74, 0.12);
  --shadow-sm: 0 2px 8px rgba(0, 33, 74, 0.06);
  --shadow-lg: 0 12px 32px rgba(0, 33, 74, 0.12);
}}

*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  background: var(--bg);
  color: var(--ink);
  font-family: "Source Sans 3", system-ui, sans-serif;
  font-size: 15px;
  line-height: 1.5;
  padding: 80px 20px 60px;
  min-height: 100vh;
  transition: background-color 0.25s ease, color 0.25s ease;
}}

.nav-bar {{
  position: fixed;
  top: 14px;
  left: 20px;
  right: 20px;
  max-width: 1040px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: var(--glass-bg);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border: 1px solid var(--glass-border);
  padding: 8px 18px;
  border-radius: 999px;
  z-index: 100;
  box-shadow: var(--shadow-sm);
}}

.nav-brand {{
  display: flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
}}

.nav-brand img {{
  height: 22px;
  width: auto;
}}

.nav-brand .tag {{
  font-family: "JetBrains Mono", monospace;
  font-size: 11px;
  font-weight: 700;
  color: var(--ink-2);
  letter-spacing: 0.08em;
  text-transform: uppercase;
}}

.nav-tools {{
  display: flex;
  align-items: center;
  gap: 6px;
}}

.dock-btn {{
  background: transparent;
  border: none;
  color: var(--ink-2);
  font-family: "JetBrains Mono", monospace;
  font-size: 12px;
  font-weight: 700;
  padding: 6px 12px;
  border-radius: 999px;
  cursor: pointer;
  transition: all 0.18s ease;
}}

.dock-btn:hover {{
  color: var(--ink);
  background: var(--rule-light);
}}

.dock-btn.active {{
  color: var(--ink);
  background: var(--panel);
  box-shadow: 0 2px 6px rgba(0,0,0,0.12);
}}

.test-container {{
  max-width: 900px;
  margin: 0 auto;
}}

.test-header-card {{
  background: var(--panel);
  border: 1px solid var(--rule);
  border-radius: var(--radius-lg);
  padding: 28px;
  margin-bottom: 24px;
  box-shadow: var(--shadow-sm);
}}

.test-eyebrow {{
  display: flex;
  align-items: center;
  gap: 8px;
  font-family: "JetBrains Mono", monospace;
  font-size: 12px;
  font-weight: 700;
  color: var(--accent);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-bottom: 8px;
}}

.test-title {{
  font-family: "Manrope", sans-serif;
  font-size: clamp(24px, 3.5vw, 36px);
  font-weight: 800;
  color: var(--ink);
  line-height: 1.2;
  margin-bottom: 12px;
}}

.test-desc {{
  font-size: 15.5px;
  color: var(--ink-2);
  line-height: 1.6;
  margin-bottom: 20px;
}}

.student-card {{
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 16px;
  padding-top: 16px;
  border-top: 1px solid var(--rule);
}}

@media (max-width: 600px) {{
  .student-card {{ grid-template-columns: 1fr; }}
}}

.input-group label {{
  display: block;
  font-family: "JetBrains Mono", monospace;
  font-size: 11.5px;
  font-weight: 700;
  color: var(--ink-3);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 6px;
}}

.input-field {{
  width: 100%;
  background: var(--panel-2);
  border: 1px solid var(--rule);
  border-radius: var(--radius-sm);
  padding: 10px 14px;
  color: var(--ink);
  font-family: inherit;
  font-size: 14.5px;
  outline: none;
  transition: border-color 0.2s ease;
}}

.input-field:focus {{
  border-color: var(--accent);
}}

/* Questions List */
.questions-list {{
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-bottom: 30px;
}}

.question-card {{
  background: var(--panel);
  border: 1px solid var(--rule);
  border-radius: var(--radius-md);
  padding: 22px;
  box-shadow: var(--shadow-sm);
  transition: border-color 0.2s ease;
}}

.question-card.answered {{
  border-color: var(--accent-ink);
}}

.question-card.correct {{
  border-color: var(--green);
}}

.question-card.wrong {{
  border-color: var(--red);
}}

.q-header {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 12px;
}}

.q-badge {{
  font-family: "JetBrains Mono", monospace;
  font-size: 11px;
  font-weight: 800;
  background: var(--accent-soft);
  color: var(--accent);
  padding: 3px 10px;
  border-radius: 999px;
}}

.q-topic {{
  font-family: "JetBrains Mono", monospace;
  font-size: 11px;
  color: var(--ink-3);
}}

.q-status {{
  font-family: "JetBrains Mono", monospace;
  font-size: 12px;
  font-weight: 700;
}}

.q-title {{
  font-size: 16.5px;
  font-weight: 600;
  color: var(--ink);
  line-height: 1.5;
  margin-bottom: 16px;
}}

.choices-list {{
  display: flex;
  flex-direction: column;
  gap: 10px;
}}

.choice-card {{
  display: flex;
  align-items: flex-start;
  gap: 12px;
  background: var(--panel-2);
  border: 1.5px solid var(--rule);
  border-radius: var(--radius-sm);
  padding: 12px 14px;
  cursor: pointer;
  transition: all 0.18s ease;
}}

.choice-card:hover {{
  background: var(--panel-hover);
  border-color: var(--ink-3);
}}

.choice-card.selected {{
  background: var(--blue-soft);
  border-color: var(--accent);
}}

.choice-card.is-correct {{
  background: var(--green-soft);
  border-color: var(--green);
}}

.choice-card.is-wrong {{
  background: var(--red-soft);
  border-color: var(--red);
}}

.choice-letter {{
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
  border-radius: 6px;
  background: var(--panel);
  border: 1px solid var(--rule);
  font-family: "JetBrains Mono", monospace;
  font-size: 12px;
  font-weight: 800;
  color: var(--ink);
  flex-shrink: 0;
}}

.choice-card.selected .choice-letter {{
  background: var(--accent);
  color: #07152D;
  border-color: var(--accent);
}}

:root[data-theme="light"] .choice-card.selected .choice-letter {{
  color: #ffffff;
}}

.choice-card.is-correct .choice-letter {{
  background: var(--green);
  color: #fff;
  border-color: var(--green);
}}

.choice-card.is-wrong .choice-letter {{
  background: var(--red);
  color: #fff;
  border-color: var(--red);
}}

.choice-text {{
  font-size: 14.5px;
  color: var(--ink);
  line-height: 1.45;
  padding-top: 1px;
}}

.feedback-box {{
  margin-top: 14px;
  padding: 12px 16px;
  border-radius: var(--radius-sm);
  font-size: 13.5px;
  line-height: 1.5;
}}

.feedback-box.correct {{
  background: var(--green-soft);
  border: 1px solid var(--green-border);
  color: var(--green);
}}

.feedback-box.wrong {{
  background: var(--red-soft);
  border: 1px solid var(--red-border);
  color: var(--red);
}}

/* Sticky Action Bar */
.submit-bar {{
  position: sticky;
  bottom: 20px;
  background: var(--glass-bg);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border: 1px solid var(--glass-border);
  border-radius: 999px;
  padding: 12px 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: var(--shadow-lg);
  z-index: 90;
  flex-wrap: wrap;
  gap: 12px;
}}

.progress-info {{
  font-family: "JetBrains Mono", monospace;
  font-size: 13px;
  font-weight: 700;
  color: var(--ink-2);
}}

.progress-info b {{
  color: var(--accent);
}}

.btn-submit {{
  background: linear-gradient(135deg, var(--accent), #0284C7);
  color: #07152D;
  border: none;
  font-family: "Manrope", sans-serif;
  font-size: 15px;
  font-weight: 800;
  padding: 12px 28px;
  border-radius: 999px;
  cursor: pointer;
  box-shadow: 0 4px 16px rgba(0, 240, 255, 0.3);
  transition: all 0.2s ease;
}}

:root[data-theme="light"] .btn-submit {{
  color: #ffffff;
}}

.btn-submit:hover {{
  transform: translateY(-1px);
  opacity: 0.95;
}}

/* Modal */
.modal-overlay {{
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.75);
  backdrop-filter: blur(8px);
  display: none;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 20px;
}}

.modal-overlay.active {{
  display: flex;
}}

.modal-content {{
  background: var(--panel);
  border: 2px solid var(--accent);
  border-radius: var(--radius-lg);
  max-width: 520px;
  width: 100%;
  padding: 32px;
  text-align: center;
  box-shadow: var(--shadow-lg);
  animation: popIn 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}}

@keyframes popIn {{
  from {{ opacity: 0; transform: scale(0.92); }}
  to {{ opacity: 1; transform: scale(1); }}
}}

.modal-score {{
  font-family: "Manrope", sans-serif;
  font-size: 54px;
  font-weight: 800;
  color: var(--accent);
  margin: 12px 0 4px;
  line-height: 1;
}}

.modal-badge {{
  display: inline-block;
  padding: 4px 14px;
  border-radius: 999px;
  font-family: "JetBrains Mono", monospace;
  font-size: 13px;
  font-weight: 800;
  margin-bottom: 12px;
}}

.modal-badge.grade-5 {{ background: var(--green-soft); color: var(--green); border: 1px solid var(--green); }}
.modal-badge.grade-4 {{ background: var(--blue-soft); color: var(--accent); border: 1px solid var(--accent); }}
.modal-badge.grade-3 {{ background: rgba(234, 179, 8, 0.15); color: #EAB308; border: 1px solid #EAB308; }}
.modal-badge.grade-2 {{ background: var(--red-soft); color: var(--red); border: 1px solid var(--red); }}

.modal-sub {{
  font-size: 15px;
  color: var(--ink-2);
  margin-bottom: 24px;
  line-height: 1.5;
}}

.modal-actions {{
  display: flex;
  gap: 10px;
  justify-content: center;
  flex-wrap: wrap;
}}

.btn-ghost {{
  background: var(--panel-2);
  border: 1px solid var(--rule);
  color: var(--ink);
  font-family: inherit;
  font-size: 13.5px;
  font-weight: 700;
  padding: 10px 18px;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.15s ease;
}}

.btn-ghost:hover {{
  background: var(--rule-light);
}}

:root[data-theme="dark"] .nav-brand img {{
  filter: brightness(0) invert(1) !important;
}}

@media print {{
  :root,
  :root:not([data-theme="light"]),
  :root[data-theme="dark"],
  :root[data-theme="light"]{{
    --bg:#fff; --sheet:#fff; --panel:transparent; --panel-2:transparent;
    --ink:#000; --ink-2:#333; --ink-3:#5E5E5E;
    --rule:#8C8C8C; --hair:#C6C6C6;
    --accent:#000; --accent-ink:#000; --accent-soft:transparent;
    --green:#000; --red:#000; --write:#B4B4B4;
  }}
  body {{ background: #fff; padding: 0; }}
  .nav-bar, .submit-bar, .modal-overlay {{ display: none !important; }}
  .question-card {{ break-inside: avoid; border: 1px solid #000; }}
  .choice-card {{ border: 1px solid #888; }}
  .feedback-box {{ display: block !important; border: 1px solid #000; }}
}}
</style>
</head>
<body>

<nav class="nav-bar">
  <a href="../../../../index.html" class="nav-brand" title="Bosh sahifa / Home" data-title-ru="Главная страница / Home" data-title-en="Home Page">
    <img src="/assets/target-logo.png" alt="Target Logo" onerror="this.style.display='none'">
    <span class="tag" data-ru="7–8-КЛАСС · КИБЕР-ТЕСТ" data-en="GRADE 7–8 · CYBER-QUIZ">7–8-SINF · KIBER-TEST</span>
  </a>
  <div class="nav-tools">
    <button type="button" class="dock-btn lang-btn active" data-lang="uz" onclick="setLang('uz')">UZ</button>
    <button type="button" class="dock-btn lang-btn" data-lang="ru" onclick="setLang('ru')">RU</button>
    <button type="button" class="dock-btn lang-btn" data-lang="en" onclick="setLang('en')">EN</button>
    <button type="button" class="dock-btn" onclick="toggleTheme()" title="Mavzu" data-title-ru="Тема" data-title-en="Theme">🌓</button>
  </div>
</nav>

<div class="test-container">
  <div class="test-header-card">
    <div class="test-eyebrow">
      <span>🛡️</span>
      <span data-ru="1-ЧЕТВЕРТЬ · РУБЕЖНЫЙ ЭКЗАМЕН" data-en="QUARTER 1 · MIDTERM EXAMINATION">1-CHORAK · ORALIQ IMTIHON</span>
    </div>
    <h1 class="test-title" data-ru="28-Урок: Большое повторение и рубежный контроль" data-en="Lesson 28: Comprehensive Review & Midterm Exam">28-Dars: Katta Takrorlash va Oraliq Nazorat</h1>
    <p class="test-desc" data-ru="Официальный проверочный онлайн-тест по материалам 1-й четверти: LLM-промпты, CSS Flexbox, JavaScript DOM, LocalStorage, игровой цикл Canvas 60 FPS, физика коллизий AABB, Web Audio API, FUT-графы и биометрия EAR (25 вопросов)." data-en="Official online examination covering Quarter 1: LLM prompts, CSS Flexbox, JavaScript DOM, LocalStorage, Canvas 60 FPS game loop, AABB collision physics, Web Audio API, FUT chemistry graphs, and EAR biometrics (25 questions).">1-chorak mavzulari bo'yicha rasmiy oraliq kiber-test: LLM promptlari, CSS Flexbox, JavaScript DOM, LocalStorage, Canvas 60 FPS o'yin tsikli, AABB to'qnashuv fizikasi, Web Audio API, FUT kimyo graflari va EAR biometriyasi (25 ta savol).</p>

    <div class="student-card">
      <div class="input-group">
        <label data-ru="Ф.И.О. Ученика *" data-en="Student Full Name *">O'quvchi F.I.Sh. *</label>
        <input type="text" id="studentName" class="input-field" placeholder="Masalan: Sardor Rustamov" data-placeholder-ru="Например: Сардор Рустамов" data-placeholder-en="e.g. Sardor Rustamov" oninput="saveProfile()">
      </div>
      <div class="input-group">
        <label data-ru="Класс *" data-en="Class / Cohort *">Sinfni Tanlang *</label>
        <select id="studentClass" class="input-field" onchange="saveProfile()">
          <option value="7-A">7-A</option>
          <option value="7-B">7-B</option>
          <option value="8-A">8-A</option>
          <option value="8-B">8-B</option>
        </select>
      </div>
    </div>
  </div>

  <!-- Questions List -->
  <div class="questions-list">
{all_cards}
  </div>
</div>

<!-- Sticky Bottom Bar -->
<div class="submit-bar">
  <div class="progress-info">
    <span data-ru="Отвечено:" data-en="Answered:">Javob berildi:</span> <b id="answeredCount">0</b> / 25
  </div>
  <button class="btn-submit" onclick="submitExam()" data-ru="Завершить экзамен" data-en="Finish Examination">Imtihonni Yakunlash</button>
</div>

<!-- Modal Results -->
<div class="modal-overlay" id="resultModal">
  <div class="modal-content">
    <div class="eyebrow" data-ru="РЕЗУЛЬТАТ ЭКЗАМЕНА" data-en="EXAM RESULTS">IMTIHON NATIJASI</div>
    <div class="modal-score" id="modalScore">0 / 25</div>
    <div class="modal-badge" id="modalBadge">Baho: -</div>
    <p class="modal-sub" id="modalSub" data-ru="Тест проверен. Ответы и пояснения подсвечены ниже." data-en="Assessment graded. Feedback and solutions highlighted below.">Test tekshirildi. Natijalar va izohlar quyida ko'rsatildi.</p>
    <div class="modal-actions">
      <button class="btn-ghost" onclick="closeModal()" data-ru="Просмотреть разбор" data-en="Review Answers">Xatolarni ko'rish</button>
      <button class="btn-ghost" onclick="window.print()" data-ru="Печать / Сохранить PDF" data-en="Print / Save PDF">Chop etish / PDF</button>
      <button class="btn-ghost" onclick="resetExam()" data-ru="Пройти заново" data-en="Retake Quiz">Qayta topshirish</button>
    </div>
  </div>
</div>

<script>
var TOTAL_QUESTIONS = 25;
var userAnswers = {{}};
var isSubmitted = false;
var currentLang = 'uz';

var TITLES = {{
  "uz": "7–8-Sinf: 28-Dars Katta Takrorlash va Oraliq Nazorat — Kiber-Test",
  "ru": "7–8-Класс: 28-Урок Большое повторение и рубежный контроль — Кибер-Тест",
  "en": "Grade 7–8: Lesson 28 Comprehensive Review & Midterm Exam — Cyber-Quiz"
}};

function setLang(lang) {{
  currentLang = lang;
  try {{ localStorage.setItem('target_lang', lang); }} catch(e) {{}}
  document.documentElement.lang = lang;
  document.querySelectorAll('.lang-btn').forEach(function(b) {{
    b.classList.toggle('active', b.getAttribute('data-lang') === lang);
  }});

  if (TITLES[lang]) {{
    document.title = TITLES[lang];
  }}

  var translatable = document.querySelectorAll('[data-ru], [data-en]');
  translatable.forEach(function(el) {{
    if (!el.getAttribute('data-uz-orig')) {{
      el.setAttribute('data-uz-orig', el.innerHTML);
    }}
    if (lang === 'uz') {{
      el.innerHTML = el.getAttribute('data-uz-orig');
    }} else if (lang === 'ru' && el.getAttribute('data-ru')) {{
      el.innerHTML = el.getAttribute('data-ru');
    }} else if (lang === 'en' && el.getAttribute('data-en')) {{
      el.innerHTML = el.getAttribute('data-en');
    }}
  }});

  var placeholders = document.querySelectorAll('[data-placeholder-ru], [data-placeholder-en]');
  placeholders.forEach(function(el) {{
    if (!el.getAttribute('data-ph-uz-orig')) {{
      el.setAttribute('data-ph-uz-orig', el.getAttribute('placeholder') || '');
    }}
    if (lang === 'uz') {{
      el.setAttribute('placeholder', el.getAttribute('data-ph-uz-orig'));
    }} else if (lang === 'ru' && el.getAttribute('data-placeholder-ru')) {{
      el.setAttribute('placeholder', el.getAttribute('data-placeholder-ru'));
    }} else if (lang === 'en' && el.getAttribute('data-placeholder-en')) {{
      el.setAttribute('placeholder', el.getAttribute('data-placeholder-en'));
    }}
  }});

  if (isSubmitted) {{
    updateFeedbacksLanguage();
  }}
}}

function toggleTheme() {{
  var cur = document.documentElement.getAttribute('data-theme') || 'dark';
  var next = cur === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  try {{ localStorage.setItem('target_theme', next); }} catch(e) {{}}
}}

function selectChoice(qKey, choiceIdx) {{
  if (isSubmitted) return;
  userAnswers[qKey] = choiceIdx;
  
  var card = document.getElementById('card_' + qKey);
  card.classList.add('answered');
  var choices = card.querySelectorAll('.choice-card');
  choices.forEach(function(c, idx) {{
    c.classList.toggle('selected', idx === choiceIdx);
  }});
  
  updateProgress();
  saveState();
}}

function updateProgress() {{
  var count = Object.keys(userAnswers).length;
  document.getElementById('answeredCount').textContent = count;
}}

function submitExam() {{
  if (isSubmitted) {{
    document.getElementById('resultModal').classList.add('active');
    return;
  }}
  
  var score = 0;
  for (var i = 1; i <= TOTAL_QUESTIONS; i++) {{
    var qKey = 'q' + i;
    var card = document.getElementById('card_' + qKey);
    var choices = card.querySelectorAll('.choice-card');
    var selectedIdx = userAnswers[qKey];
    var feedback = document.getElementById('feedback_' + qKey);
    var status = document.getElementById('status_' + qKey);
    
    var isCorrect = false;
    if (selectedIdx !== undefined) {{
      var chosen = choices[selectedIdx];
      if (chosen.getAttribute('data-correct') === 'true') {{
        isCorrect = true;
        score += 1;
      }}
    }}
    
    // Style card
    if (isCorrect) {{
      card.classList.remove('wrong');
      card.classList.add('correct');
      status.textContent = '✓ 1/1';
      status.style.color = 'var(--green)';
    }} else {{
      card.classList.remove('correct');
      card.classList.add('wrong');
      status.textContent = '✗ 0/1';
      status.style.color = 'var(--red)';
    }}
    
    // Highlight correct & chosen
    choices.forEach(function(c, idx) {{
      if (c.getAttribute('data-correct') === 'true') {{
        c.classList.add('is-correct');
      }} else if (idx === selectedIdx) {{
        c.classList.add('is-wrong');
      }}
    }});
    
    // Show feedback
    feedback.style.display = 'block';
    feedback.className = 'feedback-box ' + (isCorrect ? 'correct' : 'wrong');
  }}
  
  isSubmitted = true;
  updateFeedbacksLanguage();
  
  // Show modal
  var modalScore = document.getElementById('modalScore');
  var modalBadge = document.getElementById('modalBadge');
  modalScore.textContent = score + ' / ' + TOTAL_QUESTIONS;
  
  if (score >= 22) {{
    modalBadge.className = 'modal-badge grade-5';
    modalBadge.textContent = "A'lo (5) · Mukammal Natija";
  }} else if (score >= 18) {{
    modalBadge.className = 'modal-badge grade-4';
    modalBadge.textContent = "Yaxshi (4) · Mustahkam Bilim";
  }} else if (score >= 13) {{
    modalBadge.className = 'modal-badge grade-3';
    modalBadge.textContent = "Qoniqarli (3) · Takrorlash Zarur";
  }} else {{
    modalBadge.className = 'modal-badge grade-2';
    modalBadge.textContent = "Qoniqarsiz (2) · Qayta O'rganish Shart";
  }}
  
  document.getElementById('resultModal').classList.add('active');
  saveState();
}}

function updateFeedbacksLanguage() {{
  for (var i = 1; i <= TOTAL_QUESTIONS; i++) {{
    var qKey = 'q' + i;
    var card = document.getElementById('card_' + qKey);
    var feedback = document.getElementById('feedback_' + qKey);
    var isCorrect = card.classList.contains('correct');
    
    var attr = isCorrect ? 'data-corr-' + currentLang : 'data-inc-' + currentLang;
    var msg = feedback.getAttribute(attr);
    if (msg) feedback.innerHTML = msg;
  }}
}}

function closeModal() {{
  document.getElementById('resultModal').classList.remove('active');
}}

function resetExam() {{
  if (!confirm("Testni qayta topshirishni xohlaysizmi?")) return;
  userAnswers = {{}};
  isSubmitted = false;
  try {{ localStorage.removeItem('test_7_8_w8_l28_answers'); }} catch(e) {{}}
  location.reload();
}}

var STORAGE_KEY = "test_7_8_w8_l28_answers";

function saveState() {{
  var payload = {{
    name: document.getElementById('studentName').value,
    cls: document.getElementById('studentClass').value,
    ans: userAnswers,
    submitted: isSubmitted
  }};
  try {{ localStorage.setItem(STORAGE_KEY, JSON.stringify(payload)); }} catch(e) {{}}
}}

function loadState() {{
  try {{
    var raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return;
    var p = JSON.parse(raw);
    if (p.name) document.getElementById('studentName').value = p.name;
    if (p.cls) document.getElementById('studentClass').value = p.cls;
    if (p.ans) {{
      userAnswers = p.ans;
      for (var qKey in userAnswers) {{
        var cIdx = userAnswers[qKey];
        var card = document.getElementById('card_' + qKey);
        if (card) {{
          card.classList.add('answered');
          var choices = card.querySelectorAll('.choice-card');
          if (choices[cIdx]) choices[cIdx].classList.add('selected');
        }}
      }}
      updateProgress();
    }}
    if (p.submitted) {{
      submitExam();
    }}
  }} catch(e) {{}}
}}

function saveProfile() {{
  saveState();
}}

document.addEventListener('DOMContentLoaded', function() {{
  var savedTheme = 'dark';
  try {{ savedTheme = localStorage.getItem('target_theme') || 'dark'; }} catch(e) {{}}
  document.documentElement.setAttribute('data-theme', savedTheme);
  
  var savedLang = 'uz';
  try {{ savedLang = localStorage.getItem('target_lang') || 'uz'; }} catch(e) {{}}
  setLang(savedLang);
  
  loadState();
}});
</script>
</body>
</html>
'''
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"✓ Saved test.html: {filepath}")

def generate_google_form_gs(questions):
    filepath = "classes/7-8-sinf/8-hafta/28-dars-katta-takrorlash-va-oraliq-nazorat/google_form.gs"
    
    # Generate UZ function
    uz_lines = [
        '/**',
        ' * Target International School — Google Forms Generator Script',
        ' * Dars: 7–8-Sinf: 28-Dars Katta Takrorlash va Oraliq Nazorat — Kiber-Test',
        ' * ',
        " * QO'LLANMA:",
        ' * 1. https://script.new sahifasini oching.',
        ' * 2. Ushbu fayl kodini to\'liq nusxalab, script.new tahrirchisiga qo\'ying.',
        ' * 3. Tepada funksiyani tanlang (masalan, createGoogleForm_28_dars_katta_takrorlash_va_oraliq_nazorat_uz) va "Run" (▶️) tugmasini bosing.',
        ' * 4. Google Drive ichingizda test avtomatik yaratiladi va konsolda havola chiqadi!',
        ' */',
        '',
        '/**',
        ' * Target International School — Google Form Generator',
        ' * Dars: 7–8-Sinf: 28-Dars Katta Takrorlash va Oraliq Nazorat — Kiber-Test',
        ' * Til / Language: UZ',
        ' */',
        'function createGoogleForm_28_dars_katta_takrorlash_va_oraliq_nazorat_uz() {',
        '  var form = FormApp.create("7–8-Sinf: 28-Dars Katta Takrorlash va Oraliq Nazorat — Kiber-Test");',
        '  form.setDescription("Target International School // 7–8-Sinf // 8-Hafta // 28-Dars\\nMavzu: 1-Chorak Oraliq Nazorat Testi (25 ta savol) · Canvas 2D, O\'yin Tsikli, Fizika, FUT va Web API\\nO\'qituvchi: Ismoiljon Usmonov");',
        '  form.setIsQuiz(true);',
        '  form.setRequireLogin(false);',
        '  form.setCollectEmail(true);',
        '  form.setShowLinkToRespondAgain(false);',
        '  form.setProgressBar(true);',
        '  form.setShuffleQuestions(false);',
        '',
        '  // O\'quvchi ma\'lumotlari',
        '  form.addTextItem().setTitle("O\'quvchining F.I.Sh. (Familiya, Ism)").setRequired(true);',
        '  form.addListItem().setTitle("Sinfingizni tanlang:").setChoiceValues(["7-A", "7-B", "8-A", "8-B"]).setRequired(true);',
        ''
    ]
    
    for q in questions:
        num = q["num"]
        title_escaped = escape_js_str(f"{num}. {q['text_uz']}")
        corr_feedback = escape_js_str(f"To'g'ri! {q['expl_uz']}")
        inc_feedback = escape_js_str(f"Xato. To'g'ri javob: {q['correct']}. {q['expl_uz']}")
        
        uz_lines.append(f'  // Savol {num} (1 ball)')
        uz_lines.append(f'  var q{num} = form.addMultipleChoiceItem();')
        uz_lines.append(f'  q{num}.setTitle("{title_escaped}");')
        uz_lines.append(f'  q{num}.setPoints(1);')
        uz_lines.append(f'  q{num}.setChoices([')
        
        choice_strs = []
        for c in q["choices"]:
            c_text = escape_js_str(c["text_uz"])
            is_corr_str = "true" if c["is_correct"] else "false"
            choice_strs.append(f'    q{num}.createChoice("{c_text}", {is_corr_str})')
            
        uz_lines.append(",\n".join(choice_strs))
        uz_lines.append('  ]);')
        uz_lines.append(f'  q{num}.setFeedbackForCorrect(FormApp.createFeedback().setText("{corr_feedback}").build());')
        uz_lines.append(f'  q{num}.setFeedbackForIncorrect(FormApp.createFeedback().setText("{inc_feedback}").build());')
        uz_lines.append(f'  q{num}.setRequired(true);')
        uz_lines.append('')

    uz_lines.append('  Logger.log("✓ Google Form (UZ) yaratildi: " + form.getEditUrl());')
    uz_lines.append('  Logger.log("✓ O\'quvchilar uchun havola: " + form.getPublishedUrl());')
    uz_lines.append('}')
    uz_lines.append('')
    
    # Generate RU function
    ru_lines = [
        '/**',
        ' * Target International School — Google Form Generator',
        ' * Урок: 7–8-Класс: 28-Урок Большое повторение и рубежный контроль — Кибер-Тест',
        ' * Язык / Language: RU',
        ' */',
        'function createGoogleForm_28_dars_katta_takrorlash_va_oraliq_nazorat_ru() {',
        '  var form = FormApp.create("7–8-Класс: 28-Урок Большое повторение и рубежный контроль — Кибер-Тест");',
        '  form.setDescription("Target International School // 7–8-Класс // 8-Неделя // 28-Урок\\nТема: Рубежный тест за 1-ю четверть (25 вопросов) · Canvas 2D, Игровой цикл, Физика, FUT и Web API\\nПреподаватель: Исмоилжон Усмонов");',
        '  form.setIsQuiz(true);',
        '  form.setRequireLogin(false);',
        '  form.setCollectEmail(true);',
        '  form.setShowLinkToRespondAgain(false);',
        '  form.setProgressBar(true);',
        '  form.setShuffleQuestions(false);',
        '',
        '  // Данные ученика',
        '  form.addTextItem().setTitle("Ф.И.О. Ученика").setRequired(true);',
        '  form.addListItem().setTitle("Выберите ваш класс:").setChoiceValues(["7-A", "7-B", "8-A", "8-B"]).setRequired(true);',
        ''
    ]
    
    for q in questions:
        num = q["num"]
        title_escaped = escape_js_str(f"{num}. {q['text_ru']}")
        corr_feedback = escape_js_str(f"Верно! {q['expl_ru']}")
        inc_feedback = escape_js_str(f"Неверно. Правильный ответ: {q['correct']}. {q['expl_ru']}")
        
        ru_lines.append(f'  // Вопрос {num} (1 балл)')
        ru_lines.append(f'  var q{num} = form.addMultipleChoiceItem();')
        ru_lines.append(f'  q{num}.setTitle("{title_escaped}");')
        ru_lines.append(f'  q{num}.setPoints(1);')
        ru_lines.append(f'  q{num}.setChoices([')
        
        choice_strs = []
        for c in q["choices"]:
            c_text = escape_js_str(c["text_ru"])
            is_corr_str = "true" if c["is_correct"] else "false"
            choice_strs.append(f'    q{num}.createChoice("{c_text}", {is_corr_str})')
            
        ru_lines.append(",\n".join(choice_strs))
        ru_lines.append('  ]);')
        ru_lines.append(f'  q{num}.setFeedbackForCorrect(FormApp.createFeedback().setText("{corr_feedback}").build());')
        ru_lines.append(f'  q{num}.setFeedbackForIncorrect(FormApp.createFeedback().setText("{inc_feedback}").build());')
        ru_lines.append(f'  q{num}.setRequired(true);')
        ru_lines.append('')

    ru_lines.append('  Logger.log("✓ Google Form (RU) создана: " + form.getEditUrl());')
    ru_lines.append('  Logger.log("✓ Ссылка для учеников: " + form.getPublishedUrl());')
    ru_lines.append('}')
    
    full_gs = "\n".join(uz_lines) + "\n" + "\n".join(ru_lines)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(full_gs)
    print(f"✓ Saved google_form.gs: {filepath}")

def escape_html(text):
    if not text:
        return ""
    return (text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace('"', "&quot;"))

def escape_js_str(text):
    if not text:
        return ""
    return (text.replace("\\", "\\\\")
                .replace('"', '\\"')
                .replace("\n", "\\n")
                .replace("\r", ""))

if __name__ == "__main__":
    main()
