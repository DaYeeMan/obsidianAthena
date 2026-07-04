---
type: source-note
source_kind: paper
asset_classes: [futures, portfolio, ml, cross-asset]
implementation_class: foundational / retail-adaptable
importance: high
last_reviewed: "2026-07-02"
tags: [quant-source, futures, portfolio-timing, ml, transaction-costs, baselines]
concepts: [parametric-portfolio-policies, differentiable-sharpe, time-series-momentum, risk-parity, transaction-costs]
---

# End-to-End Parametric Portfolio Policies for Cross-Asset Futures Timing

## Citation / Link

Austin Pollok, Kevin Robik, “End-to-End Parametric Portfolio Policies for Cross-Asset Futures Timing: When Do AI Models Beat Simple Rules?” arXiv:2607.00475v1, 2026-07-01. https://arxiv.org/abs/2607.00475v1

## Summary

The paper studies whether end-to-end AI portfolio policies can beat simple rules in cross-asset futures timing. Instead of forecasting returns and then optimizing weights, the learned policy maps market state directly to portfolio weights using a differentiable Sharpe-ratio objective. The abstract reports tests on sixteen highly liquid CME futures and benchmarks against equal weight, risk parity, and time-series momentum. Learned policies rank above rules on the pooled cross-asset portfolio and in several sub-asset classes, but not uniformly. Gross LSTM and transformer performance is similar, while costs differentiate them: the transformer trades less and matches or exceeds equal weighting through moderate transaction costs.

## Core Contribution

- Puts AI portfolio policies in direct competition with simple allocation rules rather than weak ML baselines.
- Evaluates portfolio weights end-to-end instead of separating return prediction from optimization.
- Highlights turnover as a first-order model-selection criterion: models with similar gross performance can diverge after costs.
- Uses liquid CME futures, reducing but not eliminating implementation concerns.

## Practical Relevance

- Classification: **Evidence-backed at abstract level as a model-evaluation study; foundational / retail-adaptable**.
- Not an immediate strategy to deploy because full features, cost model, walk-forward design, and contract handling need verification.
- Retail adaptation is plausible using liquid futures or ETF proxies, but the first local version should compare simple rules before any deep model: equal weight, inverse vol/risk parity, time-series momentum, and volatility targeting.

## Methods and Data

Abstract-level details:

- universe: sixteen most liquid CME futures,
- task: cross-asset timing / portfolio tilts,
- policy: end-to-end mapping from market states to portfolio weights,
- objective: differentiable Sharpe-ratio loss,
- models: LSTM and transformer-style architecture,
- baselines: equal weighting, risk parity, time-series momentum,
- evaluation: out-of-sample gross and cost-aware performance.

Local minimum viable adaptation:

1. Start with daily continuous futures or ETF proxies.
2. Build equal weight, inverse-vol/risk-parity, and time-series momentum baselines.
3. Add a simple linear parametric policy before deep sequence models.
4. Track turnover, cost sensitivity, leverage/margin, roll assumptions, and regime-conditional performance.
5. Promote complex models only if they add net utility beyond simple rules.

## Leakage / Bias / Overfitting Concerns

- Differentiable Sharpe objectives can overfit through turnover, leverage, and tail-event sensitivity.
- Futures backtests are sensitive to contract roll rules, margin/cash treatment, collateral return, and volatility scaling.
- Feature construction must be strictly time-gated; cross-asset features can accidentally use unavailable settlement/roll information.
- “AI beats rules” must be tested across sub-asset classes, regimes, and cost assumptions, not only pooled gross performance.

## Transaction Cost / Capacity Treatment

The abstract explicitly compares gross and cost-aware results and notes that lower transformer turnover matters. Local use should stress test commissions, bid/ask, slippage, roll costs, exchange fees, and turnover caps. For ETF proxies, include wider spreads and borrow/funding where relevant.

## Strategy Ideas Extracted

- Hypothesis: a turnover-controlled parametric policy can improve net cross-asset timing versus equal weight, risk parity, and time-series momentum after realistic costs.
- Minimum backtest: liquid futures/ETF cross-asset universe; monthly or daily rebalanced simple rules; linear policy; walk-forward validation; cost stress; regime splits.
- Go/no-go: reject if the learned policy only wins gross, only wins in pooled metrics, or fails after moderate cost/turnover stress.

## Connections to Existing Research

### Reinforces

- [[CLQT Cost-Aware Benchmark for LLM Portfolio-Management Agents]]: AI portfolio methods need time-gated, cost-aware, strategy-consistent evaluation.
- [[Regime-Conditional Distributional Comparison of Trading Strategies]]: apparent AI superiority should be tested by regime and fold distribution, not just aggregate Sharpe.
- [[Forecast-uncertainty-aware ML asset pricing]]: learned weights should be shrunk or throttled when forecasts/policies are uncertain.

### Contradicts / Weakens

- Weakens any blanket claim that complex sequence models dominate simple allocation rules; the abstract says outperformance is not uniform and costs matter.

### Transfers Across Asset Classes or Domains

- The simple-baseline-first policy-evaluation design can transfer from futures timing to ETF allocation, crypto cross-sectional allocation, and options overlay sizing.

### Missing Validation or Method Supplied

- Supplies a practical benchmark structure for local ML portfolio work: equal weight, risk parity, time-series momentum, turnover and cost stress, and sub-asset/regime analysis.

## Framework Potential

- Candidate framework: simple-rule benchmark first AI portfolio-policy evaluation.
- Linked notes: [[CLQT Cost-Aware Benchmark for LLM Portfolio-Management Agents]], [[Regime-Conditional Distributional Comparison of Trading Strategies]], [[Forecast-uncertainty-aware ML asset pricing]].
- Testable composite hypothesis: AI portfolio policies are only useful when they improve net-of-cost, regime-robust allocation utility beyond simple rules and uncertainty-aware sizing.
- Minimum viable validation: walk-forward policy training, simple-rule baselines, cost stress, turnover cap, regime-conditional fold distributions.
- What would falsify this connection? If simple rules dominate after costs across regimes, or if learned policies win only through unstable leverage/turnover choices.

## Keep / Reject Decision

Keep as a high-value methodology/source note. Do not promote to coding-ready until the local universe, features, roll treatment, and cost assumptions are specified.

## Related Notes

- [[CLQT Cost-Aware Benchmark for LLM Portfolio-Management Agents]]
- [[Regime-Conditional Distributional Comparison of Trading Strategies]]
- [[Forecast-uncertainty-aware ML asset pricing]]
