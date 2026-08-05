---
type: source-note
source_kind: paper / HFT measurement and market-quality methodology
asset_classes: [equities, market-microstructure, execution, event-studies]
implementation_class: foundational / institutional-only as written / retail-adaptable as public-proxy benchmark
importance: medium
last_reviewed: "2026-08-04"
tags: [quant-source, high-frequency-trading, market-microstructure, liquidity-supply, liquidity-demand, earnings]
concepts: [hft-liquidity-supply-demand, hft-public-proxies, earnings-price-informativeness]
---

# Data-Driven Measures of High-Frequency Trading

## Citation / Link

Gbenga Ibikunle, Ben Moews, Dmitriy Muravyev, Khaladdin Rzayev, “Data-Driven Measures of High-Frequency Trading,” arXiv:2608.00858v1, submitted 2026-08-01. https://arxiv.org/abs/2608.00858v1

Semantic Scholar lookup was rate-limited during this run, so citation counts were not recorded.

## Summary

The paper trains machine-learning models on proprietary observed HFT activity and applies them to public intraday data to create U.S. stock HFT measures from 2010–2023. The measures distinguish liquidity-supplying and liquidity-demanding HFT and reportedly outperform conventional proxies. The abstract says the measures respond to quasi-exogenous market-structure changes and help separate the effect of HFT types on information acquisition: liquidity-supplying HFT improves price informativeness around earnings announcements, while liquidity-demanding HFT impedes it.

For this library, the paper is a market-structure state reference, not an immediately implementable signal.

## Core Contribution

- Separates HFT activity into liquidity-supplying and liquidity-demanding components.
- Provides a public-intraday-data proxy trained from proprietary ground truth.
- Links HFT regimes to earnings-announcement price informativeness.
- Gives an empirical state variable candidate for event-study and microstructure decay research.

## Practical Relevance

- Classification: **Evidence-backed at abstract level as market-microstructure measurement; foundational / institutional-only as written / retail-adaptable as public-proxy benchmark**.
- Institutional-only as written because proprietary observed HFT labels are required to reproduce the model training.
- Retail adaptation: use the paper as a benchmark for evaluating simpler public HFT/liquidity proxies, not as a direct trading signal.

## Strategy / Backtest Translation

- Hypothesis: earnings-announcement drift/reversal and intraday event strategies should behave differently under liquidity-supplying versus liquidity-demanding HFT regimes.
- Data: public intraday TAQ-like trades/quotes, earnings timestamps, spreads/depth/volume/order-imbalance proxies, market-structure event dates.
- Baselines: spread, turnover, message/trade intensity, realized spread proxy, effective spread, volatility, volume, simple earnings drift controls.
- Validation: pre-registered event windows, post-publication holdout, cost/slippage stress, factor/size/liquidity controls, and simple proxy comparison before using any ML HFT classifier.

## Risks / Failure Modes

- Original labels are proprietary; local replication may only approximate the measure.
- HFT proxies can be endogenous to volatility, news, spread, and liquidity.
- Event-study effects around earnings may not translate into retail-executable trades after spreads and short-window slippage.

## Connections to Existing Research

- Strengthens microstructure-conditioned decay and event-study validation, especially around earnings.
- Connects to [[Liquidity-Based Audit of Algorithmic Trading Strategies]], [[Microstructural Foundations of Rough Noise]], and [[The Bounce Has No Direction - Sign Magnitude and Microstructure of Equity Return Predictability]].
