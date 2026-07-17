---
type: source-note
source_kind: paper / software
asset_classes: [crypto, market-microstructure, liquidity, sentiment]
implementation_class: retail-adaptable / foundational
importance: high
last_reviewed: "2026-07-14"
tags: [quant-source, crypto, sentiment, spreads, liquidity, adverse-selection]
concepts: [extremity-premium, sentiment-extremes, fear-greed-index, liquidity-withdrawal, spread-regime]
---

# The Extremity Premium - Sentiment Regimes and Adverse Selection in Cryptocurrency Markets

## Citation / Link

Murad Farzulla, “The Extremity Premium: Sentiment Regimes and Adverse Selection in Cryptocurrency Markets,” arXiv:2602.07018v3, updated 2026-07-11. https://arxiv.org/abs/2602.07018v3

Code/data: https://github.com/studiofarzulla/sentiment-microstructure-abm

## Summary

The paper tests whether extreme crypto sentiment regimes are associated with wider spreads beyond realized-volatility effects. Using the Crypto Fear & Greed Index and Bitcoin daily data, the abstract reports that extreme fear and extreme greed regimes exhibit higher spreads than neutral periods. Extended validation over 2018–2026 reports within-volatility-quintile evidence, Ethereum replication, and cycle-level persistence, but the author explicitly flags sensitivity to functional form and the difficulty of separating pure sentiment from the index's embedded volatility component.

## Core Contribution

- Treats sentiment intensity, not sentiment direction, as a liquidity/adverse-selection state variable.
- Suggests extreme fear and extreme greed may both coincide with liquidity withdrawal.
- Provides a retail-adaptable spread/liquidity risk filter using public sentiment and daily crypto data.
- Is unusually candid about multiple testing, functional-form sensitivity, and model limitations.

## Practical Relevance

- Classification: **Plausible-to-evidence-backed at abstract level as crypto microstructure evidence; retail-adaptable / foundational**.
- More useful as a cost/liquidity filter than as directional alpha.
- Actionable adaptation: stress spreads/slippage or reduce sizing when public sentiment is in extreme tails, then test whether this improves net utility versus volatility-only filters.
- Should not be treated as proof of a pure sentiment effect because the Fear & Greed Index embeds volatility-like inputs.

## Methods and Data

Abstract-level details:

- Crypto Fear & Greed Index,
- Bitcoin daily data and Ethereum replication,
- full Fear & Greed history from 2018–2026, N = 2,896,
- volatility-quintile comparisons,
- Granger tests, placebo tests, cycle-level checks,
- code/data available,
- agent-based model used illustratively, not as inferential evidence.

Minimum local adaptation:

1. Reconstruct a timestamped sentiment-extremity variable available before the trading decision.
2. Use BTC and ETH spot/perpetual spread proxies, volume, realized volatility, and funding where available.
3. Compare sentiment-extreme states against volatility-only, drawdown, and time-of-day/liquidity controls.
4. Evaluate as a spread/slippage/sizing filter before testing any directional signal.

## Backtest / Validation Design

- Hypothesis: crypto sentiment extremes forecast wider transaction-cost states and lower market-making/liquidity-taking utility after controlling for realized volatility.
- Universe: BTC and ETH first; possibly top liquid perpetuals if spread/funding data exist.
- Baselines: realized-volatility quintiles, drawdown filters, funding/carry, momentum/reversal, liquidity state.
- Frictions: maker/taker fees, funding, spread proxy quality, exchange outage/liquidation events.
- Robustness: cycle splits, post-publication split, bootstrap under serial dependence, alternative sentiment definitions, excluding periods where F&G mechanically overlaps volatility.

## Risks / Failure Modes

- Fear & Greed may partly restate volatility and momentum, creating circularity.
- Daily data may miss intraday spread and depth dynamics.
- Public sentiment filters can decay quickly after publication.
- Liquidity effects may be venue-specific and not tradable after fees.

## Connections to Existing Research

### Reinforces

- [[When Does Order Flow Matter - State-Dependent L2 Liquidity-State Transitions in Crypto Futures]] by adding a public low-frequency state variable for crypto liquidity regimes.
- [[The Quarter-Hour Effect - Periodic Algorithmic Trading and Return Predictability in Cryptocurrency Futures]] as a reminder to condition clock-phase/order-flow effects on liquidity and sentiment stress.
- [[Herding and Liquidity in Order-Book Markets - A Robust Liquidity-Stress Crossover]] by connecting herding/intensity states to liquidity withdrawal.

### Framework Potential

- Candidate framework: public-state liquidity stress filters for crypto strategy costs.
- Minimum viable test: compare sentiment-extreme cost stress against volatility-only cost stress in a BTC/ETH strategy backtest.
- Falsifier: sentiment extremes add no net-cost or drawdown-control value beyond simple volatility/liquidity proxies.
