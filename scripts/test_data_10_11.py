#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
10–11th Grade: 25-Question Advanced Cybersecurity, Systems & AI Security Examination
English Version Only (5 options: A, B, C, D, E per question)
"""

META_10_11_EN = {
    "school_name": "TARGET INTERNATIONAL SCHOOL — YUNUSOBOD",
    "exam_title": "GRADES 10–11: ADVANCED CYBERSECURITY, SYSTEMS & AI SAFETY",
    "track_title": "Senior Engineering & CyberSecurity Track",
    "academic_year": "Academic Year 2026–2027",
    "label_name": "Student Full Name",
    "label_class": "Grade / Cohort",
    "label_date": "Date",
    "label_variant": "Variant",
    "variant_val": "Official Variant 1",
    "label_max_score": "Maximum Score",
    "unit_points": "pts",
    "label_score": "Score Earned",
    "instructions": "Instructions: For each question, choose exactly ONE correct answer from the five options provided (A, B, C, D, E). Fill in or circle your chosen letter clearly. Each correct answer is awarded 1 point."
}

KEYS_META_10_11_EN = {
    "heading": "OFFICIAL ANSWER KEY & GRADING RUBRIC",
    "subheading": "Instructor Evaluation & Verification Key (Grades 10–11, 25 Questions)",
    "table_headers": ["№", "Key", "Topic / Competency", "Technical Explanation & Justification"],
    "scale_heading": "Official 25-Point Senior Grading Scale:",
    "rubric_tiers": [
        {"grade": "Excellent (A / 5)", "range": "22 – 25 pts", "desc": "Mastery of enterprise cryptography, Zero Trust, API vulnerabilities, and AI safety"},
        {"grade": "Good (B / 4)", "range": "18 – 21 pts", "desc": "Solid grasp of IAM, container sandboxing, network defenses, and threat models"},
        {"grade": "Satisfactory (C / 3)", "range": "13 – 17 pts", "desc": "Foundations understood; requires review of PKI, SSRF, and rate-limiting"},
        {"grade": "Needs Review (D / 2)", "range": "0 – 12 pts", "desc": "Critical concepts need structured re-examination"}
    ]
}

QUESTIONS_10_11_EN = [
    {
        "text": "What is the primary operational difference between symmetric encryption (e.g., AES-256) and asymmetric encryption (e.g., RSA-4096 / ECC)?",
        "a": "Symmetric encryption uses different keys for encryption and decryption, whereas asymmetric encryption uses a single shared secret.",
        "b": "Symmetric encryption can only encrypt plain ASCII text, whereas asymmetric encryption can only encrypt binary images.",
        "c": "Symmetric encryption relies on a single shared secret key for both encryption and decryption, whereas asymmetric encryption uses a mathematically bound public/private key pair.",
        "d": "Asymmetric encryption is significantly faster in hardware throughput than symmetric encryption.",
        "e": "Symmetric encryption does not require any mathematics, relying solely on random string shuffling.",
        "correct": "C",
        "topic": "Symmetric vs Asymmetric Cryptography",
        "expl": "Symmetric ciphers (AES) use one shared key for high-speed bulk data; asymmetric ciphers (RSA/ECC) use key pairs for identity verification and key exchange."
    },
    {
        "text": "In cryptographic hash functions like SHA-256, what is the 'Avalanche Effect'?",
        "a": "Changing even a single bit in the input data results in a completely unpredictable, radical change across approximately 50% of the output hash bits.",
        "b": "The algorithm consumes exponential amounts of RAM until the server crashes.",
        "c": "Hashes automatically delete themselves after 24 hours of inactivity.",
        "d": "Multiple different input strings always produce the identical output hash.",
        "e": "The output hash string gradually decreases in character length with each iteration.",
        "correct": "A",
        "topic": "Hash Functions & Avalanche Effect",
        "expl": "The avalanche effect ensures strict pre-image resistance and unpredictability: minor input mutations drastically alter the entire digest."
    },
    {
        "text": "How do Certificate Authorities (CAs) and Public Key Infrastructure (PKI) prevent Man-in-the-Middle (MITM) attacks during a TLS handshake?",
        "a": "By physically unplugging untrusted routers along the internet backbone.",
        "b": "By having a trusted root authority cryptographically sign the server's public certificate, allowing clients to verify server domain authenticity before transmitting session secrets.",
        "c": "By converting all web traffic into analog radio frequency waves.",
        "d": "By requiring every website visitor to provide a notarized passport copy.",
        "e": "By blocking all outgoing POST requests on port 443.",
        "correct": "B",
        "topic": "PKI & TLS Handshake",
        "expl": "PKI relies on hierarchical certificate chains where root CAs sign server certificates, ensuring the client connects to the genuine domain owner."
    },
    {
        "text": "What is the core philosophical tenet of the 'Zero Trust Architecture' (ZTA) in enterprise security?",
        "a": "'Trust everything inside the corporate perimeter firewall and block only external traffic.'",
        "b": "'Trust only hardware produced by a single certified vendor.'",
        "c": "'Assume breach: Never trust, always verify every user, device, and service request, regardless of whether it originates inside or outside the network.'",
        "d": "'Disable all firewalls and rely exclusively on user passwords.'",
        "e": "'Block all internet access for employees permanently.'",
        "correct": "C",
        "topic": "Zero Trust Architecture",
        "expl": "Zero Trust discards the perimeter model in favor of continuous authentication, micro-segmentation, and dynamic context-aware authorization."
    },
    {
        "text": "In Identity and Access Management (IAM), how does Role-Based Access Control (RBAC) differ from Attribute-Based Access Control (ABAC)?",
        "a": "RBAC grants permissions based on defined job roles (e.g., 'Analyst'), while ABAC evaluates dynamic attributes (user role, IP location, device health, time of day).",
        "b": "RBAC is only used in mobile apps, while ABAC is strictly for mainframe supercomputers.",
        "c": "RBAC does not support passwords, while ABAC requires 4-digit PINs.",
        "d": "ABAC grants full administrative rights to every registered user by default.",
        "e": "There is no functional difference; they are synonymous acronyms.",
        "correct": "A",
        "topic": "IAM: RBAC vs ABAC",
        "expl": "RBAC assigns permissions statically to roles, whereas ABAC enables fine-grained, dynamic policies using environmental and contextual attributes."
    },
    {
        "text": "Why are hardware security keys (FIDO2 / WebAuthn) vastly superior to SMS-based Two-Factor Authentication (2FA)?",
        "a": "Hardware keys do not require electrical power to function.",
        "b": "SMS codes are vulnerable to SIM swapping, SS7 cellular interception, and adversary-in-the-middle phishing proxies, whereas FIDO2 uses origin-bound asymmetric crypto immune to phishing.",
        "c": "Hardware keys allow users to guess their PINs infinite times without locking.",
        "d": "SMS codes can only be received on desktop computers.",
        "e": "FIDO2 keys replace the computer's motherboard automatically.",
        "correct": "B",
        "topic": "MFA Security & FIDO2",
        "expl": "FIDO2/WebAuthn binds the cryptographic challenge directly to the verified browser domain origin, rendering credential-harvesting phishing proxies ineffective."
    },
    {
        "text": "How does the 'Token Bucket' algorithm enforce rate limiting on high-throughput REST APIs?",
        "a": "It deletes all incoming API requests immediately once the database reaches 100 megabytes.",
        "b": "Tokens are added to a bucket at a fixed rate up to a maximum capacity; each valid request consumes a token, dropping requests when the bucket is empty while permitting burst traffic.",
        "c": "It forces every client to wait exactly 60 seconds between any two consecutive HTTP requests.",
        "d": "It charges the client 1 dollar in cryptocurrency per HTTP GET query.",
        "e": "It randomizes IP addresses before processing requests.",
        "correct": "B",
        "topic": "API Rate Limiting (Token Bucket)",
        "expl": "The token bucket allows sudden bursts up to bucket capacity while guaranteeing that long-term average consumption matches the token replenishment rate."
    },
    {
        "text": "Why do secure payment gateways and webhooks require an HMAC-SHA256 signature header on incoming HTTP payloads?",
        "a": "To compress the JSON body into a smaller file size.",
        "b": "To allow the receiver to verify both payload integrity and authenticity using a shared secret, proving the request was not tampered with in transit.",
        "c": "To convert the HTTP request into a printable PDF receipt.",
        "d": "To encrypt the IP address of the sender.",
        "e": "To bypass the need for an SSL certificate.",
        "correct": "B",
        "topic": "HMAC Request Signing",
        "expl": "HMAC combines a cryptographic hash with a secret key, ensuring that any modification to headers or payload invalidates the signature."
    },
    {
        "text": "What critical vulnerability arises if a backend server improperly validates a JSON Web Token (JWT) with `{\"alg\": \"none\"}` in its header?",
        "a": "The server's hard drive is immediately formatted.",
        "b": "An attacker can forge arbitrary payloads (e.g., set `\"role\": \"admin\"`), remove the signature completely, and the server will accept it as a valid authenticated session.",
        "c": "The client browser crashes upon receiving the HTTP response.",
        "d": "The user is forced to re-enter their password every 10 seconds.",
        "e": "The server switches from IPv4 to IPv6 without administrator consent.",
        "correct": "B",
        "topic": "JWT 'alg: none' Exploit",
        "expl": "The 'alg: none' vulnerability occurs when a library accepts tokens without verifying any cryptographic signature, enabling trivial privilege escalation."
    },
    {
        "text": "In modern React applications, why does the use of `dangerouslySetInnerHTML` introduce severe security risks?",
        "a": "It slows down the virtual DOM reconciliation algorithm by 500%.",
        "b": "It bypasses React's native string sanitization and XSS escaping, allowing unescaped HTML/JavaScript inputs to execute directly in the victim's browser context.",
        "c": "It forces all CSS styling to render in black and white.",
        "d": "It requires Node.js to be recompiled from source code.",
        "e": "It automatically exposes the database administrator password in the console.",
        "correct": "B",
        "topic": "React Security & XSS Escaping",
        "expl": "React automatically escapes strings within JSX brackets `{variable}`. Using `dangerouslySetInnerHTML` disables this protection and opens the door to XSS."
    },
    {
        "text": "What is Server-Side Request Forgery (SSRF), and how do attackers frequently exploit it in cloud environments (AWS/GCP)?",
        "a": "The attacker floods the client's router with UDP packets.",
        "b": "The attacker tricks the vulnerable backend server into making HTTP requests to internal resources, such as querying the Instance Metadata Service (`http://169.254.169.254`) to steal IAM credentials.",
        "c": "The attacker sends fraudulent emails pretending to be the CEO.",
        "d": "The attacker steals the physical power cables from the cloud datacenter.",
        "e": "The attacker changes the font family on the company homepage.",
        "correct": "B",
        "topic": "SSRF & Cloud Metadata Exploitation",
        "expl": "SSRF exploits server trust to reach internal non-routable endpoints. Accessing cloud metadata (`169.254.169.254`) often leaks temporary cloud access keys."
    },
    {
        "text": "What characterizes a Broken Object Level Authorization (BOLA / IDOR) vulnerability in REST APIs?",
        "a": "The API server runs out of disk storage due to excessive log creation.",
        "b": "A regular authenticated user manipulates an object identifier (e.g., changing `/api/documents/102` to `/api/documents/103`) and accesses another user's private data because the server lacks record-level ownership checks.",
        "c": "The database uses invalid column names in SQL schemas.",
        "d": "The frontend client renders an incorrect CSS grid layout.",
        "e": "The server rejects valid JSON payloads with HTTP status 404.",
        "correct": "B",
        "topic": "BOLA / IDOR (OWASP API #1)",
        "expl": "BOLA occurs when endpoints expose object identifiers without verifying whether the requesting user actually owns or is authorized to view that specific record."
    },
    {
        "text": "In network security, how does an Amplification DDoS attack (e.g., DNS or NTP amplification) work?",
        "a": "Attackers send physical sound waves through computer speakers to disrupt CPU cooling fans.",
        "b": "The attacker sends small spoofed UDP requests with the victim's source IP to open recursive reflectors, which reply with disproportionately huge response payloads directed at the victim.",
        "c": "The attacker creates thousands of fake user profiles on LinkedIn.",
        "d": "The attacker downloads large video files using a torrent client.",
        "e": "The attacker unplugs DNS root servers manually.",
        "correct": "B",
        "topic": "DDoS Amplification Attacks",
        "expl": "UDP reflection/amplification leverages connectionless protocols: tiny queries generate 50x–70x larger responses reflected entirely onto the spoofed target IP."
    },
    {
        "text": "Which three core Linux kernel mechanisms provide process isolation and resource governance in Docker containers?",
        "a": "cron, bash, and nano.",
        "b": "Namespaces (isolating visibility), cgroups (limiting memory/CPU resources), and Seccomp (filtering system calls).",
        "c": "EXT4, FAT32, and NTFS.",
        "d": "HTML5, CSS3, and ECMAScript.",
        "e": "Bluetooth, NFC, and Wi-Fi Direct.",
        "correct": "B",
        "topic": "Container Sandboxing & Linux Kernel",
        "expl": "Docker containers are not virtual machines; they rely on Linux namespaces (PID, NET, MNT), control groups (cgroups), and seccomp filters for process sandboxing."
    },
    {
        "text": "What is the strategic purpose of the 'Defense in Depth' model in cybersecurity architecture?",
        "a": "Relying on a single, extremely expensive firewall to solve all enterprise threats.",
        "b": "Implementing multiple overlapping, layered security controls (e.g., endpoint protection, network segmentation, MFA, data encryption) so that if one layer fails, others stop the adversary.",
        "c": "Hiding company servers deep underground in concrete bunkers.",
        "d": "Encrypting data only after a breach has been officially confirmed.",
        "e": "Banning all employees from using passwords longer than 8 characters.",
        "correct": "B",
        "topic": "Defense in Depth",
        "expl": "Defense in depth ensures redundancy: no single point of failure compromises the overall security posture if a preventative barrier is breached."
    },
    {
        "text": "What is the primary function of the MITRE ATT&CK framework in threat intelligence and SOC operations?",
        "a": "Selling software licenses for antivirus programs.",
        "b": "Providing a comprehensive, structured knowledge base of real-world adversary tactics, techniques, and procedures (TTPs) to evaluate defenses and categorize intrusion behaviors.",
        "c": "Benchmarking gaming graphics cards.",
        "d": "Translating computer science textbooks into foreign languages.",
        "e": "Managing employee payroll and vacation schedules.",
        "correct": "B",
        "topic": "MITRE ATT&CK Framework",
        "expl": "MITRE ATT&CK categorizes cyber adversary behaviors into standardized matrices across the entire cyber attack lifecycle (from Initial Access to Impact)."
    },
    {
        "text": "In incident response metrics, what do MTTD and MTTR represent?",
        "a": "Maximum Transfer Throughput / Minimum Total Resistance.",
        "b": "Mean Time to Detect (average time from intrusion to detection) and Mean Time to Respond / Remediate (average time to contain and resolve the incident).",
        "c": "Mega-Thread Task Dispatch / Memory Transaction Timer Reset.",
        "d": "Master Token Ticket Distribution / Minor Technical Team Review.",
        "e": "Manual Typing Time Duration / Machine Text Translation Rate.",
        "correct": "B",
        "topic": "SOC Metrics: MTTD & MTTR",
        "expl": "MTTD reflects detection efficacy, while MTTR measures containment agility. Modern SOCs strive to minimize both metrics to reduce breach dwell time."
    },
    {
        "text": "Why do modern enterprise ransomware defense strategies mandate 'Immutable Backups' stored in an air-gapped architecture?",
        "a": "To allow anyone on the internet to edit and delete system snapshots freely.",
        "b": "Because modern ransomware actively locates and deletes online backup repositories; immutable, write-once-read-many (WORM) storage prevents encryption or deletion even by compromised admin credentials.",
        "c": "To reduce backup storage speed to zero.",
        "d": "To eliminate the need for disaster recovery drills.",
        "e": "To replace cloud computing with floppy disks.",
        "correct": "B",
        "topic": "Ransomware Defense & Immutable Backups",
        "expl": "Immutable backups cannot be overwritten or deleted for a set retention window, ensuring guaranteed recovery without paying ransoms."
    },
    {
        "text": "What distinguishes an 'Indirect Prompt Injection' attack from a 'Direct Prompt Injection' attack against an LLM?",
        "a": "Indirect injection can only be executed using physical keyboards.",
        "b": "In indirect injection, adversarial instructions are embedded within external untrusted content (e.g., a scanned PDF, webpage, or email) that the LLM retrieves and processes, hijacking model instructions without direct user prompt tampering.",
        "c": "Direct injection requires hacking into the GPU datacenter facility physically.",
        "d": "Indirect injection always results in an immediate power outage.",
        "e": "There is no difference; LLMs cannot process external content.",
        "correct": "B",
        "topic": "Direct vs Indirect Prompt Injection",
        "expl": "Indirect prompt injection occurs when LLMs ingest third-party data containing hidden malicious prompt payloads, weaponizing retrieval systems."
    },
    {
        "text": "In adversarial machine learning for computer vision, what is the Fast Gradient Sign Method (FGSM)?",
        "a": "A high-speed method for rendering 3D video game characters.",
        "b": "An attack technique that calculates the gradient of the loss function and adds subtle, imperceptible mathematical noise to an image, causing the deep neural network to misclassify it with high confidence.",
        "c": "An algorithm for compressing JPEG images without quality loss.",
        "d": "A technique for speeding up internet download speeds.",
        "e": "A method for automatically printing documents on office printers.",
        "correct": "B",
        "topic": "Adversarial Machine Learning (FGSM)",
        "expl": "FGSM perturbs input pixels along the gradient of the loss function, generating adversarial examples that fool neural networks while looking identical to human eyes."
    },
    {
        "text": "How do AI security teams deploy 'Canary Tokens' in LLM training and retrieval pipelines to detect unauthorized data exfiltration?",
        "a": "By singing bird songs through microphone inputs.",
        "b": "By placing unique, artificial decoy tokens/strings into sensitive corpora; if the token appears in external prompts, logs, or model outputs, it immediately alerts the security team of a data leak.",
        "c": "By deleting all punctuation marks from training datasets.",
        "d": "By converting all training texts into hexadecimal format.",
        "e": "By requiring LLM developers to wear yellow shirts.",
        "correct": "B",
        "topic": "Canary Tokens & AI Data Leakage",
        "expl": "Canary tokens act as tripwires: their detection in unauthorized outputs or external telemetry provides unambiguous evidence of data exfiltration."
    },
    {
        "text": "What role do Guardrail systems (such as NVIDIA NeMo Guardrails or Llama Guard) play in production LLM deployments?",
        "a": "They physically hold the server racks in place to protect against earthquakes.",
        "b": "They act as programmable input/output moderation middleware, enforcing topic boundaries, filtering PII, verifying factuality, and intercepting jailbreak attempts before user delivery.",
        "c": "They automatically increase the subscription price of the AI software.",
        "d": "They convert text prompts into high-resolution vector images.",
        "e": "They prevent the computer monitor from overheating.",
        "correct": "B",
        "topic": "LLM Guardrails Middleware",
        "expl": "Guardrails sit between the user and the LLM, validating inputs and outputs against safety policies, jailbreak signatures, and compliance boundaries."
    },
    {
        "text": "In software supply chain security, how does a 'Dependency Confusion' or 'Typosquatting' attack compromise build pipelines?",
        "a": "By causing physical short circuits in network switches.",
        "b": "Attackers register malicious packages on public registries (e.g., npm, PyPI) using names identical to internal company libraries or common misspellings, tricking build tools into downloading poisoned code into CI/CD pipelines.",
        "c": "By sending fraudulent invoices via postal mail.",
        "d": "By forcing developers to write code exclusively in Assembly language.",
        "e": "By slowing down typing speeds on mechanical keyboards.",
        "correct": "B",
        "topic": "Supply Chain Security & Typosquatting",
        "expl": "Package managers prioritize public repositories or resolve typos, pulling malicious code that executes build-time arbitrary commands during installation."
    },
    {
        "text": "What is a Software Bill of Materials (SBOM) and why has it become an international cybersecurity requirement?",
        "a": "A financial invoice sent to customers for purchasing software licenses.",
        "b": "A formal, machine-readable inventory of all third-party components, libraries, and hierarchical dependencies in an application, enabling rapid vulnerability tracking (e.g., during Log4j).",
        "c": "A list of employee names who contributed to writing code comments.",
        "d": "A warranty certificate for computer monitors and keyboards.",
        "e": "A manual describing how to install Windows on a laptop.",
        "correct": "B",
        "topic": "Software Bill of Materials (SBOM)",
        "expl": "SBOMs (SPDX/CycloneDX) provide transparent visibility into application supply chains, allowing teams to instantly identify affected software when zero-days emerge."
    },
    {
        "text": "In a modern DevSecOps CI/CD pipeline, how does Static Application Security Testing (SAST) complement Dynamic Application Security Testing (DAST)?",
        "a": "SAST tests the internet connection speed, while DAST checks monitor brightness.",
        "b": "SAST analyzes source code without executing it early in development (white-box), whereas DAST tests running applications from the outside against simulated attacks (black-box).",
        "c": "SAST is only run on weekends, while DAST is run on weekdays.",
        "d": "SAST is performed manually by human interns, while DAST is an obsolete technology.",
        "e": "There is no difference between SAST and DAST in software testing.",
        "correct": "B",
        "topic": "SAST vs DAST in DevSecOps",
        "expl": "SAST catches code flaws early in IDE/build stages, while DAST discovers runtime misconfigurations, authentication issues, and server behavior during execution."
    }
]

print("Grade 10-11 test data loaded (25 questions EN).")
