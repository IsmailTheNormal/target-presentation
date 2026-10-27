#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
10–11th Grade: 25-Question Vibecoding Senior Engineering, Autonomous Agents & LLM Architecture Exam
Instructor: Ismoiljon Usmonov · Target International School
English Version Only (5 options: A, B, C, D, E per question)
"""

META_10_11_EN = {
    "school_name": "TARGET INTERNATIONAL SCHOOL — YUNUSOBOD",
    "teacher_name": "Ismoiljon Usmonov",
    "exam_title": "GRADES 10–11: VIBECODING SENIOR ENGINEERING, AUTONOMOUS AGENTS & LLM ARCHITECTURE",
    "track_title": "Senior AI Engineering & Vibecoding Track · Instructor: Ismoiljon Usmonov",
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
    "subheading": "Instructor: Ismoiljon Usmonov · Official Vibecoding Senior Key (Grades 10–11, 25 Questions)",
    "table_headers": ["№", "Key", "Topic / Competency", "Technical Explanation & Justification"],
    "scale_heading": "Official 25-Point Senior Grading Scale:",
    "rubric_tiers": [
        {"grade": "Excellent (A / 5)", "range": "22 – 25 pts", "desc": "Mastery of LLM architecture, ReAct loops, RAG, Multi-Agent systems, and MCP"},
        {"grade": "Good (B / 4)", "range": "18 – 21 pts", "desc": "Solid grasp of tool calling, sampling math, context dynamics, and sandboxing"},
        {"grade": "Satisfactory (C / 3)", "range": "13 – 17 pts", "desc": "Core concepts understood; requires review of KV cache, BPE, and PromptOps"},
        {"grade": "Needs Review (D / 2)", "range": "0 – 12 pts", "desc": "Critical Vibecoding engineering foundations need structured re-examination"}
    ]
}

QUESTIONS_10_11_EN = [
    {
        "text": "In the modern software engineering paradigm, how does 'Vibecoding' transform the role of a Senior Software Engineer?",
        "a": "The engineer stops understanding software and blindly copies unverified AI outputs.",
        "b": "The engineer ascends to an architect and systems conductor: framing precise PRDs, orchestrating autonomous AI agent swarms, auditing code diffs, verifying safety guardrails, and steering system integration.",
        "c": "The engineer only writes documentation in Microsoft Word.",
        "d": "The engineer replaces all computers with typewriter machines.",
        "e": "The engineer is restricted to writing raw binary machine instructions.",
        "correct": "B",
        "topic": "Vibecoding as Senior Paradigm",
        "expl": "Vibecoding shifts the engineer's cognitive focus from tedious syntax typing to architectural decision-making, prompt evaluation, and multi-agent coordination."
    },
    {
        "text": "In the Transformer architecture, what is the core role of the Self-Attention mechanism and its Query, Key, Value (Q, K, V) projection matrices?",
        "a": "To compress JPEG images into WebP format.",
        "b": "To dynamically calculate pairwise relevance scores between all tokens in a sequence, allowing the model to weigh semantic relationships regardless of distance.",
        "c": "To convert Python source code into x86 assembly language.",
        "d": "To regulate the electric voltage of GPU cooling fans.",
        "e": "To permanently encrypt the model weights on disk.",
        "correct": "B",
        "topic": "Self-Attention (Q, K, V) Matrices",
        "expl": "Self-Attention computes attention weights: Softmax((Q * K^T) / sqrt(d_k)) * V, capturing long-range contextual relationships across tokens."
    },
    {
        "text": "Why does standard Full Self-Attention suffer from quadratic computational complexity O(N^2) relative to context length N?",
        "a": "Because the model must download weights over the internet for every token.",
        "b": "Because every token must compute an attention score against every other token in the sequence, producing an N x N attention matrix.",
        "c": "Because Python executes loops 10 times slower than C++.",
        "d": "Because RAM storage is physically divided into square chips.",
        "e": "Because prompt text must be translated into French before inference.",
        "correct": "B",
        "topic": "Quadratic Context Complexity O(N^2)",
        "expl": "Pairwise attention calculations between N tokens produce an N x N matrix, making compute and memory scale quadratically with context length."
    },
    {
        "text": "How does BPE (Byte-Pair Encoding) tokenization impact token economics and multi-language performance in LLMs?",
        "a": "It forces all words to be exactly 4 letters long.",
        "b": "It iteratively merges frequent byte pairs into subwords; languages with non-Latin scripts (e.g., Cyrillic or Uzbek) often require multiple tokens per word, incurring a token penalty compared to English.",
        "c": "It deletes all numbers from the input text.",
        "d": "It encrypts the prompt using AES-256 before inference.",
        "e": "It prevents the model from generating whitespace characters.",
        "correct": "B",
        "topic": "BPE Tokenization & Token Economics",
        "expl": "BPE tokenizes common subwords. Script disparity causes non-English languages to decompose into more subword tokens, consuming more context and budget."
    },
    {
        "text": "What is the function of the Key-Value (KV) Cache in GPU High-Bandwidth Memory (HBM) during auto-regressive decoding?",
        "a": "To store web browsing history in the browser cache.",
        "b": "To store precomputed Key and Value attention tensors of previous tokens, avoiding redundant quadratic re-computation for each newly generated token.",
        "c": "To replace the GPU driver with a CPU emulator.",
        "d": "To automatically convert floating-point numbers to integers.",
        "e": "To back up the database every 10 milliseconds.",
        "correct": "B",
        "topic": "KV Cache & GPU Memory Dynamics",
        "expl": "Auto-regressive generation appends one token at a time; caching prior K and V tensors avoids recomputing previous tokens, reducing per-token complexity to O(N)."
    },
    {
        "text": "What does the empirical phenomenon known as 'Lost in the Middle' describe in long-context LLM retrieval?",
        "a": "The model's power cord being unplugged halfway through inference.",
        "b": "A U-shaped retrieval accuracy curve where models demonstrate high recall for facts located at the very beginning or end of context, but frequently miss information buried in the middle.",
        "c": "The model randomly deleting the 50th line of code.",
        "d": "The model refusing to answer questions asked in the afternoon.",
        "e": "The loss of internet connectivity during API calls.",
        "correct": "B",
        "topic": "'Lost in the Middle' & Context Placement",
        "expl": "Research from Stanford shows LLM attention is strongest at context boundaries; critical instructions should be 'sandwiched' at the beginning and end."
    },
    {
        "text": "Mathematically, what effect does adjusting the Temperature parameter (T) have on the model's Softmax output probability distribution?",
        "a": "It raises the physical temperature of the silicon chip.",
        "b": "Dividing logits by T scales probability flatness: T -> 0 approaches a one-hot greedy argmax (deterministic), while T > 1 flattens the distribution, increasing sampling diversity.",
        "c": "It forces the model to output only uppercase letters.",
        "d": "It increases the network download speed of the response.",
        "e": "It permanently changes the model's training weights.",
        "correct": "B",
        "topic": "Sampling Mathematics: Temperature",
        "expl": "Softmax(z_i / T) sharpens the distribution as T decreases (making high-probability tokens dominate) and flattens it as T increases (increasing entropy)."
    },
    {
        "text": "How does Top-P (Nucleus) sampling differ fundamentally from Top-K sampling?",
        "a": "Top-P is only compatible with Python, while Top-K is strictly for JavaScript.",
        "b": "Top-K restricts sampling to a rigid fixed number of top tokens (K), while Top-P dynamically pools the smallest set of tokens whose cumulative probability exceeds threshold P.",
        "c": "Top-P sampling always picks the least probable token.",
        "d": "Top-K sampling calculates mathematical square roots.",
        "e": "There is no functional difference between Top-K and Top-P.",
        "correct": "B",
        "topic": "Top-K vs Top-P (Nucleus) Truncation",
        "expl": "Nucleus sampling adapts dynamically: in certain contexts the candidate pool is narrow (1-2 tokens), while in ambiguous contexts it expands naturally."
    },
    {
        "text": "Why is Few-Shot prompting significantly more robust than Zero-Shot prompting for structured data extraction?",
        "a": "Because Few-Shot prompts cost zero tokens.",
        "b": "Providing canonical input-output demonstration pairs anchors the model's latent representation in the desired schema, formatting style, and edge-case handling.",
        "c": "Because Few-Shot prompts disable the model's tokenizer.",
        "d": "Because Few-Shot prompts allow the model to bypass server authentication.",
        "e": "Because Zero-Shot prompting is deprecated across all cloud APIs.",
        "correct": "B",
        "topic": "In-Context Learning: Zero-Shot vs Few-Shot",
        "expl": "Few-shot examples provide in-context calibration, eliminating ambiguity and guiding the model's latent space toward strict target representations."
    },
    {
        "text": "What is the architectural purpose of a System Prompt (Model Constitution) in production LLM applications?",
        "a": "To store the user's credit card information.",
        "b": "To establish immutable behavioral bounds, persona, procedural protocols, tool permissions, and defensive refusal guardrails before user prompt injection occurs.",
        "c": "To compile TypeScript code into bytecode.",
        "d": "To restart the operating system kernel.",
        "e": "To render HTML components in the browser DOM.",
        "correct": "B",
        "topic": "System Prompts & Constitutional AI",
        "expl": "System prompts set higher-priority behavioral conditioning and constraints that frame how subsequent user inputs are interpreted and executed."
    },
    {
        "text": "Under the hood, how does LLM Tool Calling (Function Calling) execute when connected to external APIs?",
        "a": "The LLM executes arbitrary machine code directly inside its own neural network weights.",
        "b": "The model is provided JSON Schema definitions of available tools; when a tool is needed, it halts generation and outputs a structured JSON payload containing the function name and validated arguments.",
        "c": "The model sends an unencrypted SMS to the database administrator.",
        "d": "The model opens a physical terminal window on the client's laptop.",
        "e": "The model automatically rewrites its own transformer architecture.",
        "correct": "B",
        "topic": "Tool Calling Mechanics & JSON Schema",
        "expl": "The model does not execute code itself; it emits structured JSON matching the tool's JSON Schema, allowing the hosting runtime to execute the API and feed back results."
    },
    {
        "text": "What is the four-step iterative cycle of the ReAct (Reasoning + Acting) autonomous agent framework?",
        "a": "Copy, Paste, Save, Delete.",
        "b": "Thought (reasoning about state) -> Action (invoking a specific tool) -> Observation (ingesting tool output) -> Final Answer / Next Loop iteration.",
        "c": "Compile, Link, Execute, Crash.",
        "d": "Download, Unzip, Install, Reboot.",
        "e": "Request, Wait, Timeout, Fail.",
        "correct": "B",
        "topic": "The ReAct Loop Paradigm",
        "expl": "ReAct interleaves reasoning traces ('Thought') with action execution ('Action') and environment feedback ('Observation') until the goal is achieved."
    },
    {
        "text": "In Retrieval-Augmented Generation (RAG), why is chunking strategy and chunk overlap critical for retrieval quality?",
        "a": "To make text files fit on 3.5-inch floppy disks.",
        "b": "Chunking ensures semantic coherence within vector embedding limits, while overlap preserves contextual continuity across chunk boundaries, preventing split-fact loss.",
        "c": "To ensure every word in the document is capitalized.",
        "d": "To convert markdown files into binary audio files.",
        "e": "To double the cost of cloud database subscriptions.",
        "correct": "B",
        "topic": "RAG Chunking Strategies & Overlap",
        "expl": "Chunking fits text into embedding token limits; overlap ensures facts that span across chunk boundaries are not severed and lost during vector lookup."
    },
    {
        "text": "How is Cosine Similarity mathematically computed between a user query embedding vector (A) and document vector (B)?",
        "a": "By subtracting vector lengths: ||A|| - ||B||.",
        "b": "By dividing the dot product of A and B by the product of their Euclidean magnitudes: (A · B) / (||A|| * ||B||), measuring angular orientation rather than vector length.",
        "c": "By adding all numbers in vector A to vector B.",
        "d": "By converting both vectors into hexadecimal strings.",
        "e": "By multiplying vector A by the temperature parameter.",
        "correct": "B",
        "topic": "Vector Embeddings & Cosine Similarity",
        "expl": "Cosine similarity measures the cosine of the angle between two multi-dimensional vectors, evaluating semantic alignment independent of text length."
    },
    {
        "text": "In enterprise vector search engines (e.g., Pinecone, Milvus, pgvector), what advantage does HNSW (Hierarchical Navigable Small World) indexing provide over brute-force kNN?",
        "a": "HNSW guarantees that vectors consume zero bytes of RAM.",
        "b": "HNSW builds a multi-layered graph enabling logarithmic O(log N) approximate nearest neighbor (ANN) retrieval across billions of vectors, replacing linear O(N) exhaustive scans.",
        "c": "HNSW eliminates the need for mathematical vectors entirely.",
        "d": "HNSW only works on computers without internet connections.",
        "e": "HNSW automatically formats the hard drive every month.",
        "correct": "B",
        "topic": "HNSW Vector Indexing",
        "expl": "HNSW uses hierarchical skip-list graph structures for sub-linear O(log N) nearest neighbor search across massive high-dimensional datasets."
    },
    {
        "text": "In a Multi-Agent architecture (e.g., Architect, Coder, Reviewer, QA), how do specialized subagents improve code quality compared to a single monolithic prompt?",
        "a": "They consume fewer total API tokens by skipping code execution.",
        "b": "Separation of concerns: dedicated persona prompts evaluate code from distinct perspectives (e.g., adversarial QA looks for bugs, Architect ensures modularity), catching blind spots through consensus.",
        "c": "They prevent the computer from overheating.",
        "d": "They allow code to run without needing an operating system.",
        "e": "They eliminate the need for version control like Git.",
        "correct": "B",
        "topic": "Multi-Agent Architectures & Consensus",
        "expl": "Multi-agent systems divide complex tasks into specialized roles with independent evaluation loops, mitigating single-prompt fatigue and cognitive drift."
    },
    {
        "text": "How does the 'Reflexion' agent architecture enhance problem-solving over standard chain-of-thought prompting?",
        "a": "By making the screen mirror the user's reflection using the camera.",
        "b": "By incorporating verbal self-reflection after execution failure, writing retrospective critiques into episodic memory to guide subsequent trajectory attempts.",
        "c": "By automatically shutting down after any error occurs.",
        "d": "By forcing the AI model to wait 24 hours between prompt executions.",
        "e": "By translating all error messages into Latin.",
        "correct": "B",
        "topic": "Reflexion Loops & Episodic Memory",
        "expl": "Reflexion agents evaluate execution traces (e.g., failing unit tests), synthesize verbal self-critique, and utilize that critique as memory in the next iteration."
    },
    {
        "text": "What is the difference between an AI agent's Context Memory and Episodic Vector Memory?",
        "a": "Context memory is stored on floppy disks, while episodic memory is stored in the CPU cache.",
        "b": "Context memory is short-term transient state held within the active LLM context window, while episodic memory is long-term persistent experience indexed in an external vector store.",
        "c": "Context memory only works with images, while episodic memory only handles plain text.",
        "d": "There is no difference; all memory is erased when the token stream finishes.",
        "e": "Context memory requires paid licenses, while episodic memory is always free.",
        "correct": "B",
        "topic": "Short-Term Context vs Long-Term Episodic Memory",
        "expl": "Context memory is bound by context window limits ($N$ tokens); episodic memory persists across sessions in vector DBs, retrieved dynamically when relevant."
    },
    {
        "text": "How does Constrained Decoding (Grammar-Guided DFA generation) guarantee 100% syntactically valid JSON output from an LLM?",
        "a": "By retrying the prompt 100 times until a valid JSON appears.",
        "b": "By masking invalid token logits at each sampling step using a Deterministic Finite Automaton (DFA) derived from a formal grammar (CFG), making invalid syntax mathematically impossible.",
        "c": "By running regex checks after the entire response has finished streaming.",
        "d": "By converting all text to base64 encoding before generation.",
        "e": "By deleting non-JSON characters from the terminal output.",
        "correct": "B",
        "topic": "Constrained Decoding & Grammar DFAs",
        "expl": "Constrained decoding (e.g., Outlines, Guidance) adjusts logit masks at each token step according to DFA states, mathematically guaranteeing schema adherence."
    },
    {
        "text": "What distinguishes an 'Indirect Prompt Injection' attack from a direct jailbreak attempt?",
        "a": "Indirect injection can only be performed by hardware robots.",
        "b": "The malicious payload is embedded inside untrusted third-party data (e.g., web pages, PDFs, customer tickets) that the agent autonomously retrieves, hijacking execution without direct user prompt tampering.",
        "c": "Direct jailbreak requires physical physical access to the GPU server room.",
        "d": "Indirect prompt injection always causes an immediate kernel panic.",
        "e": "There is no difference between direct and indirect injection.",
        "correct": "B",
        "topic": "Indirect Prompt Injection in RAG & Agents",
        "expl": "Indirect prompt injection weapons external data streams retrieved by agents, instructing the model to exfiltrate private data or perform unauthorized tool calls."
    },
    {
        "text": "Why must autonomous code-executing AI agents run within hardened sandboxes (e.g., Docker, gVisor, or WebAssembly)?",
        "a": "To make code execute 10 times slower for visual inspection.",
        "b": "To prevent Remote Code Execution (RCE) escape: an agent running arbitrary code could delete system files, access internal network credentials, or spawn cryptominers on the host server.",
        "c": "Because Node.js cannot run without a sandbox.",
        "d": "To encrypt keyboard keystrokes during development.",
        "e": "To avoid paying cloud hosting fees.",
        "correct": "B",
        "topic": "Agent Sandboxing & RCE Isolation",
        "expl": "Agent-generated code is untrusted by definition; sandboxing limits system calls, isolates network namespaces, and protects host infrastructure from exploits."
    },
    {
        "text": "What architectural role do Guardrail systems (such as NVIDIA NeMo Guardrails or Llama Guard) fulfill in production deployments?",
        "a": "They physically mount server racks in data centers.",
        "b": "They serve as programmable validation layers intercepting both input prompts and output generations to enforce topic boundaries, scrub PII, and block toxic or adversarial payloads.",
        "c": "They automatically increase software subscription prices.",
        "d": "They convert text outputs into vector illustrations.",
        "e": "They prevent GPUs from consuming electricity.",
        "correct": "B",
        "topic": "AI Guardrails Middleware",
        "expl": "Guardrail frameworks act as pre-inference and post-inference filters, checking conversational flows against programmable safety and policy guidelines."
    },
    {
        "text": "In modern PromptOps, how does 'LLM-as-a-Judge' automated evaluation integrate into CI/CD pipelines?",
        "a": "A human judge sits in the server room and rates responses manually.",
        "b": "A high-capability model (e.g., Claude 3.5 Sonnet / GPT-4) systematically scores candidate agent outputs against gold-standard evaluation rubrics, asserting consistency across prompt releases.",
        "c": "The model deletes all unit tests that fail.",
        "d": "The model checks only if the code has comments.",
        "e": "The model compares response lengths without reading content.",
        "correct": "B",
        "topic": "PromptOps & LLM-as-a-Judge Evals",
        "expl": "Automated evaluation pipelines use capable evaluator models to score outputs on metrics like factuality, reasoning, and schema adherence in CI/CD."
    },
    {
        "text": "What is the primary objective of Anthropic's Model Context Protocol (MCP) in the AI ecosystem?",
        "a": "To replace the HTTP protocol across the entire worldwide web.",
        "b": "To provide an open, standardized protocol enabling LLM agents to seamlessly connect to external tools, local filesystems, databases, and APIs without custom point-to-point integrations.",
        "c": "To force all AI models to use the same proprietary weights.",
        "d": "To disable all open-source AI development.",
        "e": "To restrict AI usage to desktop computers only.",
        "correct": "B",
        "topic": "Model Context Protocol (MCP)",
        "expl": "MCP standardizes client-server interfaces for exposing tools, resources, and prompt templates to AI agents, replacing fragmented custom plugins."
    },
    {
        "text": "What architectural pillars define a resilient, enterprise-grade Autonomous Vibecoding production deployment?",
        "a": "A single prompt, no logs, zero automated tests, and unrestricted root privileges.",
        "b": "Deterministic schema validation, multi-agent consensus, sandboxed code execution, telemetry logging (OpenTelemetry), and continuous eval benchmarking in CI/CD.",
        "c": "Relying entirely on manual copy-pasting of code by human interns.",
        "d": "Disabling all firewall rules and removing database passwords.",
        "e": "Writing code exclusively on paper before scanning into PDF.",
        "correct": "B",
        "topic": "Enterprise Production Deployment Standards",
        "expl": "Production Vibecoding systems require deterministic schemas, sandboxed execution, continuous evaluations, and observability to ensure reliability at scale."
    }
]

print("Grade 10-11 Vibecoding test data loaded (25 questions EN). Instructor: Ismoiljon Usmonov.")
