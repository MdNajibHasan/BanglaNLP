# Zero-Shot Multi-Label Classification of Bangla Documents

Code and experiment scripts for the paper:

**Zero-Shot Multi-Label Classification of Bangla Documents: Large Decoders vs. Classic Encoders.**

This repo contains:
- The BanglaNewsNet benchmark pipeline
- Encoder-based zero-shot MLC experiments
- LLM-based embedding and prompt experiments
- Scripts to reproduce the F1, precision, and recall tables from the paper


## 1. Overview

Bangla is one of the most spoken languages in the world but still low-resource in NLP.  
This work compares classic encoders and large decoder-based models for zero-shot multi-label classification on Bangla news articles.

We:
- Build the BanglaNewsNet corpus from online Bangla news
- Create label embeddings with two strategies:
  - Label name + keywords
  - Explicit-mentions from labeled articles
- Evaluate 32 models, including LASER, LaBSE, BanglaTransformer, BLOOM, FLAN-UL2, GPT-NeoX, Gemini, GPT, Llama, Qwen, DeepSeek, BanglaLlama, and others
- Report precision, recall, and micro-F1 for encoder and LLM setups


## 2. Setup

### 2.1. Environment

```bash
git clone https://github.com/MdNajibHasan/BanglaNLP.git
cd src

python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate

pip install -r requirements.txt
