"""
Asset Generator for AetherCausal-Zero Repository
Renders high-resolution institutional PNG visual assets for GitHub README documentation.
"""

import os
import sys
from PIL import Image, ImageDraw

# Force UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')


def create_architecture_dag():
    width, height = 1200, 600
    img = Image.new("RGBA", (width, height), (11, 15, 25, 255))
    draw = ImageDraw.Draw(img)
    
    # Background Grid Lines
    for x in range(0, width, 40):
        draw.line([(x, 0), (x, height)], fill=(255, 255, 255, 8), width=1)
    for y in range(0, height, 40):
        draw.line([(0, y), (width, y)], fill=(255, 255, 255, 8), width=1)
        
    # Title Header
    draw.text((40, 30), "AETHERCAUSAL-ZERO • MULTI-AGENT STATE GRAPH ARCHITECTURE", fill=(0, 243, 255, 255))
    draw.text((40, 55), "LangGraph Orchestrated Sequential Inference & Cryptographic Payload Synthesis", fill=(148, 163, 184, 255))
    
    boxes = [
        {
            "rect": (50, 160, 290, 480),
            "color": (0, 255, 157, 255),
            "title": "QUANT BULL",
            "subtitle": "Synthesizer Node",
            "lines": ["- Positive Reflexivity Loops", "- Upward Leverage Drivers", "- Catalyst Formulations", "- Expected EV Calculation"]
        },
        {
            "rect": (340, 160, 580, 480),
            "color": (255, 51, 102, 255),
            "title": "ADVERSARIAL BEAR",
            "subtitle": "Auditor Node",
            "lines": ["- Oracle Lag Stress-Test", "- MEV Front-Running Risk", "- Liquidation Queue Depth", "- Black-Swan Scenarios"]
        },
        {
            "rect": (630, 160, 870, 480),
            "color": (255, 183, 0, 255),
            "title": "BAYESIAN ARBITER",
            "subtitle": "Causal Reasoning Node",
            "lines": ["- Bayes Theorem P(H|E)", "- 2D Causal DAG Topology", "- Verification Matrix", "- Risk-Adjusted Confidence"]
        },
        {
            "rect": (920, 160, 1160, 480),
            "color": (0, 243, 255, 255),
            "title": "EVM PAYLOAD",
            "subtitle": "Execution Simulator",
            "lines": ["- Target Contract Resolution", "- Method Selector Encoding", "- Raw Calldata Hex String", "- Safety Guardrail Check"]
        }
    ]
    
    # Draw Arrows
    arrow_y = 320
    for i in range(3):
        x1 = boxes[i]["rect"][2]
        x2 = boxes[i+1]["rect"][0]
        draw.line([(x1 + 5, arrow_y), (x2 - 5, arrow_y)], fill=(0, 243, 255, 200), width=3)
        draw.polygon([(x2 - 5, arrow_y), (x2 - 15, arrow_y - 8), (x2 - 15, arrow_y + 8)], fill=(0, 243, 255, 255))
        
    for b in boxes:
        r = b["rect"]
        draw.rectangle(r, fill=(15, 23, 42, 230), outline=b["color"], width=2)
        draw.rectangle((r[0], r[1], r[2], r[1] + 6), fill=b["color"])
        
        draw.text((r[0] + 18, r[1] + 25), b["title"], fill=(255, 255, 255, 255))
        draw.text((r[0] + 18, r[1] + 48), b["subtitle"], fill=b["color"])
        draw.line([(r[0] + 18, r[1] + 75), (r[2] - 18, r[1] + 75)], fill=(255, 255, 255, 30), width=1)
        
        curr_y = r[1] + 95
        for line in b["lines"]:
            draw.text((r[0] + 18, curr_y), line, fill=(203, 213, 225, 255))
            curr_y += 36

    os.makedirs("assets", exist_ok=True)
    img.save("assets/architecture_dag.png")
    print("[SUCCESS] Saved assets/architecture_dag.png")


def create_dashboard_overview():
    width, height = 1200, 700
    img = Image.new("RGBA", (width, height), (11, 15, 25, 255))
    draw = ImageDraw.Draw(img)
    
    # Background Grid
    for x in range(0, width, 40):
        draw.line([(x, 0), (x, height)], fill=(255, 255, 255, 6), width=1)
    for y in range(0, height, 40):
        draw.line([(0, y), (width, y)], fill=(255, 255, 255, 6), width=1)
        
    # Top Navbar Bar
    draw.rectangle((20, 20, 1180, 80), fill=(15, 23, 42, 240), outline=(255, 255, 255, 30), width=1)
    draw.text((40, 35), "AETHERCAUSAL-ZERO", fill=(0, 243, 255, 255))
    draw.text((40, 56), "Institutional Dark-Mode Causal Arbitration Dashboard", fill=(148, 163, 184, 255))
    
    # Status Badges
    draw.rectangle((900, 35, 1040, 65), fill=(0, 255, 157, 30), outline=(0, 255, 157, 100))
    draw.text((915, 43), "Live Gemini API", fill=(0, 255, 157, 255))
    draw.rectangle((1050, 35, 1160, 65), fill=(15, 23, 42, 255), outline=(255, 255, 255, 30))
    draw.text((1065, 43), "ETH Mainnet", fill=(203, 213, 225, 255))
    
    # Main Verdict Card
    draw.rectangle((20, 100, 760, 360), fill=(15, 23, 42, 220), outline=(255, 255, 255, 30), width=1)
    draw.text((40, 120), "STRATEGIC BAYESIAN VERDICT", fill=(148, 163, 184, 255))
    draw.rectangle((580, 115, 740, 145), fill=(255, 183, 0, 30), outline=(255, 183, 0, 100))
    draw.text((595, 123), "CONDITIONAL REBALANCE", fill=(255, 183, 0, 255))
    
    draw.text((40, 155), "ETH liquid staking yield decay triggers 15% collateral de-peg in Aave v3", fill=(255, 255, 255, 255))
    draw.text((40, 185), "Posterior probability P(H|E) = 0.4765. Execution permitted with reduced leverage", fill=(203, 213, 225, 255))
    draw.text((40, 205), "and dynamic slippage ceiling <= 0.5% due to Pyth oracle update lag.", fill=(203, 213, 225, 255))
    
    # Metric Boxes
    m_data = [
        ("Prior P(H)", "0.50", (148, 163, 184)),
        ("Posterior P(H|E)", "0.4765", (0, 243, 255)),
        ("Expected EV", "$23.05M", (0, 255, 157)),
        ("Risk Score", "89%", (255, 51, 102))
    ]
    for idx, (label, val, col) in enumerate(m_data):
        mx = 40 + (idx * 175)
        draw.rectangle((mx, 255, mx + 160, 335), fill=(30, 41, 59, 180), outline=(255, 255, 255, 20))
        draw.text((mx + 15, 268), label, fill=(148, 163, 184, 255))
        draw.text((mx + 15, 292), val, fill=col)

    # Gauge Chart Box
    draw.rectangle((780, 100, 1180, 360), fill=(15, 23, 42, 220), outline=(255, 255, 255, 30), width=1)
    draw.text((800, 120), "BAYESIAN CONFIDENCE GAUGE", fill=(148, 163, 184, 255))
    
    cx, cy, r = 980, 250, 90
    draw.arc([cx - r, cy - r, cx + r, cy + r], start=180, end=0, fill=(30, 41, 59, 255), width=20)
    draw.arc([cx - r, cy - r, cx + r, cy + r], start=180, end=270, fill=(0, 243, 255, 255), width=20)
    draw.text((cx - 35, cy - 25), "78.5%", fill=(255, 255, 255, 255))
    draw.text((cx - 45, cy + 15), "CONFIDENCE", fill=(0, 243, 255, 255))

    # Causal Verification Matrix Table Box
    draw.rectangle((20, 380, 1180, 670), fill=(15, 23, 42, 220), outline=(255, 255, 255, 30), width=1)
    draw.text((40, 400), "CAUSAL VERIFICATION MATRIX (BULL VS BEAR VS ARBITER)", fill=(0, 243, 255, 255))
    
    headers = ["Dimension", "Quant Bull View", "Adversarial Bear Stress", "Arbiter Verdict", "Status"]
    h_x = [40, 260, 520, 820, 1060]
    draw.line([(30, 430), (1170, 430)], fill=(255, 255, 255, 40), width=1)
    for idx, h in enumerate(headers):
        draw.text((h_x[idx], 412), h, fill=(148, 163, 184, 255))
        
    rows = [
        ("Liquidity Depth", "Robust depth ($120.0M)", "Slippage cascade if 25% drained", "Sufficient for 50% split", "PASSED"),
        ("Oracle Latency", "Negligible normal impact", "Toxic window (8s delay)", "Enforce slippage <= 0.5%", "WARNING"),
        ("Gas Volatility", "Acceptable at 35 Gwei", "Gas spike blocks unwinding", "Dynamic max fee ceiling", "PASSED"),
        ("Systemic Risk", "Isolated protocol exposure", "Cross-collateral liquidation", "Hedging swap payload active", "PASSED")
    ]
    
    ry = 445
    for r in rows:
        draw.line([(30, ry + 35), (1170, ry + 35)], fill=(255, 255, 255, 15), width=1)
        draw.text((h_x[0], ry + 8), r[0], fill=(255, 255, 255, 255))
        draw.text((h_x[1], ry + 8), r[1], fill=(203, 213, 225, 255))
        draw.text((h_x[2], ry + 8), r[2], fill=(203, 213, 225, 255))
        draw.text((h_x[3], ry + 8), r[3], fill=(203, 213, 225, 255))
        badge_col = (0, 255, 157, 255) if r[4] == "PASSED" else (255, 183, 0, 255)
        draw.text((h_x[4], ry + 8), f"[ {r[4]} ]", fill=badge_col)
        ry += 48

    os.makedirs("assets", exist_ok=True)
    img.save("assets/dashboard_overview.png")
    print("[SUCCESS] Saved assets/dashboard_overview.png")


def create_evm_payload_sim():
    width, height = 1200, 600
    img = Image.new("RGBA", (width, height), (11, 15, 25, 255))
    draw = ImageDraw.Draw(img)
    
    # Background Grid
    for x in range(0, width, 40):
        draw.line([(x, 0), (x, height)], fill=(255, 255, 255, 6), width=1)
    for y in range(0, height, 40):
        draw.line([(0, y), (width, y)], fill=(255, 255, 255, 6), width=1)
        
    # Top Header
    draw.text((40, 30), "EVM PAYLOAD SIMULATOR & SMART CONTRACT CALLDATA GENERATOR", fill=(0, 255, 157, 255))
    draw.text((40, 55), "Automated On-Chain Rebalance Payload Formulation with Dynamic Safety Guardrails", fill=(148, 163, 184, 255))
    
    # Contract Details Panel (Left)
    draw.rectangle((40, 100, 580, 540), fill=(15, 23, 42, 230), outline=(255, 255, 255, 30), width=1)
    draw.text((60, 120), "CONTRACT FUNCTION SPECIFICATION", fill=(0, 243, 255, 255))
    
    specs = [
        ("Target Contract Address", "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D", (0, 243, 255)),
        ("Function Signature", "rebalanceVaultCausal(bytes32,uint256,uint256,bool)", (255, 255, 255)),
        ("Method Selector", "0xa9059cbb", (255, 183, 0)),
        ("Estimated Gas Limit", "215,250 Gas Units", (203, 213, 225)),
        ("Account Nonce", "42", (203, 213, 225)),
        ("Safety Guardrails", "PASSED (Slippage <= 0.5%)", (0, 255, 157))
    ]
    
    sy = 160
    for label, val, col in specs:
        draw.line([(60, sy + 45), (560, sy + 45)], fill=(255, 255, 255, 15), width=1)
        draw.text((60, sy + 8), label, fill=(148, 163, 184, 255))
        draw.text((60, sy + 26), val, fill=col)
        sy += 58

    # Hex Calldata Panel (Right)
    draw.rectangle((610, 100, 1160, 540), fill=(15, 23, 42, 230), outline=(255, 255, 255, 30), width=1)
    draw.text((630, 120), "RAW ABI CALLDATA HEX PAYLOAD", fill=(255, 183, 0, 255))
    
    draw.rectangle((630, 150, 1140, 280), fill=(30, 41, 59, 200), outline=(0, 243, 255, 80))
    hex_lines = [
        "0xa9059cbb",
        "0000000000000000000000007a250d5630b4cf539739df2c5dacb4c659f2488d",
        "0000000000000000000000000000000000000000000000000000000000002710",
        "0000000000000000000000000000000000000000000000000000000000000001"
    ]
    hy = 165
    for hl in hex_lines:
        draw.text((645, hy), hl, fill=(0, 255, 157, 255) if hy == 165 else (203, 213, 225, 255))
        hy += 26
        
    draw.text((630, 310), "JSON Contract Interaction Payload", fill=(148, 163, 184, 255))
    draw.rectangle((630, 335, 1140, 510), fill=(30, 41, 59, 160), outline=(255, 255, 255, 20))
    json_snippet = [
        '{',
        '  "target": "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D",',
        '  "selector": "0xa9059cbb",',
        '  "gasLimit": 215250,',
        '  "guardrails": true,',
        '  "network": "Ethereum Mainnet"',
        '}'
    ]
    jy = 348
    for jl in json_snippet:
        draw.text((648, jy), jl, fill=(203, 213, 225, 255))
        jy += 22

    os.makedirs("assets", exist_ok=True)
    img.save("assets/evm_payload_sim.png")
    print("[SUCCESS] Saved assets/evm_payload_sim.png")


if __name__ == "__main__":
    create_architecture_dag()
    create_dashboard_overview()
    create_evm_payload_sim()
    print("[SUCCESS] All visual assets generated successfully!")
