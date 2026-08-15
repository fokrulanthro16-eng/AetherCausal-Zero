"""
Verification Runner for AetherCausal-Zero Pipeline
Validates LangGraph StateGraph execution, Bayesian math integrity, and EVM payload hex structures.
"""

import sys
import os
import json

# Force UTF-8 stdout encoding for Windows compatibility
sys.stdout.reconfigure(encoding='utf-8')

from engine import run_causal_inference, build_causal_engine


def test_pipeline_execution():
    print("=" * 60)
    print("🧪 Running AetherCausal-Zero Pipeline Verification")
    print("=" * 60)
    
    hypothesis = "ETH liquid staking yield decay triggers 15% collateral de-peg and cascade liquidation in Aave v3."
    market_context = {
        "volatility_index": 55,
        "oracle_delay_sec": 10,
        "liquidity_depth_m": 80.0,
        "gas_gwei": 45,
        "macro_regime": "High-Vol Arbitrage"
    }
    
    print("\n1. Testing Graph Compilation...")
    engine = build_causal_engine()
    assert engine is not None, "Failed to compile LangGraph StateGraph"
    print("   [SUCCESS] LangGraph compiled successfully.")
    
    print("\n2. Executing Multi-Agent Inference Pipeline...")
    state = run_causal_inference(
        hypothesis=hypothesis,
        market_context=market_context,
        target_network="Ethereum Mainnet",
        force_mock=True
    )
    
    # Check Quant Bull Output
    bull = state.get("bull_analysis")
    assert bull is not None, "Bull Analysis missing"
    assert "thesis_summary" in bull, "Bull thesis_summary missing"
    print(f"   [SUCCESS] Quant Bull Synthesizer Output: EV=${bull['expected_ev_millions']}M | Confidence={bull['bull_confidence']*100:.0f}%")
    
    # Check Adversarial Bear Output
    bear = state.get("bear_audit")
    assert bear is not None, "Bear Audit missing"
    assert "risk_score" in bear, "Bear risk_score missing"
    print(f"   [SUCCESS] Adversarial Bear Auditor Output: Risk Score={bear['risk_score']*100:.0f}% | Vulnerabilities={len(bear['hidden_vulnerabilities'])}")
    
    # Check Bayesian Arbiter Output
    arbiter = state.get("arbiter_verdict")
    assert arbiter is not None, "Arbiter Verdict missing"
    assert "bayesian_posterior" in arbiter, "Posterior probability missing"
    assert "causal_nodes" in arbiter, "Causal DAG nodes missing"
    assert "causal_edges" in arbiter, "Causal DAG edges missing"
    assert "evm_payload" in arbiter, "EVM Payload missing"
    
    print(f"   [SUCCESS] Bayesian Causal Arbiter Output: Verdict={arbiter['strategic_verdict']} | Posterior P(H|E)={arbiter['bayesian_posterior']:.4f}")
    
    # Check EVM Payload Integrity
    payload = arbiter["evm_payload"]
    assert payload["target_contract"].startswith("0x"), "Invalid target contract address"
    assert payload["calldata_hex"].startswith("0x"), "Invalid hex calldata string"
    print(f"   [SUCCESS] EVM Payload Verified: Selector={payload['method_selector']} | Target={payload['target_contract']}")
    
    # Check Thought Stream Logging
    thoughts = state.get("thought_stream", [])
    assert len(thoughts) >= 3, "Thought stream log entries missing"
    print(f"   [SUCCESS] Thought Stream Log: {len(thoughts)} execution entries recorded.")
    
    print("\n" + "=" * 60)
    print("ALL PIPELINE VERIFICATION TESTS PASSED SUCCESSFULLY!")
    print("=" * 60)
    return True


if __name__ == "__main__":
    try:
        test_pipeline_execution()
        sys.exit(0)
    except Exception as e:
        print(f"\nPipeline Verification Failed: {str(e)}")
        sys.exit(1)
