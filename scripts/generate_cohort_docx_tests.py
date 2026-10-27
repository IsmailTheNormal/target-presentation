#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Target International School — Official Vibecoding DOCX Exam Generator
Instructor: Ismoiljon Usmonov · Target International School, Yunusobod

Generates comprehensive 25-question (5 options A-E) examination papers in Microsoft Word (.docx) format:
  - 5–6-sinf (Bilingual: Uzbek with Russian in braces in ONE file)
  - 7–8-sinf (Bilingual: Uzbek with Russian in braces in ONE file)
  - 9-sinf (Bilingual: Uzbek with Russian in braces in ONE file)
  - 10–11-sinf (English Only in ONE file)

Subject: VIBECODING
Includes Official School Header, Student Identification Bar, 25 Questions with 5 choices each,
and an Instructor Answer Key & 25-Point Grading Rubric table on a dedicated final page.
"""

import os
import sys

# Ensure repository root and scripts dir are on sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR)

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

NAVY_HEX = "00214A"
CYAN_HEX = "0284C7"
LIGHT_BG_HEX = "F1F5F9"
BORDER_GRAY_HEX = "CBD5E1"
WHITE_HEX = "FFFFFF"

# 25 perfectly balanced keys (5 A, 5 B, 5 C, 5 D, 5 E)
TARGET_KEYS = [
    "C", "A", "D", "B", "E",
    "A", "E", "C", "B", "D",
    "B", "D", "A", "E", "C",
    "D", "B", "E", "C", "A",
    "E", "C", "B", "A", "D"
]

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Set inner cell padding in twips"""
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('w:top', top), ('w:bottom', bottom), ('w:left', left), ('w:right', right)]:
        node = OxmlElement(m)
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_cell_shading(cell, color_hex):
    """Set background color of a table cell"""
    shading_xml = f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>'
    cell._tc.get_or_add_tcPr().append(parse_xml(shading_xml))

def set_cell_border(cell, **kwargs):
    """
    Set cell borders: top, bottom, left, right
    kwargs format: top={"sz": 4, "val": "single", "color": "CBD5E1"}
    """
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = OxmlElement('w:tcBorders')
    for edge in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        edge_data = kwargs.get(edge)
        if edge_data:
            tag = 'w:{}'.format(edge)
            element = OxmlElement(tag)
            element.set(qn('w:val'), edge_data.get('val', 'single'))
            element.set(qn('w:sz'), str(edge_data.get('sz', 4)))
            element.set(qn('w:space'), '0')
            element.set(qn('w:color'), edge_data.get('color', 'auto'))
            tcBorders.append(element)
    tcPr.append(tcBorders)


def balance_monolingual_options(questions, target_keys=TARGET_KEYS):
    """
    Rearranges options so the correct answer lands on target_keys[i].
    """
    balanced = []
    letters = ["a", "b", "c", "d", "e"]
    for idx, q in enumerate(questions):
        t_key = target_keys[idx % len(target_keys)]
        cur_correct = q["correct"].lower()
        correct_text = q[cur_correct]
        other_texts = [q[k] for k in letters if k != cur_correct]
        
        new_q = {
            "text": q["text"],
            "correct": t_key,
            "topic": q.get("topic", ""),
            "expl": q.get("expl", "")
        }
        if "code" in q:
            new_q["code"] = q["code"]
            
        other_idx = 0
        for l in letters:
            if l.upper() == t_key:
                new_q[l] = correct_text
            else:
                new_q[l] = other_texts[other_idx]
                other_idx += 1
        balanced.append(new_q)
    return balanced


def balance_bilingual_options(uz_questions, ru_questions, target_keys=TARGET_KEYS):
    """
    Pairs each question from UZ and RU lists and moves both UZ & RU options together
    so the correct answer lands on target_keys[i].
    """
    balanced = []
    letters = ["a", "b", "c", "d", "e"]
    for idx in range(len(uz_questions)):
        qu = uz_questions[idx]
        qr = ru_questions[idx]
        t_key = target_keys[idx % len(target_keys)]
        
        cur_correct_u = qu["correct"].lower()
        correct_uz = qu[cur_correct_u]
        correct_ru = qr[cur_correct_u]
        
        other_uz = [qu[k] for k in letters if k != cur_correct_u]
        other_ru = [qr[k] for k in letters if k != cur_correct_u]
        
        new_q = {
            "text_uz": qu["text"],
            "text_ru": qr["text"],
            "correct": t_key,
            "topic_uz": qu.get("topic", ""),
            "topic_ru": qr.get("topic", ""),
            "expl_uz": qu.get("expl", ""),
            "expl_ru": qr.get("expl", "")
        }
        if "code" in qu:
            new_q["code"] = qu["code"]
            
        other_idx = 0
        for l in letters:
            if l.upper() == t_key:
                new_q[f"{l}_uz"] = correct_uz
                new_q[f"{l}_ru"] = correct_ru
            else:
                new_q[f"{l}_uz"] = other_uz[other_idx]
                new_q[f"{l}_ru"] = other_ru[other_idx]
                other_idx += 1
        balanced.append(new_q)
    return balanced


def build_bilingual_exam_docx(filename, meta, uz_questions, ru_questions, keys_meta):
    """
    Builds a unified bilingual (Uzbek with Russian in braces) test paper for Vibecoding.
    """
    processed_questions = balance_bilingual_options(uz_questions, ru_questions)
    doc = docx.Document()
    
    # Page Setup (A4, 0.65 in margins)
    for section in doc.sections:
        section.page_width = Inches(8.27)
        section.page_height = Inches(11.69)
        section.top_margin = Inches(0.6)
        section.bottom_margin = Inches(0.6)
        section.left_margin = Inches(0.65)
        section.right_margin = Inches(0.65)
        
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(9.5)
    normal_style.font.color.rgb = RGBColor(0, 33, 74)
    
    # 1. Header with Logo & Title
    header_table = doc.add_table(rows=1, cols=2)
    header_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    header_table.autofit = False
    header_table.columns[0].width = Inches(1.8)
    header_table.columns[1].width = Inches(5.17)
    
    cell_logo = header_table.cell(0, 0)
    cell_text = header_table.cell(0, 1)
    set_cell_margins(cell_logo, top=50, bottom=50, left=30, right=50)
    set_cell_margins(cell_text, top=50, bottom=50, left=50, right=30)
    
    logo_path = "assets/target-logo.png"
    p_logo = cell_logo.paragraphs[0]
    p_logo.alignment = WD_ALIGN_PARAGRAPH.LEFT
    if os.path.exists(logo_path):
        p_logo.add_run().add_picture(logo_path, width=Inches(1.55))
    else:
        run_logo = p_logo.add_run("TARGET\nSCHOOL")
        run_logo.bold = True
        run_logo.font.size = Pt(16)
        run_logo.font.color.rgb = RGBColor(0, 33, 74)
        
    p_text = cell_text.paragraphs[0]
    p_text.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    
    r1 = p_text.add_run(meta["school_name"] + "\n")
    r1.bold = True
    r1.font.size = Pt(11.5)
    r1.font.color.rgb = RGBColor(0, 33, 74)
    
    r2 = p_text.add_run(meta["exam_title"] + "\n")
    r2.bold = True
    r2.font.size = Pt(10.5)
    r2.font.color.rgb = RGBColor(2, 132, 199)
    
    r3 = p_text.add_run(meta["track_title"] + " · " + meta["academic_year"])
    r3.font.size = Pt(9)
    r3.font.color.rgb = RGBColor(100, 116, 139)
    
    # Divider line
    p_div = doc.add_paragraph()
    p_div.paragraph_format.space_before = Pt(3)
    p_div.paragraph_format.space_after = Pt(6)
    r_div = p_div.add_run("—" * 72)
    r_div.font.color.rgb = RGBColor(203, 213, 225)
    
    # 2. Student Info Table
    info_table = doc.add_table(rows=2, cols=3)
    info_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    info_table.autofit = False
    col_widths = [Inches(2.7), Inches(2.2), Inches(2.07)]
    for row in info_table.rows:
        for idx, cell in enumerate(row.cells):
            cell.width = col_widths[idx]
            set_cell_margins(cell, top=50, bottom=50, left=90, right=90)
            set_cell_shading(cell, LIGHT_BG_HEX)
            set_cell_border(cell,
                            top={"sz": 4, "val": "single", "color": BORDER_GRAY_HEX},
                            bottom={"sz": 4, "val": "single", "color": BORDER_GRAY_HEX},
                            left={"sz": 4, "val": "single", "color": BORDER_GRAY_HEX},
                            right={"sz": 4, "val": "single", "color": BORDER_GRAY_HEX})

    # Row 0
    p0 = info_table.cell(0, 0).paragraphs[0]
    p0.add_run(meta["label_name"] + ": ").bold = True
    p0.add_run("____________________")
    
    p1 = info_table.cell(0, 1).paragraphs[0]
    p1.add_run(meta["label_class"] + ": ").bold = True
    p1.add_run("___________")
    
    p2 = info_table.cell(0, 2).paragraphs[0]
    p2.add_run(meta["label_date"] + ": ").bold = True
    p2.add_run("___________")
    
    # Row 1
    p3 = info_table.cell(1, 0).paragraphs[0]
    p3.add_run(meta["label_variant"] + ": ").bold = True
    p3.add_run(meta["variant_val"])
    
    p4 = info_table.cell(1, 1).paragraphs[0]
    p4.add_run(meta["label_max_score"] + ": ").bold = True
    p4.add_run("25 " + meta["unit_points"])
    
    p5 = info_table.cell(1, 2).paragraphs[0]
    p5.add_run(meta["label_score"] + ": ").bold = True
    p5.add_run("_____ / 25")

    # Instruction banner
    p_inst = doc.add_paragraph()
    p_inst.paragraph_format.space_before = Pt(6)
    p_inst.paragraph_format.space_after = Pt(10)
    r_inst = p_inst.add_run(meta["instructions"])
    r_inst.font.italic = True
    r_inst.font.size = Pt(9)
    r_inst.font.color.rgb = RGBColor(71, 85, 105)
    
    # 3. 25 Bilingual Questions Block
    for q_idx, q in enumerate(processed_questions, 1):
        p_q = doc.add_paragraph()
        p_q.paragraph_format.space_before = Pt(7)
        p_q.paragraph_format.space_after = Pt(2.5)
        p_q.paragraph_format.keep_with_next = True
        
        # Question Number
        r_num = p_q.add_run(f"{q_idx}. ")
        r_num.bold = True
        r_num.font.size = Pt(10)
        r_num.font.color.rgb = RGBColor(0, 33, 74)
        
        # Uzbek Question Text (Bold Navy)
        r_q_uz = p_q.add_run(q["text_uz"] + " ")
        r_q_uz.bold = True
        r_q_uz.font.size = Pt(10)
        r_q_uz.font.color.rgb = RGBColor(15, 23, 42)
        
        # Russian Question Text in Parentheses (Italic Slate)
        r_q_ru = p_q.add_run(f"({q['text_ru']})")
        r_q_ru.bold = False
        r_q_ru.italic = True
        r_q_ru.font.size = Pt(9.5)
        r_q_ru.font.color.rgb = RGBColor(71, 85, 105)
        
        # Optional Code Snippet
        if q.get("code"):
            p_code = doc.add_paragraph()
            p_code.paragraph_format.left_indent = Inches(0.25)
            p_code.paragraph_format.space_before = Pt(2)
            p_code.paragraph_format.space_after = Pt(3)
            p_code.paragraph_format.keep_with_next = True
            r_code = p_code.add_run(q["code"])
            r_code.font.name = 'Consolas'
            r_code.font.size = Pt(9)
            r_code.font.color.rgb = RGBColor(30, 41, 59)
            
        # 5 Options (A, B, C, D, E) with Russian in Braces
        for opt_letter in ["A", "B", "C", "D", "E"]:
            l = opt_letter.lower()
            opt_uz = q[f"{l}_uz"].strip()
            opt_ru = q[f"{l}_ru"].strip()
            
            p_opt = doc.add_paragraph()
            p_opt.paragraph_format.left_indent = Inches(0.22)
            p_opt.paragraph_format.space_before = Pt(1)
            p_opt.paragraph_format.space_after = Pt(1.5)
            
            r_opt_lbl = p_opt.add_run(f"{opt_letter}) ")
            r_opt_lbl.bold = True
            r_opt_lbl.font.color.rgb = RGBColor(2, 132, 199)
            r_opt_lbl.font.size = Pt(9.5)
            
            # If Russian and Uzbek are completely identical (numbers or same keyword), don't duplicate
            if opt_uz.lower() == opt_ru.lower() or (len(opt_uz) <= 15 and opt_uz == opt_ru):
                r_txt = p_opt.add_run(opt_uz)
                r_txt.font.size = Pt(9.5)
                r_txt.font.color.rgb = RGBColor(30, 41, 59)
            else:
                r_uz = p_opt.add_run(opt_uz + " ")
                r_uz.font.size = Pt(9.5)
                r_uz.font.color.rgb = RGBColor(15, 23, 42)
                
                r_ru = p_opt.add_run(f"({opt_ru})")
                r_ru.italic = True
                r_ru.font.size = Pt(9)
                r_ru.font.color.rgb = RGBColor(80, 95, 115)

    # 4. Final Section: Answer Key & Grading Rubric on New Page
    doc.add_page_break()
    
    p_key_head = doc.add_paragraph()
    p_key_head.paragraph_format.space_before = Pt(8)
    p_key_head.paragraph_format.space_after = Pt(3)
    r_kh = p_key_head.add_run(keys_meta["heading"])
    r_kh.bold = True
    r_kh.font.size = Pt(12)
    r_kh.font.color.rgb = RGBColor(0, 33, 74)
    
    p_key_sub = doc.add_paragraph()
    p_key_sub.paragraph_format.space_after = Pt(8)
    r_ks = p_key_sub.add_run(keys_meta["subheading"])
    r_ks.font.size = Pt(9)
    r_ks.font.color.rgb = RGBColor(100, 116, 139)
    
    # 25-Row Answer Table
    key_table = doc.add_table(rows=len(processed_questions) + 1, cols=4)
    key_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    key_table.autofit = False
    
    k_widths = [Inches(0.55), Inches(0.85), Inches(2.2), Inches(3.37)]
    for idx, width in enumerate(k_widths):
        key_table.columns[idx].width = width
        
    # Header Row
    hdr_cells = key_table.rows[0].cells
    hdr_titles = keys_meta["table_headers"]
    for i, title in enumerate(hdr_titles):
        set_cell_margins(hdr_cells[i], top=70, bottom=70, left=70, right=70)
        set_cell_shading(hdr_cells[i], NAVY_HEX)
        p = hdr_cells[i].paragraphs[0]
        if i in [0, 1]:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(title)
        run.bold = True
        run.font.size = Pt(9)
        run.font.color.rgb = RGBColor(255, 255, 255)
        
    # Question Rows
    for idx, q in enumerate(processed_questions, 1):
        row_cells = key_table.rows[idx].cells
        for c in row_cells:
            set_cell_margins(c, top=45, bottom=45, left=70, right=70)
            if idx % 2 == 1:
                set_cell_shading(c, LIGHT_BG_HEX)
            set_cell_border(c,
                            top={"sz": 4, "val": "single", "color": BORDER_GRAY_HEX},
                            bottom={"sz": 4, "val": "single", "color": BORDER_GRAY_HEX},
                            left={"sz": 4, "val": "single", "color": BORDER_GRAY_HEX},
                            right={"sz": 4, "val": "single", "color": BORDER_GRAY_HEX})
                            
        # Col 0: Question number
        p_qnum = row_cells[0].paragraphs[0]
        p_qnum.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_qnum.add_run(str(idx)).bold = True
        
        # Col 1: Answer Key letter (Bold Cyan)
        p_ans = row_cells[1].paragraphs[0]
        p_ans.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_ak = p_ans.add_run(q["correct"])
        r_ak.bold = True
        r_ak.font.size = Pt(11)
        r_ak.font.color.rgb = RGBColor(2, 132, 199)
        
        # Col 2: Topic / Competency (Uzbek + Russian in braces)
        p_topic = row_cells[2].paragraphs[0]
        p_topic.add_run(q.get("topic_uz", "") + " ").bold = True
        r_tru = p_topic.add_run(f"({q.get('topic_ru', '')})")
        r_tru.italic = True
        r_tru.font.color.rgb = RGBColor(100, 116, 139)
        
        # Col 3: Explanation (Uzbek + Russian in braces)
        p_expl = row_cells[3].paragraphs[0]
        p_expl.add_run(q.get("expl_uz", "") + " ")
        r_eru = p_expl.add_run(f"({q.get('expl_ru', '')})")
        r_eru.italic = True
        r_eru.font.color.rgb = RGBColor(100, 116, 139)

    # 5. Grading Criteria Scale Box
    p_scale_head = doc.add_paragraph()
    p_scale_head.paragraph_format.space_before = Pt(12)
    p_scale_head.paragraph_format.space_after = Pt(4)
    r_sh = p_scale_head.add_run(keys_meta["scale_heading"])
    r_sh.bold = True
    r_sh.font.size = Pt(10.5)
    r_sh.font.color.rgb = RGBColor(0, 33, 74)
    
    scale_table = doc.add_table(rows=2, cols=4)
    scale_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    scale_table.autofit = False
    sc_widths = [Inches(1.7), Inches(1.7), Inches(1.7), Inches(1.87)]
    for idx, width in enumerate(sc_widths):
        scale_table.columns[idx].width = width
        
    shdr = scale_table.rows[0].cells
    sval = scale_table.rows[1].cells
    
    rubric_tiers = keys_meta["rubric_tiers"]
    for i, tier in enumerate(rubric_tiers):
        set_cell_margins(shdr[i], top=50, bottom=50, left=50, right=50)
        set_cell_shading(shdr[i], NAVY_HEX)
        psh = shdr[i].paragraphs[0]
        psh.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_t = psh.add_run(tier["grade"])
        r_t.bold = True
        r_t.font.size = Pt(9)
        r_t.font.color.rgb = RGBColor(255, 255, 255)
        
        set_cell_margins(sval[i], top=50, bottom=50, left=50, right=50)
        set_cell_shading(sval[i], LIGHT_BG_HEX)
        set_cell_border(sval[i],
                        top={"sz": 4, "val": "single", "color": BORDER_GRAY_HEX},
                        bottom={"sz": 4, "val": "single", "color": BORDER_GRAY_HEX},
                        left={"sz": 4, "val": "single", "color": BORDER_GRAY_HEX},
                        right={"sz": 4, "val": "single", "color": BORDER_GRAY_HEX})
        psv = sval[i].paragraphs[0]
        psv.alignment = WD_ALIGN_PARAGRAPH.CENTER
        psv.add_run(tier["range"] + "\n").bold = True
        psv.add_run(tier["desc"]).font.size = Pt(8)

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    doc.save(filename)
    print(f"✓ Saved Bilingual DOCX exam: {filename} ({len(processed_questions)} questions)")


def build_monolingual_exam_docx(filename, meta, questions, keys_meta):
    """
    Builds a monolingual Word Document test paper (for 10-11 English Only).
    """
    processed_questions = balance_monolingual_options(questions)
    doc = docx.Document()
    
    for section in doc.sections:
        section.page_width = Inches(8.27)
        section.page_height = Inches(11.69)
        section.top_margin = Inches(0.6)
        section.bottom_margin = Inches(0.6)
        section.left_margin = Inches(0.65)
        section.right_margin = Inches(0.65)
        
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(10)
    normal_style.font.color.rgb = RGBColor(0, 33, 74)
    
    # 1. Header with Logo & Title
    header_table = doc.add_table(rows=1, cols=2)
    header_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    header_table.autofit = False
    header_table.columns[0].width = Inches(1.8)
    header_table.columns[1].width = Inches(5.17)
    
    cell_logo = header_table.cell(0, 0)
    cell_text = header_table.cell(0, 1)
    set_cell_margins(cell_logo, top=50, bottom=50, left=30, right=50)
    set_cell_margins(cell_text, top=50, bottom=50, left=50, right=30)
    
    logo_path = "assets/target-logo.png"
    p_logo = cell_logo.paragraphs[0]
    p_logo.alignment = WD_ALIGN_PARAGRAPH.LEFT
    if os.path.exists(logo_path):
        p_logo.add_run().add_picture(logo_path, width=Inches(1.55))
    else:
        run_logo = p_logo.add_run("TARGET\nSCHOOL")
        run_logo.bold = True
        run_logo.font.size = Pt(16)
        run_logo.font.color.rgb = RGBColor(0, 33, 74)
        
    p_text = cell_text.paragraphs[0]
    p_text.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    
    r1 = p_text.add_run(meta["school_name"] + "\n")
    r1.bold = True
    r1.font.size = Pt(12)
    r1.font.color.rgb = RGBColor(0, 33, 74)
    
    r2 = p_text.add_run(meta["exam_title"] + "\n")
    r2.bold = True
    r2.font.size = Pt(11)
    r2.font.color.rgb = RGBColor(2, 132, 199)
    
    r3 = p_text.add_run(meta["track_title"] + " · " + meta["academic_year"])
    r3.font.size = Pt(9.5)
    r3.font.color.rgb = RGBColor(100, 116, 139)
    
    p_div = doc.add_paragraph()
    p_div.paragraph_format.space_before = Pt(3)
    p_div.paragraph_format.space_after = Pt(6)
    r_div = p_div.add_run("—" * 72)
    r_div.font.color.rgb = RGBColor(203, 213, 225)
    
    # 2. Student Info Table
    info_table = doc.add_table(rows=2, cols=3)
    info_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    info_table.autofit = False
    col_widths = [Inches(2.7), Inches(2.2), Inches(2.07)]
    for row in info_table.rows:
        for idx, cell in enumerate(row.cells):
            cell.width = col_widths[idx]
            set_cell_margins(cell, top=50, bottom=50, left=90, right=90)
            set_cell_shading(cell, LIGHT_BG_HEX)
            set_cell_border(cell,
                            top={"sz": 4, "val": "single", "color": BORDER_GRAY_HEX},
                            bottom={"sz": 4, "val": "single", "color": BORDER_GRAY_HEX},
                            left={"sz": 4, "val": "single", "color": BORDER_GRAY_HEX},
                            right={"sz": 4, "val": "single", "color": BORDER_GRAY_HEX})

    p0 = info_table.cell(0, 0).paragraphs[0]
    p0.add_run(meta["label_name"] + ": ").bold = True
    p0.add_run("____________________")
    
    p1 = info_table.cell(0, 1).paragraphs[0]
    p1.add_run(meta["label_class"] + ": ").bold = True
    p1.add_run("___________")
    
    p2 = info_table.cell(0, 2).paragraphs[0]
    p2.add_run(meta["label_date"] + ": ").bold = True
    p2.add_run("___________")
    
    p3 = info_table.cell(1, 0).paragraphs[0]
    p3.add_run(meta["label_variant"] + ": ").bold = True
    p3.add_run(meta["variant_val"])
    
    p4 = info_table.cell(1, 1).paragraphs[0]
    p4.add_run(meta["label_max_score"] + ": ").bold = True
    p4.add_run("25 " + meta["unit_points"])
    
    p5 = info_table.cell(1, 2).paragraphs[0]
    p5.add_run(meta["label_score"] + ": ").bold = True
    p5.add_run("_____ / 25")

    p_inst = doc.add_paragraph()
    p_inst.paragraph_format.space_before = Pt(6)
    p_inst.paragraph_format.space_after = Pt(10)
    r_inst = p_inst.add_run(meta["instructions"])
    r_inst.font.italic = True
    r_inst.font.size = Pt(9.5)
    r_inst.font.color.rgb = RGBColor(71, 85, 105)
    
    # 3. 25 Questions Block
    for q_idx, q in enumerate(processed_questions, 1):
        p_q = doc.add_paragraph()
        p_q.paragraph_format.space_before = Pt(7)
        p_q.paragraph_format.space_after = Pt(2.5)
        p_q.paragraph_format.keep_with_next = True
        
        r_num = p_q.add_run(f"{q_idx}. ")
        r_num.bold = True
        r_num.font.size = Pt(10.5)
        r_num.font.color.rgb = RGBColor(0, 33, 74)
        
        r_q = p_q.add_run(q["text"])
        r_q.bold = True
        r_q.font.size = Pt(10.5)
        r_q.font.color.rgb = RGBColor(15, 23, 42)
        
        if q.get("code"):
            p_code = doc.add_paragraph()
            p_code.paragraph_format.left_indent = Inches(0.25)
            p_code.paragraph_format.space_before = Pt(2)
            p_code.paragraph_format.space_after = Pt(3)
            p_code.paragraph_format.keep_with_next = True
            r_code = p_code.add_run(q["code"])
            r_code.font.name = 'Consolas'
            r_code.font.size = Pt(9.5)
            r_code.font.color.rgb = RGBColor(30, 41, 59)
            
        for opt_letter, opt_text in [("A", q["a"]), ("B", q["b"]), ("C", q["c"]), ("D", q["d"]), ("E", q["e"])]:
            p_opt = doc.add_paragraph()
            p_opt.paragraph_format.left_indent = Inches(0.25)
            p_opt.paragraph_format.space_before = Pt(1)
            p_opt.paragraph_format.space_after = Pt(1.5)
            
            r_opt_lbl = p_opt.add_run(f"{opt_letter}) ")
            r_opt_lbl.bold = True
            r_opt_lbl.font.color.rgb = RGBColor(2, 132, 199)
            r_opt_lbl.font.size = Pt(10)
            
            r_opt_txt = p_opt.add_run(opt_text)
            r_opt_txt.font.size = Pt(10)
            r_opt_txt.font.color.rgb = RGBColor(51, 65, 85)

    # 4. Final Section: Answer Key & Grading Rubric
    doc.add_page_break()
    
    p_key_head = doc.add_paragraph()
    p_key_head.paragraph_format.space_before = Pt(8)
    p_key_head.paragraph_format.space_after = Pt(3)
    r_kh = p_key_head.add_run(keys_meta["heading"])
    r_kh.bold = True
    r_kh.font.size = Pt(13)
    r_kh.font.color.rgb = RGBColor(0, 33, 74)
    
    p_key_sub = doc.add_paragraph()
    p_key_sub.paragraph_format.space_after = Pt(8)
    r_ks = p_key_sub.add_run(keys_meta["subheading"])
    r_ks.font.size = Pt(9.5)
    r_ks.font.color.rgb = RGBColor(100, 116, 139)
    
    key_table = doc.add_table(rows=len(processed_questions) + 1, cols=4)
    key_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    key_table.autofit = False
    
    k_widths = [Inches(0.55), Inches(0.85), Inches(2.2), Inches(3.37)]
    for idx, width in enumerate(k_widths):
        key_table.columns[idx].width = width
        
    hdr_cells = key_table.rows[0].cells
    hdr_titles = keys_meta["table_headers"]
    for i, title in enumerate(hdr_titles):
        set_cell_margins(hdr_cells[i], top=70, bottom=70, left=70, right=70)
        set_cell_shading(hdr_cells[i], NAVY_HEX)
        p = hdr_cells[i].paragraphs[0]
        if i in [0, 1]:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(title)
        run.bold = True
        run.font.size = Pt(9.5)
        run.font.color.rgb = RGBColor(255, 255, 255)
        
    for idx, q in enumerate(processed_questions, 1):
        row_cells = key_table.rows[idx].cells
        for c in row_cells:
            set_cell_margins(c, top=45, bottom=45, left=70, right=70)
            if idx % 2 == 1:
                set_cell_shading(c, LIGHT_BG_HEX)
            set_cell_border(c,
                            top={"sz": 4, "val": "single", "color": BORDER_GRAY_HEX},
                            bottom={"sz": 4, "val": "single", "color": BORDER_GRAY_HEX},
                            left={"sz": 4, "val": "single", "color": BORDER_GRAY_HEX},
                            right={"sz": 4, "val": "single", "color": BORDER_GRAY_HEX})
                            
        p_qnum = row_cells[0].paragraphs[0]
        p_qnum.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_qnum.add_run(str(idx)).bold = True
        
        p_ans = row_cells[1].paragraphs[0]
        p_ans.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_ak = p_ans.add_run(q["correct"])
        r_ak.bold = True
        r_ak.font.size = Pt(11)
        r_ak.font.color.rgb = RGBColor(2, 132, 199)
        
        p_topic = row_cells[2].paragraphs[0]
        p_topic.add_run(q.get("topic", ""))
        
        p_expl = row_cells[3].paragraphs[0]
        p_expl.add_run(q.get("expl", ""))

    p_scale_head = doc.add_paragraph()
    p_scale_head.paragraph_format.space_before = Pt(12)
    p_scale_head.paragraph_format.space_after = Pt(4)
    r_sh = p_scale_head.add_run(keys_meta["scale_heading"])
    r_sh.bold = True
    r_sh.font.size = Pt(11)
    r_sh.font.color.rgb = RGBColor(0, 33, 74)
    
    scale_table = doc.add_table(rows=2, cols=4)
    scale_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    scale_table.autofit = False
    sc_widths = [Inches(1.7), Inches(1.7), Inches(1.7), Inches(1.87)]
    for idx, width in enumerate(sc_widths):
        scale_table.columns[idx].width = width
        
    shdr = scale_table.rows[0].cells
    sval = scale_table.rows[1].cells
    
    rubric_tiers = keys_meta["rubric_tiers"]
    for i, tier in enumerate(rubric_tiers):
        set_cell_margins(shdr[i], top=50, bottom=50, left=50, right=50)
        set_cell_shading(shdr[i], NAVY_HEX)
        psh = shdr[i].paragraphs[0]
        psh.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_t = psh.add_run(tier["grade"])
        r_t.bold = True
        r_t.font.size = Pt(9.5)
        r_t.font.color.rgb = RGBColor(255, 255, 255)
        
        set_cell_margins(sval[i], top=50, bottom=50, left=50, right=50)
        set_cell_shading(sval[i], LIGHT_BG_HEX)
        set_cell_border(sval[i],
                        top={"sz": 4, "val": "single", "color": BORDER_GRAY_HEX},
                        bottom={"sz": 4, "val": "single", "color": BORDER_GRAY_HEX},
                        left={"sz": 4, "val": "single", "color": BORDER_GRAY_HEX},
                        right={"sz": 4, "val": "single", "color": BORDER_GRAY_HEX})
        psv = sval[i].paragraphs[0]
        psv.alignment = WD_ALIGN_PARAGRAPH.CENTER
        psv.add_run(tier["range"] + "\n").bold = True
        psv.add_run(tier["desc"]).font.size = Pt(8.5)

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    doc.save(filename)
    print(f"✓ Saved DOCX exam: {filename} ({len(processed_questions)} questions)")


def main():
    print("==========================================================")
    print(" TARGET INTERNATIONAL SCHOOL — OFFICIAL EXAM GENERATOR ")
    print(" Subject: VIBECODING | Instructor: Ismoiljon Usmonov ")
    print(" Generating Unified DOCX test papers across all 4 cohorts ")
    print("==========================================================")
    
    # Import Vibecoding Datasets
    from scripts.test_data_5_6 import QUESTIONS_5_6_UZ, QUESTIONS_5_6_RU
    from scripts.test_data_7_8 import QUESTIONS_7_8_UZ, QUESTIONS_7_8_RU
    from scripts.test_data_9 import QUESTIONS_9_UZ, QUESTIONS_9_RU
    from scripts.test_data_10_11 import META_10_11_EN, KEYS_META_10_11_EN, QUESTIONS_10_11_EN
    
    # 1. Cohort 5-6 Unified Bilingual Metadata (Vibecoding)
    META_5_6_BILINGUAL = {
        "school_name": "TARGET INTERNATIONAL SCHOOL — YUNUSOBOD",
        "exam_title": "5–6-SINF / 5–6 КЛАСС: VIBECODING ASOSLARI VA O'YIN LOYIHALARI",
        "track_title": "Vibecoding Track · O'qituvchi: Ismoiljon Usmonov",
        "academic_year": "2026–2027 O'quv Yili (Учебный Год)",
        "label_name": "O'quvchi F.I.Sh. (Ф.И.О.)",
        "label_class": "Sinfi (Класс)",
        "label_date": "Sana (Дата)",
        "label_variant": "Variant (Вариант)",
        "variant_val": "1-Variant (Rasmiy / Официальный)",
        "label_max_score": "Maksimal ball (Макс. балл)",
        "unit_points": "ball (баллов)",
        "label_score": "To'plangan ball (Набранный балл)",
        "instructions": "Ko'rsatma: Har bir savolga berilgan 5 ta variantdan (A, B, C, D, E) faqat bitta to'g'ri javobni tanlang va belgilang. (Инструкция: Выберите и отметьте только один правильный ответ из 5 предложенных вариантов A, B, C, D, E. За каждый правильный ответ начисляется 1 балл)."
    }

    KEYS_META_5_6_BILINGUAL = {
        "heading": "JAVOBLAR KALITI VA BAHOLASH MEZONI (КЛЮЧИ И КРИТЕРИИ)",
        "subheading": "O'qituvchi: Ismoiljon Usmonov · 5–6-sinf Vibecoding rasmiy kaliti (25 ta savol)",
        "table_headers": ["№", "Kalit (Ключ)", "Mavzu (Тема)", "Izoh va Tushuntirish (Пояснение)"],
        "scale_heading": "Rasmiy 25 Ballik Baholash Shkalasi (Официальная шкала 25 баллов):",
        "rubric_tiers": [
            {"grade": "A'lo / Отлично (5)", "range": "22 – 25 ball (баллов)", "desc": "Vibecoding, Canvas va AI promptlar a'lo o'zlashtirilgan / Отличный результат"},
            {"grade": "Yaxshi / Хорошо (4)", "range": "18 – 21 ball (баллов)", "desc": "O'yin mexanikasi va vizual bloklar yaxshi / Хорошее владение логикой игры"},
            {"grade": "Qoniqarli / Удовл. (3)", "range": "13 – 17 ball (баллов)", "desc": "Hodisalar va koordinatalarni takrorlash lozim / Требуется повторение"},
            {"grade": "Qoniqarsiz / Неудовл. (2)", "range": "0 – 12 ball (баллов)", "desc": "Vibecoding asoslari qayta o'rganilishi lozim / Необходимо повторное изучение"}
        ]
    }

    # 2. Cohort 7-8 Unified Bilingual Metadata (Vibecoding)
    META_7_8_BILINGUAL = {
        "school_name": "TARGET INTERNATIONAL SCHOOL — YUNUSOBOD",
        "exam_title": "7–8-SINF / 7–8 КЛАСС: VIBECODING FRONTEND, CANVAS VA O'YIN SIMULYATSIYASI",
        "track_title": "Vibecoding & Game Dev Track · O'qituvchi: Ismoiljon Usmonov",
        "academic_year": "2026–2027 O'quv Yili (Учебный Год)",
        "label_name": "O'quvchi F.I.Sh. (Ф.И.О.)",
        "label_class": "Sinfi (Класс)",
        "label_date": "Sana (Дата)",
        "label_variant": "Variant (Вариант)",
        "variant_val": "1-Variant (Rasmiy / Официальный)",
        "label_max_score": "Maksimal ball (Макс. балл)",
        "unit_points": "ball (баллов)",
        "label_score": "To'plangan ball (Набранный балл)",
        "instructions": "Ko'rsatma: Har bir savolga berilgan 5 ta variantdan (A, B, C, D, E) faqat bitta to'g'ri javobni tanlang va belgilang. (Инструкция: Выберите и отметьте только один правильный ответ из 5 предложенных вариантов A, B, C, D, E)."
    }

    KEYS_META_7_8_BILINGUAL = {
        "heading": "JAVOBLAR KALITI VA BAHOLASH MEZONI (КЛЮЧИ И КРИТЕРИИ)",
        "subheading": "O'qituvchi: Ismoiljon Usmonov · 7–8-sinf Vibecoding rasmiy kaliti (25 ta savol)",
        "table_headers": ["№", "Kalit (Ключ)", "Mavzu (Тема)", "Izoh va Tushuntirish (Пояснение)"],
        "scale_heading": "Rasmiy 25 Ballik Baholash Shkalasi (Официальная шкала 25 баллов):",
        "rubric_tiers": [
            {"grade": "A'lo / Отлично (5)", "range": "22 – 25 ball (баллов)", "desc": "Canvas, Game Loop, AABB, FUT va Web API chuqur bilim / Глубокие знания"},
            {"grade": "Yaxshi / Хорошо (4)", "range": "18 – 21 ball (баллов)", "desc": "Frontend va o'yin fizikasi yaxshi o'zlashtirilgan / Хорошее понимание"},
            {"grade": "Qoniqarli / Удовл. (3)", "range": "13 – 17 ball (баллов)", "desc": "DOM hodisalari va LocalStorage ni takrorlash lozim / Требуется повторение"},
            {"grade": "Qoniqarsiz / Неудовл. (2)", "range": "0 – 12 ball (баллов)", "desc": "Vibecoding asoslari qayta o'rganilishi zarur / Необходимо повторение"}
        ]
    }

    # 3. Cohort 9 Unified Bilingual Metadata (Vibecoding)
    META_9_BILINGUAL = {
        "school_name": "TARGET INTERNATIONAL SCHOOL — YUNUSOBOD",
        "exam_title": "9-SINF / 9 КЛАСС: VIBECODING FULL-STACK, REST API VA AGENTIK MUHANDISLIK",
        "track_title": "Vibecoding Full-Stack & DevOps Track · O'qituvchi: Ismoiljon Usmonov",
        "academic_year": "2026–2027 O'quv Yili (Учебный Год)",
        "label_name": "O'quvchi F.I.Sh. (Ф.И.О.)",
        "label_class": "Sinfi (Класс)",
        "label_date": "Sana (Дата)",
        "label_variant": "Variant (Вариант)",
        "variant_val": "1-Variant (Rasmiy / Официальный)",
        "label_max_score": "Maksimal ball (Макс. балл)",
        "unit_points": "ball (баллов)",
        "label_score": "To'plangan ball (Набранный балл)",
        "instructions": "Ko'rsatma: Har bir savolga berilgan 5 ta variantdan (A, B, C, D, E) faqat bitta to'g'ri javobni tanlang va belgilang. (Инструкция: Выберите и отметьте только один правильный ответ из 5 предложенных вариантов A, B, C, D, E)."
    }

    KEYS_META_9_BILINGUAL = {
        "heading": "JAVOBLAR KALITI VA BAHOLASH MEZONI (КЛЮЧИ И КРИТЕРИИ)",
        "subheading": "O'qituvchi: Ismoiljon Usmonov · 9-sinf Vibecoding rasmiy kaliti (25 ta savol)",
        "table_headers": ["№", "Kalit (Ключ)", "Mavzu (Тема)", "Izoh va Tushuntirish (Пояснение)"],
        "scale_heading": "Rasmiy 25 Ballik Baholash Shkalasi (Официальная шкала 25 баллов):",
        "rubric_tiers": [
            {"grade": "A'lo / Отлично (5)", "range": "22 – 25 ball (баллов)", "desc": "Express REST API, SQLite, Docker va Git bo'yicha a'lo bilim / Глубокие знания"},
            {"grade": "Yaxshi / Хорошо (4)", "range": "18 – 21 ball (баллов)", "desc": "Backend va autentifikatsiya yaxshi o'zlashtirilgan / Хорошее понимание"},
            {"grade": "Qoniqarli / Удовл. (3)", "range": "13 – 17 ball (баллов)", "desc": "SQL so'rovlari va middleware ni takrorlash lozim / Требуется повторение"},
            {"grade": "Qoniqarsiz / Неудовл. (2)", "range": "0 – 12 ball (баллов)", "desc": "Full-Stack asoslari qayta o'rganilishi lozim / Необходимо повторное изучение"}
        ]
    }

    # Generate the 4 Primary Cohort Files:
    bilingual_tasks = [
        # 1. 5-6 Bilingual in braces
        {
            "filename": "tests/TEST_5-6_SINF_VIBECODING.docx",
            "meta": META_5_6_BILINGUAL,
            "uz_questions": QUESTIONS_5_6_UZ,
            "ru_questions": QUESTIONS_5_6_RU,
            "keys_meta": KEYS_META_5_6_BILINGUAL,
            "label": "5–6-Sinf / 5–6 Класс (Vibecoding)"
        },
        # 2. 7-8 Bilingual in braces
        {
            "filename": "tests/TEST_7-8_SINF_VIBECODING.docx",
            "meta": META_7_8_BILINGUAL,
            "uz_questions": QUESTIONS_7_8_UZ,
            "ru_questions": QUESTIONS_7_8_RU,
            "keys_meta": KEYS_META_7_8_BILINGUAL,
            "label": "7–8-Sinf / 7–8 Класс (Vibecoding)"
        },
        # 3. 9 Bilingual in braces
        {
            "filename": "tests/TEST_9_SINF_VIBECODING.docx",
            "meta": META_9_BILINGUAL,
            "uz_questions": QUESTIONS_9_UZ,
            "ru_questions": QUESTIONS_9_RU,
            "keys_meta": KEYS_META_9_BILINGUAL,
            "label": "9-Sinf / 9 Класс (Vibecoding)"
        }
    ]

    for bt in bilingual_tasks:
        print(f"\n[Generating Bilingual] {bt['label']} -> {bt['filename']}...")
        build_bilingual_exam_docx(bt["filename"], bt["meta"], bt["uz_questions"], bt["ru_questions"], bt["keys_meta"])
        
    # 4. 10-11 English Only
    print(f"\n[Generating English Only] Grades 10–11 -> tests/TEST_10-11_GRADE_VIBECODING_EN.docx...")
    build_monolingual_exam_docx(
        "tests/TEST_10-11_GRADE_VIBECODING_EN.docx",
        META_10_11_EN,
        QUESTIONS_10_11_EN,
        KEYS_META_10_11_EN
    )

    print("\n==========================================================")
    print(" ALL 4 VIBECODING DOCX TEST PAPERS GENERATED IN tests/ ")
    print(" Teacher: Ismoiljon Usmonov · Target International School ")
    print("==========================================================")

if __name__ == "__main__":
    main()
