# ⚡ AetherCausal-Zero

**Institutional-Grade Multi-Agent Causal Inference & EVM Arbitrage Engine**

Powered by **LangGraph**, **Google Gemini API**, **Streamlit**, **Plotly**, and **Pydantic**.

---

## 🌟 Executive Summary

**AetherCausal-Zero** is a multi-agent framework designed to perform causal inference, tail-risk audit, and Bayesian probability updating for complex crypto, DeFi, and macro quantitative hypotheses. By orchestrating specialized AI agents (Bull Synthesizer, Bear Auditor, and Bayesian Arbiter) into a directed state graph, AetherCausal-Zero bridges LLM reasoning with automated EVM smart contract transaction payload generation.

---

## 🏛️ Multi-Agent Architecture & Flow

```
                      +-----------------------------+
                      |     User Input / Market     |
                      |   Regime & Market Metrics   |
                      +--------------+--------------+
                                     |
                                     v
                      +-----------------------------+
                      |   Quant Bull Synthesizer    |
                      |  Optimistic Thesis & Loops  |
                      +--------------+--------------+
                                     |
                                     v
                      +-----------------------------+
                      |   Adversarial Bear Auditor  |
                      |  Black Swans & MEV Stress   |
                      +--------------+--------------+
                                     |
                                     v
                      +-----------------------------+
                      |   Bayesian Causal Arbiter   |
                      | P(H|E) Update & Causal DAG  |
                      +--------------+--------------+
                                     |
                                     v
                      +-----------------------------+
                      |   EVM Transaction Payload   |
                      |   Hex Calldata & Guardrail  |
                      +-----------------------------+
```

---

## 🤖 Agents Overview

1. **Quant Bull Synthesizer (`quant_bull_synthesizer_node`)**:
   - Formulates positive reflexive loops, liquidity depth expansion, and upside catalysts.
   - Calculates initial Expected Value ($M) and structural confidence.

2. **Adversarial Bear Auditor (`adversarial_bear_auditor_node`)**:
   - Stress-tests the bull thesis against oracle delays, liquidation cascades, MEV sandwiching, and gas spikes.
   - Outputs a structural risk score and vulnerability vectors.

3. **Bayesian Causal Arbiter (`bayesian_causal_arbiter_node`)**:
   - Applies Bayes' Theorem $P(H|E) = \frac{P(E|H) \cdot P(H)}{P(E)}$ to synthesize prior probability and evidence likelihood.
   - Generates a 2D Causal Directed Acyclic Graph (DAG) topology.
   - Formulates executable EVM Smart Contract calldata with automated safety guardrails.

---

## 📁 Repository Structure

```
AetherCausal-Zero/
├── requirements.txt   # Python dependencies (langgraph, langchain-google-genai, streamlit, plotly)
├── engine.py          # LangGraph Multi-Agent execution engine & Pydantic state schemas
├── app.py             # Streamlit institutional dark-mode UI & Plotly visualization dashboard
└── README.md          # Comprehensive architecture & operational documentation
```

---

## ⚙️ Installation & Quickstart

### 1. Clone & Navigate
```bash
cd C:\Users\WALTON\.gemini\antigravity\scratch\AetherCausal-Zero
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Variables (Optional)
Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_google_gemini_api_key_here
```
*Note: If no API key is provided, AetherCausal-Zero automatically runs in high-fidelity deterministic engine mode so all features and UI elements remain fully functional.*

### 4. Run the Dashboard
```bash
streamlit run app.py
```

---

## 🖥️ Dashboard Features

- **🎯 Strategic Causal Verdict Tab**: Real-time Bayesian posterior confidence gauge, key metric tiles, and structured Bull vs. Bear vs. Arbiter verification matrix.
- **🕸️ Interactive Causal DAG Tab**: Plotly network graph visualizer showing cause-and-effect nodes (Triggers, Vulnerabilities, Catalysts, Actions) and weighted directed edges.
- **🧠 Multi-Agent Thought Stream Tab**: Live execution timeline showing step-by-step agent reasoning, timestamps, and full raw JSON outputs.
- **⚡ EVM Payload Simulator Tab**: Smart contract rebalance calldata hex generator, gas limit estimator, method selector parser, and guardrail validation status.

---

## 🛡️ License

MIT License. Built for Institutional Crypto Quantitative Research and Multi-Agent AI System Prototyping.
