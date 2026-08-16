---
type: daily-quant-research-review
created: 2026-08-14 1519 EDT
source_status: partial-feed-coverage
asset_focus: [equities, options, crypto]
tags: [quant-research, daily-review, options, market-microstructure, event-study, ML-validation]
---

# 2026-08-14 1519 Daily Quant Research Review

## Run Status

- Primary feed path used: blogwatcher-cli persistent state from `C:/Users/enson/.hermes/quant-research/state/blogwatcher-cli.db`.
- Feed coverage was partial: 6 of 7 blogwatcher feeds scanned successfully; Quantocracy failed with HTTP 302. No stdlib fallback RSS scanner was used.
- Blogwatcher found 8 new articles in this scan. Feed entries were treated as discovery leads only.
- arXiv metadata was directly validated for the promoted items through the arXiv API.
- Semantic Scholar lookup outcomes: succeeded for [[Marking-Aware Sequential VaR Recalibration for Option Books]] and [[Defensive Boosting for Online Probabilistic Forecasting]]; returned HTTP 429 for [[FlowLOB - Flow-Matching Limit Order Book Generation]], [[The Price of Permission - Classification Uncertainty in Constrained Capital Markets]], and several other checked IDs.

## Shortlist Triage

### Saved / Updated Source Notes

1. [[Marking-Aware Sequential VaR Recalibration for Option Books]]
   - Evidence quality: **Evidence-backed at abstract level as risk-control methodology**.
   - Practicality: **foundational / retail-adaptable with option-chain data**.
   - Why it matters: option-book VaR should define the book, marking rule, loss scale, and forecast-time information set before modeling. This is directly useful for SPX/SPXW option-selling and event-risk overlays.
   - Decay / failure concerns: recalibrated VaR can become false comfort if book construction changes, quote marks leak, or spread/margin mechanics are ignored.

2. [[FlowLOB - Flow-Matching Limit Order Book Generation]]
   - Evidence quality: **Plausible but untested at abstract level as simulator methodology**.
   - Practicality: **foundational / institutional-only as written / retail-adaptable as simulator benchmark**.
   - Why it matters: synthetic LOB generation should be evaluated by downstream execution-decision utility, not just path realism. Useful for the execution-cost and market-impact validation stack.
   - Decay / failure concerns: HKEX-trained synthetic realism may not transfer to U.S. equities/options or crypto; simulator artifacts can overfit execution policies.

3. [[The Price of Permission - Classification Uncertainty in Constrained Capital Markets]]
   - Evidence quality: **Plausible but untested for tradable use**.
   - Practicality: **retail-adaptable / foundational as an event-study template**.
   - Why it matters: constrained-investor-base events may be tradable only when official eligibility changes, marginal-buyer mechanism, liquidity, timestamping, and costs are validated. The U.S. unconditional permission premium result is weak/null, while Malaysian official-list inclusions are more supportive but caveated.
   - Decay / failure concerns: pre-event rejection suggests leakage/anticipation; local-market frictions and crowding can erase 10–20 day effects.

4. [[Defensive Boosting for Online Probabilistic Forecasting]]
   - Evidence quality: **Evidence-backed at abstract level as theory/method**.
   - Practicality: **foundational / retail-adaptable as forecast-audit design**.
   - Why it matters: an online forecast module that can emit interval-level no-edge/no-deploy certificates is useful for binary direction, volatility-break, and risk-throttle models.
   - Decay / failure concerns: Brier-score improvements do not imply trade utility; interval selection and base-rate leakage remain major risks.

### Screened but Not Saved

- Alpha Architect, “VIX and Trend Following Revisited”: high-interest practitioner lead, but direct fetch returned HTTP 403 during this run. Not saved because feed metadata alone is insufficient evidence.
- “AI-Driven Multiscenario Interest Rate Forecasting”: validated abstract describes a banking ALM prototype and scenario platform; useful context but too institutional and too weakly connected to current coding needs to preserve today.
- “On the Expected Maximum Deficit and the Optimal Allocation of Reserves”: mathematically rigorous reserve/risk-measure paper, but less directly useful than option-book VaR for current equities/options/crypto implementation.
- “Supervised Mixed-Frequency Learning for Macro-Financial Forecasting When Factors are Weak” and “Learning about Treatment Effects in Panels under Unknown Interference”: plausible framework leads, but not saved today to keep the daily pass focused; both remain watch-only adjacent-domain leads.
- Generic agentic/LLM trading leads from the feed were downranked unless they provided leakage controls, strong simple baselines, realistic costs, and transparent out-of-sample validation.

## Literature Connections / Framework Leads

### Reinforces

- [[Marking-Aware Sequential VaR Recalibration for Option Books]] strengthens the existing option-risk branch around [[SPX Short-Dated Put-Writing with VIX and Fractional-Kelly Sizing]], [[When the Fed Speaks - Volatility Surface Forecasts around FOMC]], and [[Conformal Kelly - Uncertainty-Scaled Fractional Position Sizing]]. The shared framework is target-definition-first option risk: define book/marking/loss/information set before applying VaR, conformal, Kelly, or event filters.
- [[FlowLOB - Flow-Matching Limit Order Book Generation]] reinforces the market-impact/execution validation branch around [[Optimal Execution with Passive Market Impact]], [[Can Large Language Models Execute Parent Orders]], and [[When Large Trades Are Not News - Liquidity Tail Risk and Price Discovery]]. The key synthesis is that simulator realism must be tested by holdout execution decisions.
- [[The Price of Permission - Classification Uncertainty in Constrained Capital Markets]] reinforces event-study inference standards from [[Bias-Robust Causal Inference for Panel Data]] and capacity/crowding standards from [[Robustness or Crowding - Experimental Design for Trading Strategy Capacity]].
- [[Defensive Boosting for Online Probabilistic Forecasting]] connects to [[Marginally Useful - Conformal Prediction Information Gap]], [[Train Often Deploy Selectively - Forward-Gated Model Replacement in Crypto Markets]], and [[CLQT Cost-Aware Benchmark for LLM Portfolio-Management Agents]]: forecast guarantees need no-edge/no-deploy handling and action attribution.

### Contradicts / Weakens

- Permission effects should not be generalized into a broad U.S. constrained-investor-base premium; the validated abstract explicitly reports no robust unconditional U.S. permission premium.
- LOB generators should not be treated as evidence that an execution policy works unless rankings transfer from synthetic data to real holdout data.

### Transfers Across Asset Classes

- Marking-aware risk targets transfer from SPX/QQQ option books to earnings straddles, FOMC option-event exclusions, and crypto option books where reliable mark definitions exist.
- Online forecast no-edge certificates can transfer to crypto regime/risk throttles, but only after base-rate and turnover/cost tests.
- Permission/classification uncertainty may transfer from Shariah lists to index/ETF eligibility, mandate eligibility, rating/collateral eligibility, and borrow/short-sale permission events.

## Registry / Queue Decisions

- Candidate registry: updated with four tracked candidates from this run.
- Framework registry: updated with a short 2026-08-14 synthesis entry.
- Open questions: updated with four new research questions.
- Coding-ready queue: reviewed but unchanged. None of today’s items supplied complete rules, data, costs, baselines, and go/no-go criteria sufficient for promotion. The Marking-Aware VaR item should feed the existing high-priority standard audit block and SPX/SPXW option-risk work rather than become a standalone queue item.

## Hygiene Check

Post-write hygiene completed after creating four source notes and this review note:

- New source titles appear in `01 Sources/Source Index.md` after the index update.
- `Research Review Index.md` links to this timestamped review note.
- Major new wikilinks point to existing notes or notes created in this run.
- Framework labels without dedicated notes were kept as plain text.
- Vault-root zero-byte markdown check found no zero-byte `.md` files at the vault root.
- Link probe found one pre-existing unresolved registry target, `Quant Research/04 Backtest Specs/Backtest Spec Index`, unrelated to this run; no new unresolved source/review links were introduced.
