---
type: source-note
source_kind: paper
asset_classes: [defi, crypto, market-microstructure, liquidity, causal-inference]
implementation_class: foundational / retail-adaptable
importance: medium
last_reviewed: "2026-07-14"
tags: [quant-source, defi, amm, uniswap, liquidity-provision, causal-inference, event-study]
concepts: [protocol-fee-switch, amm-liquidity-supply, matched-overlap-event-study, difference-in-differences, channel-admissibility]
---

# Causal Effects of Protocol-Fee Changes on Liquidity Provision in Automated Market Makers

## Citation / Link

Wen-Ting Wang, “Causal Effects of Protocol-Fee Changes on Liquidity Provision in Automated Market Makers,” arXiv:2607.08525v1, 2026-07-09. https://arxiv.org/abs/2607.08525v1

## Summary

This paper uses Uniswap protocol-fee switch events as quasi-experimental variation in liquidity-provider take-rates while trader-facing fees remain unchanged. The abstract describes a pre-specified matched-overlap event-study difference-in-differences design with frozen, hash-checked panels reconstructed from public logs. It reports no large short-run average response in active liquidity or local depth, and similarly no clear LP participation/composition response at the design's resolution. The result is framed carefully as non-detection, not a precise zero.

## Core Contribution

- Separates LP take-rate changes from trader-facing fee changes in AMM fee analysis.
- Provides a disciplined causal event-study design for public on-chain microstructure data.
- Warns against simulator evaluations that freeze the LP liquidity-supply response kernel without evidence.
- Models channel admissibility explicitly: some channels are design-identified, while dynamic-fee trader protection remains model-conditioned.

## Practical Relevance

- Classification: **Evidence-backed at abstract level as DeFi microstructure / causal-design methodology; foundational / retail-adaptable**.
- Not a direct trading signal.
- Useful for evaluating AMM liquidity-provision strategies, dynamic-fee claims, and causal event studies around protocol parameter changes.
- Retail adaptation: use public logs to test liquidity and depth changes around exogenous fee/governance events, but avoid claiming trader-facing dynamic-fee alpha from an LP-take-rate design.

## Methods and Data

Abstract-level details:

- Uniswap v3 protocol-fee switch variation,
- matched-overlap event-study difference-in-differences,
- active liquidity, local depth, LP participation/composition,
- public logs reconstructed into a frozen, hash-checked panel,
- parallel-trends gates for volume/native fee-income outcomes,
- channel-admissibility audit.

Minimum local adaptation:

1. Treat AMM fee/governance events as event-study opportunities only when treated/control pools are well matched.
2. Freeze panel construction before estimating treatment effects.
3. Track active liquidity, local depth, volume, fee income, LP addresses/composition, and token/market controls.
4. Separate estimands: LP supply response, trader routing, adverse selection/LVR, and fee income are not interchangeable.

## Backtest / Validation Design

- Hypothesis: protocol-fee/take-rate changes have limited short-run effect on liquidity supply in matched liquid pools, but the response may vary by pool risk and fee tier.
- Universe: Uniswap v3 pools with public logs, stable/liquid volatile pairs, explicit event dates.
- Baselines: matched non-treated pools, pre/post naive comparison, placebo event dates.
- Validation: event-time DiD, parallel-trends diagnostics, overlap checks, clustered standard errors or block bootstrap, robustness by pool type.

## Risks / Failure Modes

- Non-detection may reflect limited power, event selection, or short windows rather than structural insensitivity.
- On-chain logs are public but messy; pool roles and liquidity outcomes require careful reconstruction.
- Results may not transfer to trader-facing dynamic-fee changes or other AMM designs.
- Protocol/governance anticipation can contaminate event timing.

## Connections to Existing Research

### Reinforces

- [[SoK - Market Microstructure for Decentralized Prediction Markets]] as a reminder that venue/market design variables must be tagged before pooling markets.
- [[Liquidity-Based Audit of Algorithmic Trading Strategies]] and [[When Large Trades Are Not News - Liquidity Tail Risk and Price Discovery]] by treating liquidity supply as state- and design-dependent rather than constant.
- [[Settlement Manipulation in Prediction Markets]] by emphasizing event-window causal design and matched controls in crypto venues.

### Framework Potential

- Candidate framework: design-based crypto market-structure event studies.
- Minimum viable test: codify matched-overlap event windows and channel-admissibility fields for AMM/protocol-change research.
- Falsifier: event windows fail overlap/parallel-trends checks or cannot separate LP, trader, and routing channels.
