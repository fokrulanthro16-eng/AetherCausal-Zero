"""
AetherCausal-Zero: Institutional Dark-Mode Multi-Agent Causal Dashboard
Streamlit + Plotly + LangGraph + Gemini API
"""

import os
import json
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
from dotenv import load_dotenv

# Import Multi-Agent LangGraph Engine
from engine import run_causal_inference

load_dotenv()

# ==========================================
# 1. Page Configuration & Custom CSS
# ==========================================

st.set_page_config(
    page_title="AetherCausal-Zero | Multi-Agent Causal Inference",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Institutional Dark-Mode Theme CSS
st.markdown("""
<style>
    /* Dark Obsidian Base */
    .stApp {
        background-color: #0b0f19;
        color: #e2e8f0;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
    
    /* Header Styling */
    .header-title {
        font-size: 2.2rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        background: linear-gradient(135deg, #00f3ff 0%, #00ff9d 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    
    .header-subtitle {
        font-size: 0.95rem;
        color: #94a3b8;
        font-weight: 400;
        margin-bottom: 20px;
    }
    
    /* Obsidian Card Container */
    .obsidian-card {
        background: rgba(15, 23, 42, 0.75);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 20px;
        backdrop-filter: blur(12px);
        margin-bottom: 16px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
    }
    
    /* Verdict Status Pills */
    .pill-approved {
        background: rgba(0, 255, 157, 0.15);
        color: #00ff9d;
        border: 1px solid rgba(0, 255, 157, 0.4);
        padding: 6px 14px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.85rem;
        display: inline-block;
    }
    
    .pill-conditional {
        background: rgba(255, 183, 0, 0.15);
        color: #ffb700;
        border: 1px solid rgba(255, 183, 0, 0.4);
        padding: 6px 14px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.85rem;
        display: inline-block;
    }
    
    .pill-rejected {
        background: rgba(255, 51, 102, 0.15);
        color: #ff3366;
        border: 1px solid rgba(255, 51, 102, 0.4);
        padding: 6px 14px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.85rem;
        display: inline-block;
    }
    
    /* Metric Badge */
    .metric-value {
        font-size: 1.8rem;
        font-weight: 700;
        color: #ffffff;
    }
    .metric-label {
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #64748b;
    }

    /* Thought Timeline */
    .thought-node {
        border-left: 3px solid #00f3ff;
        padding-left: 14px;
        margin-bottom: 14px;
        background: rgba(30, 41, 59, 0.4);
        border-radius: 0 8px 8px 0;
        padding-top: 8px;
        padding-bottom: 8px;
    }

    /* Table Customization */
    div[data-testid="stTable"] {
        border-radius: 8px;
        overflow: hidden;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }
</style>
""", unsafe_allow_html=True)


# ==========================================
# 2. Sidebar Controls
# ==========================================

st.sidebar.markdown("### ⚙️ Institutional Settings")

# Gemini API Key Input
api_key_input = st.sidebar.text_input(
    "Google Gemini API Key",
    type="password",
    value=os.environ.get("GEMINI_API_KEY", ""),
    help="Enter Gemini API key for live LLM execution. Leaves blank for high-fidelity mock mode."
)

force_mock_toggle = st.sidebar.checkbox(
    "Force High-Fidelity Mock Mode",
    value=not bool(api_key_input),
    help="Enable deterministic simulation without remote API calls."
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🌐 Target Network & Protocol")
target_network = st.sidebar.selectbox(
    "Deployment Chain",
    ["Ethereum Mainnet", "Arbitrum One", "Base", "Solana Mainnet"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Market Regime Parameters")

vol_index = st.sidebar.slider("Volatility Index (VIX / Vol)", 10, 100, 45, help="Implied annualized market volatility.")
oracle_delay = st.sidebar.slider("Oracle Delay (Seconds)", 1, 30, 8, help="Pyth/Chainlink update lag under stress.")
liquidity_depth = st.sidebar.slider("DEX Liquidity Depth ($M)", 5.0, 500.0, 120.0, help="Available depth within 2% slippage.")
gas_price = st.sidebar.slider("Gas Base Fee (Gwei)", 5, 200, 35, help="Network execution cost factor.")
macro_regime = st.sidebar.selectbox("Macro Regime", ["High-Vol Arbitrage", "Systemic De-risk", "Yield Compression", "Liquidity Contagion"])

market_context = {
    "volatility_index": vol_index,
    "oracle_delay_sec": oracle_delay,
    "liquidity_depth_m": liquidity_depth,
    "gas_gwei": gas_price,
    "macro_regime": macro_regime
}

st.sidebar.markdown("---")
st.sidebar.markdown("### 🧪 Hypothesis Preset Selector")
preset_choice = st.sidebar.selectbox(
    "Select Scenario Preset",
    [
        "ETH Liquid Staking Yield Cascade",
        "Solana De-peg Pyth Oracle Lag",
        "RWA Treasury Yield Unwind",
        "Custom User Hypothesis"
    ]
)

presets = {
    "ETH Liquid Staking Yield Cascade": "ETH liquid staking yield decay triggers 15% collateral de-peg and cascade liquidation in Aave v3 within 72 hours.",
    "Solana De-peg Pyth Oracle Lag": "Pyth Oracle feed delay > 12s during high volatility triggers cross-DEX arbitrage liquidity drain on Solana.",
    "RWA Treasury Yield Unwind": "Tokenized US Treasury yield compression forces algorithmic unwinding of leveraged delta-neutral vaults.",
}

if preset_choice in presets:
    default_hypothesis = presets[preset_choice]
else:
    default_hypothesis = "Cross-protocol flash-loan rebalance triggers arbitrage equilibrium across decentralized liquidity pools."

hypothesis_input = st.sidebar.text_area(
    "Hypothesis to Analyze",
    value=default_hypothesis,
    height=110
)

run_button = st.sidebar.button("⚡ Run Multi-Agent Causal Engine", type="primary", use_container_width=True)


# ==========================================
# 3. Main Header & Session State Management
# ==========================================

col_h1, col_h2 = st.columns([3, 1])

with col_h1:
    st.markdown('<div class="header-title">AETHERCAUSAL-ZERO</div>', unsafe_allow_html=True)
    st.markdown('<div class="header-subtitle">LangGraph Multi-Agent Causal Inference & EVM Arbitrage Engine</div>', unsafe_allow_html=True)

with col_h2:
    mode_status = "🟢 Live Gemini LLM" if (api_key_input and not force_mock_toggle) else "⚡ Deterministic Engine"
    st.markdown(f"""
    <div style="text-align: right; padding-top: 10px;">
        <span style="background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(255,255,255,0.1); padding: 6px 12px; border-radius: 8px; font-size: 0.8rem; font-weight: 600;">
            {mode_status}
        </span>
        <br>
        <span style="font-size: 0.75rem; color: #64748b;">Chain: {target_network}</span>
    </div>
    """, unsafe_allow_html=True)

# Run Inference if button clicked or initial state empty
if "engine_result" not in st.session_state or run_button:
    with st.spinner("Executing LangGraph Multi-Agent Nodes (Bull -> Bear -> Arbiter)..."):
        res = run_causal_inference(
            hypothesis=hypothesis_input,
            market_context=market_context,
            target_network=target_network,
            api_key=api_key_input,
            force_mock=force_mock_toggle
        )
        st.session_state["engine_result"] = res

state = st.session_state["engine_result"]
arbiter = state.get("arbiter_verdict") or {}
bull = state.get("bull_analysis") or {}
bear = state.get("bear_audit") or {}
thought_stream = state.get("thought_stream") or []


# ==========================================
# 4. Interactive Tabs Layout
# ==========================================

tab1, tab2, tab3, tab4 = st.tabs([
    "🎯 Strategic Causal Verdict",
    "🕸️ Interactive Causal DAG",
    "🧠 Multi-Agent Thought Stream",
    "⚡ EVM Payload Simulator"
])


# ------------------------------------------
# TAB 1: Strategic Causal Verdict
# ------------------------------------------
with tab1:
    col_verdict, col_gauge = st.columns([1.6, 1])
    
    with col_verdict:
        verdict_code = arbiter.get("strategic_verdict", "PENDING")
        if verdict_code == "APPROVED_EXECUTION":
            pill_html = '<span class="pill-approved">✓ APPROVED EXECUTION</span>'
        elif verdict_code == "CONDITIONAL_REBALANCE":
            pill_html = '<span class="pill-conditional">⚠️ CONDITIONAL REBALANCE</span>'
        else:
            pill_html = '<span class="pill-rejected">🛑 HIGH RISK REJECTED</span>'
            
        st.markdown(f"""
        <div class="obsidian-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                <span style="font-size: 0.85rem; font-weight: 700; color: #94a3b8; letter-spacing: 0.05em;">BAYESIAN ARBITER VERDICT</span>
                {pill_html}
            </div>
            <h3 style="color: #ffffff; margin-top: 0px; font-weight: 700;">{hypothesis_input}</h3>
            <p style="color: #cbd5e1; font-size: 0.95rem; line-height: 1.6;">
                {arbiter.get("verdict_explanation", "No arbitration explanation generated.")}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # 4 Metric Tiles
        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.markdown(f"""
            <div class="obsidian-card" style="text-align: center; padding: 14px;">
                <div class="metric-label">Prior P(H)</div>
                <div class="metric-value" style="color: #94a3b8;">{arbiter.get('bayesian_prior', 0.5):.2f}</div>
            </div>
            """, unsafe_allow_html=True)
        with m2:
            st.markdown(f"""
            <div class="obsidian-card" style="text-align: center; padding: 14px;">
                <div class="metric-label">Posterior P(H|E)</div>
                <div class="metric-value" style="color: #00f3ff;">{arbiter.get('bayesian_posterior', 0.0):.2f}</div>
            </div>
            """, unsafe_allow_html=True)
        with m3:
            st.markdown(f"""
            <div class="obsidian-card" style="text-align: center; padding: 14px;">
                <div class="metric-label">Bull Expected EV</div>
                <div class="metric-value" style="color: #00ff9d;">${bull.get('expected_ev_millions', 0.0):.1f}M</div>
            </div>
            """, unsafe_allow_html=True)
        with m4:
            st.markdown(f"""
            <div class="obsidian-card" style="text-align: center; padding: 14px;">
                <div class="metric-label">Bear Risk Score</div>
                <div class="metric-value" style="color: #ff3366;">{bear.get('risk_score', 0.0)*100:.0f}%</div>
            </div>
            """, unsafe_allow_html=True)

    with col_gauge:
        confidence = arbiter.get("adjusted_confidence", 50.0)
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=confidence,
            number={'suffix': "%", 'font': {'color': "#ffffff", 'size': 38}},
            title={'text': "Causal Bayesian Confidence", 'font': {'color': "#94a3b8", 'size': 14}},
            gauge={
                'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#475569"},
                'bar': {'color': "#00f3ff" if confidence > 50 else "#ff3366"},
                'bgcolor': "rgba(15, 23, 42, 0.6)",
                'borderwidth': 1,
                'bordercolor': "rgba(255,255,255,0.1)",
                'steps': [
                    {'range': [0, 45], 'color': 'rgba(255, 51, 102, 0.2)'},
                    {'range': [45, 65], 'color': 'rgba(255, 183, 0, 0.2)'},
                    {'range': [65, 100], 'color': 'rgba(0, 255, 157, 0.2)'}
                ],
                'threshold': {
                    'line': {'color': "#ffffff", 'width': 3},
                    'thickness': 0.75,
                    'value': 65
                }
            }
        ))
        fig_gauge.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=280,
            margin=dict(l=20, r=20, t=50, b=20)
        )
        st.plotly_chart(fig_gauge, use_container_state=True)

    # Verification Matrix Table
    st.markdown("### 📋 Causal Verification Matrix (Bull vs Bear vs Arbiter)")
    matrix_data = arbiter.get("verification_matrix", [])
    if matrix_data:
        st.table(matrix_data)
    else:
        st.info("No verification matrix available.")


# ------------------------------------------
# TAB 2: Interactive Causal Graph (DAG)
# ------------------------------------------
with tab2:
    st.markdown("### 🕸️ Directed Acyclic Graph (DAG) Topology")
    st.markdown("Visualization of causal dependencies, trigger nodes, vulnerabilities, and target execution actions.")
    
    nodes = arbiter.get("causal_nodes", [])
    edges = arbiter.get("causal_edges", [])
    
    if nodes and edges:
        # Construct Plotly 2D Graph Layout
        node_x = []
        node_y = []
        node_text = []
        node_color = []
        
        # Coordinate layout positioning mapping
        pos_map = {
            "node_1": (0.1, 0.5),
            "node_2": (0.35, 0.8),
            "node_3": (0.35, 0.2),
            "node_4": (0.65, 0.5),
            "node_5": (0.9, 0.5)
        }
        
        color_map = {
            "TRIGGER": "#00f3ff",
            "VULNERABILITY": "#ff3366",
            "CATALYST": "#ffb700",
            "VERDICT_ACTION": "#00ff9d"
        }
        
        edge_x = []
        edge_y = []
        
        for edge in edges:
            src = pos_map.get(edge["source"], (0.1, 0.5))
            tgt = pos_map.get(edge["target"], (0.9, 0.5))
            edge_x.extend([src[0], tgt[0], None])
            edge_y.extend([src[1], tgt[1], None])
            
        edge_trace = go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=2, color='#475569'),
            hoverinfo='none',
            mode='lines'
        )
        
        for n in nodes:
            nid = n["id"]
            p = pos_map.get(nid, (0.5, 0.5))
            node_x.append(p[0])
            node_y.append(p[1])
            node_text.append(f"<b>{n['label']}</b><br>Type: {n['type']}<br>Impact: {n['impact_score']}")
            node_color.append(color_map.get(n['type'], "#ffffff"))
            
        node_trace = go.Scatter(
            x=node_x, y=node_y,
            mode='markers+text',
            hoverinfo='text',
            text=[n['label'] for n in nodes],
            textposition="bottom center",
            hovertext=node_text,
            marker=dict(
                size=32,
                color=node_color,
                line_width=2,
                line_color='#ffffff'
            )
        )
        
        fig_dag = go.Figure(data=[edge_trace, node_trace])
        fig_dag.update_layout(
            paper_bgcolor='rgba(15, 23, 42, 0.6)',
            plot_bgcolor='rgba(15, 23, 42, 0.6)',
            showlegend=False,
            height=400,
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            margin=dict(l=40, r=40, t=20, b=40)
        )
        st.plotly_chart(fig_dag, use_container_state=True)
    else:
        st.warning("Causal DAG layout data empty.")


# ------------------------------------------
# TAB 3: Multi-Agent Thought Stream
# ------------------------------------------
with tab3:
    st.markdown("### 🧠 Agent Execution & Reasoning Stream")
    
    for t in thought_stream:
        st.markdown(f"""
        <div class="thought-node">
            <div style="display: flex; justify-content: space-between; font-size: 0.8rem; color: #64748b; margin-bottom: 4px;">
                <span style="font-weight: 700; color: #00f3ff;">[{t.get('agent', 'Agent')}]</span>
                <span>⏱️ {t.get('timestamp', '')}</span>
            </div>
            <div style="color: #e2e8f0; font-size: 0.92rem;">
                {t.get('thought', '')}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")
    st.markdown("### 🔍 Raw Structured Agent Outputs")
    
    exp1, exp2, exp3 = st.tabs(["Quant Bull Output", "Adversarial Bear Output", "Bayesian Arbiter Output"])
    with exp1:
        st.json(bull)
    with exp2:
        st.json(bear)
    with exp3:
        st.json(arbiter)


# ------------------------------------------
# TAB 4: EVM Payload Simulator
# ------------------------------------------
with tab4:
    st.markdown("### ⚡ Automated Smart Contract Execution Payload")
    st.markdown("Formulated calldata ready for broadcast via Web3 wallet or keeper bot network.")
    
    payload = arbiter.get("evm_payload", {})
    
    col_p1, col_p2 = st.columns([1.5, 1])
    
    with col_p1:
        st.markdown(f"""
        <div class="obsidian-card">
            <h4 style="margin-top:0; color:#00ff9d;">Contract Function Call Details</h4>
            <table style="width:100%; border-collapse:collapse; color:#cbd5e1; font-size:0.9rem;">
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);">
                    <td style="padding:8px 0; color:#94a3b8;">Target Contract</td>
                    <td style="padding:8px 0; font-family:monospace; color:#00f3ff;">{payload.get('target_contract', 'N/A')}</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);">
                    <td style="padding:8px 0; color:#94a3b8;">Function Signature</td>
                    <td style="padding:8px 0; font-family:monospace;">{payload.get('function_signature', 'N/A')}</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);">
                    <td style="padding:8px 0; color:#94a3b8;">Method Selector</td>
                    <td style="padding:8px 0; font-family:monospace; color:#ffb700;">{payload.get('method_selector', 'N/A')}</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);">
                    <td style="padding:8px 0; color:#94a3b8;">Estimated Gas Limit</td>
                    <td style="padding:8px 0;">{payload.get('estimated_gas', 0):,} units</td>
                </tr>
                <tr>
                    <td style="padding:8px 0; color:#94a3b8;">Safety Guardrails</td>
                    <td style="padding:8px 0; color:{'#00ff9d' if payload.get('guardrails_passed') else '#ff3366'}; font-weight:bold;">
                        {'✓ PASSED' if payload.get('guardrails_passed') else '🛑 FAILED'}
                    </td>
                </tr>
            </table>
        </div>
        """, unsafe_allow_html=True)
        
    with col_p2:
        st.markdown("#### Raw Calldata Hex String")
        st.code(payload.get("calldata_hex", "0x"), language="text")
        
        st.markdown("#### JSON Contract Interaction Spec")
        st.code(json.dumps(payload, indent=2), language="json")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #475569; font-size: 0.8rem; padding: 10px;">
    AetherCausal-Zero v1.0.0 • LangGraph Multi-Agent Architecture • Google Gemini API Supported
</div>
""", unsafe_allow_html=True)
