#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Target International School — Grades 10–11 Vibecoding Test Data (English Only)
Subject: Vibecoding (Senior AI Systems, LLM Architecture, Agentic Coding & Enterprise Security)
Instructor: Ismoiljon Usmonov · Yunusobod Campus

Grounded directly in the 24 lessons published on the web portal (index.html & classes/10-11-sinf/):
Week 1: AI Foundations, Vibecoding Architecture, IT Infrastructure, PRD & SLA, Async JS, Deploy & Edge CDN
Week 2: REST API & CORS, High-Frequency Data Streaming, LocalStorage vs State, Secrets Management & .env, VS Code CLI, Agentic AI ReAct Cycle
Week 3: LLM Mechanics (Self-Attention O(N^2), KV Cache, BPE Tokenization, Lost in the Middle, Temperature/Top-P Sampling, Few-Shot), Tool Calling (JSON Schema, Constrained Decoding), RAG Vector Search, Multi-Agent Swarms & Memory
Week 4: Chunking & Cosine Distance, Prompt Injection (Direct vs Indirect), Agent Sandboxing (gVisor/RCE), Multi-Agent Egress DLP
Week 5: Enterprise Cryptography (AES-256 vs RSA-4096), Zero Trust & IAM (RBAC/ABAC, mTLS), API Rate Limiting (Token Bucket), HMAC Signatures, Production AI Telegram Bot (Webhooks)
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
        {"grade": "Excellent / Grade A (5)", "range": "22 – 25 pts", "desc": "Exceptional mastery of LLM internal mechanics, Agentic ReAct, Tool Calling, RAG, and Enterprise AI Security"},
        {"grade": "Good / Grade B (4)", "range": "18 – 21 pts", "desc": "Solid understanding of Vibecoding architecture, API protocols, vector embeddings, and sandboxing"},
        {"grade": "Satisfactory / Grade C (3)", "range": "13 – 17 pts", "desc": "Basic grasp of prompt engineering and REST; requires review of KV Cache, Cryptography, and Zero Trust"},
        {"grade": "Unsatisfactory / Grade F (2)", "range": "0 – 12 pts", "desc": "Foundational gaps in AI engineering and system design; remediation and re-examination required"}
    ]
}

QUESTIONS_10_11_EN = [
    {
        "text": "According to Week 1 Lesson 02, how does the modern 'Vibecoding' paradigm fundamentally redefine the role of a Senior Software Engineer?",
        "a": "Engineers no longer write any documentation and allow AI models to deploy arbitrary unverified code directly into production.",
        "b": "Engineers elevate from manual syntax typists to System Architects: defining formal specifications (PRD), boundary constraints, and verification harnesses while AI handles code synthesis.",
        "c": "Vibecoding eliminates backend systems, databases, and network protocols, reducing all software development to pure Figma visual design.",
        "d": "Engineers delegate all security keys, root server access, and billing passwords directly to autonomous AI models without human oversight.",
        "e": "It restricts developers to using only legacy procedural programming languages without access to generative AI or modern frameworks.",
        "correct": "B",
        "topic": "02: Vibecoding Architectural Philosophy",
        "expl": "Vibecoding transforms the engineer into a high-level system architect who writes deterministic specifications (PRDs) and validates AI outputs through rigor and automated tests."
    },
    {
        "text": "In Week 1 Lesson 04 ('Freelance PRD & UI'), why is a Product Requirements Document (PRD) considered an essential technical contract before issuing prompts to an AI coder?",
        "a": "Solely to inflate the hourly billing rate presented to the client.",
        "b": "To establish unambiguous functional boundaries, user stories, acceptance criteria, and edge-case behaviors, preventing AI hallucinations and scope creep.",
        "c": "To record the monitor display resolution of the developer's workstation.",
        "d": "To bypass the need for automated testing and continuous integration.",
        "e": "To convert the application into a proprietary desktop binary.",
        "correct": "B",
        "topic": "04: Technical Specifications & PRD Constraints",
        "expl": "A rigorous PRD defines functional requirements, acceptance criteria, and out-of-scope boundaries, ensuring the LLM synthesizes code aligned strictly with business logic."
    },
    {
        "text": "In Week 2 Lesson 07 ('REST APIs & JSON'), what is the architectural significance of HTTP method idempotency (e.g., PUT vs POST)?",
        "a": "Idempotent methods always run 10 times faster than non-idempotent methods.",
        "b": "An idempotent request (such as PUT or DELETE) can be repeated multiple times without changing the server state beyond the initial call, whereas POST creates new subordinate resources on each invocation.",
        "c": "Idempotency means the endpoint does not require an active TCP network connection.",
        "d": "Idempotent endpoints can only be accessed using the HTTP/1.0 protocol.",
        "e": "It prevents the browser from executing pre-flight CORS OPTIONS requests.",
        "correct": "B",
        "topic": "07: REST API Idempotency & HTTP Protocols",
        "expl": "PUT is idempotent: sending identical PUT requests N times yields the exact same state as sending it once. POST is non-idempotent: repeating it creates duplicate resources."
    },
    {
        "text": "In Week 2 Lesson 10 ('Auth & Secrets Management'), why is storing raw API secret keys directly inside frontend JavaScript code or client-side bundles a severe vulnerability?",
        "a": "Because client-side JavaScript files cannot process strings longer than 16 characters.",
        "b": "Because all client-side assets are downloaded and readable by anyone inspecting browser DevTools or decompiling bundles, enabling immediate secret theft and API quota hijacking.",
        "c": "Because browsers automatically encrypt all static files with irreversible keys.",
        "d": "Because JavaScript does not support environment variable imports.",
        "e": "Because it causes the Vercel edge deployment engine to crash.",
        "correct": "B",
        "topic": "10: Secrets Management & Client-Side Leakage",
        "expl": "Frontend code is fully exposed to the client. Secrets must remain on backend servers inside isolated .env vaults, exposed only via authenticated proxy endpoints."
    },
    {
        "text": "In Week 2 Lesson 12 ('Agentic AI & Autonomous Coding'), what is the operational cycle of the ReAct (Reasoning + Acting) autonomous agent framework?",
        "a": "Execute Code -> Delete Database -> Reboot Server -> Notify User.",
        "b": "Thought (reason about current state and goal) -> Action (invoke an external tool or execute command) -> Observation (inspect environment output) -> Iterate until completion.",
        "c": "Prompt -> Memorize -> Cache -> Shutdown.",
        "d": "Single-shot token prediction without environment feedback or error correction.",
        "e": "Continuous infinite loops that never terminate or return control to the user.",
        "correct": "B",
        "topic": "12: ReAct (Reason + Act) Autonomous Cycle",
        "expl": "The ReAct loop interleaves reasoning (Thought) with action execution (Action) and output inspection (Observation), allowing agents to iteratively fix bugs."
    },
    {
        "text": "In Week 3 Lesson 13 ('LLM Internal Architecture'), why does standard Full Self-Attention suffer from quadratic computational complexity O(N^2) relative to sequence length N?",
        "a": "Because neural networks double their parameter weights after every forward pass.",
        "b": "Because every token in the sequence must compute an attention dot-product score against every other token in the sequence, producing an N × N attention matrix.",
        "c": "Because GPUs can only process data in fixed power-of-two batches.",
        "d": "Because token embeddings are expanded into 3D polygon meshes during inference.",
        "e": "Because disk I/O read operations scale quadratically with file length.",
        "correct": "B",
        "topic": "13: Self-Attention Quadratic Scaling O(N^2)",
        "expl": "Full attention calculates softmax((Q * K^T) / sqrt(d_k)) * V, requiring an N x N matrix multiplication that scales quadratically with sequence length N."
    },
    {
        "text": "In Week 3 Lesson 13, how does Byte-Pair Encoding (BPE) tokenization impact non-English languages (such as Uzbek) compared to English?",
        "a": "Non-English languages are compressed into fewer tokens than English.",
        "b": "Because BPE vocabularies are predominantly trained on English corpora, non-English words are split into multiple multi-byte subword chunks, resulting in higher token costs and latency.",
        "c": "BPE completely refuses to tokenize UTF-8 multi-byte characters.",
        "d": "Token counts are identical across all human languages regardless of training data.",
        "e": "Non-English text bypasses the embedding layer completely.",
        "correct": "B",
        "topic": "13: BPE Tokenization & Multi-Language Economics",
        "expl": "Underrepresented languages suffer from token fragmentation in BPE, consuming significantly more tokens per sentence and degrading effective context capacity."
    },
    {
        "text": "In Week 3 Lesson 13, what critical role does the Key-Value (KV) Cache play in High-Bandwidth Memory (HBM) during autoregressive LLM decoding?",
        "a": "It clears GPU VRAM after every generated token to prevent memory leaks.",
        "b": "It stores previously computed Key and Value projection tensors so that past tokens do not need their attention matrices recomputed for each newly generated token.",
        "c": "It converts floating-point weights into binary machine code.",
        "d": "It replaces the need for temperature sampling.",
        "e": "It prevents the model from generating repeating loops.",
        "correct": "B",
        "topic": "13: KV Cache & VRAM Scaling Dynamics",
        "expl": "KV Caching avoids recomputing Keys and Values for historical context during auto-regressive generation, trading GPU VRAM for massive inference speedups."
    },
    {
        "text": "In Week 3 Lesson 13, what does Stanford's 'Lost in the Middle' empirical phenomenon reveal about LLM context window attention?",
        "a": "LLMs accurately retrieve information located exclusively in the exact mathematical center of the prompt.",
        "b": "LLMs exhibit a U-shaped attention curve: retrieval accuracy is highest at the extreme beginning and end of the context window, and significantly degrades in the middle.",
        "c": "Context windows longer than 1,000 tokens always cause deterministic model crashes.",
        "d": "Placing critical instructions in the center of a prompt prevents jailbreaking.",
        "e": "Temperature must be set to 2.0 to activate middle-context memory.",
        "correct": "B",
        "topic": "13: 'Lost in the Middle' Context Placement",
        "expl": "Research shows models recall information best at the start (primacy effect) and end (recency effect) of long prompts, suffering degradation in the middle."
    },
    {
        "text": "In Week 3 Lesson 13, how does the Temperature parameter (T) mathematically alter the token probability distribution in the Softmax layer?",
        "a": "Higher temperature rounds all probabilities to integers 0 or 1.",
        "b": "Dividing logits by T > 1 flattens the distribution toward uniform probability (increasing entropy and diversity), while T -> 0 concentrates probability onto the top logit (greedy argmax).",
        "c": "Temperature controls the physical clock frequency of the GPU tensor cores.",
        "d": "T = 0 generates completely random gibberish.",
        "e": "Temperature only affects image generation models, having zero effect on text LLMs.",
        "correct": "B",
        "topic": "13: Sampling Mathematics: Softmax & Temperature",
        "expl": "In Softmax(z_i / T), as T -> 0, the maximum logit approaches probability 1.0 (deterministic). Higher T flattens the distribution, producing more diverse outputs."
    },
    {
        "text": "In Week 3 Lesson 13, how does Nucleus Sampling (Top-P) differ from fixed Top-K truncation?",
        "a": "Top-K sorts tokens alphabetically, whereas Top-P sorts them by word length.",
        "b": "Top-K restricts candidate tokens to a rigid fixed count K, whereas Top-P dynamically adjusts the candidate pool by accumulating tokens until their cumulative probability exceeds P.",
        "c": "Top-P evaluates tokens in the reverse order of generation.",
        "d": "Top-P requires manual human intervention for every token generated.",
        "e": "Top-K is an asymmetric cryptographic cipher, whereas Top-P is a hashing function.",
        "correct": "B",
        "topic": "13: Top-K vs Top-P (Nucleus) Sampling",
        "expl": "Top-P (Nucleus) dynamically expands when multiple tokens are plausible and contracts when only one token has high confidence, outperforming rigid Top-K."
    },
    {
        "text": "In Week 3 Lesson 13, why does Few-Shot In-Context prompting dramatically outperform Zero-Shot prompting for complex structured outputs?",
        "a": "Few-Shot prompting permanently updates model weights through gradient descent.",
        "b": "Providing 2–3 concrete input-output demonstration exemplars establishes a concrete semantic vector attractor, guiding the model's latent attention distribution toward the desired pattern.",
        "c": "Few-Shot prompting reduces API costs by 90%.",
        "d": "Few-Shot prompting bypasses the tokenization layer entirely.",
        "e": "Zero-Shot prompting is deprecated across all modern foundational models.",
        "correct": "B",
        "topic": "13: Few-Shot In-Context Latent Steering",
        "expl": "Exemplars align the model's conditioned generation manifold without weight fine-tuning, dramatically reducing formatting errors in structured tasks."
    },
    {
        "text": "In Week 3 Lesson 14 ('Tool Calling & Functions'), what role does a JSON Schema contract play when integrating external tools with an LLM?",
        "a": "It converts SQL database queries into binary machine assembly.",
        "b": "It provides a formal schema defining parameter types, descriptions, and required fields, allowing the model to generate structured, deterministic arguments that programmatic code can execute.",
        "c": "It formats CSS stylesheets for browser rendering.",
        "d": "It encrypts network traffic between the client and DNS resolvers.",
        "e": "It prevents the model from generating text responses.",
        "correct": "B",
        "topic": "14: Tool Calling & JSON Schema Contracts",
        "expl": "JSON Schema provides the mathematical syntax contract: the model produces structured JSON arguments conforming strictly to declared types and required keys."
    },
    {
        "text": "In Week 3 Lesson 14, how does Constrained Decoding (e.g., Grammar-Guided DFA generation) mathematically guarantee 100% valid JSON outputs from an LLM?",
        "a": "By running an asynchronous background validator that deletes invalid files.",
        "b": "During each step of autoregressive generation, a Deterministic Finite Automaton (DFA) masks out logits of any tokens that would violate the context-free grammar, allowing only valid tokens to be sampled.",
        "c": "By setting model temperature to 1.5.",
        "d": "By retraining model weights on billions of JSON files.",
        "e": "By translating all outputs into binary Base64 strings.",
        "correct": "B",
        "topic": "14: Constrained Decoding & Grammar DFAs",
        "expl": "Constrained decoding applies logit masking at inference time: if the next token violates JSON syntax rules, its logit is masked to -infinity, guaranteeing valid syntax."
    },
    {
        "text": "In Week 3 Lesson 15 ('RAG & Vector Search'), how does Retrieval-Augmented Generation fundamentally eliminate hallucination on proprietary data?",
        "a": "By permanently deleting false facts from the pre-trained weights of the foundational model.",
        "b": "By retrieving semantically relevant text chunks from a verified external vector database and injecting them into the LLM context window as factual grounding evidence.",
        "c": "By increasing model parameter size from 7B to 70B.",
        "d": "By converting all user questions into regex patterns.",
        "e": "By restricting the model to 10-word responses.",
        "correct": "B",
        "topic": "15: RAG Semantic Grounding & Hallucination Mitigation",
        "expl": "RAG separates knowledge storage (vector database) from reasoning (LLM), conditioning generation directly on retrieved factual chunks."
    },
    {
        "text": "In Week 3 Lesson 16 ('Multi-Agent Systems & Memory'), what is the architectural distinction between Context Window Memory and Long-Term Episodic Vector Memory?",
        "a": "Context memory is stored on persistent SSD drives, while episodic memory is volatile RAM.",
        "b": "Context memory is the ephemeral, token-bounded working buffer of the current inference pass, whereas episodic memory is an external vector store where past experiences and summaries are retrieved via semantic similarity.",
        "c": "Episodic memory only stores user passwords and credit card numbers.",
        "d": "Context memory requires GPU fine-tuning, whereas episodic memory does not.",
        "e": "Multi-agent systems cannot utilize episodic memory due to consensus locks.",
        "correct": "B",
        "topic": "16: Context Buffer vs Long-Term Episodic Memory",
        "expl": "Working memory is limited by context window length. Episodic memory persists across sessions in a vector index, retrieved dynamically via embeddings."
    },
    {
        "text": "In Week 4 Lesson 17 ('RAG & Embeddings'), why is Cosine Similarity preferred over Euclidean Distance (L2) when comparing dense embedding vectors of varying document lengths?",
        "a": "Cosine similarity only works on 2-dimensional integers.",
        "b": "Cosine similarity evaluates the angular orientation between two normalized vectors in high-dimensional space, measuring conceptual alignment regardless of vector magnitude.",
        "c": "Euclidean distance cannot be calculated on modern GPUs.",
        "d": "Cosine similarity guarantees 100% keyword matching accuracy.",
        "e": "Euclidean distance is an asymmetric algorithm that violates linear algebra.",
        "correct": "B",
        "topic": "17: High-Dimensional Embeddings & Cosine Similarity",
        "expl": "Cosine similarity computes dot(A, B) / (||A|| * ||B||), measuring direction rather than magnitude, making it ideal for semantic similarity across varied lengths."
    },
    {
        "text": "In Week 4 Lesson 18 ('Prompt Injection & AI Safety'), what is the critical difference between a 'Direct Prompt Injection' and an 'Indirect Prompt Injection' attack?",
        "a": "Direct injections use Python code, whereas indirect injections use JavaScript.",
        "b": "In direct injection, the adversary interacts directly with the chat input; in indirect injection, the adversary embeds malicious payload instructions inside untrusted third-party data (e.g., webpage, PDF, email) that an agent fetches and processes.",
        "c": "Direct injections damage computer hardware; indirect injections only affect software.",
        "d": "Indirect injections can only occur when the model is offline.",
        "e": "There is no architectural difference between direct and indirect prompt injection.",
        "correct": "B",
        "topic": "18: Direct vs Indirect Prompt Injection",
        "expl": "Indirect prompt injection occurs when an agent ingests untrusted external content (e.g., web scraping) containing hidden adversarial commands that hijack agent execution."
    },
    {
        "text": "In Week 4 Lesson 19 ('AI Agent Sandboxing & RCE Defense'), why is running autonomous code-generating agents inside gVisor or MicroVMs (e.g., Firecracker) essential?",
        "a": "To accelerate Python script execution speeds by 500%.",
        "b": "To prevent Remote Code Execution (RCE) escapes: standard Docker containers share the host Linux kernel, whereas gVisor intercepts syscalls in userspace and MicroVMs provide hardware-isolated virtualization.",
        "c": "Because autonomous agents cannot run on Linux without virtual machines.",
        "d": "To eliminate the need for GPU drivers.",
        "e": "To bypass operating system file permission checks.",
        "correct": "B",
        "topic": "19: Agent Sandboxing & gVisor Syscall Interception",
        "expl": "Container escapes compromise host machines. Hardened runtimes like gVisor intercept system calls in userspace, containing untrusted autonomous code execution."
    },
    {
        "text": "In Week 4 Lesson 20 ('Multi-Agent Security & Demo Day'), what is the primary defensive role of an Outbound Data Loss Prevention (Egress DLP) proxy in an autonomous agent network?",
        "a": "To download external dependencies faster from NPM and PyPI.",
        "b": "To inspect, sanitize, and block outgoing network requests from agents, preventing accidental or malicious exfiltration of API keys, PII, or internal database dumps.",
        "c": "To convert HTTP responses into WebSocket streams.",
        "d": "To shut down the agent whenever network latency exceeds 50ms.",
        "e": "To automatically commit code to public GitHub repositories.",
        "correct": "B",
        "topic": "20: Outbound Egress DLP & Exfiltration Defense",
        "expl": "Egress DLP monitors outbound traffic from agents, enforcing zero-leakage policies on proprietary credentials, database records, and system prompts."
    },
    {
        "text": "In Week 5 Lesson 21 ('Enterprise Cryptography'), why is AES-256-GCM combined with RSA-4096 / ECC in modern hybrid cryptosystems?",
        "a": "Because RSA is used for symmetric bulk data encryption and AES is used for digital signatures.",
        "b": "Because asymmetric RSA/ECC efficiently solves key exchange and digital identity verification without a pre-shared secret, while symmetric AES-256-GCM provides ultra-fast, authenticated encryption for bulk payload data.",
        "c": "Because AES-256 can only encrypt messages containing fewer than 64 characters.",
        "d": "Because RSA does not require mathematical prime numbers.",
        "e": "Because both ciphers are vulnerable to simple brute-force attacks.",
        "correct": "B",
        "topic": "21: Hybrid Cryptography: AES-256-GCM & Asymmetric RSA",
        "expl": "Asymmetric ciphers (RSA/ECC) are computationally heavy and used to exchange symmetric session keys; symmetric ciphers (AES-GCM) encrypt large payloads at wire speed."
    },
    {
        "text": "In Week 5 Lesson 22 ('Zero Trust & IAM Architecture'), what is the core tenet of the 'Zero Trust' security model and the Principle of Least Privilege?",
        "a": "Trust all internal network traffic behind the corporate office firewall implicitly.",
        "b": "Never trust, always verify: assume breach, verify identity and authorization explicitly on every request, and grant subjects only the minimum access permissions necessary to perform their tasks.",
        "c": "Eliminate all user passwords and allow anonymous access across all microservices.",
        "d": "Grant root administrator privileges to every developer to speed up sprint velocity.",
        "e": "Disable multi-factor authentication (MFA) on production database clusters.",
        "correct": "B",
        "topic": "22: Zero Trust Architecture & Least Privilege",
        "expl": "Zero Trust discards perimeter defense: every microservice request must authenticate, authorize via RBAC/ABAC, and enforce minimum required permissions."
    },
    {
        "text": "In Week 5 Lesson 23 ('API Security & Rate Limiting'), how does the 'Token Bucket' algorithm throttle high-volume client requests?",
        "a": "It deletes client accounts that make more than 5 requests per day.",
        "b": "Tokens are added to a bucket at a constant fill rate up to a max capacity; each request consumes a token, allowing short bursts while strictly capping long-term request rates.",
        "c": "It randomly drops 50% of all incoming TCP packets at the NIC layer.",
        "d": "It requires users to solve an interactive visual captcha on every single API request.",
        "e": "It delays every response by exactly 5 seconds regardless of traffic load.",
        "correct": "B",
        "topic": "23: Token Bucket Rate Limiting Algorithm",
        "expl": "Token Bucket permits burstiness up to bucket capacity while enforcing a strict steady-state refill rate, protecting production backends from DDoS and quota exhaustion."
    },
    {
        "text": "In Week 5 Lesson 23, why are HMAC (Hash-based Message Authentication Code) signatures used to secure webhooks between external providers and backend services?",
        "a": "To compress JSON payloads into gzip archives before network transmission.",
        "b": "To verify both data integrity and data authenticity, proving mathematically that the webhook payload was signed with a shared secret and was not tampered with in transit.",
        "c": "To convert HTTP POST webhooks into GET queries.",
        "d": "To hide the IP address of the destination server.",
        "e": "To disable HTTPS certificate checks on webhook endpoints.",
        "correct": "B",
        "topic": "23: Webhook Integrity & HMAC Digital Signatures",
        "expl": "HMAC combines a cryptographic hash (SHA-256) with a shared secret key, enabling the receiver to verify that the webhook payload genuinely originated from the trusted provider."
    },
    {
        "text": "In Week 5 Lesson 24 ('Production AI Telegram Bot'), why is an event-driven Webhook architecture superior to Long Polling for enterprise AI bot deployments?",
        "a": "Long polling is completely illegal under international telecommunication standards.",
        "b": "Webhooks push events instantly via HTTP POST over TLS only when a message arrives, eliminating continuous empty network polling loops, reducing server CPU/memory overhead, and enabling horizontal scaling behind a load balancer.",
        "c": "Webhooks do not require a domain name or SSL certificate.",
        "d": "Long polling uses quantum computing, which is unavailable in cloud data centers.",
        "e": "Webhooks restrict bots to receiving a maximum of 1 message per hour.",
        "correct": "B",
        "topic": "24: Telegram Bot Architecture: Webhooks vs Long Polling",
        "expl": "Webhooks provide real-time event-driven delivery (push) rather than wasteful polling (pull), enabling instant AI responses and serverless edge scaling."
    }
]

print("Grade 10-11 Vibecoding test data loaded (25 questions EN). Instructor: Ismoiljon Usmonov.")
