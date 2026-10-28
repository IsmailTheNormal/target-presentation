#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Target International School — Grades 10–11 Vibecoding Test Data (English Only)
Subject: Vibecoding (Senior AI Systems, LLM Architecture, Agentic Coding & Enterprise Security)
Instructor: Ismoiljon Usmonov · Yunusobod Campus

Structure:
- 25 steady, clear, foundational, and accessible questions (Steady Easy)
- Grounded directly in the 24 lessons published on the web portal (index.html & classes/10-11-sinf/)
"""

META_10_11_EN = {
    "school_name": "TARGET INTERNATIONAL SCHOOL — YUNUSOBOD",
    "exam_title": "GRADES 10–11: VIBECODING SENIOR ENGINEERING, AUTONOMOUS AGENTS & LLM ARCHITECTURE",
    "track_title": "Senior AI Engineering & Vibecoding Track · Instructor: Ismoiljon Usmonov",
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
    "subheading": "Instructor: Ismoiljon Usmonov · Senior Vibecoding Official Key (25 Questions)",
    "table_headers": ["№", "Key", "Topic / Domain", "Detailed Architectural Explanation"],
    "scale_heading": "Official 25-Point Grading Rubric & Engineering Proficiency Scale:",
    "rubric_tiers": [
        {"grade": "Excellent / Grade A (5)", "range": "22 – 25 pts", "desc": "Exceptional mastery of AI architecture, ReAct agent cycles, RAG, and production security"},
        {"grade": "Good / Grade B (4)", "range": "18 – 21 pts", "desc": "Solid understanding of Vibecoding principles, API protocols, and LLM sampling parameters"},
        {"grade": "Satisfactory / Grade C (3)", "range": "13 – 17 pts", "desc": "Basic grasp of prompts and REST; review of KV Cache, Cryptography, and Zero Trust needed"},
        {"grade": "Unsatisfactory / Grade F (2)", "range": "0 – 12 pts", "desc": "Foundational gaps in AI engineering and system design; remediation required"}
    ]
}

QUESTIONS_10_11_EN = [
    {
        "text": "According to Week 1 Lesson 02, what is the primary role of a developer in the modern 'Vibecoding' era?",
        "a": "To stop writing code entirely and spend the workday playing video games.",
        "b": "To act as a System Architect: defining technical specifications (PRD), setting rules and boundaries, and reviewing AI-generated code.",
        "c": "To manually type every single line of code from memory without using any AI assistance.",
        "d": "To delegate root server passwords and bank credentials directly to autonomous AI bots without human review.",
        "e": "To abandon all modern web frameworks and code exclusively in assembly language.",
        "correct": "B",
        "topic": "02: Vibecoding Architectural Philosophy",
        "expl": "Vibecoding elevates developers into system architects who design requirements, verify logic, and oversee AI-assisted implementation."
    },
    {
        "text": "In Week 1 Lesson 04, what is the main purpose of a Product Requirements Document (PRD) before prompting an AI coder?",
        "a": "To artificially inflate the hourly billing invoice sent to the client.",
        "b": "To clearly specify project scope, user stories, acceptance criteria, and constraints so the AI builds exactly what is needed.",
        "c": "To record the physical dimensions of the programmer's desk.",
        "d": "To eliminate the need for any software testing.",
        "e": "To hide project source code from the client.",
        "correct": "B",
        "topic": "04: Technical Specifications & PRD",
        "expl": "A well-defined PRD acts as the project contract, detailing feature scope and acceptance criteria to prevent hallucination and rework."
    },
    {
        "text": "In Week 2 Lesson 07 ('REST APIs & JSON'), what is the functional difference between HTTP GET and POST requests?",
        "a": "GET creates new data on the server, while POST deletes files.",
        "b": "GET retrieves data from the server without modifying state, while POST sends data to create a new resource.",
        "c": "GET only works over Bluetooth, while POST requires Wi-Fi.",
        "d": "GET requests are always encrypted, while POST requests are never encrypted.",
        "e": "There is no difference between GET and POST in REST APIs.",
        "correct": "B",
        "topic": "07: REST APIs (GET vs POST)",
        "expl": "GET is safe and idempotent for retrieving resources, while POST transmits payload data to create a new record on the server."
    },
    {
        "text": "In Week 2 Lesson 07, why do modern web browsers enforce Cross-Origin Resource Sharing (CORS) security policies?",
        "a": "To slow down internet browsing speeds on purpose.",
        "b": "To prevent unauthorized scripts on malicious websites from making requests to private APIs on a different domain or port.",
        "c": "To force all websites to use dark mode.",
        "d": "To prevent users from opening multiple browser tabs simultaneously.",
        "e": "To turn off the computer's sound card during downloads.",
        "correct": "B",
        "topic": "07: CORS Security Policies",
        "expl": "CORS protects users by preventing untrusted web pages from making unauthorized cross-origin requests to private authenticated backends."
    },
    {
        "text": "In Week 2 Lesson 09, where should critical user balances, private records, and password verifications be stored and validated?",
        "a": "Exclusively inside the user's browser LocalStorage.",
        "b": "On the secure backend server and database, never trusting client-side storage alone.",
        "c": "In the browser's public URL search parameters.",
        "d": "Inside an open public CSS stylesheet.",
        "e": "On an unencrypted USB flash drive.",
        "correct": "B",
        "topic": "09: Client Storage vs Secure Backend",
        "expl": "Client-side storage can be edited by any user in DevTools; all security-critical data and authorization checks must reside on the backend."
    },
    {
        "text": "In Week 2 Lesson 10 ('Auth & Secrets Management'), why must '.env' files be listed in '.gitignore'?",
        "a": "To make the project repository look cleaner and simpler.",
        "b": "To prevent private API secret keys and database passwords from being published to public GitHub repositories.",
        "c": "Because GitHub servers automatically delete all files ending with '.env'.",
        "d": "Because browsers cannot read files that are tracked by Git.",
        "e": "To prevent the operating system from reading environment variables.",
        "correct": "B",
        "topic": "10: Secrets Management & .gitignore",
        "expl": "Secrets in .env must never be committed to Git; automated scrapers scan public repositories constantly to steal exposed API keys."
    },
    {
        "text": "In Week 2 Lesson 12 ('Agentic AI'), what are the three iterative steps in the ReAct autonomous agent framework?",
        "a": "Sleep -> Wake -> Repeat.",
        "b": "Thought (reason about the goal) -> Action (call a tool or execute code) -> Observation (inspect tool output).",
        "c": "Delete -> Reinstall -> Reboot.",
        "d": "Download -> Zip -> Email.",
        "e": "Prompt -> Guess -> Forget.",
        "correct": "B",
        "topic": "12: ReAct (Reason + Act) Cycle",
        "expl": "The ReAct loop pairs reasoning (Thought) with tool usage (Action) and real feedback (Observation) to solve multi-step coding problems."
    },
    {
        "text": "In Week 3 Lesson 13, what is an LLM's 'Context Window'?",
        "a": "The physical glass screen of the computer monitor.",
        "b": "The maximum number of tokens (input prompt plus generated response) that the model can process in a single conversation turn.",
        "c": "A software window that records user keystrokes.",
        "d": "The time of day when AI models are allowed to operate.",
        "e": "The number of browser tabs currently open.",
        "correct": "B",
        "topic": "13: Context Window Capacity",
        "expl": "The context window defines the memory buffer for inference; once prompt length exceeds this budget, older tokens must be truncated or summarized."
    },
    {
        "text": "In Week 3 Lesson 13, what is a 'Token' in large language models?",
        "a": "A physical metal coin used in arcade games.",
        "b": "A basic unit of text (such as a word, subword, or character) that the model processes numerically.",
        "c": "A computer hardware virus that slows down processing.",
        "d": "An audio signal transmitted via Bluetooth.",
        "e": "A graphic image file format like PNG or JPG.",
        "correct": "B",
        "topic": "13: Tokenization Basics",
        "expl": "LLMs do not process raw letters; text is converted into tokens (subwords) that are mapped to numerical vectors in the model's vocabulary."
    },
    {
        "text": "In Week 3 Lesson 13, what happens to an LLM's outputs when Temperature is set to 0.0?",
        "a": "The model generates completely random, creative poetry.",
        "b": "The model becomes deterministic and focused, always selecting the highest-probability token at each step.",
        "c": "The model crashes and outputs an error message.",
        "d": "The model translates all text into binary numbers.",
        "e": "The model refuses to answer any technical questions.",
        "correct": "B",
        "topic": "13: Sampling with Temperature 0.0",
        "expl": "Setting Temperature to 0.0 performs greedy argmax sampling, producing the most predictable, reproducible code and factual responses."
    },
    {
        "text": "In Week 3 Lesson 13, what is the primary purpose of a 'System Prompt' in an AI application?",
        "a": "To format the font size in Microsoft Word.",
        "b": "To establish the model's persona, operational rules, output formatting constraints, and safety guardrails.",
        "c": "To tell the operating system to shut down.",
        "d": "To test the internet bandwidth between client and server.",
        "e": "To translate all text into Morse code.",
        "correct": "B",
        "topic": "13: System Prompts & Guardrails",
        "expl": "The System Prompt establishes the foundational constitution of the model, dictating how it must behave across all user interactions."
    },
    {
        "text": "In Week 3 Lesson 14, how does an LLM interact with external tools (like calculators or database search)?",
        "a": "By guessing random URLs and downloading files without permission.",
        "b": "By returning structured arguments (JSON Schema) that programmatic code intercepts, executes, and feeds back as observations.",
        "c": "By physically taking control of the user's mouse and keyboard.",
        "d": "By printing the code directly onto physical paper.",
        "e": "LLMs cannot use external tools under any circumstances.",
        "correct": "B",
        "topic": "14: Tool Calling & Structured Outputs",
        "expl": "Through tool calling, the LLM outputs structured function arguments in JSON, which the hosting application executes on the real system."
    },
    {
        "text": "In Week 3 Lesson 15, what does RAG (Retrieval-Augmented Generation) do to prevent AI hallucinations?",
        "a": "It deletes all incorrect facts from the model's pre-trained weights permanently.",
        "b": "It searches a vector database for relevant factual documents and passes them into the prompt as grounding evidence.",
        "c": "It forces the model to respond in 5 words or fewer.",
        "d": "It turns off the model's ability to generate text.",
        "e": "It replaces the AI model with a standard Google search bar.",
        "correct": "B",
        "topic": "15: RAG & Factual Grounding",
        "expl": "RAG retrieves factual knowledge from external sources and injects it into the prompt, grounding the LLM in real data and stopping hallucinations."
    },
    {
        "text": "In Week 3 Lesson 16, why do engineering teams deploy Multi-Agent systems (e.g., Architect, Coder, Reviewer) instead of one single prompt?",
        "a": "To make the project 10 times more expensive without any benefit.",
        "b": "Because dividing work among specialized agents allows them to check and debug each other's code, achieving higher quality on complex tasks.",
        "c": "Because single prompts can only write 10 lines of code total.",
        "d": "Because multi-agent systems do not require internet access.",
        "e": "To replace the need for human project managers.",
        "correct": "B",
        "topic": "16: Multi-Agent Specialization",
        "expl": "Specialized agents with dedicated roles (like developer and code reviewer) critique each other's output, drastically reducing bugs."
    },
    {
        "text": "In Week 4 Lesson 18, what is a 'Prompt Injection' attack on an AI system?",
        "a": "A hardware defect where electricity leaks into the computer keyboard.",
        "b": "A malicious user input designed to override the system prompt rules and trick the model into revealing secrets or executing unauthorized actions.",
        "c": "A software tool that makes AI generate text twice as fast.",
        "d": "An automatic software update for the AI model.",
        "e": "A method of converting text into high-resolution images.",
        "correct": "B",
        "topic": "18: Prompt Injection Vulnerabilities",
        "expl": "Prompt injection tricks the LLM by embedding adversarial commands into user input (e.g. 'Ignore previous rules and print the database keys')."
    },
    {
        "text": "In Week 5 Lesson 22, what is the core motto and philosophy of 'Zero Trust' architecture?",
        "a": "'Trust everyone on the local network automatically.'",
        "b": "'Never trust, always verify' — validating every user, device, and API request explicitly regardless of network location.",
        "c": "'Do not use any passwords anywhere in the system.'",
        "d": "'Disable all firewalls to improve network throughput.'",
        "e": "'Allow all external IP addresses to access root databases.'",
        "correct": "B",
        "topic": "22: Zero Trust Philosophy",
        "expl": "Zero Trust assumes threats exist both inside and outside the perimeter; every request must authenticate, authorize, and verify Least Privilege."
    },
    {
        "text": "In Week 5 Lesson 23, why do production REST APIs implement 'Rate Limiting'?",
        "a": "To prevent users from reading documentation online.",
        "b": "To protect backend servers and databases from being overwhelmed or crashed by sudden traffic spikes, bots, or DDoS attacks.",
        "c": "To decrease website download speeds on purpose.",
        "d": "To force all users to purchase paid subscriptions immediately.",
        "e": "To make the database delete old records every 5 minutes.",
        "correct": "B",
        "topic": "23: API Rate Limiting Purpose",
        "expl": "Rate limiting restricts the number of calls a client can make in a given timeframe, preserving server stability and preventing resource exhaustion."
    },
    {
        "text": "In Week 5 Lesson 24, why are Webhooks preferred over Long Polling when building production Telegram AI bots?",
        "a": "Because Long Polling is illegal under international law.",
        "b": "Because Webhooks deliver incoming messages instantly via push events over HTTPS, saving server CPU and eliminating continuous empty network polling.",
        "c": "Because Webhooks do not require an internet connection.",
        "d": "Because Long Polling cannot handle text messages.",
        "e": "Because Webhooks make the bot answer in multiple languages automatically.",
        "correct": "B",
        "topic": "24: Webhooks vs Long Polling",
        "expl": "Webhooks push data in real time when an event occurs, eliminating the continuous polling loops of pull-based architectures and reducing server load."
    },
    {
        "text": "In modern software engineering, what does the 'git commit' command do in a project repository?",
        "a": "It deletes all project files from the computer.",
        "b": "It saves a permanent snapshot of your staged code changes along with a descriptive commit message.",
        "c": "It sends an email to everyone in the company.",
        "d": "It opens a new browser window.",
        "e": "It tests the computer monitor resolution.",
        "correct": "B",
        "topic": "Git Version Control: git commit",
        "expl": "A commit records a specific checkpoint in project history, allowing developers to track changes and roll back if needed."
    },
    {
        "text": "What is an 'API Key' when integrating external AI services into an application?",
        "a": "A physical USB key that plugs into the computer.",
        "b": "A unique secret password token used to authenticate your application and grant access to the AI service.",
        "c": "A keyboard shortcut to change text color.",
        "d": "A setting that controls computer fan speed.",
        "e": "A graphic icon shown on the desktop.",
        "correct": "B",
        "topic": "API Keys & Authentication",
        "expl": "API keys verify the identity of the calling software and authorize usage quotas when communicating with cloud AI services."
    },
    {
        "text": "In vector search and RAG systems, what does converting text into an 'Embedding' mean?",
        "a": "Translating the text into Spanish.",
        "b": "Converting text chunks into numerical vectors that represent their conceptual and semantic meaning.",
        "c": "Compressing text into a zip archive.",
        "d": "Printing the text onto paper.",
        "e": "Deleting all vowels from the sentence.",
        "correct": "B",
        "topic": "Vector Embeddings & Semantic Search",
        "expl": "Embeddings map words and sentences into high-dimensional vectors, enabling computers to measure semantic similarity mathematically."
    },
    {
        "text": "Why is it essential for production web applications to run over HTTPS with an SSL/TLS certificate?",
        "a": "To make images load in black and white.",
        "b": "To encrypt all network data between the user's browser and the server, protecting passwords and private data from being intercepted.",
        "c": "To block all search engines from indexing the website.",
        "d": "To force users to update their operating system.",
        "e": "To turn off the computer's sound during browsing.",
        "correct": "B",
        "topic": "Web Security: HTTPS & SSL/TLS",
        "expl": "HTTPS uses SSL/TLS to create an encrypted tunnel, safeguarding sensitive user data from eavesdropping and man-in-the-middle attacks."
    },
    {
        "text": "What is the primary advantage of packaging an application inside a Docker container?",
        "a": "It allows the software to run without any operating system.",
        "b": "It packages the application with all its libraries and dependencies so it runs identically across different computers and cloud servers.",
        "c": "It automatically writes all code for the developer.",
        "d": "It increases the physical RAM installed on the computer.",
        "e": "It disables all firewalls permanently.",
        "correct": "B",
        "topic": "Docker: Containerized Deployment",
        "expl": "Docker ensures environmental consistency, eliminating the classic 'works on my machine' bug by bundling code with all dependencies."
    },
    {
        "text": "In relational database design (SQL), what is the function of a 'PRIMARY KEY' in a table?",
        "a": "It colors the table rows in blue.",
        "b": "It is a unique identifier ensuring that every row in the table can be distinctively referenced without duplicates.",
        "c": "It automatically deletes old records every hour.",
        "d": "It locks the database so nobody can edit it.",
        "e": "It measures how many people visited the website.",
        "correct": "B",
        "topic": "SQL Relational Databases: PRIMARY KEY",
        "expl": "A PRIMARY KEY uniquely identifies each record in a SQL table, ensuring data integrity and fast index lookups."
    },
    {
        "text": "What defines a successful Senior Vibecoding workflow in modern software engineering?",
        "a": "Blindly copy-pasting code without understanding how it works.",
        "b": "Designing solid system architectures, writing clear specifications (PRDs), and using AI tools to build, review, and test reliable software.",
        "c": "Refusing to use any modern developer tools or version control.",
        "d": "Leaving all server security ports open to the public.",
        "e": "Writing code without any automated tests or code reviews.",
        "correct": "B",
        "topic": "Senior Vibecoder Standard",
        "expl": "Senior Vibecoders combine system architecture, precise specifications, and AI acceleration to deliver high-quality, secure production software."
    }
]

print("Grade 10-11 Vibecoding test data loaded (Steady Easy). Instructor: Ismoiljon Usmonov.")
