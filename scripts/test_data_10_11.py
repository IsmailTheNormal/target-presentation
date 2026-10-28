#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Target International School — Grades 10–11 Vibecoding Test Data (English Only)
Subject: Vibecoding (AI Engineering, Web Development, Prompt Systems & Security)
Instructor: Ismoiljon Usmonov · Yunusobod Campus

Structure:
- 25 well-balanced, high-school accessible questions in clear, professional English.
- Rigorous yet accessible Vibecoding curriculum:
  * Vibecoding Philosophy & Workflow
  * Prompt Engineering: System Prompts, Few-Shot, Chain-of-Thought
  * LLM Mechanics: Hallucinations, Temperature, Context Window, RAG
  * Web Foundations: HTML Structure, CSS Flexbox, JavaScript DOM Events, DevTools Console
  * Data & APIs: REST APIs, JSON Format, Asynchronous fetch(), DevTools Network (404)
  * State & Storage: Browser LocalStorage
  * Full-Stack & Architecture: Frontend vs Backend
  * Developer Tooling: Git Version Control, Web Deployment (Vercel)
  * Security & Secrets: .env Private Keys, HTTPS Encryption, Prompt Injection
"""

META_10_11_EN = {
    "school_name": "TARGET INTERNATIONAL SCHOOL — YUNUSOBOD",
    "exam_title": "GRADES 10–11: VIBECODING, WEB ARCHITECTURE & ARTIFICIAL INTELLIGENCE",
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
        {"grade": "Excellent (5)", "range": "22 – 25 pts", "desc": "Outstanding grasp of Vibecoding workflow, prompt systems, web architecture, and AI security"},
        {"grade": "Good (4)", "range": "18 – 21 pts", "desc": "Solid understanding of web development, AI prompting, and core developer tools"},
        {"grade": "Satisfactory (3)", "range": "13 – 17 pts", "desc": "Understands basics; needs further practice with APIs, prompt techniques, and async flow"},
        {"grade": "Unsatisfactory (2)", "range": "0 – 12 pts", "desc": "Foundational review of Vibecoding principles and web concepts required"}
    ]
}

QUESTIONS_10_11_EN = [
    # 1
    {
        "text": "In modern software engineering, what is the core philosophy of 'Vibecoding'?",
        "a": "Relying 100% on AI without ever testing or running the code.",
        "b": "Writing all code in binary machine language by hand.",
        "c": "Guiding and directing AI assistants to generate code while the human developer plans the architecture, logic, and tests.",
        "d": "Copying outdated code snippets from old printed textbooks.",
        "e": "Disabling all internet access while building a website.",
        "correct": "C",
        "topic": "01: Vibecoding Philosophy",
        "expl": "Vibecoding empowers developers to direct AI models to write code while maintaining human architectural vision and testing."
    },
    # 2
    {
        "text": "Which component of an AI prompt establishes the model's persona, rules, and behavioral boundaries?",
        "a": "The Wi-Fi configuration script",
        "b": "The System Prompt (or system instruction)",
        "c": "The computer's BIOS settings",
        "d": "The CSS style sheet",
        "e": "The HDMI display driver",
        "correct": "B",
        "topic": "02: System Prompts",
        "expl": "The System Prompt defines the AI's role, behavioral guidelines, constraints, and operational context."
    },
    # 3
    {
        "text": "What is 'Few-Shot Prompting' when instructing an AI model?",
        "a": "Providing the AI with 1 to 3 clear examples of expected input-output pairs before asking it to solve a new task.",
        "b": "Asking the AI only three words in total.",
        "c": "Restarting the computer three times before submitting a prompt.",
        "d": "Sending three identical prompts simultaneously to crash the server.",
        "e": "Running code on three separate monitors at the same time.",
        "correct": "A",
        "topic": "03: Few-Shot Prompting",
        "expl": "Few-shot prompting provides concrete input-output examples so the AI can recognize patterns and format responses accurately."
    },
    # 4
    {
        "text": "What is meant by an AI 'Hallucination'?",
        "a": "When the computer monitor displays random colors due to a broken cable.",
        "b": "When an AI model generates factually incorrect or non-existent code libraries with high confidence.",
        "c": "When the computer's CPU temperature drops below zero degrees.",
        "d": "When the battery of a laptop drains faster than expected.",
        "e": "When a web browser opens two tabs instead of one.",
        "correct": "B",
        "topic": "04: AI Hallucinations",
        "expl": "AI hallucination refers to plausible-sounding but factually wrong outputs, such as inventing functions or fake API endpoints."
    },
    # 5
    {
        "text": "When adjusting the 'Temperature' parameter of a Large Language Model (LLM), what is the effect of setting it to 0.0?",
        "a": "The AI model completely shuts down and stops answering.",
        "b": "The model becomes highly creative, unpredictable, and writes fictional stories.",
        "c": "The outputs become focused, deterministic, and repeatable for the same prompt.",
        "d": "The speed of your home Wi-Fi connection increases.",
        "e": "The model automatically deletes your codebase.",
        "correct": "C",
        "topic": "05: LLM Temperature",
        "expl": "Low temperature (near 0) produces deterministic and predictable outputs, ideal for structured code generation."
    },
    # 6
    {
        "text": "What does the 'Context Window' of an AI model refer to?",
        "a": "The physical glass window in a computer laboratory.",
        "b": "The maximum number of tokens (words/characters) the model can read and remember in a single session.",
        "c": "The operating system's desktop background wallpaper.",
        "d": "The dimensions of the browser window in pixels.",
        "e": "The amount of free space remaining on a hard drive.",
        "correct": "B",
        "topic": "06: Context Window",
        "expl": "The context window represents the memory limit of an AI model for input prompts and generated responses."
    },
    # 7
    {
        "text": "In web development, what role does HTML play in creating a web application?",
        "a": "It defines the foundational structure and semantic content (headings, paragraphs, buttons, forms).",
        "b": "It connects the computer directly to a database server.",
        "c": "It styles the page with shadows, gradients, and animations.",
        "d": "It executes server-side background tasks and handles cryptography.",
        "e": "It compiles JavaScript code into binary machine code.",
        "correct": "A",
        "topic": "07: HTML Structure",
        "expl": "HTML provides the structural skeleton and DOM elements of a webpage."
    },
    # 8
    {
        "text": "Which CSS property is commonly used to easily center and distribute child elements horizontally and vertically?",
        "a": "display: flex (with justify-content and align-items)",
        "b": "text-decoration: underline",
        "c": "color: transparent",
        "d": "font-weight: bold",
        "e": "cursor: pointer",
        "correct": "A",
        "topic": "08: CSS Flexbox Layout",
        "expl": "Flexbox provides powerful layout tools to align and space items along main and cross axes."
    },
    # 9
    {
        "text": "In JavaScript, what method is used to execute a function when a user clicks a button?",
        "a": "button.addEventListener('click', handlerFunction)",
        "b": "button.delete('click')",
        "c": "button.sendEmail('click')",
        "d": "button.restartSystem()",
        "e": "button.printDocument()",
        "correct": "A",
        "topic": "09: JavaScript Event Listeners",
        "expl": "addEventListener('click', ...) binds an event listener to handle user interactions on DOM elements."
    },
    # 10
    {
        "text": "Where can developers open the 'Console' to view logged messages and JavaScript runtime errors?",
        "a": "In Microsoft Paint",
        "b": "Inside the Browser Developer Tools (Inspect / F12)",
        "c": "In the computer's BIOS setup menu",
        "d": "Inside the laptop's sound settings",
        "e": "On the physical keyboard labels",
        "correct": "B",
        "topic": "10: Browser DevTools Console",
        "expl": "The browser Developer Tools console displays console.log() statements, warnings, and uncaught runtime errors."
    },
    # 11
    {
        "text": "What is the primary purpose of browser 'localStorage'?",
        "a": "To store permanent files on an external USB flash drive.",
        "b": "To save key-value data directly in the user's browser that persists even after closing or refreshing the tab.",
        "c": "To increase the physical RAM memory of the computer.",
        "d": "To transmit secret passwords across open Wi-Fi networks.",
        "e": "To print receipts from a connected receipt printer.",
        "correct": "B",
        "topic": "11: Browser LocalStorage",
        "expl": "LocalStorage allows web apps to save lightweight key-value pairs (like theme or score) across browser sessions."
    },
    # 12
    {
        "text": "What is an API (Application Programming Interface)?",
        "a": "A physical cable that plugs into a computer monitor.",
        "b": "A software intermediary that allows two different applications to communicate and exchange data.",
        "c": "An antivirus tool that scans files for corrupted sectors.",
        "d": "A type of physical keyboard layout used in Europe.",
        "e": "A battery charging standard for mobile devices.",
        "correct": "B",
        "topic": "12: What is an API",
        "expl": "APIs define protocols and rules that allow distinct software services (like web apps and weather servers) to talk."
    },
    # 13
    {
        "text": "Which of the following represents valid JSON (JavaScript Object Notation)?",
        "a": "{ \"username\": \"alex\", \"score\": 95, \"active\": true }",
        "b": "<username>alex</username><score>95</score>",
        "c": "username = alex, score = 95, active = true",
        "d": "SELECT * FROM users WHERE username = 'alex';",
        "e": "PRINT \"alex\" TO 95",
        "correct": "A",
        "topic": "13: JSON Data Format",
        "expl": "JSON formats data as key-value pairs enclosed in curly braces with double-quoted string keys."
    },
    # 14
    {
        "text": "What is the key distinction between Frontend and Backend in web development?",
        "a": "Frontend runs in the user's browser (UI/UX), while Backend runs on a remote server (logic, database, authentication).",
        "b": "Frontend is written only in binary, while Backend is written in English.",
        "c": "Frontend is hardware like mice, while Backend is software like games.",
        "d": "Frontend requires no electricity, while Backend uses battery power.",
        "e": "Frontend cannot display images, while Backend only displays images.",
        "correct": "A",
        "topic": "14: Frontend vs Backend",
        "expl": "The Frontend handles presentation and client interactions, while the Backend processes business logic and data storage."
    },
    # 15
    {
        "text": "Why do developers use Git version control in their coding projects?",
        "a": "To compress video files into smaller zip archives.",
        "b": "To track changes in source code over time, create branches for features, and revert bugs if needed.",
        "c": "To replace the computer's motherboard with an upgraded model.",
        "d": "To automatically pay monthly server hosting bills.",
        "e": "To generate random passwords for social media accounts.",
        "correct": "B",
        "topic": "15: Git Version Control",
        "expl": "Git tracks code history, manages branching, and facilitates collaborative development."
    },
    # 16
    {
        "text": "Why should private API keys (e.g. OpenAI or Gemini API keys) be kept in an environment file (like '.env') rather than hardcoded in public client-side JavaScript?",
        "a": "Because JavaScript cannot read text longer than 10 characters.",
        "b": "To prevent anyone from inspecting your public code on GitHub and stealing your private API credentials and credits.",
        "c": "Because .env files automatically double the speed of your internet.",
        "d": "Because client-side code will crash if any key is longer than 5 digits.",
        "e": "Because browsers only allow websites that lack API keys.",
        "correct": "B",
        "topic": "16: Environment Secrets (.env)",
        "expl": "Secret API keys must stay server-side or in .env to prevent malicious actors from extracting and abusing them."
    },
    # 17
    {
        "text": "What does 'Deploying' a web application mean?",
        "a": "Deleting the repository and reinstalling the operating system.",
        "b": "Publishing the application onto a web server (like Vercel or Netlify) so users worldwide can access it via a URL.",
        "c": "Printing out the source code on A4 paper sheets.",
        "d": "Converting the web application into an audio podcast file.",
        "e": "Running an offline virus scan on your local computer.",
        "correct": "B",
        "topic": "17: Web Application Deployment",
        "expl": "Deploying transfers built web assets to live cloud servers, making the website accessible via a public domain name."
    },
    # 18
    {
        "text": "When an AI chatbot writes a piece of code that does not work, what is the most effective Vibecoding debugging strategy?",
        "a": "Give up immediately and change your project topic.",
        "b": "Copy the exact console error message and stack trace, and prompt the AI: 'Here is the error I received, what caused it and how do I fix it?'.",
        "c": "Send 20 angry emojis to the AI chatbot without any code.",
        "d": "Turn off your computer and wait 24 hours.",
        "e": "Delete your operating system files to clear memory.",
        "correct": "B",
        "topic": "18: Effective AI Debugging",
        "expl": "Providing full error traces and context enables AI assistants to accurately pinpoint syntax or logical flaws."
    },
    # 19
    {
        "text": "Why is 'Chain-of-Thought' prompting (asking the AI to 'think step by step') helpful for complex programming tasks?",
        "a": "It slows down your internet so the computer doesn't overheat.",
        "b": "It forces the model to break down multi-step logic sequentially before producing the final code, reducing reasoning errors.",
        "c": "It automatically translates code into 10 different foreign languages.",
        "d": "It guarantees that no bugs will ever occur in any computer program.",
        "e": "It bypasses all password security protections on the web.",
        "correct": "B",
        "topic": "19: Chain-of-Thought Prompting",
        "expl": "Step-by-step reasoning enables LLMs to decompose complex logic into intermediate stages, significantly improving accuracy."
    },
    # 20
    {
        "text": "In JavaScript, what is the role of an asynchronous operation like 'fetch()'?",
        "a": "It freezes the entire computer until the server responds.",
        "b": "It sends an HTTP network request to retrieve data from a server in the background without blocking the user interface.",
        "c": "It shuts down the browser tab after 5 seconds.",
        "d": "It formats the computer's hard drive automatically.",
        "e": "It physically ejects the USB flash drive.",
        "correct": "B",
        "topic": "20: Asynchronous Fetch in JavaScript",
        "expl": "fetch() performs non-blocking asynchronous HTTP requests, retrieving remote data while the user interface stays responsive."
    },
    # 21
    {
        "text": "When inspecting web requests in the DevTools 'Network' tab, what does an HTTP status code of 404 signify?",
        "a": "200 OK — The request was completely successful.",
        "b": "Not Found — The server could not locate the requested resource or URL.",
        "c": "Unauthorized — The user needs to enter a username and password.",
        "d": "Internal Server Error — The server crashed.",
        "e": "Payment Required — The user must pay money to see the page.",
        "correct": "B",
        "topic": "21: HTTP Status Code 404",
        "expl": "Status code 404 Not Found indicates that the client was able to communicate with the server, but the requested endpoint doesn't exist."
    },
    # 22
    {
        "text": "What is a 'Prompt Injection' attack against an AI application?",
        "a": "Injecting physical ink into the computer monitor screen.",
        "b": "Crafting malicious user input designed to trick the AI into ignoring its system safety instructions and revealing confidential data.",
        "c": "Upgrading the computer's cooling fan with liquid nitrogen.",
        "d": "Installing an antivirus update from an official website.",
        "e": "Typing on the keyboard using only one hand.",
        "correct": "B",
        "topic": "22: AI Prompt Injection",
        "expl": "Prompt injection exploits the language interface by inserting instructions that override the model's intended constraints."
    },
    # 23
    {
        "text": "What is the best practice for building a complex application with AI (Iterative Vibecoding)?",
        "a": "Prompting the AI to generate a 5,000-line full-stack app in a single prompt.",
        "b": "Building the application modularly step-by-step, verifying and testing each component before moving to the next.",
        "c": "Never running the code until the entire project is 100% finished.",
        "d": "Refusing to read any code generated by the AI assistant.",
        "e": "Asking the AI to guess what features you need without explaining them.",
        "correct": "B",
        "topic": "23: Iterative Vibecoding Workflow",
        "expl": "Modular, iterative development allows developers to test, verify, and refine code in manageable increments."
    },
    # 24
    {
        "text": "What does HTTPS with SSL/TLS encryption protect against when users visit a website?",
        "a": "It prevents attackers on public Wi-Fi from intercepting and reading transmitted passwords, cookies, and sensitive data.",
        "b": "It prevents the laptop battery from ever running out of power.",
        "c": "It stops all software bugs from appearing in your source code.",
        "d": "It permanently increases the resolution of your computer screen.",
        "e": "It automatically finishes your school homework for you.",
        "correct": "A",
        "topic": "24: HTTPS & Traffic Encryption",
        "expl": "HTTPS encrypts data in transit between the client and server, mitigating man-in-the-middle interception attacks."
    },
    # 25
    {
        "text": "In modern AI systems, what is 'Retrieval-Augmented Generation' (RAG) used for?",
        "a": "Generating random colors for website background styling.",
        "b": "Fetching relevant, verified information from an external knowledge base or documents and providing it to the AI before it answers.",
        "c": "Deleting old files from a hard drive to free up space.",
        "d": "Increasing the volume of laptop speakers during video playback.",
        "e": "Automatically turning off the computer after 10 minutes of inactivity.",
        "correct": "B",
        "topic": "25: Retrieval-Augmented Generation (RAG)",
        "expl": "RAG augments LLM prompts with retrieved factual documents, grounding responses in verified truth and reducing hallucinations."
    }
]

print("Grade 10-11 Vibecoding test data loaded (Balanced High-School Level English). Instructor: Ismoiljon Usmonov.")
