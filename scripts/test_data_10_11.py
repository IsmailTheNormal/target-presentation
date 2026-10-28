#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Target International School — Grades 10–11 Vibecoding Test Data (English Only)
Subject: Vibecoding (AI Tools, Web Foundations, Prompt Engineering & Security)
Instructor: Ismoiljon Usmonov · Yunusobod Campus

Structure:
- 25 easy, clear, accessible, and student-friendly questions in simple English.
- Covers the core curriculum lessons: Vibecoding, Prompts, Web basics (HTML/CSS/JS),
  Frontend & Backend, APIs, JSON, LocalStorage, .env secrets, Git, AI concepts (Context,
  Temperature, System Prompt, Tool Calling, Hallucinations, RAG, Prompt Injection),
  HTTPS, and Deploying.
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
        {"grade": "Excellent (5)", "range": "22 – 25 pts", "desc": "Great understanding of AI prompting, web basics, APIs, and online safety"},
        {"grade": "Good (4)", "range": "18 – 21 pts", "desc": "Good grasp of web development and core AI concepts"},
        {"grade": "Satisfactory (3)", "range": "13 – 17 pts", "desc": "Understands basics; needs to review APIs, LocalStorage, and prompts"},
        {"grade": "Unsatisfactory (2)", "range": "0 – 12 pts", "desc": "Foundational review of Vibecoding and web basics required"}
    ]
}

QUESTIONS_10_11_EN = [
    # 1
    {
        "text": "What does 'Vibecoding' mean in modern software development?",
        "a": "Playing computer video games instead of coding.",
        "b": "Using AI assistants to help you build and write code faster while you plan and test the project.",
        "c": "Writing all computer code on paper without using a computer.",
        "d": "Turning off your computer monitor while coding.",
        "e": "Deleting all your project files every single evening.",
        "correct": "B",
        "topic": "01: What is Vibecoding",
        "expl": "Vibecoding means building software with the help of AI assistants while you design the logic and test the results."
    },
    # 2
    {
        "text": "What is a 'Prompt' when working with AI tools like ChatGPT or Claude?",
        "a": "A dangerous virus that deletes files from your hard drive.",
        "b": "The written question, instruction, or task that you type into the AI.",
        "c": "The power cord connected to your laptop.",
        "d": "A special key on the keyboard that deletes the operating system.",
        "e": "The name of a computer brand.",
        "correct": "B",
        "topic": "02: What is a Prompt",
        "expl": "A prompt is the instruction or question you provide to the AI model to get an answer or code."
    },
    # 3
    {
        "text": "How can you get the best and most accurate code from an AI assistant?",
        "a": "Just type a single vague word like 'website'.",
        "b": "Give clear instructions, explain what features you want, and specify the programming language.",
        "c": "Send only smiling emojis without any words.",
        "d": "Ask the AI to guess what you want without giving any details.",
        "e": "Turn off your internet connection while asking.",
        "correct": "B",
        "topic": "03: Writing Good Prompts",
        "expl": "Clear prompts that describe the goal, features, and tech stack give the most reliable code."
    },
    # 4
    {
        "text": "In web development, what is HTML used for?",
        "a": "Styling colors, fonts, and background animations.",
        "b": "Creating the basic structure and content of a web page (headings, text, buttons, images).",
        "c": "Playing sound through the computer speakers.",
        "d": "Charging the laptop battery.",
        "e": "Connecting a mouse via Bluetooth.",
        "correct": "B",
        "topic": "04: HTML Basics",
        "expl": "HTML provides the skeleton and structural content (text, images, links, forms) of any webpage."
    },
    # 5
    {
        "text": "In web development, what is CSS used for?",
        "a": "Writing database queries to store passwords.",
        "b": "Styling the web page with colors, fonts, spacing, and responsive layouts.",
        "c": "Connecting the computer to a printer.",
        "d": "Calculating complex mathematical formulas.",
        "e": "Measuring the room temperature.",
        "correct": "B",
        "topic": "05: CSS Basics",
        "expl": "CSS controls the visual presentation, styling, colors, and layout of a website."
    },
    # 6
    {
        "text": "In web development, what is JavaScript used for?",
        "a": "Printing text onto physical paper sheets.",
        "b": "Making the web page interactive, responding to clicks, and handling logic and animations.",
        "c": "Cleaning dust off the laptop keyboard.",
        "d": "Changing the electrical voltage of the wall plug.",
        "e": "Drawing images with a pen on paper.",
        "correct": "B",
        "topic": "06: JavaScript Basics",
        "expl": "JavaScript brings web pages to life by handling user interactions, animations, and dynamic logic."
    },
    # 7
    {
        "text": "What is the 'Frontend' of a website?",
        "a": "The hidden server computer stored in another country.",
        "b": "The visual user interface that people see and interact with in their web browser.",
        "c": "The power supply cable inside the computer case.",
        "d": "The database containing thousands of user passwords.",
        "e": "The internet provider's office building.",
        "correct": "B",
        "topic": "07: Frontend Definition",
        "expl": "Frontend refers to the client side — the user interface and visual design that users interact with directly."
    },
    # 8
    {
        "text": "What is the 'Backend' of a web application?",
        "a": "The computer monitor sitting on your desk.",
        "b": "The server-side code and database that handle business logic, data storage, and authentication behind the scenes.",
        "c": "The background image set in your CSS stylesheet.",
        "d": "The computer mouse and trackpad.",
        "e": "A video player on YouTube.",
        "correct": "B",
        "topic": "08: Backend Definition",
        "expl": "Backend refers to the server side that processes business logic, manages databases, and handles security."
    },
    # 9
    {
        "text": "What is an API (Application Programming Interface) used for?",
        "a": "To turn off the computer when you go to sleep.",
        "b": "To allow two different software applications or servers to communicate and exchange data with each other.",
        "c": "To clean up physical dust from the screen.",
        "d": "To make your laptop battery last forever.",
        "e": "To turn on the room light switch.",
        "correct": "B",
        "topic": "09: What is an API",
        "expl": "An API is a bridge that allows different apps to communicate, such as fetching weather data from a remote server."
    },
    # 10
    {
        "text": "What is JSON (JavaScript Object Notation)?",
        "a": "A brand of computer monitors.",
        "b": "A lightweight and easy-to-read text format for sending and sharing structured data between computers.",
        "c": "A high-speed internet cable.",
        "d": "An antivirus software program.",
        "e": "A video game controller.",
        "correct": "B",
        "topic": "10: What is JSON",
        "expl": "JSON is a standard text-based format for representing structured data (key-value pairs) between client and server."
    },
    # 11
    {
        "text": "What does the HTTP status code '404' mean when you open a link?",
        "a": "The page loaded successfully without errors.",
        "b": "The requested web page or file was Not Found on the server.",
        "c": "Your computer has run out of battery.",
        "d": "Your password was accepted.",
        "e": "The internet was permanently deleted.",
        "correct": "B",
        "topic": "11: HTTP Status Code 404",
        "expl": "Status code 404 Not Found indicates that the server could not find the requested webpage or file."
    },
    # 12
    {
        "text": "In REST APIs, what is the HTTP 'GET' method used for?",
        "a": "Deleting all files from the server.",
        "b": "Requesting and reading data from a server without modifying it.",
        "c": "Shutting down the server completely.",
        "d": "Changing the administrator's password.",
        "e": "Formatting the hard drive.",
        "correct": "B",
        "topic": "12: HTTP GET Method",
        "expl": "GET requests are used to retrieve information from a server safely without altering server state."
    },
    # 13
    {
        "text": "In REST APIs, what is the HTTP 'POST' method used for?",
        "a": "Closing the browser window.",
        "b": "Sending new data to the server (for example, creating a new user or submitting a form).",
        "c": "Turning off the laptop Wi-Fi.",
        "d": "Reading an article on Wikipedia.",
        "e": "Changing the screen brightness.",
        "correct": "B",
        "topic": "13: HTTP POST Method",
        "expl": "POST requests send new data to the server, typically used when creating new accounts or submitting form data."
    },
    # 14
    {
        "text": "Where does the browser save data when you use 'localStorage' in JavaScript?",
        "a": "On a physical USB drive plugged into the wall.",
        "b": "Directly inside the user's browser, so data remains saved even if you refresh or close the tab.",
        "c": "In an email sent to your teacher.",
        "d": "On a printed sheet of paper.",
        "e": "On an orbiting satellite.",
        "correct": "B",
        "topic": "14: LocalStorage in Browser",
        "expl": "LocalStorage stores key-value pairs in the user's browser disk, preserving settings and scores across refreshes."
    },
    # 15
    {
        "text": "Why should private API keys and passwords be kept in a '.env' file instead of written openly in public code?",
        "a": "Because code cannot run if it contains letters.",
        "b": "To protect your secret keys so strangers on the internet cannot steal them or misuse your account.",
        "c": "Because '.env' files make websites load 100 times faster.",
        "d": "Because public repositories delete all passwords automatically.",
        "e": "Because computers can only read '.env' files.",
        "correct": "B",
        "topic": "15: Keeping Secrets in .env",
        "expl": "Private keys must be stored in .env and ignored by Git to prevent hackers from stealing them on public repositories."
    },
    # 16
    {
        "text": "Why do software developers use Git and GitHub?",
        "a": "To watch streaming movies for free.",
        "b": "To track changes in their code, save project history, and collaborate smoothly with team members.",
        "c": "To buy physical computer parts online.",
        "d": "To charge their smartphone batteries.",
        "e": "To clean the desktop background image.",
        "correct": "B",
        "topic": "16: Git and GitHub Basics",
        "expl": "Git tracks code revisions over time, and GitHub hosts repositories online so teams can collaborate and review code."
    },
    # 17
    {
        "text": "What does an AI's 'Context Window' mean?",
        "a": "The physical glass window in your computer room.",
        "b": "The maximum amount of text and conversation history that the AI can remember and process at one time.",
        "c": "The time of day when you are allowed to use the internet.",
        "d": "The size of your computer monitor in centimeters.",
        "e": "The number of browser tabs currently open.",
        "correct": "B",
        "topic": "17: AI Context Window",
        "expl": "The context window is the memory limit of the AI model during a single prompt and response interaction."
    },
    # 18
    {
        "text": "What happens when you set the AI Temperature setting to 0 (zero)?",
        "a": "The computer gets cold and freezes.",
        "b": "The AI becomes very focused, predictable, and gives consistent, repeatable answers.",
        "c": "The AI starts telling random funny stories.",
        "d": "The AI deletes your project code.",
        "e": "The AI refuses to speak English.",
        "correct": "B",
        "topic": "18: AI Temperature 0",
        "expl": "Temperature 0 produces deterministic outputs, making the model choose the most likely words each time."
    },
    # 19
    {
        "text": "What is a 'System Prompt' in an AI chatbot?",
        "a": "A message shown when Windows crashes.",
        "b": "The background instructions that tell the AI its role, persona, and rules of behavior.",
        "c": "A sound played when turning on the laptop.",
        "d": "An advertisement shown in a web browser.",
        "e": "A command to delete all files on the hard drive.",
        "correct": "B",
        "topic": "19: System Prompt Role",
        "expl": "The System Prompt sets the baseline instructions, telling the AI how to act, what rules to follow, and what tone to use."
    },
    # 20
    {
        "text": "What does 'Tool Calling' allow modern AI models to do?",
        "a": "Call a friend's mobile phone number.",
        "b": "Use external tools (like a calculator, web search, or database) to get real data and perform actions.",
        "c": "Repair broken hardware with a screwdriver.",
        "d": "Increase the physical RAM of the computer.",
        "e": "Change the room temperature.",
        "correct": "B",
        "topic": "20: AI Tool Calling",
        "expl": "Tool calling allows AI models to run external functions (like searching the web or querying a database) to get accurate facts."
    },
    # 21
    {
        "text": "What is an AI 'Hallucination'?",
        "a": "When the computer monitor turns purple.",
        "b": "When an AI makes up incorrect or fake facts while sounding completely confident.",
        "c": "When the laptop battery runs out.",
        "d": "When the Wi-Fi connection is slow.",
        "e": "When the user forgets their password.",
        "correct": "B",
        "topic": "21: AI Hallucinations",
        "expl": "Hallucination is when an AI generates false or unverified facts that look convincing but are actually untrue."
    },
    # 22
    {
        "text": "How does RAG (Retrieval-Augmented Generation) help an AI give truthful answers?",
        "a": "By replacing the computer processor with a faster chip.",
        "b": "By finding real, verified documents first and giving them to the AI to read before it answers.",
        "c": "By turning off the AI model completely.",
        "d": "By deleting all old documents from your computer.",
        "e": "By making the website text change colors.",
        "correct": "B",
        "topic": "22: RAG and Factual Answers",
        "expl": "RAG retrieves relevant facts from real documents and gives them to the AI as context, preventing made-up answers."
    },
    # 23
    {
        "text": "What is a 'Prompt Injection' attack?",
        "a": "Injecting liquid into the computer keyboard.",
        "b": "When a malicious user types a tricky prompt to make the AI ignore its safety rules and reveal secrets.",
        "c": "A needle used to fix broken microchips.",
        "d": "A software update for your computer mouse.",
        "e": "A cable used to charge phones.",
        "correct": "B",
        "topic": "23: Prompt Injection Attack",
        "expl": "Prompt injection is when someone inputs deceptive text to bypass the AI's safety guardrails or steal private data."
    },
    # 24
    {
        "text": "Why should websites use 'HTTPS' with a secure padlock icon?",
        "a": "Because HTTPS makes photos load in black and white.",
        "b": "Because HTTPS encrypts the connection so hackers cannot spy on passwords and private data.",
        "c": "Because websites cannot show text without HTTPS.",
        "d": "Because HTTPS costs $1000 per minute to use.",
        "e": "Because HTTP is only for video games.",
        "correct": "B",
        "topic": "24: HTTPS and Encryption",
        "expl": "HTTPS encrypts data between the browser and the server, protecting passwords and sensitive info from interception."
    },
    # 25
    {
        "text": "What does 'Deploying' your website (for example on Vercel or GitHub Pages) mean?",
        "a": "Deleting the website files from your computer.",
        "b": "Publishing your website on the internet so anyone in the world can visit it using a link.",
        "c": "Printing your code on a paper printer.",
        "d": "Hiding your website so nobody can ever see it.",
        "e": "Turning off your Wi-Fi router permanently.",
        "correct": "B",
        "topic": "25: Deploying Websites Online",
        "expl": "Deploying means hosting and publishing your project online, giving it a live URL that anyone can access."
    }
]

print("Grade 10-11 Vibecoding test data loaded (Super Easy & Clear English). Instructor: Ismoiljon Usmonov.")
