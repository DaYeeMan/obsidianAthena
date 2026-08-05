---
type: source-note
source_kind: paper / public prediction-market microstructure dataset and negative-result benchmark
asset_classes: [prediction-markets, crypto, bitcoin, market-microstructure]
implementation_class: foundational / retail-adaptable with dataset
importance: high
last_reviewed: "2026-07-30"
tags: [quant-source, polymarket, binance, prediction-markets, microstructure, dataset, negative-result]
concepts: [openmarket-dataset, polymarket-binance-paired-data, settlement-window-benchmark, prediction-market-negative-result]
---

# OpenMarket Synchronized Polymarket-Binance Dataset

## Citation / Link

Gregory Young, “OpenMarket: A Synchronized Polymarket-Binance Dataset for High-Frequency Prediction-Market Research,” arXiv:2607.26245v1, submitted 2026-07-28. https://arxiv.org/abs/2607.26245v1

Comment: 23 pages, 7 figures, 3 tables. Dataset: https://huggingface.co/datasets/gregyoung14/openmarket-btc-polymarket. Code: https://github.com/gregyoung14/openmarket, tag v0.5.2. Semantic Scholar lookup was rate-limited during this run, so citation counts were not recorded.

## Summary

The paper releases a synchronized millisecond-level corpus pairing Polymarket BTC 15-minute binary markets with Binance BTC/USDT order flow. The author reports that the original trading attempt did not produce a tradable edge: a walk-forward logistic model over 43 microstructure features slightly underperformed the probability already implied by Polymarket's own order book, and simulated trading was negative after stated fee and slippage assumptions. The frozen archive contains hundreds of millions of deduplicated rows across archival snapshots and explicitly documents pairing metadata.

For this library, the useful contribution is not alpha. It is a public data/infrastructure benchmark for prediction-market settlement and cross-venue microstructure research, plus a negative base-rate warning against assuming underlying crypto order flow beats the prediction-market book.

## Core Contribution

- Releases paired Polymarket/Binance high-frequency data with code and versioned archive metadata.
- Provides an explicit negative out-of-sample trading result under stated frictions.
- Establishes Polymarket order-book probability as a strong baseline for 15-minute BTC event contracts.
- Creates a feasible dataset path for testing settlement manipulation, structural volatility, and venue-design hypotheses already in this library.

## Practical Relevance

- Classification: **Evidence-backed at abstract level as a public dataset and negative-result benchmark; foundational / retail-adaptable with dataset**.
- Retail adaptation is realistic because dataset and code are public, but execution realism remains difficult: fees, spreads, partial fills, latency, resolution rules, and changing platform mechanics are material.
- Best use is as a validation sandbox, not as a production trading signal.

## Methods and Data

- Polymarket BTC 15-minute binary markets paired to Binance BTC/USDT order-flow data.
- 43 microstructure features and walk-forward logistic benchmark.
- Simulation includes stated fee and slippage assumptions.
- Dataset spans 2026-02-12 through 2026-05-15 in the abstract.

## Leakage / Bias / Overfitting Concerns

- Short sample and BTC-specific event design limit generalization.
- Millisecond pairing requires strict reference-time and decision-time checks.
- Feature engineering can accidentally use post-resolution or unavailable book states.
- The negative result may depend on the chosen logistic model, but it is still a strong baseline warning.

## Transaction Cost / Capacity Treatment

The abstract explicitly includes fees/slippage and reports negative net simulated trading. Any future study should stress maker/taker fees, CLOB queue position, failed orders, stale quotes, latency, and market-impact assumptions.

## Strategy Ideas Extracted

No immediate alpha strategy. Candidate research use: build a descriptive event-study panel around settlement windows, probability buckets, spread/depth, Binance order-flow pressure, and post-settlement reversal; compare any signal against Polymarket-book probability, no-trade, and simple near-resolution avoidance.

## Connections to Existing Research

### Reinforces

- [[Settlement Manipulation in Prediction Markets]] — supplies a possible public dataset for settlement-window tests.
- [[Prediction-Market Structural Volatility Risk Filter]] — enables structural-volatility and time-to-resolution covariates.
- [[SoK - Market Microstructure for Decentralized Prediction Markets]] — adds dataset grounding to venue-design taxonomy.

### Contradicts / Weakens

Weakens naive cross-venue order-flow alpha: Binance BTC/USDT microstructure features did not beat Polymarket's own order-book probability in the reported out-of-sample test.

### Transfers Across Asset Classes or Domains

The benchmark-first pattern transfers to any event-linked market: the venue-implied probability is a hard baseline, and external-underlying features must beat it after latency and fees.

### Missing Validation or Method Supplied

Supplies public synchronized data and a negative baseline for prediction-market research, which had previously been a data blocker in this library.

## Framework Potential

- Candidate framework: prediction-market venue/data-quality validation and settlement-window event studies.
- Linked notes: [[Settlement Manipulation in Prediction Markets]], [[Prediction-Market Structural Volatility Risk Filter]], [[SoK - Market Microstructure for Decentralized Prediction Markets]].
- Testable composite hypothesis: ultra-short BTC prediction-market settlement windows show measurable order-flow pressure/reversal only in specific probability/time-to-resolution/liquidity states, and only if the effect beats Polymarket-book probability and no-trade baselines after frictions.
- Minimum viable validation: reproduce the author's negative logistic benchmark, then run predeclared settlement-window panels with matched non-settlement controls.
- What would falsify this connection? No incremental net utility after using book-implied probability, avoiding near-resolution windows, and paying realistic fees/spreads.

## Keep / Reject Decision

Keep as a high-value source and possible future data path. Do not promote a prediction-market strategy to the coding queue yet; first verify dataset accessibility and reproduce the negative benchmark.

## Related Notes

- [[Settlement Manipulation in Prediction Markets]]
- [[Prediction-Market Structural Volatility Risk Filter]]
- [[SoK - Market Microstructure for Decentralized Prediction Markets]]
