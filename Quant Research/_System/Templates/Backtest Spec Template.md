---
type: backtest-spec-template
tags: [quant-research, backtest]
---

# {{strategy_name}} Backtest Spec

## Research Question


## Hypothesis


## Asset Class / Universe


## Data Requirements

| Field | Frequency | Source | Bias/Quality Concern |
|---|---|---|---|

## Signal Definition


## Portfolio / Position Rules


## Entry / Exit Rules


## Transaction Costs and Frictions

- commissions:
- bid/ask spread:
- slippage:
- borrow/funding:
- option exercise/assignment/settlement:
- crypto exchange fees/funding:
- liquidity/capacity:

## Baselines


## Validation Design

- train/test split:
- walk-forward design:
- purging/embargo if needed:
- regime splits:
- post-publication test:
- parameter stability:

## Metrics

- CAGR / total return
- volatility
- Sharpe / Sortino
- max drawdown
- expected shortfall / VaR
- turnover
- hit rate and payoff asymmetry
- tail loss / crash exposure
- capacity / liquidity utilization

## Failure Modes


## Decision Rule

What result would make this worth continuing, revising, or rejecting?
