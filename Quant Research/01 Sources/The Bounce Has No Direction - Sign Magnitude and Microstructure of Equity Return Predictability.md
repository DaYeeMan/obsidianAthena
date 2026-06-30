---
type: source-note
source_kind: paper
asset_classes: [equities, market-microstructure]
implementation_class: foundational
importance: high
last_reviewed: "2026-06-30"
tags: [quant-source, equities, microstructure, return-predictability, transaction-costs]
concepts: [bid-ask-bounce, reversal, variance-ratio, microstructure-noise]
---

# The Bounce Has No Direction - Sign, Magnitude, and the Microstructure of Equity Return Predictability

## Citation / Link

Victoria Portnaya, “The Bounce Has No Direction: Sign, Magnitude, and the Microstructure of Equity Return Predictability,” arXiv:2606.29591v1, 2026-06-28. https://arxiv.org/abs/2606.29591v1

## Summary

The paper argues that statistically significant lag-1 autocorrelation in SPY and related instruments should not automatically be interpreted as directional reversal. It introduces a Fourier-Residue Identity that decomposes autocorrelation into sign and magnitude channels. In the abstract, SPY lag-1 autocorrelation is driven by magnitude shrinkage rather than sign reversal, consistent with bid-ask bounce and stale/non-synchronous constituent pricing rather than a clean directional alpha.

## Core Contribution

- Separates return predictability into direction/sign and magnitude components.
- Reinterprets common variance-ratio/autocorrelation evidence through a microstructure lens.
- Reports evidence that lag-1 SPY autocorrelation is magnitude-driven, while a different lag-3 channel may contain directional reversal.

## Practical Relevance

- Classification: **Evidence-backed as a diagnostic / foundational**.
- Not a direct retail strategy until translated into a cost-aware rule; lag-1 effects are especially vulnerable to spreads and stale prices.
- Useful as a warning against naïve close-to-close reversal strategies that treat all negative autocorrelation as exploitable directional predictability.

## Methods and Data

Abstract evidence covers six U.S. instruments over 1993–2026 plus a 21-instrument cross-asset panel. Local use should replicate only with:

- adjusted OHLC or intraday bars where available,
- bid/ask or spread proxies,
- lag-specific sign-vs-magnitude decomposition,
- conservative transaction-cost assumptions.

## Leakage / Bias / Overfitting Concerns

- Close-to-close signals can reflect execution-unreachable closing prints or stale index constituent effects.
- Directional claims need out-of-sample, post-cost testing by instrument and regime.
- If applied to ETFs, include spread, borrow/cash, and market-on-close/open execution assumptions.

## Transaction Cost / Capacity Treatment

Critical. The most plausible explanation is microstructure friction itself. Any trading test must require profitability net of spreads, commissions, slippage, and market-on-close/open constraints. Treat lag-1 reversal as suspect until it survives costs.

## Strategy Ideas Extracted

No immediate alpha promotion. Candidate test: compare lag-1 and lag-3 reversal/magnitude-shrinkage rules across SPY/liquid ETFs with realistic close/open fills and a no-trade threshold tied to spread/volatility.

## Connections to Existing Research

### Reinforces

- [[2026-06-28 Daily Quant Research Review]] square-root impact / capacity reference: apparent predictability can be dominated by trading frictions.

### Contradicts / Weakens

- Weakens naïve short-horizon ETF mean-reversion interpretations that do not separate directional reversal from microstructure bounce.

### Transfers Across Asset Classes or Domains

- Similar diagnostic should be applied to crypto high-frequency reversal/lead-lag claims before treating autocorrelation as alpha.

### Missing Validation or Method Supplied

- Supplies a sign-vs-magnitude diagnostic that can be added before coding short-horizon reversal strategies.

## Framework Potential

- Candidate framework: [[Microstructure-aware predictability decomposition]]
- Linked notes: square-root impact reference, [[CryptoGAT - Are Time Series Models Effective for Cryptocurrency Forecasting]], [[Liquidity-Based Audit of Algorithmic Trading Strategies]]
- Testable composite hypothesis: many short-horizon return-predictability signals lose directional content once decomposed into sign, magnitude, and cost channels.
- Minimum viable validation: daily/intraday liquid ETFs and crypto majors, lag decomposition, post-cost long/short rules.
- What would falsify this connection? Directional channel remains significant and profitable net of costs across assets and regimes.

## Keep / Reject Decision

**Keep** as a high-value foundational diagnostic and decay warning for short-horizon mean reversion.

## Related Notes

- [[2026-06-30 0044 Daily Quant Research Review]]
