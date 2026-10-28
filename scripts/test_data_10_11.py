#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Target International School — Grades 10–11 Vibecoding Test Data (English Only)
Subject: Vibecoding (General Computing, AI Tools, Web Basics & Digital Literacy)
Instructor: Ismoiljon Usmonov · Yunusobod Campus

Structure:
- 25 general, student-friendly, and accessible questions in clear everyday English.
- Broad non-specific foundations: What is AI, Software vs Hardware, The Internet,
  Web Browsers, Search Engines, AI Chatbots, Prompts, Clear Communication with AI,
  Vibecoding, Websites, HTML, CSS, JavaScript, Bugs & Debugging, Strong Passwords,
  Account Safety, Cloud Storage, Malware & Viruses, Wi-Fi, Handling AI Errors,
  Safe Websites (HTTPS), Operating Systems, and Testing Software.
"""

META_10_11_EN = {
    "school_name": "TARGET INTERNATIONAL SCHOOL — YUNUSOBOD",
    "exam_title": "GRADES 10–11: VIBECODING, WEB BASICS & ARTIFICIAL INTELLIGENCE",
    "track_title": "Vibecoding & AI Systems Track · Instructor: Ismoiljon Usmonov",
    "academic_year": "Academic Year 2026–2027",
    "label_name": "Student Full Name",
    "label_class": "Grade / Section",
    "label_date": "Date",
    "label_variant": "Variant",
    "variant_val": "Variant 1 (Official)",
    "label_max_score": "Maximum Score",
    "unit_points": "pts",
    "label_score": "Final Score",
    "instructions": "Instructions: For each question, choose and mark exactly ONE correct answer from the 5 options (A, B, C, D, E). Each correct answer is awarded 1 point (Total: 25 points)."
}

KEYS_META_10_11_EN = {
    "heading": "OFFICIAL ANSWER KEY & 25-POINT GRADING RUBRIC",
    "subheading": "Instructor: Ismoiljon Usmonov · Grades 10–11 Vibecoding Official Key (25 Questions)",
    "table_headers": ["№", "Key", "Topic / Lesson", "Explanation"],
    "scale_heading": "Official 25-Point Grading Rubric:",
    "rubric_tiers": [
        {"grade": "Excellent (5)", "range": "22 – 25 pts", "desc": "Great general knowledge of AI, computing, web foundations, and online safety"},
        {"grade": "Good (4)", "range": "18 – 21 pts", "desc": "Good grasp of everyday technology, web basics, and AI prompts"},
        {"grade": "Satisfactory (3)", "range": "13 – 17 pts", "desc": "Understands general basics; needs to review web roles and computing safety"},
        {"grade": "Unsatisfactory (2)", "range": "0 – 12 pts", "desc": "Foundational review of general computing and Vibecoding required"}
    ]
}

QUESTIONS_10_11_EN = [
    # 1
    {
        "text": "What does the abbreviation 'AI' stand for in technology?",
        "a": "Artificial Intelligence",
        "b": "Automatic Internet",
        "c": "Advanced Illustration",
        "d": "Apple Information",
        "e": "Audio Interface",
        "correct": "A",
        "topic": "01: What AI Means",
        "expl": "AI stands for Artificial Intelligence, which refers to computer systems designed to perform tasks that typically require human intelligence."
    },
    # 2
    {
        "text": "What is computer software?",
        "a": "The physical keyboard and mouse you touch with your hands",
        "b": "The metal case and wires inside a desktop computer",
        "c": "Programs and applications that instruct a computer on what tasks to perform",
        "d": "The glass screen of a smartphone",
        "e": "The power cable plugged into an electrical outlet",
        "correct": "C",
        "topic": "02: Computer Software",
        "expl": "Software consists of programs, apps, and operating systems that tell computer hardware what to do."
    },
    # 3
    {
        "text": "Which of the following is an example of computer HARDWARE?",
        "a": "A physical computer monitor (screen)",
        "b": "The Google Chrome web browser",
        "c": "The Windows operating system",
        "d": "A mobile video game app",
        "e": "A PDF document file",
        "correct": "A",
        "topic": "03: Hardware vs Software",
        "expl": "Hardware is the physical machinery you can see and touch, such as monitors, keyboards, mice, and memory chips."
    },
    # 4
    {
        "text": "What is the Internet?",
        "a": "A single supercomputer located in one school",
        "b": "A global network connecting millions of computers worldwide to share data and information",
        "c": "A brand of laptop chargers",
        "d": "A physical television antenna",
        "e": "A single software file stored on your desktop",
        "correct": "B",
        "topic": "04: What is the Internet",
        "expl": "The Internet is a vast worldwide network of interconnected computer networks."
    },
    # 5
    {
        "text": "What is a web browser (such as Google Chrome, Apple Safari, or Mozilla Firefox)?",
        "a": "An application used to open, view, and navigate websites on the internet",
        "b": "A tool used to wipe physical dust off computer screens",
        "c": "A special cable that connects your laptop to a printer",
        "d": "A camera sensor built into a mobile phone",
        "e": "A battery that supplies electricity to the keyboard",
        "correct": "A",
        "topic": "05: Web Browsers",
        "expl": "A web browser is software designed to retrieve, format, and display webpages from the World Wide Web."
    },
    # 6
    {
        "text": "What is a search engine (such as Google or Bing)?",
        "a": "A website that helps users search for and discover information across the internet",
        "b": "The physical engine inside an electric car",
        "c": "A cooling fan mounted inside a computer case",
        "d": "An application that only plays music without an internet connection",
        "e": "A button on the keyboard that powers off the laptop",
        "correct": "A",
        "topic": "06: Search Engines",
        "expl": "Search engines index the internet and return relevant websites when you enter keywords or questions."
    },
    # 7
    {
        "text": "What is an AI chatbot (such as ChatGPT or Claude)?",
        "a": "A mechanical robot that vacuums your living room floor",
        "b": "An AI-powered computer program capable of having conversations and answering questions",
        "c": "A physical pair of audio headphones",
        "d": "A television remote control",
        "e": "A dangerous computer virus that erases documents",
        "correct": "B",
        "topic": "07: AI Chatbots",
        "expl": "AI chatbots are software applications trained on language models to chat, answer questions, and assist users."
    },
    # 8
    {
        "text": "When chatting with an AI assistant, what is a 'Prompt'?",
        "a": "The message, question, or instruction that you type into the AI",
        "b": "A broken button on your computer keyboard",
        "c": "The sound made by the laptop cooling fan",
        "d": "The secret Wi-Fi password for your home network",
        "e": "The battery percentage shown on your smartphone",
        "correct": "A",
        "topic": "08: What is a Prompt",
        "expl": "A prompt is any text prompt, query, or instruction submitted to an AI model to elicit a response."
    },
    # 9
    {
        "text": "How can you get the most helpful and accurate response from an AI assistant?",
        "a": "By providing clear instructions and enough specific details about what you need",
        "b": "By typing only a single random word and waiting for the AI to guess",
        "c": "By disconnecting your computer from the internet before asking",
        "d": "By sending only random emojis without any explanation",
        "e": "By sitting in complete silence without typing any words",
        "correct": "A",
        "topic": "09: Clear Communication with AI",
        "expl": "Clear and detailed prompts allow the AI to understand your exact context and generate relevant answers."
    },
    # 10
    {
        "text": "What does 'Vibecoding' mean in modern technology?",
        "a": "Building websites and software projects with the assistance of AI tools",
        "b": "Listening to loud music on headphones without touching a computer",
        "c": "Playing computer games all day without doing school work",
        "d": "Printing out lines of computer code on sheets of paper",
        "e": "Turning off your laptop screen while studying in the library",
        "correct": "A",
        "topic": "10: What is Vibecoding",
        "expl": "Vibecoding describes the modern workflow of creating applications by collaborating with AI coding assistants."
    },
    # 11
    {
        "text": "What is a website?",
        "a": "A physical paper book stored on a library bookshelf",
        "b": "A collection of related web pages on the internet containing text, images, and links",
        "c": "A protective plastic case for a smartphone",
        "d": "A small silicon memory chip inside a calculator",
        "e": "An ink cartridge used inside a paper printer",
        "correct": "B",
        "topic": "11: What is a Website",
        "expl": "A website is a collection of interconnected web pages hosted on web servers and identified by a domain name."
    },
    # 12
    {
        "text": "When creating a web page, what is HTML primarily used for?",
        "a": "Building the basic structure and adding content like headings, paragraphs, and images",
        "b": "Changing the physical color of your laptop keyboard",
        "c": "Connecting a computer mouse using Bluetooth",
        "d": "Increasing the sound volume of the laptop speakers",
        "e": "Cooling down the computer processor during heavy use",
        "correct": "A",
        "topic": "12: Role of HTML",
        "expl": "HTML provides the skeleton and structural elements (text, images, links) of every web page."
    },
    # 13
    {
        "text": "When creating a web page, what is CSS primarily used for?",
        "a": "Styling the web page with colors, fonts, spacing, and attractive visual layouts",
        "b": "Saving text files onto a physical USB flash drive",
        "c": "Wiping dust away from computer keys",
        "d": "Installing antivirus protection against viruses",
        "e": "Turning on the electrical power button of the monitor",
        "correct": "A",
        "topic": "13: Role of CSS",
        "expl": "CSS controls the presentation, visual styling, colors, and layout of HTML documents."
    },
    # 14
    {
        "text": "When creating a web page, what is JavaScript primarily used for?",
        "a": "Making the web page interactive, such as responding to button clicks and user actions",
        "b": "Writing essays inside Microsoft Word",
        "c": "Recharging the laptop's lithium battery",
        "d": "Adjusting the height of your computer desk",
        "e": "Plugging a display cable into the wall socket",
        "correct": "A",
        "topic": "14: Role of JavaScript",
        "expl": "JavaScript enables dynamic interactivity, animations, and responsive user actions on web pages."
    },
    # 15
    {
        "text": "In computer programming, what is a 'Bug'?",
        "a": "An actual living insect crawling inside the computer",
        "b": "A mistake or error in code that prevents a program from working correctly",
        "c": "A newly purchased computer mouse",
        "d": "A high-speed internet cable",
        "e": "A keyboard shortcut used to print a document",
        "correct": "B",
        "topic": "15: What is a Bug",
        "expl": "A software bug is an error, flaw, or fault in a computer program that produces incorrect or unexpected results."
    },
    # 16
    {
        "text": "What does 'Debugging' mean in software development?",
        "a": "Finding, investigating, and fixing errors or mistakes in program code",
        "b": "Purchasing a brand-new laptop at an electronics store",
        "c": "Washing a computer keyboard with soapy water",
        "d": "Erasing the computer's entire operating system",
        "e": "Updating your personal profile picture on social media",
        "correct": "A",
        "topic": "16: What is Debugging",
        "expl": "Debugging is the routine process of identifying, isolating, and resolving defects in computer software."
    },
    # 17
    {
        "text": "Which of the following is the best example of a strong, secure password?",
        "a": "123456",
        "b": "password",
        "c": "TrG#98!mKx$2",
        "d": "qwerty",
        "e": "1111",
        "correct": "C",
        "topic": "17: What is a Strong Password",
        "expl": "A strong password combines uppercase and lowercase letters, numbers, and special symbols, making it hard to guess."
    },
    # 18
    {
        "text": "Why should you NEVER share your private account passwords with strangers?",
        "a": "Because your laptop screen will immediately shut down",
        "b": "To protect your personal data and prevent unauthorized people from accessing your accounts",
        "c": "Because passwords stop working if someone else speaks them aloud",
        "d": "Because your home internet connection speed will immediately drop to zero",
        "e": "Because the computer screen brightness will become very dark",
        "correct": "B",
        "topic": "18: Account Security",
        "expl": "Keeping passwords confidential prevents identity theft, data breaches, and unauthorized account access."
    },
    # 19
    {
        "text": "What is Cloud Storage (such as Google Drive, OneDrive, or iCloud)?",
        "a": "Saving files on secure internet servers so you can access them from any computer or phone",
        "b": "Keeping printed paper documents inside a plastic school folder",
        "c": "Placing a computer hard drive inside a refrigerator",
        "d": "Saving music files only onto a plastic CD disk",
        "e": "Writing notes with chalk on a classroom blackboard",
        "correct": "A",
        "topic": "19: Cloud Storage",
        "expl": "Cloud storage allows data to be maintained, managed, and backed up remotely over the internet."
    },
    # 20
    {
        "text": "What is computer malware or a virus?",
        "a": "Harmful software created to damage computers, disrupt systems, or steal personal data",
        "b": "A physical scratch on a laptop computer screen",
        "c": "A free utility tool that cleans your keyboard",
        "d": "An official update released by the operating system",
        "e": "An application that helps you organize your school homework",
        "correct": "A",
        "topic": "20: Computer Viruses and Malware",
        "expl": "Malware is malicious software designed to compromise, harm, or exploit computer devices and networks."
    },
    # 21
    {
        "text": "What is Wi-Fi used for in everyday life?",
        "a": "Connecting computers, phones, and devices to the internet wirelessly without cables",
        "b": "Physically making a laptop computer screen wider",
        "c": "Printing color photographs on paper with ink",
        "d": "Cooling down the computer's internal battery",
        "e": "Transmitting electric power across rooms without batteries",
        "correct": "A",
        "topic": "21: What is Wi-Fi",
        "expl": "Wi-Fi is a wireless networking technology that allows devices to connect to local networks and the internet."
    },
    # 22
    {
        "text": "What is the best action to take if an AI assistant generates code that contains an error?",
        "a": "Throw the computer away and buy a new one",
        "b": "Read the error message, test what failed, and ask the AI to fix that specific mistake",
        "c": "Stop using computers and smartphones forever",
        "d": "Pretend the program is working and ignore the error completely",
        "e": "Delete your web browser and internet connection",
        "correct": "B",
        "topic": "22: Dealing with AI Mistakes",
        "expl": "When code has errors, reading the error message and prompting the AI with the error details helps resolve the bug."
    },
    # 23
    {
        "text": "When browsing the web, what does a lock icon (HTTPS) in the browser address bar indicate?",
        "a": "The connection between your browser and the website is encrypted and secure",
        "b": "The website is locked and visitors are forbidden from opening it",
        "c": "Your computer has completely run out of hard drive storage",
        "d": "Visitors must pay cash before viewing the webpage",
        "e": "The website creator has turned off their personal computer",
        "correct": "A",
        "topic": "23: Safe Websites (HTTPS)",
        "expl": "The lock icon indicates an HTTPS connection that encrypts communication between the browser and web server."
    },
    # 24
    {
        "text": "What is an Operating System (such as Microsoft Windows, Apple macOS, or Linux)?",
        "a": "The core software that manages computer hardware resources and allows applications to run",
        "b": "A website used exclusively for streaming funny videos",
        "c": "A physical wooden desk designed for holding computers",
        "d": "An electric cable that connects a laptop charger to the wall",
        "e": "A quick antivirus scan that runs once every year",
        "correct": "A",
        "topic": "24: Operating Systems",
        "expl": "An operating system is the fundamental system software that manages hardware, files, and running applications."
    },
    # 25
    {
        "text": "Why is it important to test your website or application before sharing it with users?",
        "a": "To ensure all buttons, links, and features work properly without confusing errors",
        "b": "Because computers only run software that has never been tested",
        "c": "To deliberately make the project file size ten times bigger",
        "d": "To change the physical color of your computer mouse",
        "e": "Because testing automatically deletes the entire website forever",
        "correct": "A",
        "topic": "25: Software Testing",
        "expl": "Testing verifies functionality, discovers hidden bugs, and ensures a smooth, working experience for end users."
    }
]

print("Grade 10-11 Vibecoding test data loaded (General, Non-Specific & Student-Friendly English). Instructor: Ismoiljon Usmonov.")
