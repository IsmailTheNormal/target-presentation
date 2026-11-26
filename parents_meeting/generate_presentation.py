"""
Target International School - Official Parents' Meeting Presentation Generator
Generates:
1. Target_International_School_Parent_Meeting_Master_2026_2027.pptx (Part A: 18-Slide Master School Deck)
2. Target_International_School_Parent_Meeting_Complete_Teacher_Deck.pptx (Part A + Part B: Integrated 26-Slide Homeroom Deck)

Design System:
- Palette: Navy #12243D, Panel #1B334F, Gold #BE995B, Champagne #DCC497, Cream #F8F6F0, White #FFFFFF, Slate #5A7E9F
- Typography: Aptos / Arial (16:9 Widescreen)
- Brand Logo: High-res Target International School logo on every slide
"""

import os
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

# Design System Colors
C_NAVY_DARK = RGBColor(0x12, 0x24, 0x3D)       # #12243D Primary brand dark
C_NAVY_PANEL = RGBColor(0x1B, 0x33, 0x4F)      # #1B334F Secondary dark panel
C_BEIGE_BG = RGBColor(0xF8, 0xF6, 0xF0)        # #F8F6F0 Warm cream slide background
C_BEIGE_CARD = RGBColor(0xEC, 0xE5, 0xD7)      # #ECE5D7 Secondary card container
C_BORDER_LIGHT = RGBColor(0xE5, 0xE9, 0xEB)    # #E5E9EB Clean light card border
C_WHITE = RGBColor(0xFF, 0xFF, 0xFF)           # #FFFFFF Pure white cards
C_GOLD = RGBColor(0xBE, 0x99, 0x5B)            # #BE995B Primary brand gold
C_GOLD_LIGHT = RGBColor(0xDC, 0xC4, 0x97)      # #DCC497 Soft champagne gold
C_TEXT_DARK = RGBColor(0x12, 0x24, 0x3D)       # #12243D Primary heading text
C_TEXT_BODY = RGBColor(0x2F, 0x37, 0x40)       # #2F3740 Body text (charcoal)
C_TEXT_MUTED = RGBColor(0x6F, 0x77, 0x7F)      # #6F777F Subtitles & footnotes
C_ACCENT_BLUE = RGBColor(0x5A, 0x7E, 0x9F)     # #5A7E9F Accent slate blue
C_ACCENT_GREEN = RGBColor(0x5B, 0x85, 0x74)    # #5B8574 Accent sage green
C_ACCENT_CORAL = RGBColor(0xBA, 0x70, 0x5E)    # #BA705E Accent coral

FONT_HEADING = "Aptos"
FONT_BODY = "Aptos"

LOGO_COLOR_PATH = "/home/dpdp/target/parents_meeting/presentations/target-logo-transparent.png"
LOGO_WHITE_PATH = "/home/dpdp/target/parents_meeting/presentations/target-logo-white.png"

def set_slide_background(slide, color):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color

def add_header(slide, section_tag, title, subtitle):
    # Category Tracker / Section Tag
    tb_tag = slide.shapes.add_textbox(Inches(0.72), Inches(0.42), Inches(9.6), Inches(0.3))
    tf_tag = tb_tag.text_frame
    tf_tag.word_wrap = True
    tf_tag.margin_left = tf_tag.margin_right = tf_tag.margin_top = tf_tag.margin_bottom = 0
    p_tag = tf_tag.paragraphs[0]
    p_tag.text = section_tag.upper()
    p_tag.font.name = FONT_HEADING
    p_tag.font.size = Pt(9.5)
    p_tag.font.bold = True
    p_tag.font.color.rgb = C_GOLD

    # Title
    tb_title = slide.shapes.add_textbox(Inches(0.72), Inches(0.74), Inches(9.6), Inches(0.62))
    tf_title = tb_title.text_frame
    tf_title.word_wrap = True
    tf_title.margin_left = tf_title.margin_right = tf_title.margin_top = tf_title.margin_bottom = 0
    p_title = tf_title.paragraphs[0]
    p_title.text = title
    p_title.font.name = FONT_HEADING
    p_title.font.size = Pt(25)
    p_title.font.bold = True
    p_title.font.color.rgb = C_TEXT_DARK

    # Subtitle
    tb_sub = slide.shapes.add_textbox(Inches(0.72), Inches(1.38), Inches(9.6), Inches(0.38))
    tf_sub = tb_sub.text_frame
    tf_sub.word_wrap = True
    tf_sub.margin_left = tf_sub.margin_right = tf_sub.margin_top = tf_sub.margin_bottom = 0
    p_sub = tf_sub.paragraphs[0]
    p_sub.text = subtitle
    p_sub.font.name = FONT_BODY
    p_sub.font.size = Pt(11)
    p_sub.font.color.rgb = C_TEXT_MUTED

    # Logo in top right
    if os.path.exists(LOGO_COLOR_PATH):
        try:
            slide.shapes.add_picture(LOGO_COLOR_PATH, Inches(10.65), Inches(0.46), width=Inches(1.95))
        except Exception:
            pass

def add_footer(slide, slide_num, total_slides=18, is_dark=False):
    tb_left = slide.shapes.add_textbox(Inches(0.72), Inches(7.05), Inches(9.0), Inches(0.25))
    tf_left = tb_left.text_frame
    tf_left.word_wrap = True
    tf_left.margin_left = tf_left.margin_right = tf_left.margin_top = tf_left.margin_bottom = 0
    p_left = tf_left.paragraphs[0]
    p_left.text = "TARGET INTERNATIONAL SCHOOL   •   PARENT MEETING   •   2026–2027"
    p_left.font.name = FONT_HEADING
    p_left.font.size = Pt(8)
    p_left.font.bold = True
    p_left.font.color.rgb = C_GOLD_LIGHT if is_dark else C_TEXT_MUTED

    tb_num = slide.shapes.add_textbox(Inches(11.8), Inches(6.98), Inches(0.8), Inches(0.3))
    tf_num = tb_num.text_frame
    tf_num.word_wrap = False
    tf_num.margin_left = tf_num.margin_right = tf_num.margin_top = tf_num.margin_bottom = 0
    p_num = tf_num.paragraphs[0]
    p_num.alignment = PP_ALIGN.RIGHT
    p_num.text = f"{slide_num:02d}"
    p_num.font.name = FONT_HEADING
    p_num.font.size = Pt(11)
    p_num.font.bold = True
    p_num.font.color.rgb = C_GOLD

def add_card(slide, left, top, width, height, fill_color=C_WHITE, border_color=C_BORDER_LIGHT, border_width=Pt(1)):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = fill_color
    if border_color:
        card.line.color.rgb = border_color
        card.line.width = border_width
    else:
        card.line.fill.background()
    return card

def add_rect(slide, left, top, width, height, fill_color, border_color=None):
    r = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    r.fill.solid()
    r.fill.fore_color.rgb = fill_color
    if border_color:
        r.line.color.rgb = border_color
        r.line.width = Pt(1)
    else:
        r.line.fill.background()
    return r

def build_master_deck(prs):
    blank_layout = prs.slide_layouts[6]

    # =========================================================================
    # SLIDE 1: COVER SLIDE (Dark Navy)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1, C_NAVY_DARK)

    # Decorative Right Accent Panel
    add_rect(s1, Inches(9.25), Inches(0), Inches(4.083), Inches(7.5), C_NAVY_PANEL)
    add_rect(s1, Inches(9.0), Inches(0), Inches(0.08), Inches(7.5), C_GOLD)
    
    # Graphic Bars on the right panel
    add_rect(s1, Inches(9.8), Inches(1.4), Inches(0.22), Inches(4.2), C_GOLD)
    add_rect(s1, Inches(10.35), Inches(1.65), Inches(0.22), Inches(3.8), C_GOLD_LIGHT)
    add_rect(s1, Inches(10.9), Inches(1.9), Inches(0.22), Inches(3.4), C_BEIGE_CARD)
    add_rect(s1, Inches(11.45), Inches(2.15), Inches(0.22), Inches(3.0), C_ACCENT_BLUE)
    add_rect(s1, Inches(12.0), Inches(2.4), Inches(0.22), Inches(2.6), C_GOLD)

    # Welcome badge on right
    tb_w = s1.shapes.add_textbox(Inches(9.8), Inches(6.2), Inches(2.7), Inches(0.3))
    tf_w = tb_w.text_frame
    p_w = tf_w.paragraphs[0]
    p_w.text = "WELCOME PARENTS"
    p_w.font.name = FONT_HEADING
    p_w.font.size = Pt(11)
    p_w.font.bold = True
    p_w.font.color.rgb = C_WHITE

    # Logo on Cover
    if os.path.exists(LOGO_WHITE_PATH):
        try:
            s1.shapes.add_picture(LOGO_WHITE_PATH, Inches(0.85), Inches(0.68), width=Inches(2.8))
        except Exception:
            pass

    # Main Presentation Title
    tb_m = s1.shapes.add_textbox(Inches(0.85), Inches(2.1), Inches(7.8), Inches(1.8))
    tf_m = tb_m.text_frame
    tf_m.word_wrap = True
    p_m1 = tf_m.paragraphs[0]
    p_m1.text = "BEYOND EDUCATION:"
    p_m1.font.name = FONT_HEADING
    p_m1.font.size = Pt(32)
    p_m1.font.bold = True
    p_m1.font.color.rgb = C_WHITE

    p_m2 = tf_m.add_paragraph()
    p_m2.text = "BUILDING KNOWLEDGE, CHARACTER & FUTURE SUCCESS"
    p_m2.font.name = FONT_HEADING
    p_m2.font.size = Pt(25)
    p_m2.font.bold = True
    p_m2.font.color.rgb = C_GOLD_LIGHT

    # Subtitle
    tb_sub = s1.shapes.add_textbox(Inches(0.85), Inches(4.1), Inches(7.8), Inches(0.5))
    tf_sub = tb_sub.text_frame
    tf_sub.word_wrap = True
    p_s = tf_sub.paragraphs[0]
    p_s.text = "An International Learning Environment. A World of Opportunities."
    p_s.font.name = FONT_BODY
    p_s.font.size = Pt(15)
    p_s.font.color.rgb = C_BEIGE_CARD

    # Event Banner
    add_rect(s1, Inches(0.85), Inches(4.9), Inches(5.5), Inches(0.05), C_GOLD)
    tb_ev = s1.shapes.add_textbox(Inches(0.85), Inches(5.1), Inches(7.8), Inches(0.6))
    tf_ev = tb_ev.text_frame
    p_ev1 = tf_ev.paragraphs[0]
    p_ev1.text = "PARENTS' MEETING   |   ACADEMIC YEAR 2026–2027"
    p_ev1.font.name = FONT_HEADING
    p_ev1.font.size = Pt(11)
    p_ev1.font.bold = True
    p_ev1.font.color.rgb = C_WHITE
    p_ev2 = tf_ev.add_paragraph()
    p_ev2.text = "A shared partnership between school, students and families"
    p_ev2.font.name = FONT_BODY
    p_ev2.font.size = Pt(11)
    p_ev2.font.color.rgb = C_GOLD_LIGHT

    add_footer(s1, 1, is_dark=True)

    # =========================================================================
    # SLIDE 2: OUR INTERNATIONAL EDUCATION ENVIRONMENT
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2, C_BEIGE_BG)
    add_header(s2, "01 / INTRODUCTION — WHO WE ARE", "Our International Education Environment",
               "High standards, modern campus infrastructure and a shared commitment to every learner.")
    
    col_w = Inches(3.75)
    gap = Inches(0.3)
    start_x = Inches(0.72)
    top_y = Inches(1.95)
    card_h = Inches(3.7)

    # Card 1: Who We Are
    add_card(s2, start_x, top_y, col_w, card_h)
    add_rect(s2, start_x, top_y, col_w, Inches(0.08), C_NAVY_DARK)
    tb = s2.shapes.add_textbox(start_x + Inches(0.25), top_y + Inches(0.2), col_w - Inches(0.5), card_h - Inches(0.4))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "WHO WE ARE & VISION"
    p.font.name = FONT_HEADING
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_NAVY_DARK
    
    points1 = [
        "A premier international school dedicated to nurturing confident, capable and ethical global leaders.",
        "Clear educational vision: fostering academic excellence, intellectual curiosity, and real-world skills.",
        "Core Values: Excellence, Responsibility, Respect, and Uncompromising Integrity.",
        "Modern campus designed for collaborative inquiry, active discussion, and digital innovation."
    ]
    for pt in points1:
        p = tf.add_paragraph()
        p.text = "• " + pt
        p.font.name = FONT_BODY
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_TEXT_BODY
        p.space_before = Pt(8)

    # Card 2: Academic Standards
    c2_x = start_x + col_w + gap
    add_card(s2, c2_x, top_y, col_w, card_h)
    add_rect(s2, c2_x, top_y, col_w, Inches(0.08), C_GOLD)
    tb = s2.shapes.add_textbox(c2_x + Inches(0.25), top_y + Inches(0.2), col_w - Inches(0.5), card_h - Inches(0.4))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "ACADEMIC STANDARDS"
    p.font.name = FONT_HEADING
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_NAVY_DARK
    
    points2 = [
        "Curriculum fully aligned with rigorous Cambridge International benchmarks and modern best practices.",
        "English-medium academic environment empowering global communication and scientific literacy.",
        "High expectations for conceptual depth, logical rigor, and independent problem-solving.",
        "Continuous syllabus compliance monitoring ensuring no student is left behind."
    ]
    for pt in points2:
        p = tf.add_paragraph()
        p.text = "• " + pt
        p.font.name = FONT_BODY
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_TEXT_BODY
        p.space_before = Pt(8)

    # Card 3: Commitment to Families
    c3_x = c2_x + col_w + gap
    add_card(s2, c3_x, top_y, col_w, card_h)
    add_rect(s2, c3_x, top_y, col_w, Inches(0.08), C_ACCENT_BLUE)
    tb = s2.shapes.add_textbox(c3_x + Inches(0.25), top_y + Inches(0.2), col_w - Inches(0.5), card_h - Inches(0.4))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "COMMITMENT TO FAMILIES"
    p.font.name = FONT_HEADING
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_NAVY_DARK
    
    points3 = [
        "A true partnership between school and home: transparent updates, open doors, and mutual respect.",
        "Holistic care: safeguarding student emotional wellbeing, healthy socialization, and self-confidence.",
        "Individualized academic support plans identifying strengths and addressing learning gaps early.",
        "Clear university preparation pathways designed to secure admissions to top global universities."
    ]
    for pt in points3:
        p = tf.add_paragraph()
        p.text = "• " + pt
        p.font.name = FONT_BODY
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_TEXT_BODY
        p.space_before = Pt(8)

    # Bottom Highlight Card
    add_card(s2, Inches(0.72), Inches(5.82), Inches(11.89), Inches(0.95), fill_color=C_WHITE, border_color=C_GOLD)
    tb_b = s2.shapes.add_textbox(Inches(0.95), Inches(5.92), Inches(11.4), Inches(0.75))
    tf_b = tb_b.text_frame
    tf_b.word_wrap = True
    p_b1 = tf_b.paragraphs[0]
    p_b1.text = "OUR GUIDING PRINCIPLE FOR EVERY LEARNER"
    p_b1.font.name = FONT_HEADING
    p_b1.font.size = Pt(10)
    p_b1.font.bold = True
    p_b1.font.color.rgb = C_GOLD
    p_b2 = tf_b.add_paragraph()
    p_b2.text = "\"Every child has potential. Our responsibility is to recognise it, develop it and prepare every student for a successful future.\""
    p_b2.font.name = FONT_HEADING
    p_b2.font.size = Pt(13)
    p_b2.font.bold = True
    p_b2.font.color.rgb = C_NAVY_DARK

    add_footer(s2, 2)

    # =========================================================================
    # SLIDE 3: OUR INTERNATIONAL ACADEMIC PATHWAYS
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3, C_BEIGE_BG)
    add_header(s3, "02 / ACADEMIC SYSTEM — HOW WE EDUCATE", "Our International Academic Pathways",
               "A connected educational trajectory from strong cognitive foundations to elite pre-university qualifications.")

    step_w = Inches(2.78)
    step_gap = Inches(0.25)
    step_h = Inches(4.0)

    steps_data = [
        ("01", "CAMBRIDGE PRIMARY &\nLOWER SECONDARY", "Grades 1–7",
         [
             "Strong foundations in English, Mathematics, Sciences and Computing.",
             "Inquiry-based learning fostering critical thinking and problem-solving.",
             "Formative diagnostic assessments mapping student progress.",
             "Developing confident English communication and academic discipline."
         ], C_NAVY_DARK),
        ("02", "CAMBRIDGE IGCSE\nQUALIFICATIONS", "Grades 8–9",
         [
             "Rigorous subject specialization across STEM and Economics tracks.",
             "Comprehensive preparation for international external examinations.",
             "Advanced laboratory experiments, analytical writing, and research tasks.",
             "Globally recognized certification valued by international institutions."
         ], C_GOLD),
        ("03", "CAMBRIDGE AS & A LEVEL\nADVANCED PATHWAY", "Grades 10–11",
         [
             "In-depth mastery in chosen pre-university specializations.",
             "Rigorous academic standards accepted by Ivy League, Russell Group, and global universities.",
             "Extensive independent study, essay argumentation, and quantitative analysis.",
             "Direct credit and competitive advantage for international university entry."
         ], C_ACCENT_BLUE),
        ("04", "WESTERN & AUSTRALIAN\nPATHWAY (PLANNED)", "Introduction 2027",
         [
             "Planned introduction of an Australian / Western education curriculum track.",
             "Dual-qualification pathways catering to diverse student career goals.",
             "Applied practical coursework, portfolio evaluations, and vocational electives.",
             "Expanded direct admission routes to universities in Australia, Canada, and Europe."
         ], C_ACCENT_GREEN)
    ]

    for i, (num, title, grade, items, accent) in enumerate(steps_data):
        cur_x = start_x + i * (step_w + step_gap)
        add_card(s3, cur_x, top_y, step_w, step_h)
        add_rect(s3, cur_x, top_y, step_w, Inches(0.08), accent)
        
        tb_num = s3.shapes.add_textbox(cur_x + Inches(0.2), top_y + Inches(0.18), Inches(0.8), Inches(0.45))
        tf_num = tb_num.text_frame
        p_n = tf_num.paragraphs[0]
        p_n.text = num
        p_n.font.name = FONT_HEADING
        p_n.font.size = Pt(22)
        p_n.font.bold = True
        p_n.font.color.rgb = accent

        tb_g = s3.shapes.add_textbox(cur_x + Inches(1.1), top_y + Inches(0.22), Inches(1.5), Inches(0.3))
        tf_g = tb_g.text_frame
        p_g = tf_g.paragraphs[0]
        p_g.alignment = PP_ALIGN.RIGHT
        p_g.text = grade
        p_g.font.name = FONT_HEADING
        p_g.font.size = Pt(9.5)
        p_g.font.bold = True
        p_g.font.color.rgb = C_TEXT_MUTED

        tb_t = s3.shapes.add_textbox(cur_x + Inches(0.2), top_y + Inches(0.68), step_w - Inches(0.4), Inches(0.75))
        tf_t = tb_t.text_frame
        tf_t.word_wrap = True
        p_t = tf_t.paragraphs[0]
        p_t.text = title
        p_t.font.name = FONT_HEADING
        p_t.font.size = Pt(11)
        p_t.font.bold = True
        p_t.font.color.rgb = C_NAVY_DARK

        tb_b = s3.shapes.add_textbox(cur_x + Inches(0.2), top_y + Inches(1.45), step_w - Inches(0.4), step_h - Inches(1.55))
        tf_b = tb_b.text_frame
        tf_b.word_wrap = True
        for j, it in enumerate(items):
            p = tf_b.paragraphs[0] if j == 0 else tf_b.add_paragraph()
            p.text = "• " + it
            p.font.name = FONT_BODY
            p.font.size = Pt(9.5)
            p.font.color.rgb = C_TEXT_BODY
            if j > 0:
                p.space_before = Pt(6)

    tb_bot = s3.shapes.add_textbox(Inches(0.72), Inches(6.12), Inches(11.89), Inches(0.6))
    tf_bot = tb_bot.text_frame
    p_bot = tf_bot.paragraphs[0]
    p_bot.text = "Continuous Curriculum Alignment: All academic pathways follow strict Cambridge International standards and are taught by certified subject specialists."
    p_bot.font.name = FONT_BODY
    p_bot.font.size = Pt(10.5)
    p_bot.font.color.rgb = C_TEXT_MUTED

    add_footer(s3, 3)

    # =========================================================================
    # SLIDE 4: SPECIALISATION FROM GRADES 8–9
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4, C_BEIGE_BG)
    add_header(s4, "02 / ACADEMIC SYSTEM — HOW WE EDUCATE", "Specialisation from Grades 8–9: Science vs Economics",
               "Targeted pathways aligned with student passions, aptitudes and long-term university goals.")

    col_w4 = Inches(5.8)
    gap4 = Inches(0.29)
    top_y4 = Inches(1.95)
    h4 = Inches(4.05)

    # Science Pathway
    add_card(s4, Inches(0.72), top_y4, col_w4, h4)
    add_rect(s4, Inches(0.72), top_y4, col_w4, Inches(0.55), C_NAVY_DARK)
    tb_st = s4.shapes.add_textbox(Inches(0.95), top_y4 + Inches(0.1), col_w4 - Inches(0.5), Inches(0.4))
    tf_st = tb_st.text_frame
    p = tf_st.paragraphs[0]
    p.text = "SCIENCE & STEM PATHWAY"
    p.font.name = FONT_HEADING
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_WHITE

    tb_sb = s4.shapes.add_textbox(Inches(0.95), top_y4 + Inches(0.68), col_w4 - Inches(0.5), h4 - Inches(0.8))
    tf_sb = tb_sb.text_frame
    tf_sb.word_wrap = True
    
    p = tf_sb.paragraphs[0]
    p.text = "CORE CURRICULUM SUBJECTS"
    p.font.name = FONT_HEADING
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = C_GOLD
    
    sc_subjects = [
        "Advanced Mathematics: Pure Mathematics, Mechanics, Statistics & Calculus",
        "Physics: Mechanics, Waves, Electricity, Thermal & Quantum Physics",
        "Chemistry: Physical Chemistry, Inorganic Analysis, Organic Synthesis",
        "Biology: Molecular Biology, Genetics, Human Physiology, Ecology",
        "Computer Science & IT: Algorithms, Vibecoding, AI Foundations, Python"
    ]
    for sub in sc_subjects:
        p = tf_sb.add_paragraph()
        p.text = "• " + sub
        p.font.name = FONT_BODY
        p.font.size = Pt(9.5)
        p.font.color.rgb = C_TEXT_BODY
        p.space_before = Pt(4)

    p = tf_sb.add_paragraph()
    p.text = "CAREER & UNIVERSITY DESTINATIONS"
    p.font.name = FONT_HEADING
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = C_NAVY_DARK
    p.space_before = Pt(10)

    p = tf_sb.add_paragraph()
    p.text = "Medicine, Biomedical Sciences, Computer Engineering, Artificial Intelligence, Mechanical & Aerospace Engineering, Data Science, Architecture."
    p.font.name = FONT_BODY
    p.font.size = Pt(9.5)
    p.font.color.rgb = C_TEXT_MUTED
    p.space_before = Pt(3)

    # Economics Pathway
    ec_x = Inches(0.72) + col_w4 + gap4
    add_card(s4, ec_x, top_y4, col_w4, h4)
    add_rect(s4, ec_x, top_y4, col_w4, Inches(0.55), C_GOLD)
    tb_et = s4.shapes.add_textbox(ec_x + Inches(0.25), top_y4 + Inches(0.1), col_w4 - Inches(0.5), Inches(0.4))
    tf_et = tb_et.text_frame
    p = tf_et.paragraphs[0]
    p.text = "ECONOMICS & BUSINESS PATHWAY"
    p.font.name = FONT_HEADING
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_NAVY_DARK

    tb_eb = s4.shapes.add_textbox(ec_x + Inches(0.25), top_y4 + Inches(0.68), col_w4 - Inches(0.5), h4 - Inches(0.8))
    tf_eb = tb_eb.text_frame
    tf_eb.word_wrap = True

    p = tf_eb.paragraphs[0]
    p.text = "CORE CURRICULUM SUBJECTS"
    p.font.name = FONT_HEADING
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = C_GOLD

    ec_subjects = [
        "Economics: Microeconomics, Macroeconomics, Market Structures, Fiscal Policy",
        "Business Studies: Marketing, Operations, Human Resources, Strategy",
        "Accounting & Finance: Financial Reporting, Auditing, Balance Sheets",
        "Applied Mathematics: Business Statistics, Financial Modeling, Optimization",
        "Global Perspectives & Research: Academic Writing, Global Trade, Policy Debate"
    ]
    for sub in ec_subjects:
        p = tf_eb.add_paragraph()
        p.text = "• " + sub
        p.font.name = FONT_BODY
        p.font.size = Pt(9.5)
        p.font.color.rgb = C_TEXT_BODY
        p.space_before = Pt(4)

    p = tf_eb.add_paragraph()
    p.text = "CAREER & UNIVERSITY DESTINATIONS"
    p.font.name = FONT_HEADING
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = C_NAVY_DARK
    p.space_before = Pt(10)

    p = tf_eb.add_paragraph()
    p.text = "International Economics, Investment Banking, Corporate Law, Management Consulting, International Relations, Fintech, Public Policy, Entrepreneurship."
    p.font.name = FONT_BODY
    p.font.size = Pt(9.5)
    p.font.color.rgb = C_TEXT_MUTED
    p.space_before = Pt(3)

    tb_g4 = s4.shapes.add_textbox(Inches(0.72), Inches(6.12), Inches(11.89), Inches(0.6))
    tf_g4 = tb_g4.text_frame
    p_g4 = tf_g4.paragraphs[0]
    p_g4.text = "Individual Guidance: Subject selection is guided by student academic assessments, psychological profiling, and personal university admissions roadmaps."
    p_g4.font.name = FONT_BODY
    p_g4.font.size = Pt(10.5)
    p_g4.font.color.rgb = C_TEXT_MUTED

    add_footer(s4, 4)

    # =========================================================================
    # SLIDE 5: GRADES 10–11: UNIVERSITY PREPARATION
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5, C_BEIGE_BG)
    add_header(s5, "02 / ACADEMIC SYSTEM — HOW WE EDUCATE", "Grades 10–11: University Preparation Programme",
               "A structured pre-university ecosystem ensuring competitive worldwide admissions.")

    card_w5 = Inches(3.78)
    card_h5 = Inches(1.9)
    gap_x5 = Inches(0.27)
    gap_y5 = Inches(0.22)
    start_x5 = Inches(0.72)
    start_y5 = Inches(1.95)

    u_pillars = [
        ("IELTS ACADEMIC INTENSIVE",
         "Target Band 7.5–8.5+",
         "Weekly full-length mock examinations, rigorous Task 1 & 2 academic essay writing coaching, and native-speaker oral interview simulations.",
         C_NAVY_DARK),
        ("DIGITAL SAT PREPARATION",
         "Target Score 1450–1550+",
         "Mastery of adaptive digital testing format: advanced Algebra, Geometry, and analytical Reading & Writing reasoning strategies.",
         C_GOLD),
        ("ACADEMIC ENGLISH & RESEARCH",
         "Pre-University Scholarly Skills",
         "Extended essay writing, research methodology, academic citation standards, and critical analysis of scholarly articles.",
         C_ACCENT_BLUE),
        ("UNIVERSITY APPLICATION GUIDANCE",
         "Global Admissions Strategy",
         "Comprehensive guidance on Common App, UCAS, and global portals: personal statements, institutional selection, and recommendation letters.",
         C_ACCENT_GREEN),
        ("PORTFOLIO & PROFILE BUILDING",
         "Extracurricular Distinction",
         "Guiding students in leadership initiatives, Olympiad credentials, published papers, social impact projects, and interview preparation.",
         C_ACCENT_CORAL),
        ("INTENSIVE PREPARATION SYSTEM",
         "The High-Focus 'Bunker' Programme",
         "Dedicated distraction-free study pods, supervised evening revision hours, peer study groups, and targeted one-on-one mentor consultations.",
         C_NAVY_DARK)
    ]

    for idx, (title, tag, desc, color) in enumerate(u_pillars):
        row = idx // 3
        col = idx % 3
        cur_x = start_x5 + col * (card_w5 + gap_x5)
        cur_y = start_y5 + row * (card_h5 + gap_y5)
        
        add_card(s5, cur_x, cur_y, card_w5, card_h5)
        add_rect(s5, cur_x, cur_y, card_w5, Inches(0.06), color)
        
        tb = s5.shapes.add_textbox(cur_x + Inches(0.2), cur_y + Inches(0.12), card_w5 - Inches(0.4), card_h5 - Inches(0.2))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = FONT_HEADING
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_NAVY_DARK

        p2 = tf.add_paragraph()
        p2.text = tag
        p2.font.name = FONT_HEADING
        p2.font.size = Pt(9.5)
        p2.font.bold = True
        p2.font.color.rgb = color
        p2.space_before = Pt(2)

        p3 = tf.add_paragraph()
        p3.text = desc
        p3.font.name = FONT_BODY
        p3.font.size = Pt(9)
        p3.font.color.rgb = C_TEXT_BODY
        p3.space_before = Pt(4)

    tb_b5 = s5.shapes.add_textbox(Inches(0.72), Inches(6.15), Inches(11.89), Inches(0.5))
    tf_b5 = tb_b5.text_frame
    p_b5 = tf_b5.paragraphs[0]
    p_b5.text = "Proven Admissions Results: 100% of our Grade 10–11 students receive personalized academic profiling and tailored university roadmap plans."
    p_b5.font.name = FONT_BODY
    p_b5.font.size = Pt(10.5)
    p_b5.font.color.rgb = C_TEXT_MUTED

    add_footer(s5, 5)

    # =========================================================================
    # SLIDE 6: OUR LEARNING MATERIALS & RESOURCES
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6, C_BEIGE_BG)
    add_header(s6, "02 / ACADEMIC SYSTEM — HOW WE EDUCATE", "Our Learning Materials & Curriculum Resources",
               "Cambridge-endorsed textbooks, hybrid resources and cutting-edge digital learning platforms.")

    col_w6 = Inches(2.78)
    gap6 = Inches(0.25)
    top_y6 = Inches(1.95)
    h6 = Inches(4.0)

    mat_cards = [
        ("CAMBRIDGE-ENDORSED\nTEXTBOOKS",
         "Primary, IGCSE & A Level",
         [
             "Official Cambridge University Press and Hodder Education endorsed textbooks.",
             "Standardized across Mathematics, Sciences, Business and English.",
             "Direct alignment with international exam learning objectives.",
             "Clear worked examples, structured theory, and end-of-chapter review problems."
         ], C_NAVY_DARK),
        ("HYBRID PROGRAMME\nCOURSEWARE",
         "Target Academic Blends",
         [
             "Custom school-curated course packs connecting Cambridge standards with national mastery.",
             "Bilingual scientific and economic terminology glossaries.",
             "Advanced problem-solving supplements designed by senior faculty.",
             "Structured study notes and concept maps for efficient review."
         ], C_GOLD),
        ("EXAMINATION WORKBOOKS\n& PAST PAPERS",
         "10-Year Exam Banks",
         [
             "Topic-by-topic past paper question banks covering recent Cambridge cycles.",
             "Official Cambridge mark scheme breakdowns and examiner commentary.",
             "Weekly revision workbooks reinforcing homework retention.",
             "Timed exam simulation booklets to build test-taking stamina."
         ], C_ACCENT_BLUE),
        ("DIGITAL LEARNING\nPLATFORMS",
         "Smart E-Learning Tools",
         [
             "School learning management portal with 24/7 syllabus access.",
             "Interactive online STEM simulations and digital laboratories.",
             "Automated diagnostic quizzes providing immediate feedback.",
             "Cloud-based assignment submission and teacher grading commentary."
         ], C_ACCENT_GREEN)
    ]

    for idx, (title, sub, bullets, color) in enumerate(mat_cards):
        cur_x = start_x + idx * (col_w6 + gap6)
        add_card(s6, cur_x, top_y6, col_w6, h6)
        add_rect(s6, cur_x, top_y6, col_w6, Inches(0.08), color)
        
        tb = s6.shapes.add_textbox(cur_x + Inches(0.2), top_y6 + Inches(0.18), col_w6 - Inches(0.4), Inches(0.85))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = FONT_HEADING
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_NAVY_DARK

        p_s = tf.add_paragraph()
        p_s.text = sub
        p_s.font.name = FONT_HEADING
        p_s.font.size = Pt(9.5)
        p_s.font.bold = True
        p_s.font.color.rgb = color
        p_s.space_before = Pt(2)

        tb_b = s6.shapes.add_textbox(cur_x + Inches(0.2), top_y6 + Inches(1.15), col_w6 - Inches(0.4), h6 - Inches(1.25))
        tf_b = tb_b.text_frame
        tf_b.word_wrap = True
        for j, b in enumerate(bullets):
            p = tf_b.paragraphs[0] if j == 0 else tf_b.add_paragraph()
            p.text = "• " + b
            p.font.name = FONT_BODY
            p.font.size = Pt(9.5)
            p.font.color.rgb = C_TEXT_BODY
            if j > 0:
                p.space_before = Pt(6)

    tb_b6 = s6.shapes.add_textbox(Inches(0.72), Inches(6.12), Inches(11.89), Inches(0.6))
    tf_b6 = tb_b6.text_frame
    p_b6 = tf_b6.paragraphs[0]
    p_b6.text = "Resource Standard: Every student receives official printed coursebooks and verified portal credentials at the start of the academic year."
    p_b6.font.name = FONT_BODY
    p_b6.font.size = Pt(10.5)
    p_b6.font.color.rgb = C_TEXT_MUTED

    add_footer(s6, 6)

    # =========================================================================
    # SLIDE 7: TEACHER PERFORMANCE & LESSON QUALITY
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7, C_BEIGE_BG)
    add_header(s7, "03 / ACADEMIC QUALITY & MONITORING", "Teacher Performance & Lesson Quality Assurance",
               "How Target International School systematically evaluates teaching delivery and drives continuous improvement.")

    grid_w7 = Inches(5.8)
    grid_h7 = Inches(1.9)
    gap_x7 = Inches(0.29)
    gap_y7 = Inches(0.22)
    top_y7 = Inches(1.95)

    q_cards = [
        ("CLASSROOM AUDIO-RECORDING TECHNOLOGY",
         "Pedagogical Analysis & Clarity",
         "Where implemented, lessons are digitally recorded to evaluate teacher explanation clarity, student question response time, and pacing. Recordings serve as constructive evidence for internal peer reviews and pedagogical coaching.",
         C_NAVY_DARK),
        ("STRUCTURED LESSON OBSERVATIONS",
         "Academic Leadership Audits",
         "The Academic Director and Cambridge coordinators conduct regular announced and unannounced classroom evaluations using internationally benchmarked rubrics: active engagement, conceptual clarity, and task differentiation.",
         C_GOLD),
        ("CURRICULUM & SYLLABUS COMPLIANCE",
         "Rigorous Coverage Audits",
         "Every subject department maps weekly lesson completion against the official Cambridge scheme of work. Automated tracking guarantees no core concepts or exam preparation modules are compressed or omitted.",
         C_ACCENT_BLUE),
        ("CONTINUOUS PROFESSIONAL DEVELOPMENT (CPD)",
         "Teacher Growth & Cambridge Training",
         "Faculty participate in bi-weekly instructional workshops, Cambridge assessment webinars, modern pedagogy circles, and peer observation sessions to ensure teaching methodology reflects the latest educational research.",
         C_ACCENT_GREEN)
    ]

    for idx, (title, sub, desc, color) in enumerate(q_cards):
        r = idx // 2
        c = idx % 2
        cur_x = Inches(0.72) + c * (grid_w7 + gap_x7)
        cur_y = top_y7 + r * (grid_h7 + gap_y7)
        
        add_card(s7, cur_x, cur_y, grid_w7, grid_h7)
        add_rect(s7, cur_x, cur_y, grid_w7, Inches(0.06), color)
        
        tb = s7.shapes.add_textbox(cur_x + Inches(0.25), cur_y + Inches(0.15), grid_w7 - Inches(0.5), grid_h7 - Inches(0.25))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = FONT_HEADING
        p.font.size = Pt(11.5)
        p.font.bold = True
        p.font.color.rgb = C_NAVY_DARK

        p2 = tf.add_paragraph()
        p2.text = sub
        p2.font.name = FONT_HEADING
        p2.font.size = Pt(9.5)
        p2.font.bold = True
        p2.font.color.rgb = color
        p2.space_before = Pt(2)

        p3 = tf.add_paragraph()
        p3.text = desc
        p3.font.name = FONT_BODY
        p3.font.size = Pt(9.5)
        p3.font.color.rgb = C_TEXT_BODY
        p3.space_before = Pt(4)

    tb_b7 = s7.shapes.add_textbox(Inches(0.72), Inches(6.15), Inches(11.89), Inches(0.5))
    tf_b7 = tb_b7.text_frame
    p_b7 = tf_b7.paragraphs[0]
    p_b7.text = "Pedagogical Support: Monitoring is not punitive — it provides our academic leaders with clear diagnostic data to support every teacher in excelling."
    p_b7.font.name = FONT_BODY
    p_b7.font.size = Pt(10.5)
    p_b7.font.color.rgb = C_TEXT_MUTED

    add_footer(s7, 7)

    # =========================================================================
    # SLIDE 8: SMART CLASSROOM & STUDENT ENGAGEMENT
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8, C_BEIGE_BG)
    add_header(s8, "03 / ACADEMIC QUALITY & MONITORING", "Smart Classroom & Student Engagement",
               "Integrating modern educational technology, student safety and responsible classroom analytics.")

    card_w8 = Inches(5.8)
    card_h8 = Inches(3.95)
    top_y8 = Inches(1.95)

    # Left: Smart Infrastructure & Safety
    add_card(s8, Inches(0.72), top_y8, card_w8, card_h8)
    add_rect(s8, Inches(0.72), top_y8, card_w8, Inches(0.55), C_NAVY_DARK)
    tb_8l = s8.shapes.add_textbox(Inches(0.95), top_y8 + Inches(0.1), card_w8 - Inches(0.5), Inches(0.4))
    tf_8l = tb_8l.text_frame
    p = tf_8l.paragraphs[0]
    p.text = "SMART INFRASTRUCTURE & SAFETY"
    p.font.name = FONT_HEADING
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_WHITE

    tb_lb = s8.shapes.add_textbox(Inches(0.95), top_y8 + Inches(0.68), card_w8 - Inches(0.5), card_h8 - Inches(0.8))
    tf_lb = tb_lb.text_frame
    tf_lb.word_wrap = True

    pts_8l = [
        ("HD Classroom Cameras", "Continuous camera infrastructure ensuring physical safeguarding, positive behavior, and a secure learning environment."),
        ("Interactive Touch Smartboards", "Every classroom is equipped with large interactive 4K touch displays for dynamic multimedia presentations, live student demonstrations, and collaborative problem solving."),
        ("Secure Campus Network", "Restricted educational Wi-Fi with AI-powered content filtering protecting students from digital distractions and harmful material."),
        ("Digital Attendance Registers", "Instant automated lesson-by-lesson attendance and punctuality logging with immediate alert system for tutors.")
    ]
    for idx, (head, body) in enumerate(pts_8l):
        p = tf_lb.paragraphs[0] if idx == 0 else tf_lb.add_paragraph()
        p.text = head + ": "
        p.font.name = FONT_HEADING
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = C_NAVY_DARK
        if idx > 0:
            p.space_before = Pt(8)

        run = p.add_run()
        run.text = body
        run.font.name = FONT_BODY
        run.font.size = Pt(9.5)
        run.font.bold = False
        run.font.color.rgb = C_TEXT_BODY

    # Right: Engagement Analytics & Support
    c8r_x = Inches(0.72) + card_w8 + Inches(0.29)
    add_card(s8, c8r_x, top_y8, card_w8, card_h8)
    add_rect(s8, c8r_x, top_y8, card_w8, Inches(0.55), C_GOLD)
    tb_8r = s8.shapes.add_textbox(c8r_x + Inches(0.25), top_y8 + Inches(0.1), card_w8 - Inches(0.5), Inches(0.4))
    tf_8r = tb_8r.text_frame
    p = tf_8r.paragraphs[0]
    p.text = "STUDENT ENGAGEMENT & SUPPORT"
    p.font.name = FONT_HEADING
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_NAVY_DARK

    tb_rb = s8.shapes.add_textbox(c8r_x + Inches(0.25), top_y8 + Inches(0.68), card_w8 - Inches(0.5), card_h8 - Inches(0.8))
    tf_rb = tb_rb.text_frame
    tf_rb.word_wrap = True

    pts_8r = [
        ("Participation Tracking", "Observing student hand-raising, classroom contributions, peer discussions, and practical task execution during every block."),
        ("Early Support Identification", "Quickly recognizing students who hesitate, struggle with specific exercises, or disengage, enabling immediate teacher intervention."),
        ("Responsible Classroom Analytics", "Ethical observation of learning habits to inform teacher differentiation without invasive or unverified behavioral profiling."),
        ("Privacy & Strict Confidentiality", "Classroom recordings and observational data are strictly confidential, restricted to authorized leadership, and governed by school privacy policy.")
    ]
    for idx, (head, body) in enumerate(pts_8r):
        p = tf_rb.paragraphs[0] if idx == 0 else tf_rb.add_paragraph()
        p.text = head + ": "
        p.font.name = FONT_HEADING
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = C_GOLD
        if idx > 0:
            p.space_before = Pt(8)

        run = p.add_run()
        run.text = body
        run.font.name = FONT_BODY
        run.font.size = Pt(9.5)
        run.font.bold = False
        run.font.color.rgb = C_TEXT_BODY

    tb_b8 = s8.shapes.add_textbox(Inches(0.72), Inches(6.12), Inches(11.89), Inches(0.6))
    tf_b8 = tb_b8.text_frame
    p_b8 = tf_b8.paragraphs[0]
    p_b8.text = "Data Protection Commitment: All classroom technology serves one primary goal — student safety, pedagogical excellence, and targeted academic care."
    p_b8.font.name = FONT_BODY
    p_b8.font.size = Pt(10.5)
    p_b8.font.color.rgb = C_TEXT_MUTED

    add_footer(s8, 8)

    # =========================================================================
    # SLIDE 9: MEET OUR ACADEMIC TEAM
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9, C_BEIGE_BG)
    add_header(s9, "03 / ACADEMIC QUALITY & MONITORING", "Meet Our Academic Team",
               "Dedicated subject specialists holding advanced international qualifications and pedagogical experience.")

    stat_w9 = Inches(3.78)
    stat_gap9 = Inches(0.27)
    stat_h9 = Inches(1.15)
    top_y9 = Inches(1.95)

    stats = [
        ("100%", "ACADEMIC DEGREE QUALIFIED", "Master's & Bachelor's in their teaching subjects"),
        ("8.2 YRS", "AVERAGE TEACHING EXPERIENCE", "Proven international & Cambridge school track records"),
        ("1 : 12", "TEACHER-TO-STUDENT RATIO", "Personalized mentoring & individualized attention")
    ]
    for idx, (val, title, caption) in enumerate(stats):
        cur_x = Inches(0.72) + idx * (stat_w9 + stat_gap9)
        add_card(s9, cur_x, top_y9, stat_w9, stat_h9)
        
        tb = s9.shapes.add_textbox(cur_x + Inches(0.2), top_y9 + Inches(0.12), stat_w9 - Inches(0.4), stat_h9 - Inches(0.24))
        tf = tb.text_frame
        p = tf.paragraphs[0]
        p.text = val
        p.font.name = FONT_HEADING
        p.font.size = Pt(22)
        p.font.bold = True
        p.font.color.rgb = C_GOLD

        p2 = tf.add_paragraph()
        p2.text = title + " • " + caption
        p2.font.name = FONT_BODY
        p2.font.size = Pt(9)
        p2.font.bold = True
        p2.font.color.rgb = C_NAVY_DARK

    dept_w9 = Inches(2.78)
    dept_gap9 = Inches(0.25)
    dept_top9 = Inches(3.3)
    dept_h9 = Inches(2.75)

    depts = [
        ("ENGLISH &\nHUMANITIES",
         "Language, Literature & History",
         [
             "Cambridge English First Language & Second Language specialists.",
             "IELTS certified examiners and academic writing mentors.",
             "World History & Global Perspectives debate coaches.",
             "Focus: advanced argumentation and critical thinking."
         ], C_NAVY_DARK),
        ("MATHEMATICS &\nSCIENCES",
         "STEM Core Faculty",
         [
             "Senior educators with degrees in Pure Mathematics, Physics & Chemistry.",
             "National & International Olympiad medal-winning trainers.",
             "Extensive laboratory research and practical demonstration background.",
             "Focus: analytical problem solving and scientific rigor."
         ], C_GOLD),
        ("TECHNOLOGY &\nROBOTICS",
         "Computing & Innovation",
         [
             "Software engineers and Computer Science degree holders.",
             "Vibecoding, Python, AI foundations, and robotics hackathon leaders.",
             "Hands-on practical engineering and app architecture guidance.",
             "Focus: modern engineering and technological literacy."
         ], C_ACCENT_BLUE),
        ("ECONOMICS &\nCOMMERCE",
         "Business & Social Sciences",
         [
             "Specialists in Micro/Macroeconomics, Business Studies & Accounting.",
             "Real-world financial modeling and business case-study instructors.",
             "University admissions mentors for business and finance faculties.",
             "Focus: market literacy, strategic analysis & leadership."
         ], C_ACCENT_GREEN)
    ]

    for idx, (title, sub, bullets, color) in enumerate(depts):
        cur_x = Inches(0.72) + idx * (dept_w9 + dept_gap9)
        add_card(s9, cur_x, dept_top9, dept_w9, dept_h9)
        add_rect(s9, cur_x, dept_top9, dept_w9, Inches(0.06), color)
        
        tb = s9.shapes.add_textbox(cur_x + Inches(0.2), dept_top9 + Inches(0.15), dept_w9 - Inches(0.4), dept_h9 - Inches(0.3))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = FONT_HEADING
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_NAVY_DARK

        p2 = tf.add_paragraph()
        p2.text = sub
        p2.font.name = FONT_BODY
        p2.font.size = Pt(8.5)
        p2.font.bold = True
        p2.font.color.rgb = color
        p2.space_before = Pt(2)

        for j, b in enumerate(bullets):
            p = tf.add_paragraph()
            p.text = "• " + b
            p.font.name = FONT_BODY
            p.font.size = Pt(9)
            p.font.color.rgb = C_TEXT_BODY
            p.space_before = Pt(4)

    tb_b9 = s9.shapes.add_textbox(Inches(0.72), Inches(6.15), Inches(11.89), Inches(0.5))
    tf_b9 = tb_b9.text_frame
    p_b9 = tf_b9.paragraphs[0]
    p_b9.text = "Teacher Profiles: Comprehensive biographies, academic credentials and office hours are accessible through our school administration portal."
    p_b9.font.name = FONT_BODY
    p_b9.font.size = Pt(10.5)
    p_b9.font.color.rgb = C_TEXT_MUTED

    add_footer(s9, 9)

    # =========================================================================
    # SLIDE 10: OUR STUDENTS' ACHIEVEMENTS: PAST, PRESENT & FUTURE
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_background(s10, C_BEIGE_BG)
    add_header(s10, "04 / ASSESSMENT, ACHIEVEMENTS & STUDENT DEVELOPMENT", "Our Students' Achievements: Past, Present & Future",
               "Celebrating verified competition victories, ongoing academic growth and upcoming horizons.")

    col_w10 = Inches(3.75)
    gap10 = Inches(0.3)
    top_y10 = Inches(1.95)
    h10 = Inches(4.05)

    achieve_cols = [
        ("PAST ACHIEVEMENTS",
         "Olympiad Victories & Milestones",
         [
             "National & Regional Olympiad Medals in Mathematics, Physics, and English.",
             "Top percentile rankings in Cambridge Checkpoint diagnostic assessments.",
             "100% successful progression rate across all secondary school grades.",
             "Distinguished awards in regional debate tournaments and scientific essay challenges.",
             "Graduates accepted into leading international and domestic universities."
         ], C_NAVY_DARK),
        ("PRESENT TERM PROGRESS",
         "Current Academic Momentum",
         [
             "100% completion of Term 1 Cambridge syllabus objectives across all classes.",
             "High average homework completion rate exceeding 92% school-wide.",
             "Active student participation in weekly coding hackathons and STEM clubs.",
             "Consistent growth in reading comprehension, analytical writing, and mental arithmetic.",
             "High attendance rate (over 94%) reflecting strong student engagement."
         ], C_GOLD),
        ("UPCOMING HORIZONS",
         "Future Competitions & Goals",
         [
             "Confirmed registrations for SASMO, American Math Competitions (AMC), and Kangaroo Math.",
             "World Scholar's Cup (WSC) regional and global round preparation teams.",
             "Target International School Annual Science & Technology Fair.",
             "Target benchmark: Over 85% of students targeting A*/A in Cambridge mock assessments.",
             "Structured SAT & IELTS candidate milestone evaluations."
         ], C_ACCENT_GREEN)
    ]

    for idx, (title, sub, bullets, color) in enumerate(achieve_cols):
        cur_x = Inches(0.72) + idx * (col_w10 + gap10)
        add_card(s10, cur_x, top_y10, col_w10, h10)
        add_rect(s10, cur_x, top_y10, col_w10, Inches(0.5), color)
        
        tb = s10.shapes.add_textbox(cur_x + Inches(0.2), top_y10 + Inches(0.08), col_w10 - Inches(0.4), Inches(0.4))
        tf = tb.text_frame
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = FONT_HEADING
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = C_WHITE if color != C_GOLD else C_NAVY_DARK

        tb_b = s10.shapes.add_textbox(cur_x + Inches(0.25), top_y10 + Inches(0.6), col_w10 - Inches(0.5), h10 - Inches(0.7))
        tf_b = tb_b.text_frame
        tf_b.word_wrap = True
        
        p = tf_b.paragraphs[0]
        p.text = sub
        p.font.name = FONT_HEADING
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = color if color != C_WHITE else C_NAVY_DARK

        for j, b in enumerate(bullets):
            p = tf_b.add_paragraph()
            p.text = "• " + b
            p.font.name = FONT_BODY
            p.font.size = Pt(9.5)
            p.font.color.rgb = C_TEXT_BODY
            p.space_before = Pt(6)

    tb_b10 = s10.shapes.add_textbox(Inches(0.72), Inches(6.12), Inches(11.89), Inches(0.6))
    tf_b10 = tb_b10.text_frame
    p_b10 = tf_b10.paragraphs[0]
    p_b10.text = "Celebrating Every Learner: We celebrate not only top test scores, but also determination, character growth, and personal improvement."
    p_b10.font.name = FONT_BODY
    p_b10.font.size = Pt(10.5)
    p_b10.font.color.rgb = C_TEXT_MUTED

    add_footer(s10, 10)

    # =========================================================================
    # SLIDE 11: OUR WEEKLY ASSESSMENT SYSTEM
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_background(s11, C_BEIGE_BG)
    add_header(s11, "04 / ASSESSMENT, ACHIEVEMENTS & STUDENT DEVELOPMENT", "Our Weekly Assessment System: 4-Week Cycle",
               "A continuous cycle balancing rigorous academic mastery with student psychological wellbeing.")

    step_w11 = Inches(2.78)
    gap11 = Inches(0.25)
    top_y11 = Inches(1.95)
    h11 = Inches(3.7)

    cycle_data = [
        ("WEEK 1", "PSYCHOLOGICAL &\nWELLBEING CHECK",
         [
             "Evaluates emotional wellbeing, adaptation, and school belonging.",
             "Monitors stress levels, sleep routines, and social dynamics.",
             "Conducted by homeroom tutors and school psychologist.",
             "Ensures positive mental health for academic readiness."
         ], C_NAVY_DARK),
        ("WEEK 2", "ACADEMIC SUBJECT\nDIAGNOSTIC TEST",
         [
             "Formative assessments across core academic subjects.",
             "Tests concept retention, problem-solving, and homework consistency.",
             "Provides quick diagnostic insight to subject teachers.",
             "Pinpoints topics requiring reinforcement."
         ], C_GOLD),
        ("WEEK 3", "PSYCHOLOGICAL &\nENGAGEMENT REVIEW",
         [
             "Monitors classroom focus, study discipline, and participation habits.",
             "Identifies students who may feel overwhelmed or demotivated.",
             "Provides one-on-one pastoral counseling where needed.",
             "Strengthens student resilience and positive mindset."
         ], C_ACCENT_BLUE),
        ("WEEK 4", "ACADEMIC PROGRESS\nEVALUATION & MOCK",
         [
             "Comprehensive unit assessment evaluating analytical depth.",
             "Simulates Cambridge exam question formats and time management.",
             "Detailed score breakdown shared with parents.",
             "Actionable study plan created for the subsequent cycle."
         ], C_ACCENT_GREEN)
    ]

    for idx, (wk, title, bullets, color) in enumerate(cycle_data):
        cur_x = Inches(0.72) + idx * (step_w11 + gap11)
        add_card(s11, cur_x, top_y11, step_w11, h11)
        add_rect(s11, cur_x, top_y11, step_w11, Inches(0.08), color)
        
        tb = s11.shapes.add_textbox(cur_x + Inches(0.2), top_y11 + Inches(0.18), step_w11 - Inches(0.4), Inches(0.95))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = wk
        p.font.name = FONT_HEADING
        p.font.size = Pt(20)
        p.font.bold = True
        p.font.color.rgb = color

        p2 = tf.add_paragraph()
        p2.text = title
        p2.font.name = FONT_HEADING
        p2.font.size = Pt(11)
        p2.font.bold = True
        p2.font.color.rgb = C_NAVY_DARK
        p2.space_before = Pt(2)

        tb_b = s11.shapes.add_textbox(cur_x + Inches(0.2), top_y11 + Inches(1.3), step_w11 - Inches(0.4), h11 - Inches(1.4))
        tf_b = tb_b.text_frame
        tf_b.word_wrap = True
        for j, b in enumerate(bullets):
            p = tf_b.paragraphs[0] if j == 0 else tf_b.add_paragraph()
            p.text = "• " + b
            p.font.name = FONT_BODY
            p.font.size = Pt(9.5)
            p.font.color.rgb = C_TEXT_BODY
            if j > 0:
                p.space_before = Pt(6)

    add_card(s11, Inches(0.72), Inches(5.82), Inches(11.89), Inches(0.95), fill_color=C_WHITE, border_color=C_GOLD)
    tb_b11 = s11.shapes.add_textbox(Inches(0.95), Inches(5.92), Inches(11.4), Inches(0.75))
    tf_b11 = tb_b11.text_frame
    p = tf_b11.paragraphs[0]
    p.text = "EARLY INTERVENTION ADVANTAGE"
    p.font.name = FONT_HEADING
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = C_GOLD

    p2 = tf_b11.add_paragraph()
    p2.text = "The alternating 4-week cycle ensures that learning gaps or emotional hurdles are identified within days, allowing teachers and parents to deliver targeted support before termly examinations."
    p2.font.name = FONT_BODY
    p2.font.size = Pt(11)
    p2.font.color.rgb = C_NAVY_DARK

    add_footer(s11, 11)

    # =========================================================================
    # SLIDE 12: TERMLY EXAMINATION & ACADEMIC ANALYTICS
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    set_slide_background(s12, C_BEIGE_BG)
    add_header(s12, "04 / ASSESSMENT, ACHIEVEMENTS & STUDENT DEVELOPMENT", "Termly Examination & Academic Analytics",
               "Standardized examination administration, secure moderation and comprehensive analytics reporting.")

    p_w12 = Inches(2.78)
    p_gap12 = Inches(0.25)
    p_h12 = Inches(1.8)
    top_y12 = Inches(1.95)

    stages = [
        ("STAGE 1", "REVISION & PREPARATION",
         "Subject teachers prepare comprehensive syllabus revision matrices, past paper practice sets, and targeted review sessions for students."),
        ("STAGE 2", "STANDARDIZED EXAMS",
         "Examinations conducted under formal Cambridge exam conditions, overseen directly by the official Cambridge Exam Officer."),
        ("STAGE 3", "SECURE MODERATION",
         "Double-blind grading, standardized rubric moderation, and departmental score verification ensure complete evaluation fairness."),
        ("STAGE 4", "DATA ANALYTICS REPORT",
         "Comprehensive analytics dashboards generated: subject proficiency, cohort comparisons, and individualized student action plans.")
    ]

    for idx, (stg, title, desc) in enumerate(stages):
        cur_x = Inches(0.72) + idx * (p_w12 + p_gap12)
        add_card(s12, cur_x, top_y12, p_w12, p_h12)
        add_rect(s12, cur_x, top_y12, p_w12, Inches(0.06), C_GOLD)
        
        tb = s12.shapes.add_textbox(cur_x + Inches(0.2), top_y12 + Inches(0.12), p_w12 - Inches(0.4), p_h12 - Inches(0.2))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = stg
        p.font.name = FONT_HEADING
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = C_GOLD

        p2 = tf.add_paragraph()
        p2.text = title
        p2.font.name = FONT_HEADING
        p2.font.size = Pt(11)
        p2.font.bold = True
        p2.font.color.rgb = C_NAVY_DARK
        p2.space_before = Pt(2)

        p3 = tf.add_paragraph()
        p3.text = desc
        p3.font.name = FONT_BODY
        p3.font.size = Pt(9)
        p3.font.color.rgb = C_TEXT_BODY
        p3.space_before = Pt(4)

    bot_y12 = Inches(3.95)
    bot_h12 = Inches(2.05)
    col_w12 = Inches(5.8)

    # Left: Analytics Details
    add_card(s12, Inches(0.72), bot_y12, col_w12, bot_h12)
    add_rect(s12, Inches(0.72), bot_y12, col_w12, Inches(0.45), C_NAVY_DARK)
    tb_l = s12.shapes.add_textbox(Inches(0.95), bot_y12 + Inches(0.08), col_w12 - Inches(0.5), Inches(0.35))
    tf_l = tb_l.text_frame
    p = tf_l.paragraphs[0]
    p.text = "INDIVIDUAL ACADEMIC ANALYTICS DASHBOARDS"
    p.font.name = FONT_HEADING
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_WHITE

    tb_lb = s12.shapes.add_textbox(Inches(0.95), bot_y12 + Inches(0.55), col_w12 - Inches(0.5), bot_h12 - Inches(0.65))
    tf_lb = tb_lb.text_frame
    tf_lb.word_wrap = True
    analytics_pts = [
        "Every family receives a transparent diagnostic report after termly examinations.",
        "Detailed breakdown: raw score, class average, cohort percentile, and topic mastery.",
        "Specific teacher recommendations outlining clear focus areas for the next term."
    ]
    for idx, pt in enumerate(analytics_pts):
        p = tf_lb.paragraphs[0] if idx == 0 else tf_lb.add_paragraph()
        p.text = "• " + pt
        p.font.name = FONT_BODY
        p.font.size = Pt(9.5)
        p.font.color.rgb = C_TEXT_BODY
        if idx > 0:
            p.space_before = Pt(4)

    # Right: Calendar & Timeline
    r_x12 = Inches(0.72) + col_w12 + Inches(0.29)
    add_card(s12, r_x12, bot_y12, col_w12, bot_h12)
    add_rect(s12, r_x12, bot_y12, col_w12, Inches(0.45), C_GOLD)
    tb_r = s12.shapes.add_textbox(r_x12 + Inches(0.25), bot_y12 + Inches(0.08), col_w12 - Inches(0.5), Inches(0.35))
    tf_r = tb_r.text_frame
    p = tf_r.paragraphs[0]
    p.text = "EXAMINATION TIMELINE & WINDOW"
    p.font.name = FONT_HEADING
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_NAVY_DARK

    tb_rb = s12.shapes.add_textbox(r_x12 + Inches(0.25), bot_y12 + Inches(0.55), col_w12 - Inches(0.5), bot_h12 - Inches(0.65))
    tf_rb = tb_rb.text_frame
    tf_rb.word_wrap = True
    time_pts = [
        "Official Examination Window: 20th–30th of the designated examination month.",
        "Strict compliance with Target International School approved calendar.",
        "Parent consultations held immediately following publication of exam results."
    ]
    for idx, pt in enumerate(time_pts):
        p = tf_rb.paragraphs[0] if idx == 0 else tf_rb.add_paragraph()
        p.text = "• " + pt
        p.font.name = FONT_BODY
        p.font.size = Pt(9.5)
        p.font.color.rgb = C_TEXT_BODY
        if idx > 0:
            p.space_before = Pt(4)

    tb_b12 = s12.shapes.add_textbox(Inches(0.72), Inches(6.15), Inches(11.89), Inches(0.5))
    tf_b12 = tb_b12.text_frame
    p_b12 = tf_b12.paragraphs[0]
    p_b12.text = "Standardization: All examinations are overseen by the Cambridge Exam Officer to guarantee absolute credibility and procedural integrity."
    p_b12.font.name = FONT_BODY
    p_b12.font.size = Pt(10.5)
    p_b12.font.color.rgb = C_TEXT_MUTED

    add_footer(s12, 12)

    # =========================================================================
    # SLIDE 13: OLYMPIADS & FUTURE ACADEMIC OPPORTUNITIES
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    set_slide_background(s13, C_BEIGE_BG)
    add_header(s13, "04 / ASSESSMENT, ACHIEVEMENTS & STUDENT DEVELOPMENT", "Olympiads & Future Academic Opportunities",
               "Empowering students to challenge themselves against top national and international peers.")

    card_w13 = Inches(5.8)
    card_h13 = Inches(1.9)
    gap_x13 = Inches(0.29)
    gap_y13 = Inches(0.22)
    top_y13 = Inches(1.95)

    olympiad_cards = [
        ("MATHEMATICS OLYMPIADS",
         "SASMO, AMC 8/10/12, Kangaroo Math",
         "Structured preparation for elite mathematical challenges: developing non-routine problem solving, spatial intuition, and rigorous logical deduction under competitive timed conditions.",
         C_NAVY_DARK),
        ("SCIENCE & RESEARCH COMPETITIONS",
         "Physics, Chemistry & Biology Olympiads",
         "Hands-on scientific inquiry, experimental design contests, environmental symposiums, and national science olympiads. Students learn to defend hypotheses with empirical data.",
         C_GOLD),
        ("WORLD SCHOLAR'S CUP & DEBATE",
         "Global Academic Tournaments",
         "Team debate, collaborative writing, and multidisciplinary scholar's bowl. Training students to articulate nuanced perspectives on history, social issues, science, and literature.",
         C_ACCENT_BLUE),
        ("INNOVATION, AI & ROBOTICS HACKATHONS",
         "Target Vibecoding & STEM Challenges",
         "School and national hackathons where students build real-world software applications, robotics prototypes, and AI solutions, translating classroom theory into tangible engineering achievements.",
         C_ACCENT_GREEN)
    ]

    for idx, (title, sub, desc, color) in enumerate(olympiad_cards):
        r = idx // 2
        c = idx % 2
        cur_x = Inches(0.72) + c * (card_w13 + gap_x13)
        cur_y = top_y13 + r * (card_h13 + gap_y13)
        
        add_card(s13, cur_x, cur_y, card_w13, card_h13)
        add_rect(s13, cur_x, cur_y, card_w13, Inches(0.06), color)
        
        tb = s13.shapes.add_textbox(cur_x + Inches(0.25), cur_y + Inches(0.15), card_w13 - Inches(0.5), card_h13 - Inches(0.25))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = FONT_HEADING
        p.font.size = Pt(11.5)
        p.font.bold = True
        p.font.color.rgb = C_NAVY_DARK

        p2 = tf.add_paragraph()
        p2.text = sub
        p2.font.name = FONT_HEADING
        p2.font.size = Pt(9.5)
        p2.font.bold = True
        p2.font.color.rgb = color
        p2.space_before = Pt(2)

        p3 = tf.add_paragraph()
        p3.text = desc
        p3.font.name = FONT_BODY
        p3.font.size = Pt(9.5)
        p3.font.color.rgb = C_TEXT_BODY
        p3.space_before = Pt(4)

    tb_b13 = s13.shapes.add_textbox(Inches(0.72), Inches(6.15), Inches(11.89), Inches(0.5))
    tf_b13 = tb_b13.text_frame
    p_b13 = tf_b13.paragraphs[0]
    p_b13.text = "Mentorship Support: Dedicated after-school Olympiad training clubs and faculty coaching ensure every registered candidate is thoroughly prepared."
    p_b13.font.name = FONT_BODY
    p_b13.font.size = Pt(10.5)
    p_b13.font.color.rgb = C_TEXT_MUTED

    add_footer(s13, 13)

    # =========================================================================
    # SLIDE 14: SCHOOL EVENTS & EXTRACURRICULAR ACTIVITIES
    # =========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    set_slide_background(s14, C_BEIGE_BG)
    add_header(s14, "05 / SCHOOL LIFE & STUDENT WELFARE", "School Events & Extracurricular Activities",
               "Nurturing leadership, creativity, team spirit and social responsibility beyond academic lessons.")

    col_w14 = Inches(3.75)
    gap14 = Inches(0.3)
    top_y14 = Inches(1.95)
    h14 = Inches(4.05)

    ev_cols = [
        ("SUCCESSFULLY COMPLETED",
         "Recent School Highlights",
         [
             "Grand Academic Opening & Welcome Assembly",
             "Teachers' Day Appreciation Gala & Student Concert",
             "Autumn Inter-House Sports & Cross-Country Championship",
             "First Quarter Science & Robotics Interactive Showcase",
             "Community Charity Book Drive & Student Art Exhibition"
         ], C_NAVY_DARK),
        ("WEEKLY CLUBS & SOCIETIES",
         "Active Student Engagement",
         [
             "Robotics, AI & Vibecoding Innovation Studio",
             "Model United Nations (MUN) & Parliamentary Debate",
             "Chess Academy: Tactical Theory & Blitz Tournaments",
             "Performing Arts, Drama Society & School Choir",
             "Competitive Sports: Football, Basketball & Table Tennis"
         ], C_GOLD),
        ("UPCOMING CELEBRATIONS",
         "Calendar Ahead",
         [
             "Target International School Winter Gala & Concert",
             "Open Classroom Days: Parents invited into live lessons",
             "Target Science Fair & Student Innovation Expo",
             "Spring Educational Field Trips & University Tours",
             "Annual Target International Sports Olympiad"
         ], C_ACCENT_BLUE)
    ]

    for idx, (title, sub, bullets, color) in enumerate(ev_cols):
        cur_x = Inches(0.72) + idx * (col_w14 + gap14)
        add_card(s14, cur_x, top_y14, col_w14, h14)
        add_rect(s14, cur_x, top_y14, col_w14, Inches(0.5), color)
        
        tb = s14.shapes.add_textbox(cur_x + Inches(0.2), top_y14 + Inches(0.08), col_w14 - Inches(0.4), Inches(0.4))
        tf = tb.text_frame
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = FONT_HEADING
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = C_WHITE if color != C_GOLD else C_NAVY_DARK

        tb_b = s14.shapes.add_textbox(cur_x + Inches(0.25), top_y14 + Inches(0.6), col_w14 - Inches(0.5), h14 - Inches(0.7))
        tf_b = tb_b.text_frame
        tf_b.word_wrap = True
        
        p = tf_b.paragraphs[0]
        p.text = sub
        p.font.name = FONT_HEADING
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = color if color != C_WHITE else C_NAVY_DARK

        for j, b in enumerate(bullets):
            p = tf_b.add_paragraph()
            p.text = "• " + b
            p.font.name = FONT_BODY
            p.font.size = Pt(9.5)
            p.font.color.rgb = C_TEXT_BODY
            p.space_before = Pt(6)

    tb_b14 = s14.shapes.add_textbox(Inches(0.72), Inches(6.12), Inches(11.89), Inches(0.6))
    tf_b14 = tb_b14.text_frame
    p_b14 = tf_b14.paragraphs[0]
    p_b14.text = "Holistic Development: Extracurricular participation builds communication, empathy, and leadership skills essential for competitive university profiles."
    p_b14.font.name = FONT_BODY
    p_b14.font.size = Pt(10.5)
    p_b14.font.color.rgb = C_TEXT_MUTED

    add_footer(s14, 14)

    # =========================================================================
    # SLIDE 15: STUDENT COUNSELLING & UNIVERSITY GUIDANCE
    # =========================================================================
    s15 = prs.slides.add_slide(blank_layout)
    set_slide_background(s15, C_BEIGE_BG)
    add_header(s15, "05 / SCHOOL LIFE & STUDENT WELFARE", "Student Counselling & University Guidance",
               "Personalized psychological care, academic mentorship and strategic university admissions roadmaps.")

    col_w15 = Inches(2.78)
    gap15 = Inches(0.25)
    top_y15 = Inches(1.95)
    h15 = Inches(4.0)

    counsel_cards = [
        ("FULL-TIME SCHOOL\nPSYCHOLOGIST",
         "Emotional & Social Care",
         [
             "Confidential 1-on-1 counseling support for students facing academic pressure or social transitions.",
             "Regular stress management and mindfulness workshops before examination periods.",
             "Proactive communication with homeroom tutors to support sensitive student needs."
         ], C_NAVY_DARK),
        ("INDIVIDUAL CAREER\n& UNIVERSITY MAPPING",
         "Pre-University Strategy",
         [
             "Personalized academic pathway counseling beginning from Grade 8 onwards.",
             "Mapping student profiles to leading universities across the US, UK, Europe, Australia, and Asia.",
             "Clear guidance on subject prerequisites, minimum GPA, and testing targets."
         ], C_GOLD),
        ("STANDARDIZED TEST\nTIMELINE PLANNING",
         "IELTS, SAT & A-Levels",
         [
             "Strategic test scheduling to prevent student burnout.",
             "Phased milestone targets starting in Grade 10.",
             "Balances standardized testing preparation with regular school grades.",
             "Regular diagnostic mock exams track readiness."
         ], C_ACCENT_BLUE),
        ("APPLICATION ESSAYS\n& PORTFOLIO MENTORSHIP",
         "Standout Admissions Profiles",
         [
             "One-on-one personal statement and college essay coaching.",
             "Polishing extracurricular resumes and activity lists.",
             "Guidance on securing compelling teacher recommendation letters.",
             "Mock interview preparation for competitive scholarships."
         ], C_ACCENT_GREEN)
    ]

    for idx, (title, sub, bullets, color) in enumerate(counsel_cards):
        cur_x = Inches(0.72) + idx * (col_w15 + gap15)
        add_card(s15, cur_x, top_y15, col_w15, h15)
        add_rect(s15, cur_x, top_y15, col_w15, Inches(0.08), color)
        
        tb = s15.shapes.add_textbox(cur_x + Inches(0.2), top_y15 + Inches(0.18), col_w15 - Inches(0.4), Inches(0.85))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = FONT_HEADING
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_NAVY_DARK

        p_s = tf.add_paragraph()
        p_s.text = sub
        p_s.font.name = FONT_HEADING
        p_s.font.size = Pt(9.5)
        p_s.font.bold = True
        p_s.font.color.rgb = color
        p_s.space_before = Pt(2)

        tb_b = s15.shapes.add_textbox(cur_x + Inches(0.2), top_y15 + Inches(1.15), col_w15 - Inches(0.4), h15 - Inches(1.25))
        tf_b = tb_b.text_frame
        tf_b.word_wrap = True
        
        for j, b in enumerate(bullets):
            p = tf_b.paragraphs[0] if j == 0 else tf_b.add_paragraph()
            p.text = "• " + b
            p.font.name = FONT_BODY
            p.font.size = Pt(9.5)
            p.font.color.rgb = C_TEXT_BODY
            if j > 0:
                p.space_before = Pt(6)

    tb_b15 = s15.shapes.add_textbox(Inches(0.72), Inches(6.12), Inches(11.89), Inches(0.6))
    tf_b15 = tb_b15.text_frame
    p_b15 = tf_b15.paragraphs[0]
    p_b15.text = "Admissions Commitment: We guide every family through university application deadlines, scholarship criteria, and financial aid procedures."
    p_b15.font.name = FONT_BODY
    p_b15.font.size = Pt(10.5)
    p_b15.font.color.rgb = C_TEXT_MUTED

    add_footer(s15, 15)

    # =========================================================================
    # SLIDE 16: NUTRITION & SCHOOL FOOD MENU
    # =========================================================================
    s16 = prs.slides.add_slide(blank_layout)
    set_slide_background(s16, C_BEIGE_BG)
    add_header(s16, "05 / SCHOOL LIFE & STUDENT WELFARE", "Nutrition & School Food Menu",
               "Wholesome, balanced meals prepared daily under strict hygiene and dietary standards.")

    col_w16 = Inches(3.75)
    gap16 = Inches(0.3)
    top_y16 = Inches(1.95)
    h16 = Inches(3.7)

    meal_stages = [
        ("BREAKFAST", "Morning Energy & Focus",
         [
             "Warm whole-grain porridges: oatmeal with honey, buckwheat, rice pudding.",
             "Protein choices: boiled farm eggs, fresh cottage cheese, omelettes.",
             "Freshly baked whole-grain bread, natural butter, and premium cheese.",
             "Beverages: hot herbal teas, lemon tea, and natural cacao."
         ], C_GOLD),
        ("LUNCH", "Balanced 3-Course Nutrition",
         [
             "First Course: Rich bone broth soups, vegetable minestrone, lentil soup.",
             "Main Course: Lean beef stroganoff, roasted poultry, grilled fish fillets.",
             "Side Dishes: Steamed vegetables, brown rice, potato puree, buckwheat.",
             "Fresh garden salads and homemade seasonal dried fruit compotes."
         ], C_NAVY_DARK),
        ("AFTERNOON SNACK", "Afternoon Energy Recharge",
         [
             "Fresh seasonal fruits: crisp apples, sweet pears, bananas, oranges.",
             "Light baked pastries: cottage cheese buns, whole-wheat biscuits.",
             "Dairy refreshments: kefir, natural yogurt, and warm milk.",
             "Nutritious nuts, dried fruits, and natural herbal infusions."
         ], C_ACCENT_GREEN)
    ]

    for idx, (title, sub, bullets, color) in enumerate(meal_stages):
        cur_x = Inches(0.72) + idx * (col_w16 + gap16)
        add_card(s16, cur_x, top_y16, col_w16, h16)
        add_rect(s16, cur_x, top_y16, col_w16, Inches(0.08), color)
        
        tb = s16.shapes.add_textbox(cur_x + Inches(0.2), top_y16 + Inches(0.18), col_w16 - Inches(0.4), Inches(0.85))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = FONT_HEADING
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = color

        p2 = tf.add_paragraph()
        p2.text = sub
        p2.font.name = FONT_HEADING
        p2.font.size = Pt(10)
        p2.font.bold = True
        p2.font.color.rgb = C_NAVY_DARK
        p2.space_before = Pt(2)

        tb_b = s16.shapes.add_textbox(cur_x + Inches(0.2), top_y16 + Inches(1.15), col_w16 - Inches(0.4), h16 - Inches(1.25))
        tf_b = tb_b.text_frame
        tf_b.word_wrap = True
        for j, b in enumerate(bullets):
            p = tf_b.paragraphs[0] if j == 0 else tf_b.add_paragraph()
            p.text = "• " + b
            p.font.name = FONT_BODY
            p.font.size = Pt(9.5)
            p.font.color.rgb = C_TEXT_BODY
            if j > 0:
                p.space_before = Pt(6)

    add_card(s16, Inches(0.72), Inches(5.82), Inches(11.89), Inches(0.95), fill_color=C_WHITE, border_color=C_GOLD)
    tb_b16 = s16.shapes.add_textbox(Inches(0.95), Inches(5.92), Inches(11.4), Inches(0.75))
    tf_b16 = tb_b16.text_frame
    p = tf_b16.paragraphs[0]
    p.text = "FOOD HYGIENE & INDIVIDUAL DIETARY REQUIREMENTS"
    p.font.name = FONT_HEADING
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = C_GOLD

    p2 = tf_b16.add_paragraph()
    p2.text = "Certified sanitary standards, daily meal sample preservation, and verified fresh local suppliers. Parents are encouraged to notify the school medical officer of any food allergies or specific dietary restrictions."
    p2.font.name = FONT_BODY
    p2.font.size = Pt(10.5)
    p2.font.color.rgb = C_NAVY_DARK

    add_footer(s16, 16)

    # =========================================================================
    # SLIDE 17: STUDENT SAFETY, SECURITY & SCHOOL IDENTITY
    # =========================================================================
    s17 = prs.slides.add_slide(blank_layout)
    set_slide_background(s17, C_BEIGE_BG)
    add_header(s17, "05 / SCHOOL LIFE & STUDENT WELFARE", "Student Safety, Security & School Identity",
               "A secure campus environment, proud school dress code and shared standards of mutual respect.")

    col_w17 = Inches(3.75)
    gap17 = Inches(0.3)
    top_y17 = Inches(1.95)
    h17 = Inches(4.05)

    sec_pillars = [
        ("CAMPUS SAFETY & SECURITY",
         "24/7 Safeguarding Protocol",
         [
             "Electronic Access Control: Secure biometric and turnstile campus entry.",
             "Visitor ID Registration: Strict visitor badges and escort procedures.",
             "CCTV Coverage: Full HD monitoring across hallways and campus grounds.",
             "Medical Staff on Duty: Full-time qualified nurse on campus at all times.",
             "Safeguarding Governance: Zero tolerance for unauthorized campus presence."
         ], C_NAVY_DARK),
        ("OFFICIAL SCHOOL UNIFORM",
         "Pride, Unity & Discipline",
         [
             "Official Target Uniform: Navy blazer, formal shirts, tailored trousers/skirts.",
             "Fosters Equality: Eliminates fashion distractions and socioeconomic barriers.",
             "Professional Demeanor: Prepares students for corporate and academic etiquette.",
             "Dress Code Standards: Mandatory daily adherence to clean, complete uniform.",
             "Sportswear Policy: Official Target sports kit strictly during PE lessons."
         ], C_GOLD),
        ("STUDENT RESPONSIBILITY",
         "Code of Conduct & Character",
         [
             "Attendance & Punctuality: Morning registration at 08:50; promptness required.",
             "Device-Free Zones: Personal phones stored securely during academic lessons.",
             "Mutual Respect: Zero tolerance for bullying, disruption, or disrespect.",
             "Campus Care: Respect for school property, cleanliness, and laboratory equipment.",
             "Academic Integrity: Strict adherence to honor code in tests and coursework."
         ], C_ACCENT_BLUE)
    ]

    for idx, (title, sub, bullets, color) in enumerate(sec_pillars):
        cur_x = Inches(0.72) + idx * (col_w17 + gap17)
        add_card(s17, cur_x, top_y17, col_w17, h17)
        add_rect(s17, cur_x, top_y17, col_w17, Inches(0.5), color)
        
        tb = s17.shapes.add_textbox(cur_x + Inches(0.2), top_y17 + Inches(0.08), col_w17 - Inches(0.4), Inches(0.4))
        tf = tb.text_frame
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = FONT_HEADING
        p.font.size = Pt(11.5)
        p.font.bold = True
        p.font.color.rgb = C_WHITE if color != C_GOLD else C_NAVY_DARK

        tb_b = s17.shapes.add_textbox(cur_x + Inches(0.25), top_y17 + Inches(0.6), col_w17 - Inches(0.5), h17 - Inches(0.7))
        tf_b = tb_b.text_frame
        tf_b.word_wrap = True
        
        p = tf_b.paragraphs[0]
        p.text = sub
        p.font.name = FONT_HEADING
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = color if color != C_WHITE else C_NAVY_DARK

        for j, b in enumerate(bullets):
            p = tf_b.add_paragraph()
            p.text = "• " + b
            p.font.name = FONT_BODY
            p.font.size = Pt(9.5)
            p.font.color.rgb = C_TEXT_BODY
            p.space_before = Pt(6)

    tb_b17 = s17.shapes.add_textbox(Inches(0.72), Inches(6.12), Inches(11.89), Inches(0.6))
    tf_b17 = tb_b17.text_frame
    p_b17 = tf_b17.paragraphs[0]
    p_b17.text = "Safe & Respectful Culture: Target International School maintains a disciplined, warm and inclusive environment where every child feels protected."
    p_b17.font.name = FONT_BODY
    p_b17.font.size = Pt(10.5)
    p_b17.font.color.rgb = C_TEXT_MUTED

    add_footer(s17, 17)

    # =========================================================================
    # SLIDE 18: TOGETHER WE BUILD THEIR FUTURE (CLOSING SLIDE - Dark Navy)
    # =========================================================================
    s18 = prs.slides.add_slide(blank_layout)
    set_slide_background(s18, C_NAVY_DARK)

    # Header Tracker
    tb_t18 = s18.shapes.add_textbox(Inches(0.72), Inches(0.42), Inches(9.6), Inches(0.3))
    tf_t18 = tb_t18.text_frame
    p = tf_t18.paragraphs[0]
    p.text = "06 / PARTNERSHIP & CLOSING"
    p.font.name = FONT_HEADING
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = C_GOLD

    # Main Title
    tb_m18 = s18.shapes.add_textbox(Inches(0.72), Inches(0.74), Inches(9.6), Inches(0.65))
    tf_m18 = tb_m18.text_frame
    p = tf_m18.paragraphs[0]
    p.text = "Together We Build Their Future"
    p.font.name = FONT_HEADING
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = C_WHITE

    # Logo in top right
    if os.path.exists(LOGO_WHITE_PATH):
        try:
            s18.shapes.add_picture(LOGO_WHITE_PATH, Inches(10.65), Inches(0.46), width=Inches(1.95))
        except Exception:
            pass

    # Big Golden Quote Box
    add_card(s18, Inches(0.72), Inches(1.5), Inches(11.89), Inches(1.35), fill_color=C_NAVY_PANEL, border_color=C_GOLD, border_width=Pt(1.5))
    tb_q = s18.shapes.add_textbox(Inches(1.0), Inches(1.6), Inches(11.3), Inches(1.15))
    tf_q = tb_q.text_frame
    tf_q.word_wrap = True
    p_q = tf_q.paragraphs[0]
    p_q.text = "\"Every child has potential. Our responsibility is to recognise it, develop it and prepare every student for a successful future.\""
    p_q.font.name = FONT_HEADING
    p_q.font.size = Pt(16)
    p_q.font.bold = True
    p_q.font.color.rgb = C_GOLD_LIGHT

    p_qs = tf_q.add_paragraph()
    p_qs.text = "— Target International School Educational Leadership"
    p_qs.font.name = FONT_BODY
    p_qs.font.size = Pt(11)
    p_qs.font.color.rgb = C_BEIGE_CARD
    p_qs.space_before = Pt(4)

    # 3 Partnership Pillar Cards
    c18_w = Inches(3.75)
    c18_gap = Inches(0.3)
    c18_top = Inches(3.05)
    c18_h = Inches(2.35)

    part_pillars = [
        ("TRANSPARENT COMMUNICATION",
         "Direct & Timely Updates",
         [
             "Direct communication with homeroom teachers and tutors.",
             "Regular academic performance and attendance reports.",
             "Open-door policy for scheduled parent consultations."
         ]),
        ("ACTIVE COLLABORATION",
         "Working Hand-in-Hand",
         [
             "Immediate collaboration when learning support is needed.",
             "Shared reinforcement of study habits and positive discipline at home.",
             "Active participation in school workshops and parent councils."
         ]),
        ("CELEBRATING SUCCESS",
         "Shared Community Pride",
         [
             "Joint celebration of student academic milestones and character growth.",
             "Encouraging resilience and perseverance through challenges.",
             "Building confident, compassionate leaders together."
         ])
    ]

    for idx, (title, sub, bullets) in enumerate(part_pillars):
        cur_x = Inches(0.72) + idx * (c18_w + c18_gap)
        add_card(s18, cur_x, c18_top, c18_w, c18_h, fill_color=C_NAVY_PANEL, border_color=C_GOLD_LIGHT)
        
        tb = s18.shapes.add_textbox(cur_x + Inches(0.2), c18_top + Inches(0.12), c18_w - Inches(0.4), c18_h - Inches(0.24))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = FONT_HEADING
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_GOLD

        p2 = tf.add_paragraph()
        p2.text = sub
        p2.font.name = FONT_HEADING
        p2.font.size = Pt(9.5)
        p2.font.bold = True
        p2.font.color.rgb = C_WHITE
        p2.space_before = Pt(2)

        for b in bullets:
            p = tf.add_paragraph()
            p.text = "• " + b
            p.font.name = FONT_BODY
            p.font.size = Pt(9.5)
            p.font.color.rgb = C_BEIGE_CARD
            p.space_before = Pt(4)

    # Bottom Contact & Q&A Box
    add_card(s18, Inches(0.72), Inches(5.6), Inches(11.89), Inches(1.15), fill_color=C_NAVY_PANEL, border_color=C_BORDER_LIGHT)
    tb_c18 = s18.shapes.add_textbox(Inches(0.95), Inches(5.7), Inches(11.4), Inches(0.95))
    tf_c18 = tb_c18.text_frame
    tf_c18.word_wrap = True
    
    p = tf_c18.paragraphs[0]
    p.text = "PARENT QUESTIONS, FEEDBACK & SUGGESTIONS"
    p.font.name = FONT_HEADING
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_GOLD

    p2 = tf_c18.add_paragraph()
    p2.text = "We welcome your thoughts, questions and suggestions. Please feel free to speak directly with your homeroom teacher, subject specialists, and school leadership today."
    p2.font.name = FONT_BODY
    p2.font.size = Pt(10)
    p2.font.color.rgb = C_WHITE
    p2.space_before = Pt(2)

    p3 = tf_c18.add_paragraph()
    p3.text = "Target International School  •  Yunusobod Campus  •  Thank you for your trust, dedication and partnership."
    p3.font.name = FONT_BODY
    p3.font.size = Pt(9.5)
    p3.font.color.rgb = C_GOLD_LIGHT
    p3.space_before = Pt(2)

    add_footer(s18, 18, is_dark=True)


def build_teacher_additions(prs, total_slides=26):
    """
    Appends the 8 class-specific slides (Part B) to create the Complete Homeroom Teacher Deck.
    """
    blank_layout = prs.slide_layouts[6]

    # -------------------------------------------------------------------------
    # SLIDE 19: CLASS PROFILE & HOMEROOM INTRODUCTION
    # -------------------------------------------------------------------------
    s19 = prs.slides.add_slide(blank_layout)
    set_slide_background(s19, C_BEIGE_BG)
    add_header(s19, "PART B / INDIVIDUAL CLASS PRESENTATION", "Class Profile & Learning Community",
               "Detailed academic snapshot, student roster and homeroom tutor introduction.")

    # 3 Cards
    c_w = Inches(3.75)
    c_gap = Inches(0.3)
    c_top = Inches(1.95)
    c_h = Inches(4.0)

    # Card 1: Class Profile
    add_card(s19, Inches(0.72), c_top, c_w, c_h)
    add_rect(s19, Inches(0.72), c_top, c_w, Inches(0.5), C_NAVY_DARK)
    tb = s19.shapes.add_textbox(Inches(0.95), c_top + Inches(0.1), c_w - Inches(0.5), Inches(0.35))
    tf = tb.text_frame
    p = tf.paragraphs[0]
    p.text = "CLASS OVERVIEW"
    p.font.name = FONT_HEADING
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_WHITE

    tb_b = s19.shapes.add_textbox(Inches(0.95), c_top + Inches(0.65), c_w - Inches(0.5), c_h - Inches(0.8))
    tf_b = tb_b.text_frame
    tf_b.word_wrap = True
    overview_items = [
        "Class / Year Group: [Fill in e.g. Grade 10A]",
        "Homeroom Teacher: [Full Name / Role]",
        "Total Students Enrolled: [e.g. 18 Students]",
        "Academic Year: 2026–2027",
        "Class Motto: Excellence, Collaboration & Growth"
    ]
    for idx, item in enumerate(overview_items):
        p = tf_b.paragraphs[0] if idx == 0 else tf_b.add_paragraph()
        p.text = "• " + item
        p.font.name = FONT_BODY
        p.font.size = Pt(10)
        p.font.color.rgb = C_TEXT_BODY
        if idx > 0:
            p.space_before = Pt(8)

    # Card 2: Attendance & Dynamics
    c2_x = Inches(0.72) + c_w + c_gap
    add_card(s19, c2_x, c_top, c_w, c_h)
    add_rect(s19, c2_x, c_top, c_w, Inches(0.5), C_GOLD)
    tb = s19.shapes.add_textbox(c2_x + Inches(0.25), c_top + Inches(0.1), c_w - Inches(0.5), Inches(0.35))
    tf = tb.text_frame
    p = tf.paragraphs[0]
    p.text = "ATTENDANCE & DISCIPLINE"
    p.font.name = FONT_HEADING
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_NAVY_DARK

    tb_b2 = s19.shapes.add_textbox(c2_x + Inches(0.25), c_top + Inches(0.65), c_w - Inches(0.5), c_h - Inches(0.8))
    tf_b2 = tb_b2.text_frame
    tf_b2.word_wrap = True
    att_items = [
        "Class Attendance Rate: [e.g. 96.4%]",
        "Homework On-Time Completion: [e.g. 93%]",
        "Uniform & Dress Code Compliance: 100%",
        "Classroom Harmony: Strong peer collaboration and active engagement in group tasks.",
        "Punctuality Record: Morning line-up at 08:50 observed consistently."
    ]
    for idx, item in enumerate(att_items):
        p = tf_b2.paragraphs[0] if idx == 0 else tf_b2.add_paragraph()
        p.text = "• " + item
        p.font.name = FONT_BODY
        p.font.size = Pt(10)
        p.font.color.rgb = C_TEXT_BODY
        if idx > 0:
            p.space_before = Pt(8)

    # Card 3: Key Objectives
    c3_x = c2_x + c_w + c_gap
    add_card(s19, c3_x, c_top, c_w, c_h)
    add_rect(s19, c3_x, c_top, c_w, Inches(0.5), C_ACCENT_BLUE)
    tb = s19.shapes.add_textbox(c3_x + Inches(0.25), c_top + Inches(0.1), c_w - Inches(0.5), Inches(0.35))
    tf = tb.text_frame
    p = tf.paragraphs[0]
    p.text = "TERM 1–2 CLASS PRIORITIES"
    p.font.name = FONT_HEADING
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_WHITE

    tb_b3 = s19.shapes.add_textbox(c3_x + Inches(0.25), c_top + Inches(0.65), c_w - Inches(0.5), c_h - Inches(0.8))
    tf_b3 = tb_b3.text_frame
    tf_b3.word_wrap = True
    t_items = [
        "Mastery of Cambridge syllabus objectives across all subjects.",
        "Intensive diagnostic mock exams for Cambridge and IELTS candidates.",
        "Strengthening student academic self-reliance and note-taking habits.",
        "Encouraging 100% participation in school Olympiads and science fairs."
    ]
    for idx, item in enumerate(t_items):
        p = tf_b3.paragraphs[0] if idx == 0 else tf_b3.add_paragraph()
        p.text = "• " + item
        p.font.name = FONT_BODY
        p.font.size = Pt(10)
        p.font.color.rgb = C_TEXT_BODY
        if idx > 0:
            p.space_before = Pt(8)

    tb_b19 = s19.shapes.add_textbox(Inches(0.72), Inches(6.12), Inches(11.89), Inches(0.6))
    tf_b19 = tb_b19.text_frame
    p_b19 = tf_b19.paragraphs[0]
    p_b19.text = "Homeroom Teacher Role: Serving as primary mentor, academic coordinator, and daily point of contact for student welfare."
    p_b19.font.name = FONT_BODY
    p_b19.font.size = Pt(10.5)
    p_b19.font.color.rgb = C_TEXT_MUTED

    add_footer(s19, 19, total_slides)

    # -------------------------------------------------------------------------
    # SLIDE 20: OUR TEACHING TEAM — SUBJECT SPECIALISTS
    # -------------------------------------------------------------------------
    s20 = prs.slides.add_slide(blank_layout)
    set_slide_background(s20, C_BEIGE_BG)
    add_header(s20, "PART B / INDIVIDUAL CLASS PRESENTATION", "Subject Teachers for Our Class",
               "Meet the certified educators teaching and mentoring our students daily.")

    # 3 Teacher Profile Cards
    card_w20 = Inches(3.75)
    card_gap20 = Inches(0.3)
    card_top20 = Inches(1.95)
    card_h20 = Inches(4.0)

    teachers = [
        ("TEACHER 1", "[Teacher Full Name]", "English Language & Literature",
         "Master's in Linguistics • 7 Years Teaching Experience",
         "Focus: Academic writing, IELTS preparation, structured reading analysis, and classroom speech fluency."),
        ("TEACHER 2", "[Teacher Full Name]", "Mathematics & Science",
         "Master's in Applied Mathematics • 9 Years Experience",
         "Focus: Conceptual rigor, algebraic mechanics, laboratory experiments, and Olympiad problem-solving."),
        ("TEACHER 3", "[Teacher Full Name]", "IT, Robotics & Vibecoding",
         "B.S. in Software Engineering • Certified Tech Mentor",
         "Focus: Algorithm design, Python, AI foundations, and practical software engineering portfolios.")
    ]

    for idx, (badge, name, subject, quals, approach) in enumerate(teachers):
        cur_x = Inches(0.72) + idx * (card_w20 + card_gap20)
        add_card(s20, cur_x, card_top20, card_w20, card_h20)
        add_rect(s20, cur_x, card_top20, card_w20, Inches(0.08), C_GOLD)
        
        # Photo placeholder
        add_card(s20, cur_x + Inches(0.3), card_top20 + Inches(0.25), card_w20 - Inches(0.6), Inches(1.4), fill_color=C_BEIGE_CARD, border_color=C_GOLD_LIGHT)
        tb_p = s20.shapes.add_textbox(cur_x + Inches(0.3), card_top20 + Inches(0.7), card_w20 - Inches(0.6), Inches(0.5))
        tf_p = tb_p.text_frame
        p = tf_p.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        p.text = "[TEACHER PHOTOGRAPH]"
        p.font.name = FONT_HEADING
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = C_TEXT_MUTED

        # Info Box
        tb_i = s20.shapes.add_textbox(cur_x + Inches(0.25), card_top20 + Inches(1.8), card_w20 - Inches(0.5), card_h20 - Inches(1.9))
        tf_i = tb_i.text_frame
        tf_i.word_wrap = True

        p = tf_i.paragraphs[0]
        p.text = name
        p.font.name = FONT_HEADING
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = C_NAVY_DARK

        p2 = tf_i.add_paragraph()
        p2.text = subject
        p2.font.name = FONT_HEADING
        p2.font.size = Pt(10.5)
        p2.font.bold = True
        p2.font.color.rgb = C_GOLD
        p2.space_before = Pt(2)

        p3 = tf_i.add_paragraph()
        p3.text = quals
        p3.font.name = FONT_BODY
        p3.font.size = Pt(9)
        p3.font.bold = True
        p3.font.color.rgb = C_TEXT_MUTED
        p3.space_before = Pt(4)

        p4 = tf_i.add_paragraph()
        p4.text = approach
        p4.font.name = FONT_BODY
        p4.font.size = Pt(9.5)
        p4.font.color.rgb = C_TEXT_BODY
        p4.space_before = Pt(6)

    tb_b20 = s20.shapes.add_textbox(Inches(0.72), Inches(6.12), Inches(11.89), Inches(0.6))
    tf_b20 = tb_b20.text_frame
    p_b20 = tf_b20.paragraphs[0]
    p_b20.text = "Teacher Consultations: All subject specialists hold weekly consultation slots for individual student feedback and parent meetings."
    p_b20.font.name = FONT_BODY
    p_b20.font.size = Pt(10.5)
    p_b20.font.color.rgb = C_TEXT_MUTED

    add_footer(s20, 20, total_slides)

    # -------------------------------------------------------------------------
    # SLIDE 21: EVIDENCE OF ACADEMIC PROGRESS
    # -------------------------------------------------------------------------
    s21 = prs.slides.add_slide(blank_layout)
    set_slide_background(s21, C_BEIGE_BG)
    add_header(s21, "PART B / INDIVIDUAL CLASS PRESENTATION", "Class Academic Performance & Results",
               "Verified assessment data, subject averages and learning target progression.")

    # 4 KPI Stat Boxes on Top
    kpi_w = Inches(2.78)
    kpi_gap = Inches(0.25)
    kpi_top = Inches(1.95)
    kpi_h = Inches(1.25)

    kpis = [
        ("CLASS GPA AVERAGE", "[84.2%]", "Target: 85%+ overall", C_GOLD),
        ("ASSESSMENT PASS RATE", "[95.8%]", "Completed all unit tests", C_NAVY_DARK),
        ("STUDENTS EXCEEDING", "[12 Students]", "Demonstrating A*/A mastery", C_ACCENT_GREEN),
        ("TARGETED SUPPORT", "[3 Students]", "Receiving booster sessions", C_ACCENT_CORAL)
    ]
    for idx, (label, val, cap, col) in enumerate(kpis):
        cur_x = Inches(0.72) + idx * (kpi_w + kpi_gap)
        add_card(s21, cur_x, kpi_top, kpi_w, kpi_h)
        add_rect(s21, cur_x, kpi_top, kpi_w, Inches(0.06), col)
        
        tb = s21.shapes.add_textbox(cur_x + Inches(0.2), kpi_top + Inches(0.12), kpi_w - Inches(0.4), kpi_h - Inches(0.24))
        tf = tb.text_frame
        p = tf.paragraphs[0]
        p.text = label
        p.font.name = FONT_HEADING
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = C_TEXT_MUTED

        p2 = tf.add_paragraph()
        p2.text = val
        p2.font.name = FONT_HEADING
        p2.font.size = Pt(20)
        p2.font.bold = True
        p2.font.color.rgb = col
        p2.space_before = Pt(2)

        p3 = tf.add_paragraph()
        p3.text = cap
        p3.font.name = FONT_BODY
        p3.font.size = Pt(8.5)
        p3.font.color.rgb = C_TEXT_BODY
        p3.space_before = Pt(2)

    # 2 Bottom Cards: Subject Breakdown & Data Insights
    bot_top21 = Inches(3.45)
    bot_h21 = Inches(2.55)
    w_21 = Inches(5.8)

    # Left: Subject Breakdown
    add_card(s21, Inches(0.72), bot_top21, w_21, bot_h21)
    add_rect(s21, Inches(0.72), bot_top21, w_21, Inches(0.45), C_NAVY_DARK)
    tb_l = s21.shapes.add_textbox(Inches(0.95), bot_top21 + Inches(0.08), w_21 - Inches(0.5), Inches(0.35))
    tf_l = tb_l.text_frame
    p = tf_l.paragraphs[0]
    p.text = "SUBJECT PERFORMANCE BREAKDOWN"
    p.font.name = FONT_HEADING
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_WHITE

    tb_lb = s21.shapes.add_textbox(Inches(0.95), bot_top21 + Inches(0.55), w_21 - Inches(0.5), bot_h21 - Inches(0.65))
    tf_lb = tb_lb.text_frame
    tf_lb.word_wrap = True
    sub_data = [
        "English Language: [Average: 86%] • Strong debate & vocabulary acquisition.",
        "Mathematics: [Average: 82%] • High problem-solving speed; focus on proofs.",
        "Sciences (Physics/Chemistry): [Average: 85%] • Excellent practical lab work.",
        "Computer Science / Vibecoding: [Average: 91%] • Outstanding project delivery."
    ]
    for idx, pt in enumerate(sub_data):
        p = tf_lb.paragraphs[0] if idx == 0 else tf_lb.add_paragraph()
        p.text = "• " + pt
        p.font.name = FONT_BODY
        p.font.size = Pt(9.5)
        p.font.color.rgb = C_TEXT_BODY
        if idx > 0:
            p.space_before = Pt(6)

    # Right: Data-Driven Next Steps
    r_x21 = Inches(0.72) + w_21 + Inches(0.29)
    add_card(s21, r_x21, bot_top21, w_21, bot_h21)
    add_rect(s21, r_x21, bot_top21, w_21, Inches(0.45), C_GOLD)
    tb_r = s21.shapes.add_textbox(r_x21 + Inches(0.25), bot_top21 + Inches(0.08), w_21 - Inches(0.5), Inches(0.35))
    tf_r = tb_r.text_frame
    p = tf_r.paragraphs[0]
    p.text = "KEY TAKEAWAYS & ACTION PLAN"
    p.font.name = FONT_HEADING
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_NAVY_DARK

    tb_rb = s21.shapes.add_textbox(r_x21 + Inches(0.25), bot_top21 + Inches(0.55), w_21 - Inches(0.5), bot_h21 - Inches(0.65))
    tf_rb = tb_rb.text_frame
    tf_rb.word_wrap = True
    actions = [
        "Identified Strengths: High conceptual understanding in STEM subjects and coding.",
        "Priority Improvement Area: Structuring longer analytical essays under timed conditions.",
        "Targeted Action: Weekly 45-minute booster clinics for students scoring below 75%.",
        "Parent Collaboration: Ensuring quiet study routine and 8 hours of sleep at home."
    ]
    for idx, pt in enumerate(actions):
        p = tf_rb.paragraphs[0] if idx == 0 else tf_rb.add_paragraph()
        p.text = "• " + pt
        p.font.name = FONT_BODY
        p.font.size = Pt(9.5)
        p.font.color.rgb = C_TEXT_BODY
        if idx > 0:
            p.space_before = Pt(6)

    tb_b21 = s21.shapes.add_textbox(Inches(0.72), Inches(6.15), Inches(11.89), Inches(0.5))
    tf_b21 = tb_b21.text_frame
    p_b21 = tf_b21.paragraphs[0]
    p_b21.text = "Evidence-Based Growth: We use real assessment data to adjust lesson pacing and provide immediate individualized support."
    p_b21.font.name = FONT_BODY
    p_b21.font.size = Pt(10.5)
    p_b21.font.color.rgb = C_TEXT_MUTED

    add_footer(s21, 21, total_slides)

    # -------------------------------------------------------------------------
    # SLIDE 22: EVERY LEARNER MATTERS — INDIVIDUAL SUPPORT
    # -------------------------------------------------------------------------
    s22 = prs.slides.add_slide(blank_layout)
    set_slide_background(s22, C_BEIGE_BG)
    add_header(s22, "PART B / INDIVIDUAL CLASS PRESENTATION", "Every Learner Matters: Holistic Development",
               "Understanding student strengths, addressing hurdles and tailoring individual action plans.")

    # 5 Holistic Domains (Top)
    dom_w = Inches(2.21)
    dom_gap = Inches(0.21)
    dom_top = Inches(1.95)
    dom_h = Inches(1.55)

    domains = [
        ("ACADEMIC MASTERY", "Subject depth, reading comprehension & logical problem solving.", C_NAVY_DARK),
        ("PARTICIPATION", "Discussion, curiosity, active questions & task ownership.", C_GOLD),
        ("SOCIAL-EMOTIONAL", "Respect, empathy, peer collaboration & emotional stability.", C_ACCENT_BLUE),
        ("RESPONSIBILITY", "Homework consistency, organization, punctuality & integrity.", C_ACCENT_GREEN),
        ("CREATIVITY & STEM", "Original thinking, coding projects, innovation & design.", C_ACCENT_CORAL)
    ]

    for idx, (title, desc, col) in enumerate(domains):
        cur_x = Inches(0.72) + idx * (dom_w + dom_gap)
        add_card(s22, cur_x, dom_top, dom_w, dom_h)
        add_rect(s22, cur_x, dom_top, dom_w, Inches(0.06), col)
        
        tb = s22.shapes.add_textbox(cur_x + Inches(0.15), dom_top + Inches(0.12), dom_w - Inches(0.3), dom_h - Inches(0.2))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = FONT_HEADING
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = C_NAVY_DARK

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.name = FONT_BODY
        p2.font.size = Pt(8.5)
        p2.font.color.rgb = C_TEXT_BODY
        p2.space_before = Pt(4)

    # Individual Student Action Plan Template (Bottom)
    plan_top = Inches(3.75)
    plan_h = Inches(2.25)
    add_card(s22, Inches(0.72), plan_top, Inches(11.89), plan_h, fill_color=C_WHITE, border_color=C_GOLD)
    add_rect(s22, Inches(0.72), plan_top, Inches(11.89), Inches(0.45), C_NAVY_PANEL)

    tb_pt = s22.shapes.add_textbox(Inches(0.95), plan_top + Inches(0.08), Inches(11.4), Inches(0.35))
    tf_pt = tb_pt.text_frame
    p = tf_pt.paragraphs[0]
    p.text = "CONFIDENTIAL 1-ON-1 PARENT FEEDBACK FORMAT"
    p.font.name = FONT_HEADING
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_GOLD_LIGHT

    tb_pb = s22.shapes.add_textbox(Inches(0.95), plan_top + Inches(0.55), Inches(11.4), plan_h - Inches(0.65))
    tf_pb = tb_pb.text_frame
    tf_pb.word_wrap = True

    p = tf_pb.paragraphs[0]
    p.text = "During individual consultations today, each family receives a customized student development profile:"
    p.font.name = FONT_BODY
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = C_NAVY_DARK

    plan_pts = [
        "1. Verified Academic Strengths: Specific subject triumphs, high-scoring units, and notable class contributions.",
        "2. Growth Areas & Next Steps: Targeted academic skills or study habits requiring reinforcement over the coming weeks.",
        "3. Personalized Action Plan: Agreed strategies between teacher, student and parents with a set review timeline."
    ]
    for pt in plan_pts:
        p = tf_pb.add_paragraph()
        p.text = pt
        p.font.name = FONT_BODY
        p.font.size = Pt(9.5)
        p.font.color.rgb = C_TEXT_BODY
        p.space_before = Pt(4)

    tb_b22 = s22.shapes.add_textbox(Inches(0.72), Inches(6.15), Inches(11.89), Inches(0.5))
    tf_b22 = tb_b22.text_frame
    p_b22 = tf_b22.paragraphs[0]
    p_b22.text = "Privacy Notice: Individual student assessments and feedback are strictly confidential and shared solely with that student's parents."
    p_b22.font.name = FONT_BODY
    p_b22.font.size = Pt(10.5)
    p_b22.font.color.rgb = C_TEXT_MUTED

    add_footer(s22, 22, total_slides)

    # -------------------------------------------------------------------------
    # SLIDE 23: LIFE BEYOND LESSONS — CLASS CELEBRATIONS
    # -------------------------------------------------------------------------
    s23 = prs.slides.add_slide(blank_layout)
    set_slide_background(s23, C_BEIGE_BG)
    add_header(s23, "PART B / INDIVIDUAL CLASS PRESENTATION", "Class Life & Shared Experiences",
               "How our class community builds friendship, leadership and unforgettable memories.")

    col_w23 = Inches(3.75)
    gap23 = Inches(0.3)
    top_y23 = Inches(1.95)
    h23 = Inches(4.05)

    ev_class = [
        ("CLASS EVENT 1", "[Event / Celebration Name]",
         "[Date / Term Milestone]\n\n"
         "Highlights & Student Participation:\n"
         "• Active involvement of every student in role assignments and stage preparation.\n"
         "• Fostered public speaking confidence and creative artistic expression.\n"
         "• Collaborative team effort strengthening peer bonds."),
        ("CLASS EVENT 2", "[Project / Field Trip / Contest]",
         "[Date / Term Milestone]\n\n"
         "Highlights & Student Participation:\n"
         "• Hands-on educational visit connecting classroom curriculum to real-world context.\n"
         "• Group project presentations evaluated by guest mentors and teachers.\n"
         "• Outstanding student leadership, curiosity, and teamwork demonstrated."),
        ("CLASS EVENT 3", "[Sports Day / Community Fair]",
         "[Date / Term Milestone]\n\n"
         "Highlights & Student Participation:\n"
         "• Enthusiastic participation in inter-house tournaments and charity initiatives.\n"
         "• Demonstrating sportsmanship, resilience, and Target International School pride.\n"
         "• Recognized with class awards and certificates of achievement.")
    ]

    for idx, (tag, title, desc) in enumerate(ev_class):
        cur_x = Inches(0.72) + idx * (col_w23 + gap23)
        add_card(s23, cur_x, top_y23, col_w23, h23)
        add_rect(s23, cur_x, top_y23, col_w23, Inches(0.5), C_NAVY_DARK if idx != 1 else C_GOLD)
        
        tb = s23.shapes.add_textbox(cur_x + Inches(0.2), top_y23 + Inches(0.08), col_w23 - Inches(0.4), Inches(0.4))
        tf = tb.text_frame
        p = tf.paragraphs[0]
        p.text = tag
        p.font.name = FONT_HEADING
        p.font.size = Pt(11.5)
        p.font.bold = True
        p.font.color.rgb = C_WHITE if idx != 1 else C_NAVY_DARK

        # Photo placeholder
        add_card(s23, cur_x + Inches(0.25), top_y23 + Inches(0.65), col_w23 - Inches(0.5), Inches(1.3), fill_color=C_BEIGE_CARD, border_color=C_GOLD_LIGHT)
        tb_p = s23.shapes.add_textbox(cur_x + Inches(0.25), top_y23 + Inches(1.05), col_w23 - Inches(0.5), Inches(0.4))
        tf_p = tb_p.text_frame
        p = tf_p.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        p.text = "[ADD EVENT PHOTOGRAPH]"
        p.font.name = FONT_HEADING
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = C_TEXT_MUTED

        tb_b = s23.shapes.add_textbox(cur_x + Inches(0.25), top_y23 + Inches(2.05), col_w23 - Inches(0.5), h23 - Inches(2.15))
        tf_b = tb_b.text_frame
        tf_b.word_wrap = True
        
        p = tf_b.paragraphs[0]
        p.text = title
        p.font.name = FONT_HEADING
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_NAVY_DARK

        p2 = tf_b.add_paragraph()
        p2.text = desc
        p2.font.name = FONT_BODY
        p2.font.size = Pt(9)
        p2.font.color.rgb = C_TEXT_BODY
        p2.space_before = Pt(4)

    tb_b23 = s23.shapes.add_textbox(Inches(0.72), Inches(6.12), Inches(11.89), Inches(0.6))
    tf_b23 = tb_b23.text_frame
    p_b23 = tf_b23.paragraphs[0]
    p_b23.text = "Community Building: These shared memories create a positive classroom culture where students encourage and uplift one another."
    p_b23.font.name = FONT_BODY
    p_b23.font.size = Pt(10.5)
    p_b23.font.color.rgb = C_TEXT_MUTED

    add_footer(s23, 23, total_slides)

    # -------------------------------------------------------------------------
    # SLIDE 24: LOOKING AHEAD — CLASS GOALS
    # -------------------------------------------------------------------------
    s24 = prs.slides.add_slide(blank_layout)
    set_slide_background(s24, C_BEIGE_BG)
    add_header(s24, "PART B / INDIVIDUAL CLASS PRESENTATION", "Our Class Goals & Upcoming Milestones",
               "Clear, measurable targets for academic achievement, Olympiads and character development.")

    card_w24 = Inches(3.78)
    card_h24 = Inches(1.9)
    gap_x24 = Inches(0.27)
    gap_y24 = Inches(0.22)
    top_y24 = Inches(1.95)

    goals = [
        ("ACADEMIC TARGETS", "Term 2 Syllabus Mastery",
         "Targeting a class-wide GPA average of 86%+ through structured homework routines, unit revision packs, and proactive booster sessions.", C_NAVY_DARK),
        ("CAMBRIDGE & OLYMPIADS", "Competition Readiness",
         "Preparing designated student squads for SASMO, AMC Math, and World Scholar's Cup with specialized after-school training.", C_GOLD),
        ("PROJECTS & SHOWCASES", "Hands-on Engineering & Art",
         "Developing student-led STEM prototypes, coding apps, and debate exhibitions for the upcoming Target School Innovation Expo.", C_ACCENT_BLUE),
        ("EDUCATIONAL VISITS", "Experiential Learning",
         "Planned scientific excursions to state university laboratories, IT parks, and cultural heritage centers to expand student perspective.", C_ACCENT_GREEN),
        ("WELLBEING & PASTORAL", "Social-Emotional Resilience",
         "Continuing fortnightly psychologist-led workshops focusing on positive study habits, stress management, and collaborative friendship.", C_ACCENT_CORAL),
        ("PARENT PARTNERSHIP", "Continuous Communication",
         "Bi-weekly digital performance summaries, direct tutor office hours, and collaborative home-school reinforcement of positive routines.", C_NAVY_DARK)
    ]

    for idx, (title, sub, desc, col) in enumerate(goals):
        r = idx // 3
        c = idx % 3
        cur_x = Inches(0.72) + c * (card_w24 + gap_x24)
        cur_y = top_y24 + r * (card_h24 + gap_y24)
        
        add_card(s24, cur_x, cur_y, card_w24, card_h24)
        add_rect(s24, cur_x, cur_y, card_w24, Inches(0.06), col)
        
        tb = s24.shapes.add_textbox(cur_x + Inches(0.2), cur_y + Inches(0.12), card_w24 - Inches(0.4), card_h24 - Inches(0.2))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = FONT_HEADING
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_NAVY_DARK

        p2 = tf.add_paragraph()
        p2.text = sub
        p2.font.name = FONT_HEADING
        p2.font.size = Pt(9.5)
        p2.font.bold = True
        p2.font.color.rgb = col
        p2.space_before = Pt(2)

        p3 = tf.add_paragraph()
        p3.text = desc
        p3.font.name = FONT_BODY
        p3.font.size = Pt(9)
        p3.font.color.rgb = C_TEXT_BODY
        p3.space_before = Pt(4)

    tb_b24 = s24.shapes.add_textbox(Inches(0.72), Inches(6.15), Inches(11.89), Inches(0.5))
    tf_b24 = tb_b24.text_frame
    p_b24 = tf_b24.paragraphs[0]
    p_b24.text = "Our Shared Commitment: Every milestone is achievable when school, student and parents move forward in close alignment."
    p_b24.font.name = FONT_BODY
    p_b24.font.size = Pt(10.5)
    p_b24.font.color.rgb = C_TEXT_MUTED

    add_footer(s24, 24, total_slides)

    # -------------------------------------------------------------------------
    # SLIDE 25: REFLECTION AND IMPROVEMENT — CLASS SWOT
    # -------------------------------------------------------------------------
    s25 = prs.slides.add_slide(blank_layout)
    set_slide_background(s25, C_BEIGE_BG)
    add_header(s25, "PART B / INDIVIDUAL CLASS PRESENTATION", "Class SWOT Analysis: Turning Insight into Action",
               "Honest, evidence-based reflection focusing on targeted academic improvement and student support.")

    swot_w = Inches(5.8)
    swot_h = Inches(1.9)
    top_y25 = Inches(1.95)

    swot_data = [
        ("STRENGTHS (WHAT IS WORKING WELL)",
         "High Engagement & STEM Aptitude",
         "• Outstanding enthusiasm in mathematics, computing and scientific inquiries.\n"
         "• Strong camaraderie, mutual peer support, and positive classroom conduct.\n"
         "• High attendance rate and reliable daily homework submission.",
         C_NAVY_DARK),
        ("AREAS TO IMPROVE (WHERE SUPPORT IS NEEDED)",
         "Academic Writing & Time Management",
         "• Extended analytical essay composition under timed Cambridge conditions.\n"
         "• Systematic revision habits rather than last-minute test cramming.\n"
         "• Reading endurance for complex academic texts and scientific terminology.",
         C_ACCENT_CORAL),
        ("OPPORTUNITIES (WHAT WE CAN BUILD ON)",
         "Olympiads, Hackathons & Competitions",
         "• Expanding participation in national and international STEM Olympiads.\n"
         "• Student-led clubs, debate circles, and interactive science fair booths.\n"
         "• Accelerated Cambridge Checkpoint / IGCSE preparatory modules.",
         C_GOLD),
        ("CHALLENGES & SOLUTIONS (HOW WE RESPOND)",
         "Targeted Strategies for Consistent Growth",
         "• Challenge: Exam anxiety -> Solution: Phased weekly mocks and psychologist sessions.\n"
         "• Challenge: Varied learning speeds -> Solution: Differentiated tasks and booster clinics.\n"
         "• Challenge: Distractions -> Solution: Strict phone-free policy and clear home study guidelines.",
         C_ACCENT_BLUE)
    ]

    for idx, (title, sub, body, col) in enumerate(swot_data):
        r = idx // 2
        c = idx % 2
        cur_x = Inches(0.72) + c * (swot_w + Inches(0.29))
        cur_y = top_y25 + r * (swot_h + Inches(0.22))
        
        add_card(s25, cur_x, cur_y, swot_w, swot_h)
        add_rect(s25, cur_x, cur_y, swot_w, Inches(0.06), col)
        
        tb = s25.shapes.add_textbox(cur_x + Inches(0.25), cur_y + Inches(0.12), swot_w - Inches(0.5), swot_h - Inches(0.2))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = FONT_HEADING
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_NAVY_DARK

        p2 = tf.add_paragraph()
        p2.text = sub
        p2.font.name = FONT_HEADING
        p2.font.size = Pt(9.5)
        p2.font.bold = True
        p2.font.color.rgb = col
        p2.space_before = Pt(2)

        p3 = tf.add_paragraph()
        p3.text = body
        p3.font.name = FONT_BODY
        p3.font.size = Pt(9)
        p3.font.color.rgb = C_TEXT_BODY
        p3.space_before = Pt(3)

    tb_b25 = s25.shapes.add_textbox(Inches(0.72), Inches(6.15), Inches(11.89), Inches(0.5))
    tf_b25 = tb_b25.text_frame
    p_b25 = tf_b25.paragraphs[0]
    p_b25.text = "Continuous Improvement: Honest evaluation is the first step toward genuine excellence — our focus is always on solutions, not blame."
    p_b25.font.name = FONT_BODY
    p_b25.font.size = Pt(10.5)
    p_b25.font.color.rgb = C_TEXT_MUTED

    add_footer(s25, 25, total_slides)

    # -------------------------------------------------------------------------
    # SLIDE 26: CLOSING PARTNERSHIP & HOMEROOM Q&A (Dark Navy)
    # -------------------------------------------------------------------------
    s26 = prs.slides.add_slide(blank_layout)
    set_slide_background(s26, C_NAVY_DARK)

    # Header Tracker
    tb_t26 = s26.shapes.add_textbox(Inches(0.72), Inches(0.42), Inches(9.6), Inches(0.3))
    tf_t26 = tb_t26.text_frame
    p = tf_t26.paragraphs[0]
    p.text = "PART B / INDIVIDUAL CLASS PRESENTATION"
    p.font.name = FONT_HEADING
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = C_GOLD

    # Main Title
    tb_m26 = s26.shapes.add_textbox(Inches(0.72), Inches(0.74), Inches(9.6), Inches(0.65))
    tf_m26 = tb_m26.text_frame
    p = tf_m26.paragraphs[0]
    p.text = "Thank You for Your Trust & Partnership"
    p.font.name = FONT_HEADING
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = C_WHITE

    if os.path.exists(LOGO_WHITE_PATH):
        try:
            s26.shapes.add_picture(LOGO_WHITE_PATH, Inches(10.65), Inches(0.46), width=Inches(1.95))
        except Exception:
            pass

    # 3 Next Steps Cards
    c26_w = Inches(3.75)
    c26_gap = Inches(0.3)
    c26_top = Inches(1.8)
    c26_h = Inches(3.4)

    steps_close = [
        ("1-ON-1 CONSULTATIONS", "Meet With Subject Teachers",
         "• Individual 10-minute feedback sessions available right now.\n"
         "• Review your child's specific test papers, homework portfolio and attendance.\n"
         "• Agree on targeted home and school support actions for the coming month."),
        ("COMMUNICATION CHANNELS", "Stay Constantly Connected",
         "• Official Telegram parent group and homeroom tutor contact.\n"
         "• Weekly Friday academic progress and homework briefings.\n"
         "• Urgent matters: Direct line to Homeroom Tutor & School Administration."),
        ("UPCOMING PARENT EVENTS", "Mark Your Calendar",
         "• Next Parent Progress Update: [Confirmed Date]\n"
         "• Open Classroom Teaching Day: [Confirmed Date]\n"
         "• Target International School Winter Gala: [Confirmed Date]")
    ]

    for idx, (title, sub, desc) in enumerate(steps_close):
        cur_x = Inches(0.72) + idx * (c26_w + c26_gap)
        add_card(s26, cur_x, c26_top, c26_w, c26_h, fill_color=C_NAVY_PANEL, border_color=C_GOLD_LIGHT)
        
        tb = s26.shapes.add_textbox(cur_x + Inches(0.2), c26_top + Inches(0.2), c26_w - Inches(0.4), c26_h - Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = FONT_HEADING
        p.font.size = Pt(11.5)
        p.font.bold = True
        p.font.color.rgb = C_GOLD

        p2 = tf.add_paragraph()
        p2.text = sub
        p2.font.name = FONT_HEADING
        p2.font.size = Pt(10)
        p2.font.bold = True
        p2.font.color.rgb = C_WHITE
        p2.space_before = Pt(2)

        p3 = tf.add_paragraph()
        p3.text = desc
        p3.font.name = FONT_BODY
        p3.font.size = Pt(9.5)
        p3.font.color.rgb = C_BEIGE_CARD
        p3.space_before = Pt(8)

    # Bottom Contact Bar
    add_card(s26, Inches(0.72), Inches(5.45), Inches(11.89), Inches(1.3), fill_color=C_NAVY_PANEL, border_color=C_GOLD, border_width=Pt(1.5))
    tb_c26 = s26.shapes.add_textbox(Inches(0.95), Inches(5.55), Inches(11.4), Inches(1.1))
    tf_c26 = tb_c26.text_frame
    tf_c26.word_wrap = True
    
    p = tf_c26.paragraphs[0]
    p.text = "QUESTIONS & INDIVIDUAL DISCUSSIONS ARE NOW OPEN"
    p.font.name = FONT_HEADING
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_GOLD_LIGHT

    p2 = tf_c26.add_paragraph()
    p2.text = "Thank you for attending today's Parents' Meeting. Your active support, feedback and partnership make our students' extraordinary achievements possible."
    p2.font.name = FONT_BODY
    p2.font.size = Pt(10.5)
    p2.font.color.rgb = C_WHITE
    p2.space_before = Pt(2)

    p3 = tf_c26.add_paragraph()
    p3.text = "Target International School  •  Yunusobod Campus  •  Beyond Education: Building Knowledge, Character & Future Success"
    p3.font.name = FONT_BODY
    p3.font.size = Pt(9.5)
    p3.font.color.rgb = C_BEIGE_CARD
    p3.space_before = Pt(2)

    add_footer(s26, 26, total_slides, is_dark=True)


def main():
    out_dir = "/home/dpdp/target/parents_meeting/presentations"
    os.makedirs(out_dir, exist_ok=True)

    # 1. Build Part A: 18-Slide Master School Presentation
    prs18 = pptx.Presentation()
    prs18.slide_width = Inches(13.333)
    prs18.slide_height = Inches(7.5)
    build_master_deck(prs18)
    file_master = os.path.join(out_dir, "Target_International_School_Parent_Meeting_2026_2027.pptx")
    prs18.save(file_master)
    print(f"Generated 18-Slide Master Deck: {file_master}")

    # 2. Build Part A + Part B: 26-Slide Complete Homeroom Teacher Presentation
    prs26 = pptx.Presentation()
    prs26.slide_width = Inches(13.333)
    prs26.slide_height = Inches(7.5)
    build_master_deck(prs26)
    build_teacher_additions(prs26, total_slides=26)
    file_complete = os.path.join(out_dir, "Target_International_School_Parent_Meeting_Complete_Teacher_Deck.pptx")
    prs26.save(file_complete)
    print(f"Generated 26-Slide Complete Teacher Deck: {file_complete}")

if __name__ == "__main__":
    main()
