import json

with open('/home/dpdp/target/parents_meeting/working-inventory.json') as f:
    inv = json.load(f)

replacements = {}

def add_para(text, font_size=None, bold=None, color=None, alignment=None, bullet=None, level=None, space_before=None):
    p = {"text": text}
    if font_size is not None: p["font_size"] = font_size
    if bold is not None: p["bold"] = bold
    if color is not None: p["color"] = color
    if alignment is not None and not bullet: p["alignment"] = alignment
    if bullet:
        p["bullet"] = True
        p["level"] = level if level is not None else 0
    if space_before is not None: p["space_before"] = space_before
    return p

# Slide 00: Cover
s0 = {}
s0["shape-0"] = {"paragraphs": [add_para("TARGET", font_size=20.0, bold=True, color="FFFFFF")]}
s0["shape-1"] = {"paragraphs": [add_para("INTERNATIONAL SCHOOL", font_size=10.0, bold=True, color="DCC497")]}
s0["shape-2"] = {"paragraphs": [
    add_para("BEYOND EDUCATION:", font_size=32.0, bold=True, color="FFFFFF"),
    add_para("BUILDING KNOWLEDGE, CHARACTER & FUTURE SUCCESS", font_size=24.0, bold=True, color="FFFFFF")
]}
s0["shape-3"] = {"paragraphs": [add_para("An International Learning Environment. A World of Opportunities.", font_size=15.0, color="DCC497")]}
s0["shape-4"] = {"paragraphs": [add_para("PARENTS' MEETING   |   ACADEMIC YEAR 2026–2027", font_size=10.0, bold=True, color="FFFFFF")]}
s0["shape-5"] = {"paragraphs": [add_para("A shared partnership between school, students and families", font_size=11.0, color="ECE5D7")]}
s0["shape-6"] = {"paragraphs": [add_para("WELCOME PARENTS", font_size=11.0, bold=True, color="FFFFFF")]}
s0["shape-7"] = {"paragraphs": [add_para("TARGET INTERNATIONAL SCHOOL   •   PARENT MEETING   •   2026–2027", font_size=7.0, bold=True, color="DCC497")]}
s0["shape-8"] = {"paragraphs": [add_para("01", font_size=9.0, bold=True, color="BE995B", alignment="RIGHT")]}
replacements["slide-0"] = s0

# Slide 01: Environment
s1 = {}
s1["shape-0"] = {"paragraphs": [add_para("01 / INTRODUCTION — WHO WE ARE", font_size=9.0, bold=True, color="BE995B")]}
s1["shape-1"] = {"paragraphs": [add_para("Our International Education Environment", font_size=25.0, bold=True, color="12243D")]}
s1["shape-2"] = {"paragraphs": [add_para("High standards, modern campus infrastructure and a holistic commitment to every learner.", font_size=11.0, color="6F777F")]}
s1["shape-3"] = {"paragraphs": [add_para("Dear Parents & Guardians,", font_size=15.0, bold=True, color="12243D")]}
s1["shape-4"] = {"paragraphs": [
    add_para("Thank you for being an essential part of the Target International School family. Our school is founded on a clear mission: nurturing confident, capable, and principled global thinkers.", font_size=10.0, color="2F3740"),
    add_para("We combine internationally accredited Cambridge standards with holistic pastoral care, rigorous STEM education, and personalized university preparation.", font_size=10.0, color="2F3740", space_before=6.0)
]}
s1["shape-5"] = {"paragraphs": [add_para("CAMPUS", font_size=9.0, bold=True, color="6F777F")]}
s1["shape-6"] = {"paragraphs": [add_para("EXCELLENCE   •   RESPONSIBILITY   •   INTEGRITY", font_size=8.0, bold=True, color="FFFFFF")]}
s1["shape-7"] = {"paragraphs": [add_para("Target International School Campus & Academic Community", font_size=8.0, color="6F777F")]}
s1["shape-8"] = {"paragraphs": [add_para("One community. One shared purpose.", font_size=13.0, bold=True, color="12243D")]}
s1["shape-9"] = {"paragraphs": [add_para("TARGET INTERNATIONAL SCHOOL   •   PARENT MEETING   •   2026–2027", font_size=7.0, bold=True, color="6F777F")]}
s1["shape-10"] = {"paragraphs": [add_para("02", font_size=9.0, bold=True, color="BE995B", alignment="RIGHT")]}
replacements["slide-1"] = s1

# Slide 02: Academic Pathways
s2 = {}
s2["shape-0"] = {"paragraphs": [add_para("02 / ACADEMIC SYSTEM — HOW WE EDUCATE", font_size=9.0, bold=True, color="BE995B")]}
s2["shape-1"] = {"paragraphs": [add_para("Our International Academic Pathways", font_size=25.0, bold=True, color="12243D")]}
s2["shape-2"] = {"paragraphs": [add_para("A connected educational journey from foundational skills to elite global qualifications.", font_size=11.0, color="6F777F")]}
s2["shape-3"] = {"paragraphs": [add_para("01", font_size=21.0, bold=True, color="BE995B")]}
s2["shape-4"] = {"paragraphs": [add_para("→", font_size=15.0, bold=True, color="BE995B")]}
s2["shape-5"] = {"paragraphs": [add_para("02", font_size=21.0, bold=True, color="BE995B")]}
s2["shape-6"] = {"paragraphs": [add_para("→", font_size=15.0, bold=True, color="BE995B")]}
s2["shape-7"] = {"paragraphs": [add_para("03", font_size=21.0, bold=True, color="BE995B")]}
s2["shape-8"] = {"paragraphs": [add_para("→", font_size=15.0, bold=True, color="BE995B")]}
s2["shape-9"] = {"paragraphs": [add_para("04", font_size=21.0, bold=True, color="BE995B")]}
s2["shape-10"] = {"paragraphs": [add_para("CAMBRIDGE PRIMARY & LOWER SEC.", font_size=10.0, bold=True, color="12243D")]}
s2["shape-11"] = {"paragraphs": [add_para("Grades 1–7: English, Mathematics, Sciences, Computing foundations & critical inquiry", font_size=9.0, color="6F777F")]}
s2["shape-12"] = {"paragraphs": [add_para("CAMBRIDGE IGCSE", font_size=10.0, bold=True, color="12243D")]}
s2["shape-13"] = {"paragraphs": [add_para("Grades 8–9: Rigorous subject specialization, external assessments & lab research", font_size=9.0, color="6F777F")]}
s2["shape-14"] = {"paragraphs": [add_para("CAMBRIDGE AS & A LEVEL", font_size=10.0, bold=True, color="12243D")]}
s2["shape-15"] = {"paragraphs": [add_para("Grades 10–11: Advanced subject mastery accepted by leading worldwide universities", font_size=9.0, color="6F777F")]}
s2["shape-16"] = {"paragraphs": [add_para("WESTERN & AUSTRALIAN PATHWAY", font_size=10.0, bold=True, color="12243D")]}
s2["shape-17"] = {"paragraphs": [add_para("Planned 2027: Dual-diploma opportunities, practical portfolios & Australian track", font_size=9.0, color="6F777F")]}
s2["shape-18"] = {"paragraphs": [add_para("Continuous Alignment: All pathways follow official Cambridge standards and are taught by certified subject specialists.", font_size=9.0, color="6F777F")]}
s2["shape-19"] = {"paragraphs": [add_para("TARGET INTERNATIONAL SCHOOL   •   PARENT MEETING   •   2026–2027", font_size=7.0, bold=True, color="6F777F")]}
s2["shape-20"] = {"paragraphs": [add_para("03", font_size=9.0, bold=True, color="BE995B", alignment="RIGHT")]}
replacements["slide-2"] = s2

# Slide 03: Specialisation
s3 = {}
s3["shape-0"] = {"paragraphs": [add_para("02 / ACADEMIC SYSTEM — HOW WE EDUCATE", font_size=9.0, bold=True, color="BE995B")]}
s3["shape-1"] = {"paragraphs": [add_para("Specialisation from Grades 8–9: Science vs Economics", font_size=25.0, bold=True, color="12243D")]}
s3["shape-2"] = {"paragraphs": [add_para("Targeted academic pathways aligned with student strengths and long-term university goals.", font_size=11.0, color="6F777F")]}
s3["shape-3"] = {"paragraphs": [add_para("SCIENCE & STEM PATHWAY", font_size=12.0, bold=True, color="12243D")]}
s3["shape-4"] = {"paragraphs": [add_para("Mathematics, Physics, Chemistry, Biology & Vibecoding. Focus on laboratory inquiry, quantitative reasoning, and engineering design. Destination: Top STEM & Medical faculties.", font_size=9.5, color="2F3740")]}
s3["shape-5"] = {"paragraphs": [add_para("ECONOMICS & BUSINESS PATHWAY", font_size=12.0, bold=True, color="12243D")]}
s3["shape-6"] = {"paragraphs": [add_para("Economics, Business Studies, Accounting, Statistics & Global Trade. Focus on financial analysis, business case competitions, and market strategy. Destination: Top Business & Law schools.", font_size=9.5, color="2F3740")]}
s3["shape-7"] = {"paragraphs": [add_para("LABORATORY & RESEARCH", font_size=12.0, bold=True, color="12243D")]}
s3["shape-8"] = {"paragraphs": [add_para("Hands-on experimental verification, coding prototypes, scientific method defense, and algorithmic simulations in modern lab facilities.", font_size=9.5, color="2F3740")]}
s3["shape-9"] = {"paragraphs": [add_para("CASE STUDY & ENTREPRENEURSHIP", font_size=12.0, bold=True, color="12243D")]}
s3["shape-10"] = {"paragraphs": [add_para("Analyzing real global corporate cases, financial statement modeling, startup simulations, and developing professional negotiation skills.", font_size=9.5, color="2F3740")]}
s3["shape-11"] = {"paragraphs": [add_para("Diagnostic Selection: Guided by academic diagnostic scores, psychologist evaluations, and individual family admissions roadmaps.", font_size=9.0, color="6F777F")]}
s3["shape-12"] = {"paragraphs": [add_para("TARGET INTERNATIONAL SCHOOL   •   PARENT MEETING   •   2026–2027", font_size=7.0, bold=True, color="6F777F")]}
s3["shape-13"] = {"paragraphs": [add_para("04", font_size=9.0, bold=True, color="BE995B", alignment="RIGHT")]}
replacements["slide-3"] = s3

# Slide 04: University Prep
s4 = {}
s4["shape-0"] = {"paragraphs": [add_para("02 / ACADEMIC SYSTEM — HOW WE EDUCATE", font_size=9.0, bold=True, color="BE995B")]}
s4["shape-1"] = {"paragraphs": [add_para("Grades 10–11: University Preparation Programme", font_size=25.0, bold=True, color="12243D")]}
s4["shape-2"] = {"paragraphs": [add_para("A comprehensive pre-university ecosystem ensuring competitive worldwide admissions.", font_size=11.0, color="6F777F")]}
s4["shape-3"] = {"paragraphs": [add_para("IELTS ACADEMIC INTENSIVE", font_size=11.0, bold=True, color="12243D")]}
s4["shape-4"] = {"paragraphs": [add_para("Target Band 7.5–8.5+: Weekly full-length mock exams, Task 1 & 2 academic essays, and speaking interview coaching.", font_size=9.0, color="6F777F")]}
s4["shape-5"] = {"paragraphs": [add_para("DIGITAL SAT PREPARATION", font_size=11.0, bold=True, color="12243D")]}
s4["shape-6"] = {"paragraphs": [add_para("Target 1450–1550+: Mastery of adaptive digital Math modules, Reading & Writing analysis, and speed strategies.", font_size=9.0, color="6F777F")]}
s4["shape-7"] = {"paragraphs": [add_para("ACADEMIC RESEARCH & WRITING", font_size=11.0, bold=True, color="12243D")]}
s4["shape-8"] = {"paragraphs": [add_para("Pre-university research paper defense, formal essay argumentation, citation standards, and critical thinking.", font_size=9.0, color="6F777F")]}
s4["shape-9"] = {"paragraphs": [add_para("UNIVERSITY APPLICATION GUIDANCE", font_size=11.0, bold=True, color="12243D")]}
s4["shape-10"] = {"paragraphs": [add_para("Common App, UCAS & global portals: personal statement workshops, activity list refinement, and recommendations.", font_size=9.0, color="6F777F")]}
s4["shape-11"] = {"paragraphs": [add_para("PORTFOLIO & PROFILE BUILDING", font_size=11.0, bold=True, color="12243D")]}
s4["shape-12"] = {"paragraphs": [add_para("Olympiad medals, student council leadership, published research, and community service initiatives.", font_size=9.0, color="6F777F")]}
s4["shape-13"] = {"paragraphs": [add_para("THE 'BUNKER' SYSTEM", font_size=11.0, bold=True, color="12243D")]}
s4["shape-14"] = {"paragraphs": [add_para("Dedicated high-focus study pods, supervised evening revision hours, peer bootcamps, and 1-on-1 mentor support.", font_size=9.0, color="6F777F")]}
s4["shape-15"] = {"paragraphs": [add_para("Admissions Commitment: 100% of our Grade 10–11 students receive personalized academic profiling and tailored university roadmap plans.", font_size=9.0, color="6F777F")]}
s4["shape-16"] = {"paragraphs": [add_para("TARGET INTERNATIONAL SCHOOL   •   PARENT MEETING   •   2026–2027", font_size=7.0, bold=True, color="6F777F")]}
s4["shape-17"] = {"paragraphs": [add_para("05", font_size=9.0, bold=True, color="BE995B", alignment="RIGHT")]}
replacements["slide-4"] = s4

# Slide 05: Learning Materials
s5 = {}
s5["shape-0"] = {"paragraphs": [add_para("02 / ACADEMIC SYSTEM — HOW WE EDUCATE", font_size=9.0, bold=True, color="BE995B")]}
s5["shape-1"] = {"paragraphs": [add_para("Our Learning Materials & Curriculum Resources", font_size=25.0, bold=True, color="12243D")]}
s5["shape-2"] = {"paragraphs": [add_para("Cambridge-endorsed textbooks, hybrid courseware and cutting-edge digital learning platforms.", font_size=11.0, color="6F777F")]}
s5["shape-3"] = {"paragraphs": [add_para("CAMBRIDGE-ENDORSED TEXTBOOKS", font_size=12.0, bold=True, color="12243D")]}
s5["shape-4"] = {"paragraphs": [add_para("Official Cambridge University Press and Hodder Education endorsed textbooks across Mathematics, Sciences, Business and English.", font_size=9.5, color="2F3740")]}
s5["shape-5"] = {"paragraphs": [add_para("HYBRID PROGRAMME COURSEWARE", font_size=12.0, bold=True, color="12243D")]}
s5["shape-6"] = {"paragraphs": [add_para("Custom school-curated packs connecting Cambridge standards with national curriculum mastery, including bilingual glossaries.", font_size=9.5, color="2F3740")]}
s5["shape-7"] = {"paragraphs": [add_para("EXAM WORKBOOKS & PAST PAPERS", font_size=12.0, bold=True, color="12243D")]}
s5["shape-8"] = {"paragraphs": [add_para("Topic-by-topic 10-year past paper question banks, official Cambridge mark schemes, and weekly revision workbooks.", font_size=9.5, color="2F3740")]}
s5["shape-9"] = {"paragraphs": [add_para("DIGITAL LEARNING PLATFORMS", font_size=12.0, bold=True, color="12243D")]}
s5["shape-10"] = {"paragraphs": [add_para("School LMS portal, virtual science simulations, coding playgrounds, automated diagnostic quizzes, and homework tracking.", font_size=9.5, color="2F3740")]}
s5["shape-11"] = {"paragraphs": [add_para("Resource Guarantee: Every student receives official printed coursebooks and verified portal credentials at the start of term.", font_size=9.0, color="6F777F")]}
s5["shape-12"] = {"paragraphs": [add_para("TARGET INTERNATIONAL SCHOOL   •   PARENT MEETING   •   2026–2027", font_size=7.0, bold=True, color="6F777F")]}
s5["shape-13"] = {"paragraphs": [add_para("06", font_size=9.0, bold=True, color="BE995B", alignment="RIGHT")]}
replacements["slide-5"] = s5

# Slide 06: Quality Assurance
s6 = {}
s6["shape-0"] = {"paragraphs": [add_para("03 / ACADEMIC QUALITY & MONITORING", font_size=9.0, bold=True, color="BE995B")]}
s6["shape-1"] = {"paragraphs": [add_para("Teacher Performance & Lesson Quality Assurance", font_size=25.0, bold=True, color="12243D")]}
s6["shape-2"] = {"paragraphs": [add_para("How Target International School systematically monitors teaching delivery and drives continuous improvement.", font_size=11.0, color="6F777F")]}
s6["shape-3"] = {"paragraphs": [add_para("AUDIO-RECORDING TECHNOLOGY", font_size=12.0, bold=True, color="12243D")]}
s6["shape-4"] = {"paragraphs": [add_para("Where implemented, lessons are digitally recorded to evaluate explanation clarity, student talk time, and lesson pacing.", font_size=9.5, color="2F3740")]}
s6["shape-5"] = {"paragraphs": [add_para("STRUCTURED LESSON OBSERVATIONS", font_size=12.0, bold=True, color="12243D")]}
s6["shape-6"] = {"paragraphs": [add_para("Academic leadership conducts regular unannounced evaluations using international rubrics: active engagement and differentiation.", font_size=9.5, color="2F3740")]}
s6["shape-7"] = {"paragraphs": [add_para("SYLLABUS & CURRICULUM COMPLIANCE", font_size=12.0, bold=True, color="12243D")]}
s6["shape-8"] = {"paragraphs": [add_para("Real-time weekly tracking of curriculum milestones guarantees no Cambridge learning objectives are omitted or rushed.", font_size=9.5, color="2F3740")]}
s6["shape-9"] = {"paragraphs": [add_para("PROFESSIONAL DEVELOPMENT (CPD)", font_size=12.0, bold=True, color="12243D")]}
s6["shape-10"] = {"paragraphs": [add_para("Bi-weekly teacher pedagogical workshops, Cambridge assessment webinars, modern pedagogy circles, and peer observations.", font_size=9.5, color="2F3740")]}
s6["shape-11"] = {"paragraphs": [add_para("Pedagogical Support: Monitoring is not punitive — it provides leadership with clear diagnostic data to support every teacher.", font_size=9.0, color="6F777F")]}
s6["shape-12"] = {"paragraphs": [add_para("TARGET INTERNATIONAL SCHOOL   •   PARENT MEETING   •   2026–2027", font_size=7.0, bold=True, color="6F777F")]}
s6["shape-13"] = {"paragraphs": [add_para("07", font_size=9.0, bold=True, color="BE995B", alignment="RIGHT")]}
replacements["slide-6"] = s6

# Slide 07: Smart Classroom
s7 = {}
s7["shape-0"] = {"paragraphs": [add_para("03 / ACADEMIC QUALITY & MONITORING", font_size=9.0, bold=True, color="BE995B")]}
s7["shape-1"] = {"paragraphs": [add_para("Smart Classroom & Student Engagement", font_size=25.0, bold=True, color="12243D")]}
s7["shape-2"] = {"paragraphs": [add_para("Integrating modern educational technology, student safety and responsible classroom analytics.", font_size=11.0, color="6F777F")]}
s7["shape-3"] = {"paragraphs": [add_para("01", font_size=21.0, bold=True, color="BE995B")]}
s7["shape-4"] = {"paragraphs": [add_para("02", font_size=21.0, bold=True, color="BE995B")]}
s7["shape-5"] = {"paragraphs": [add_para("03", font_size=21.0, bold=True, color="BE995B")]}
s7["shape-6"] = {"paragraphs": [add_para("SMART INFRASTRUCTURE", font_size=12.0, bold=True, color="12243D")]}
s7["shape-7"] = {"paragraphs": [add_para("ENGAGEMENT TRACKING", font_size=12.0, bold=True, color="12243D")]}
s7["shape-8"] = {"paragraphs": [add_para("DATA PRIVACY COMPLIANCE", font_size=12.0, bold=True, color="12243D")]}
s7["shape-9"] = {"paragraphs": [add_para("HD safety cameras and 4K interactive touch smartboards in every classroom enabling active multimedia inquiry.", font_size=9.5, color="6F777F")]}
s7["shape-10"] = {"paragraphs": [add_para("Monitoring student focus, participation patterns, and quickly identifying learners needing additional support.", font_size=9.5, color="6F777F")]}
s7["shape-11"] = {"paragraphs": [add_para("Camera and audio data are strictly confidential, protected under governance, and restricted to authorized leaders.", font_size=9.5, color="6F777F")]}
s7["shape-12"] = {"paragraphs": [add_para("CAMPUS SAFETY & ETHICS", font_size=9.0, bold=True, color="BE995B")]}
s7["shape-13"] = {"paragraphs": [add_para("All educational technology serves one primary purpose: student physical safety, academic growth, and targeted care.", font_size=9.5, color="2F3740")]}
s7["shape-14"] = {"paragraphs": [add_para("TARGET INTERNATIONAL SCHOOL   •   PARENT MEETING   •   2026–2027", font_size=7.0, bold=True, color="6F777F")]}
s7["shape-15"] = {"paragraphs": [add_para("08", font_size=9.0, bold=True, color="BE995B", alignment="RIGHT")]}
replacements["slide-7"] = s7

# Slide 08: Academic Team (Cleanly mapped to avoid overflow!)
s8 = {}
s8["shape-0"] = {"paragraphs": [add_para("03 / ACADEMIC QUALITY & MONITORING", font_size=9.0, bold=True, color="BE995B")]}
s8["shape-1"] = {"paragraphs": [add_para("Meet Our Academic Team", font_size=25.0, bold=True, color="12243D")]}
s8["shape-2"] = {"paragraphs": [add_para("Dedicated subject specialists holding advanced international qualifications and pedagogical experience.", font_size=11.0, color="6F777F")]}
s8["shape-3"] = {"paragraphs": [add_para("PHOTO", font_size=9.0, bold=True, color="6F777F")]}
s8["shape-4"] = {"paragraphs": [add_para("PHOTO", font_size=9.0, bold=True, color="6F777F")]}
s8["shape-5"] = {"paragraphs": [add_para("PHOTO", font_size=9.0, bold=True, color="6F777F")]}
s8["shape-6"] = {"paragraphs": [add_para("Profile 1", font_size=8.0, color="6F777F")]}
s8["shape-7"] = {"paragraphs": [add_para("English & Humanities", font_size=12.0, bold=True, color="12243D")]}
s8["shape-8"] = {"paragraphs": [add_para("Profile 2", font_size=8.0, color="6F777F")]}
s8["shape-9"] = {"paragraphs": [add_para("Mathematics & Sciences", font_size=12.0, bold=True, color="12243D")]}
s8["shape-10"] = {"paragraphs": [add_para("Profile 3", font_size=8.0, color="6F777F")]}
s8["shape-11"] = {"paragraphs": [add_para("Technology & Robotics", font_size=12.0, bold=True, color="12243D")]}
s8["shape-12"] = {"paragraphs": [add_para("Cambridge English & Literature", font_size=10.0, bold=True, color="BE995B")]}
s8["shape-13"] = {"paragraphs": [add_para("Master's in Linguistics • IELTS Examiners • Focus: Academic writing and analytical debate.", font_size=8.5, color="6F777F")]}
s8["shape-14"] = {"paragraphs": [add_para("Pure Math, Physics & Chemistry", font_size=10.0, bold=True, color="BE995B")]}
s8["shape-15"] = {"paragraphs": [add_para("M.S. in Applied Mathematics • Olympiad Trainers • Focus: Problem solving and lab research.", font_size=8.5, color="6F777F")]}
s8["shape-16"] = {"paragraphs": [add_para("Computer Science & Vibecoding", font_size=10.0, bold=True, color="BE995B")]}
s8["shape-17"] = {"paragraphs": [add_para("B.S. in Software Engineering • AI Mentors • Focus: Python, algorithm design & robotics.", font_size=8.5, color="6F777F")]}
s8["shape-18"] = {"paragraphs": [add_para("TARGET INTERNATIONAL SCHOOL   •   PARENT MEETING   •   2026–2027", font_size=7.0, bold=True, color="6F777F")]}
s8["shape-19"] = {"paragraphs": [add_para("09", font_size=9.0, bold=True, color="BE995B", alignment="RIGHT")]}
replacements["slide-8"] = s8

# Slide 09: Student Achievements
s9 = {}
s9["shape-0"] = {"paragraphs": [add_para("04 / ASSESSMENT, ACHIEVEMENTS & STUDENT DEVELOPMENT", font_size=9.0, bold=True, color="BE995B")]}
s9["shape-1"] = {"paragraphs": [add_para("Our Students' Achievements: Past, Present & Future", font_size=25.0, bold=True, color="12243D")]}
s9["shape-2"] = {"paragraphs": [add_para("Celebrating verified competition victories, ongoing academic growth and upcoming horizons.", font_size=11.0, color="6F777F")]}
s9["shape-3"] = {"paragraphs": [add_para("01", font_size=21.0, bold=True, color="BE995B")]}
s9["shape-4"] = {"paragraphs": [add_para("02", font_size=21.0, bold=True, color="BE995B")]}
s9["shape-5"] = {"paragraphs": [add_para("03", font_size=21.0, bold=True, color="BE995B")]}
s9["shape-6"] = {"paragraphs": [add_para("PAST ACHIEVEMENTS", font_size=12.0, bold=True, color="12243D")]}
s9["shape-7"] = {"paragraphs": [add_para("PRESENT MOMENTUM", font_size=12.0, bold=True, color="12243D")]}
s9["shape-8"] = {"paragraphs": [add_para("UPCOMING HORIZONS", font_size=12.0, bold=True, color="12243D")]}
s9["shape-9"] = {"paragraphs": [add_para("National Olympiad medals in Math and Sciences; top percentile rankings in Cambridge Checkpoint diagnostic exams.", font_size=9.5, color="6F777F")]}
s9["shape-10"] = {"paragraphs": [add_para("100% Term 1 syllabus completion, 92%+ homework submission consistency, and active coding hackathon participation.", font_size=9.5, color="6F777F")]}
s9["shape-11"] = {"paragraphs": [add_para("SASMO, Kangaroo Math, AMC registrations confirmed; World Scholar's Cup teams entering regional and global rounds.", font_size=9.5, color="6F777F")]}
s9["shape-12"] = {"paragraphs": [add_para("STUDENT RECOGNITION", font_size=9.0, bold=True, color="BE995B")]}
s9["shape-13"] = {"paragraphs": [add_para("We celebrate not only top scores, but also determination, character growth, and personal improvement across all grades.", font_size=9.5, color="2F3740")]}
s9["shape-14"] = {"paragraphs": [add_para("TARGET INTERNATIONAL SCHOOL   •   PARENT MEETING   •   2026–2027", font_size=7.0, bold=True, color="6F777F")]}
s9["shape-15"] = {"paragraphs": [add_para("10", font_size=9.0, bold=True, color="BE995B", alignment="RIGHT")]}
replacements["slide-9"] = s9

# Slide 10: Weekly Assessment System
s10 = {}
s10["shape-0"] = {"paragraphs": [add_para("04 / ASSESSMENT, ACHIEVEMENTS & STUDENT DEVELOPMENT", font_size=9.0, bold=True, color="BE995B")]}
s10["shape-1"] = {"paragraphs": [add_para("Our Weekly Assessment System: 4-Week Cycle", font_size=25.0, bold=True, color="12243D")]}
s10["shape-2"] = {"paragraphs": [add_para("A continuous cycle balancing rigorous academic mastery with student psychological wellbeing.", font_size=11.0, color="6F777F")]}
s10["shape-3"] = {"paragraphs": [add_para("01", font_size=21.0, bold=True, color="BE995B")]}
s10["shape-4"] = {"paragraphs": [add_para("→", font_size=15.0, bold=True, color="BE995B")]}
s10["shape-5"] = {"paragraphs": [add_para("02", font_size=21.0, bold=True, color="BE995B")]}
s10["shape-6"] = {"paragraphs": [add_para("→", font_size=15.0, bold=True, color="BE995B")]}
s10["shape-7"] = {"paragraphs": [add_para("03", font_size=21.0, bold=True, color="BE995B")]}
s10["shape-8"] = {"paragraphs": [add_para("→", font_size=15.0, bold=True, color="BE995B")]}
s10["shape-9"] = {"paragraphs": [add_para("04", font_size=21.0, bold=True, color="BE995B")]}
s10["shape-10"] = {"paragraphs": [add_para("WEEK 1: PSYCHOLOGICAL", font_size=11.0, bold=True, color="12243D")]}
s10["shape-11"] = {"paragraphs": [add_para("Emotional wellbeing, adaptation, school belonging, and stress level evaluation", font_size=9.0, color="6F777F")]}
s10["shape-12"] = {"paragraphs": [add_para("WEEK 2: ACADEMIC", font_size=11.0, bold=True, color="12243D")]}
s10["shape-13"] = {"paragraphs": [add_para("Core subject formative diagnostics: testing concept retention and problem solving", font_size=9.0, color="6F777F")]}
s10["shape-14"] = {"paragraphs": [add_para("WEEK 3: PSYCHOLOGICAL", font_size=11.0, bold=True, color="12243D")]}
s10["shape-15"] = {"paragraphs": [add_para("Classroom focus, study discipline, peer collaboration, and resilience check", font_size=9.0, color="6F777F")]}
s10["shape-16"] = {"paragraphs": [add_para("WEEK 4: ACADEMIC", font_size=11.0, bold=True, color="12243D")]}
s10["shape-17"] = {"paragraphs": [add_para("Comprehensive unit progress review, Cambridge question styles & parent report", font_size=9.0, color="6F777F")]}
s10["shape-18"] = {"paragraphs": [add_para("Early Intervention Advantage: The alternating 4-week cycle catches learning gaps or emotional hurdles within days, before termly exams.", font_size=9.0, color="6F777F")]}
s10["shape-19"] = {"paragraphs": [add_para("TARGET INTERNATIONAL SCHOOL   •   PARENT MEETING   •   2026–2027", font_size=7.0, bold=True, color="6F777F")]}
s10["shape-20"] = {"paragraphs": [add_para("11", font_size=9.0, bold=True, color="BE995B", alignment="RIGHT")]}
replacements["slide-10"] = s10

# Slide 11: Termly Exams (Correctly mapped to match small shape-11..14 and wide shape-16..19!)
s11 = {}
s11["shape-0"] = {"paragraphs": [add_para("04 / ASSESSMENT, ACHIEVEMENTS & STUDENT DEVELOPMENT", font_size=9.0, bold=True, color="BE995B")]}
s11["shape-1"] = {"paragraphs": [add_para("Termly Examination & Academic Analytics", font_size=25.0, bold=True, color="12243D")]}
s11["shape-2"] = {"paragraphs": [add_para("Standardized examination administration, secure moderation and comprehensive analytics reporting.", font_size=11.0, color="6F777F")]}
s11["shape-3"] = {"paragraphs": [add_para("STAGE 1: PREPARATION", font_size=8.5, bold=True, color="BE995B")]}
s11["shape-4"] = {"paragraphs": [add_para("Review", font_size=16.0, bold=True, color="12243D")]}
s11["shape-5"] = {"paragraphs": [add_para("STAGE 2: TESTING", font_size=8.5, bold=True, color="BE995B")]}
s11["shape-6"] = {"paragraphs": [add_para("Exams", font_size=16.0, bold=True, color="12243D")]}
s11["shape-7"] = {"paragraphs": [add_para("STAGE 3: MODERATION", font_size=8.5, bold=True, color="BE995B")]}
s11["shape-8"] = {"paragraphs": [add_para("Marking", font_size=16.0, bold=True, color="12243D")]}
s11["shape-9"] = {"paragraphs": [add_para("STAGE 4: ANALYTICS", font_size=8.5, bold=True, color="BE995B")]}
s11["shape-10"] = {"paragraphs": [add_para("Reports", font_size=16.0, bold=True, color="12243D")]}
s11["shape-11"] = {"paragraphs": [add_para("%", font_size=10.0, color="BE995B")]}
s11["shape-12"] = {"paragraphs": [add_para("%", font_size=10.0, color="BE995B")]}
s11["shape-13"] = {"paragraphs": [add_para("%", font_size=10.0, color="BE995B")]}
s11["shape-14"] = {"paragraphs": [add_para("%", font_size=10.0, color="BE995B")]}
s11["shape-15"] = {"paragraphs": [add_para("KEY PROTOCOLS & TIMELINE", font_size=10.0, bold=True, color="12243D")]}
s11["shape-16"] = {"paragraphs": [add_para("Official Examination Window: 20th–30th of the designated examination month.", font_size=9.5, color="2F3740")]}
s11["shape-17"] = {"paragraphs": [add_para("Standardized Cambridge testing protocols overseen by Cambridge Exam Officer.", font_size=9.5, color="2F3740")]}
s11["shape-18"] = {"paragraphs": [add_para("Individual academic diagnostic dashboards generated with topic-level gap analysis.", font_size=9.5, color="2F3740")]}
s11["shape-19"] = {"paragraphs": [add_para("Parent consultations and personalized academic support plans scheduled post-exam.", font_size=9.5, color="2F3740")]}
s11["shape-20"] = {"paragraphs": [add_para("TARGET INTERNATIONAL SCHOOL   •   PARENT MEETING   •   2026–2027", font_size=7.0, bold=True, color="6F777F")]}
s11["shape-21"] = {"paragraphs": [add_para("12", font_size=9.0, bold=True, color="BE995B", alignment="RIGHT")]}
replacements["slide-11"] = s11

# Slide 12: Olympiads
s12 = {}
s12["shape-0"] = {"paragraphs": [add_para("04 / ASSESSMENT, ACHIEVEMENTS & STUDENT DEVELOPMENT", font_size=9.0, bold=True, color="BE995B")]}
s12["shape-1"] = {"paragraphs": [add_para("Olympiads & Future Academic Opportunities", font_size=25.0, bold=True, color="12243D")]}
s12["shape-2"] = {"paragraphs": [add_para("Empowering students to challenge themselves against top national and international peers.", font_size=11.0, color="6F777F")]}
s12["shape-3"] = {"paragraphs": [add_para("MATHEMATICS OLYMPIADS", font_size=12.0, bold=True, color="12243D")]}
s12["shape-4"] = {"paragraphs": [add_para("SASMO, American Math Competitions (AMC 8/10), and Kangaroo Math with weekly training clubs.", font_size=9.5, color="2F3740")]}
s12["shape-5"] = {"paragraphs": [add_para("SCIENCE & STEM CHALLENGES", font_size=12.0, bold=True, color="12243D")]}
s12["shape-6"] = {"paragraphs": [add_para("International Physics, Chemistry & Biology Olympiads, experimental design fairs, and environmental symposiums.", font_size=9.5, color="2F3740")]}
s12["shape-7"] = {"paragraphs": [add_para("WORLD SCHOLAR'S CUP", font_size=12.0, bold=True, color="12243D")]}
s12["shape-8"] = {"paragraphs": [add_para("Team debate, collaborative essay writing, and multidisciplinary scholar's bowl in regional and global rounds.", font_size=9.5, color="2F3740")]}
s12["shape-9"] = {"paragraphs": [add_para("INNOVATION & AI HACKATHONS", font_size=12.0, bold=True, color="12243D")]}
s12["shape-10"] = {"paragraphs": [add_para("Target Vibecoding hackathons, robotics challenges, and software application showcases building real engineering portfolios.", font_size=9.5, color="2F3740")]}
s12["shape-11"] = {"paragraphs": [add_para("Mentorship Plan: Dedicated after-school coaching squads ensure every registered candidate is thoroughly prepared.", font_size=9.0, color="6F777F")]}
s12["shape-12"] = {"paragraphs": [add_para("TARGET INTERNATIONAL SCHOOL   •   PARENT MEETING   •   2026–2027", font_size=7.0, bold=True, color="6F777F")]}
s12["shape-13"] = {"paragraphs": [add_para("13", font_size=9.0, bold=True, color="BE995B", alignment="RIGHT")]}
replacements["slide-12"] = s12

# Slide 13: School Events
s13 = {}
s13["shape-0"] = {"paragraphs": [add_para("05 / SCHOOL LIFE & STUDENT WELFARE", font_size=9.0, bold=True, color="BE995B")]}
s13["shape-1"] = {"paragraphs": [add_para("School Events & Extracurricular Activities", font_size=25.0, bold=True, color="12243D")]}
s13["shape-2"] = {"paragraphs": [add_para("Nurturing leadership, creativity, team spirit and social responsibility beyond academic lessons.", font_size=11.0, color="6F777F")]}
s13["shape-3"] = {"paragraphs": [add_para("01", font_size=21.0, bold=True, color="BE995B")]}
s13["shape-4"] = {"paragraphs": [add_para("02", font_size=21.0, bold=True, color="BE995B")]}
s13["shape-5"] = {"paragraphs": [add_para("03", font_size=21.0, bold=True, color="BE995B")]}
s13["shape-6"] = {"paragraphs": [add_para("SUCCESSFULLY COMPLETED", font_size=12.0, bold=True, color="12243D")]}
s13["shape-7"] = {"paragraphs": [add_para("WEEKLY CLUBS & SOCIETIES", font_size=12.0, bold=True, color="12243D")]}
s13["shape-8"] = {"paragraphs": [add_para("UPCOMING CELEBRATIONS", font_size=12.0, bold=True, color="12243D")]}
s13["shape-9"] = {"paragraphs": [add_para("Academic Opening Assembly, Teachers' Day Gala, Autumn Sports Tournament, and Quarter 1 Science Fair.", font_size=9.5, color="6F777F")]}
s13["shape-10"] = {"paragraphs": [add_para("Robotics & Vibecoding Studio, MUN, Debate Society, Chess Academy, Drama, and Football & Basketball teams.", font_size=9.5, color="6F777F")]}
s13["shape-11"] = {"paragraphs": [add_para("Winter Gala & Charity Concert, Parent Open Classroom Days, Target Science Fair, and Annual Sports Olympiad.", font_size=9.5, color="6F777F")]}
s13["shape-12"] = {"paragraphs": [add_para("HOLISTIC SKILLS", font_size=9.0, bold=True, color="BE995B")]}
s13["shape-13"] = {"paragraphs": [add_para("Extracurricular participation builds communication, empathy, public speaking and leadership essential for elite universities.", font_size=9.5, color="2F3740")]}
s13["shape-14"] = {"paragraphs": [add_para("TARGET INTERNATIONAL SCHOOL   •   PARENT MEETING   •   2026–2027", font_size=7.0, bold=True, color="6F777F")]}
s13["shape-15"] = {"paragraphs": [add_para("14", font_size=9.0, bold=True, color="BE995B", alignment="RIGHT")]}
replacements["slide-13"] = s13

# Slide 14: Counselling & Guidance
s14 = {}
s14["shape-0"] = {"paragraphs": [add_para("05 / SCHOOL LIFE & STUDENT WELFARE", font_size=9.0, bold=True, color="BE995B")]}
s14["shape-1"] = {"paragraphs": [add_para("Student Counselling & University Guidance", font_size=25.0, bold=True, color="12243D")]}
s14["shape-2"] = {"paragraphs": [add_para("Personalized psychological care, academic mentorship and strategic university admissions roadmaps.", font_size=11.0, color="6F777F")]}
s14["shape-3"] = {"paragraphs": [add_para("FULL-TIME PSYCHOLOGIST", font_size=12.0, bold=True, color="12243D")]}
s14["shape-4"] = {"paragraphs": [add_para("Confidential 1-on-1 counseling, exam anxiety workshops, emotional regulation, and positive study habits coaching.", font_size=9.5, color="2F3740")]}
s14["shape-5"] = {"paragraphs": [add_para("CAREER & UNIVERSITY MAPPING", font_size=12.0, bold=True, color="12243D")]}
s14["shape-6"] = {"paragraphs": [add_para("Personalized university guidance starting from Grade 8: US, UK (UCAS), Europe, Australia, and Asia requirements.", font_size=9.5, color="2F3740")]}
s14["shape-7"] = {"paragraphs": [add_para("TEST TIMELINE PLANNING", font_size=12.0, bold=True, color="12243D")]}
s14["shape-8"] = {"paragraphs": [add_para("Strategic testing roadmap for IELTS, SAT, and A-Levels starting in Grade 10 to prevent burnout and maximize scores.", font_size=9.5, color="2F3740")]}
s14["shape-9"] = {"paragraphs": [add_para("ESSAYS & PORTFOLIO MENTORSHIP", font_size=12.0, bold=True, color="12243D")]}
s14["shape-10"] = {"paragraphs": [add_para("One-on-one personal statement editing, extracurricular resume building, interview practice, and recommendations.", font_size=9.5, color="2F3740")]}
s14["shape-11"] = {"paragraphs": [add_para("Admissions Commitment: We guide every family through university application deadlines, requirements, and scholarship criteria.", font_size=9.0, color="6F777F")]}
s14["shape-12"] = {"paragraphs": [add_para("TARGET INTERNATIONAL SCHOOL   •   PARENT MEETING   •   2026–2027", font_size=7.0, bold=True, color="6F777F")]}
s14["shape-13"] = {"paragraphs": [add_para("15", font_size=9.0, bold=True, color="BE995B", alignment="RIGHT")]}
replacements["slide-14"] = s14

# Slide 15: Nutrition
s15 = {}
s15["shape-0"] = {"paragraphs": [add_para("05 / SCHOOL LIFE & STUDENT WELFARE", font_size=9.0, bold=True, color="BE995B")]}
s15["shape-1"] = {"paragraphs": [add_para("Nutrition & School Food Menu", font_size=25.0, bold=True, color="12243D")]}
s15["shape-2"] = {"paragraphs": [add_para("Wholesome, balanced meals prepared daily under strict hygiene and dietary standards.", font_size=11.0, color="6F777F")]}
s15["shape-3"] = {"paragraphs": [add_para("01", font_size=21.0, bold=True, color="BE995B")]}
s15["shape-4"] = {"paragraphs": [add_para("02", font_size=21.0, bold=True, color="BE995B")]}
s15["shape-5"] = {"paragraphs": [add_para("03", font_size=21.0, bold=True, color="BE995B")]}
s15["shape-6"] = {"paragraphs": [add_para("BREAKFAST (MORNING FOCUS)", font_size=12.0, bold=True, color="12243D")]}
s15["shape-7"] = {"paragraphs": [add_para("LUNCH (BALANCED 3-COURSE)", font_size=12.0, bold=True, color="12243D")]}
s15["shape-8"] = {"paragraphs": [add_para("AFTERNOON SNACK (RECHARGE)", font_size=12.0, bold=True, color="12243D")]}
s15["shape-9"] = {"paragraphs": [add_para("Warm whole-grain porridges, boiled farm eggs, fresh cottage cheese, baked whole-wheat bread, butter, and tea.", font_size=9.5, color="6F777F")]}
s15["shape-10"] = {"paragraphs": [add_para("Nutrient-rich soups, lean meats (beef/poultry/fish), complex carbs (rice, buckwheat, puree), fresh salads, and compote.", font_size=9.5, color="6F777F")]}
s15["shape-11"] = {"paragraphs": [add_para("Seasonal fruits (apples, pears, bananas), light baked pastries, kefir, natural yogurt, and herbal infusions.", font_size=9.5, color="6F777F")]}
s15["shape-12"] = {"paragraphs": [add_para("HYGIENE & DIETARY CARE", font_size=9.0, bold=True, color="BE995B")]}
s15["shape-13"] = {"paragraphs": [add_para("Certified sanitary standards, daily food sample preservation, and individual attention to student allergies and dietary needs.", font_size=9.5, color="2F3740")]}
s15["shape-14"] = {"paragraphs": [add_para("TARGET INTERNATIONAL SCHOOL   •   PARENT MEETING   •   2026–2027", font_size=7.0, bold=True, color="6F777F")]}
s15["shape-15"] = {"paragraphs": [add_para("16", font_size=9.0, bold=True, color="BE995B", alignment="RIGHT")]}
replacements["slide-15"] = s15

# Slide 16: Safety & Uniform
s16 = {}
s16["shape-0"] = {"paragraphs": [add_para("05 / SCHOOL LIFE & STUDENT WELFARE", font_size=9.0, bold=True, color="BE995B")]}
s16["shape-1"] = {"paragraphs": [add_para("Student Safety, Security & School Identity", font_size=25.0, bold=True, color="12243D")]}
s16["shape-2"] = {"paragraphs": [add_para("A secure campus environment, proud dress code and shared standards of mutual respect.", font_size=11.0, color="6F777F")]}
s16["shape-3"] = {"paragraphs": [add_para("01", font_size=21.0, bold=True, color="BE995B")]}
s16["shape-4"] = {"paragraphs": [add_para("02", font_size=21.0, bold=True, color="BE995B")]}
s16["shape-5"] = {"paragraphs": [add_para("03", font_size=21.0, bold=True, color="BE995B")]}
s16["shape-6"] = {"paragraphs": [add_para("CAMPUS SECURITY", font_size=14.0, bold=True, color="FFFFFF")]}
s16["shape-7"] = {"paragraphs": [add_para("Biometric access turnstiles, 24/7 security guard patrol, full HD CCTV coverage, and nurse on duty.", font_size=10.0, color="ECE5D7")]}
s16["shape-8"] = {"paragraphs": [add_para("OFFICIAL UNIFORM", font_size=14.0, bold=True, color="FFFFFF")]}
s16["shape-9"] = {"paragraphs": [add_para("Target navy blazers, formal shirts, tailored trousers/skirts fostering equality and school pride.", font_size=10.0, color="ECE5D7")]}
s16["shape-10"] = {"paragraphs": [add_para("RESPONSIBILITY", font_size=14.0, bold=True, color="FFFFFF")]}
s16["shape-11"] = {"paragraphs": [add_para("Morning line-up at 08:50, phone-free academic lessons, mutual respect, and academic integrity.", font_size=10.0, color="ECE5D7")]}
s16["shape-12"] = {"paragraphs": [add_para("Safe & Respectful Culture: Target International School maintains a disciplined and caring atmosphere.", font_size=13.0, color="DCC497")]}
s16["shape-13"] = {"paragraphs": [add_para("TARGET INTERNATIONAL SCHOOL   •   PARENT MEETING   •   2026–2027", font_size=7.0, bold=True, color="DCC497")]}
s16["shape-14"] = {"paragraphs": [add_para("17", font_size=9.0, bold=True, color="BE995B", alignment="RIGHT")]}
replacements["slide-16"] = s16

# Slide 17: Closing
s17 = {}
s17["shape-0"] = {"paragraphs": [add_para("TARGET INTERNATIONAL SCHOOL", font_size=10.0, bold=True, color="BE995B")]}
s17["shape-1"] = {"paragraphs": [
    add_para("TOGETHER WE BUILD", font_size=32.0, bold=True, color="FFFFFF"),
    add_para("THEIR FUTURE.", font_size=32.0, bold=True, color="FFFFFF")
]}
s17["shape-2"] = {"paragraphs": [add_para("\"Every child has potential. Our responsibility is to recognise it, develop it and prepare every student for a successful future.\"", font_size=15.0, color="DCC497")]}
s17["shape-3"] = {"paragraphs": [add_para("Thank you for your trust, dedication and active partnership with Target International School.", font_size=12.0, color="ECE5D7")]}
s17["shape-4"] = {"paragraphs": [add_para("PARENT MEETING   •   ACADEMIC YEAR 2026–2027   •   Q&A NOW OPEN", font_size=10.0, bold=True, color="BE995B")]}
s17["shape-5"] = {"paragraphs": [add_para("TARGET INTERNATIONAL SCHOOL   •   PARENT MEETING   •   2026–2027", font_size=7.0, bold=True, color="DCC497")]}
s17["shape-6"] = {"paragraphs": [add_para("18", font_size=9.0, bold=True, color="BE995B", alignment="RIGHT")]}
replacements["slide-17"] = s17

with open('/home/dpdp/target/parents_meeting/replacement-text.json', 'w') as f:
    json.dump(replacements, f, indent=2)

print('Updated replacement-text.json with zero overflow risk!')
