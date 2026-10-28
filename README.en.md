[Español](https://github.com/Rxyxs) · **English**

![Banner](assets/banner.gif)

<div align="center">

# Pablo Reyes

**Data Scientist · Universidad Mayor · Santiago, Chile**

<a href="https://rxyxs.github.io/"><img src="https://img.shields.io/badge/Portfolio-0D1117?style=for-the-badge&logo=githubpages&logoColor=00FF66" alt="Portfolio"></a>
<a href="https://www.linkedin.com/in/pablo-reyes-pino"><img src="https://img.shields.io/badge/LinkedIn-0D1117?style=for-the-badge&logo=linkedin&logoColor=00FF66" alt="LinkedIn"></a>
<a href="https://rxyxs.github.io/assets/cv/Pablo_Reyes_CV_EN.pdf"><img src="https://img.shields.io/badge/CV-0D1117?style=for-the-badge&logo=adobeacrobatreader&logoColor=00FF66" alt="CV"></a>
<a href="mailto:preyesp09@gmail.com"><img src="https://img.shields.io/badge/Email-0D1117?style=for-the-badge&logo=gmail&logoColor=00FF66" alt="Email"></a>

</div>

---

I'm a data scientist in Santiago, Chile. What interests me is the part of the job after the model is trained: **whether the number holds up on real data and whether someone can make a decision with it**. That's why most of my projects start from Chilean public data, such as Cochilco, the CMF, ChileCompra or the CNE, and from concrete problems in mining, energy and finance.

Often the result wasn't the one I expected. A hospital readmission model reached an AUC of 0.805 because it counted all of a patient's visits, including the very readmission it was meant to predict; using only what the hospital knows at discharge, and testing on new patients, it lands at 0.671. Switching pension funds at the bottom of a crash feels prudent, but across 2,000 histories built from 24 years of daily fund values it costs 1.9 points of real return a year. I publish those findings the same as the positive ones, and every number comes from code that runs end to end. And when I moved ten projects from simulated to real data, almost all of them lost their headline result; how much, and why, is further down.

## Featured projects

<table>
<tr>
<td width="50%" valign="top">
<h3><a href="https://github.com/Rxyxs/chile-pension-fund-switching-cost">Panic-switching pension funds</a></h3>
<sub>real data · <a href="https://rxyxs.github.io/chile-pension-fund-switching-cost/">page</a></sub>
<p>24 years of daily unit values, in UF. Switching to Fund E at the bottom of a crash costs <b>1.9 points</b> of real return a year; switching earlier gets the <b>same Sharpe</b> as a static mix: there is no timing, there is less equity.</p>
<code>duckdb</code> <code>counterfactual-analysis</code> <code>behavioral-finance</code>
</td>
<td width="50%" valign="top">
<h3><a href="https://github.com/Rxyxs/chile-mining-fleet-causal-impact">Causal impact in a mining fleet</a></h3>
<sub>real + simulated · <a href="https://rxyxs.github.io/chile-mining-fleet-causal-impact/">page</a></sub>
<p>Did the maintenance program work, and on which trucks? On real sensor data from 60,000 Scania trucks, <b>the default DRLearner collapses (r = −0.01)</b>; the cause was isolated and it recovers to 0.61–0.79.</p>
<code>causal-inference</code> <code>econml</code> <code>difference-in-differences</code>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<h3><a href="https://github.com/Rxyxs/retail-demand-forecasting-favorita">Retail demand as an inventory decision</a></h3>
<sub>real data · <a href="https://rxyxs.github.io/retail-demand-forecasting-favorita/">page</a></sub>
<p>3,000,888 sales rows. A quarter of the "zero demand" was <b>stores that had not opened yet</b>, and the model with the best metric leaves a stockout on <b>41%</b> of store-days.</p>
<code>demand-forecasting</code> <code>lightgbm</code> <code>quantile-regression</code>
</td>
<td width="50%" valign="top">
<h3><a href="https://github.com/Rxyxs/chile-mining-ops-agent">Mining operations agent with a local LLM</a></h3>
<sub>real data · <a href="https://rxyxs.github.io/chile-mining-ops-agent/">page</a></sub>
<p>An agent with Qwen 2.5 running on CPU, over real plant and ChileCompra data, measured on 100 queries: it picks the right tool <b>99 times</b> but miscopies large amounts; returning them in millions lifts grounded answers from <b>67 to 86</b>.</p>
<code>llm-agent</code> <code>tool-calling</code> <code>evaluation</code>
</td>
</tr>
</table>

## Expected vs. observed data behavior

Twelve projects were first designed on simulated data, which encodes what each problem is expected to look like, and then evaluated with the same method on real data. The table compares the expected metric with the observed one and summarizes what explains the gap.

| Project | Metric | Expected → observed | Interpretation |
|---|---|---|---|
| **[E-commerce fraud pipeline](https://github.com/Rxyxs/fraud-detection-techniques-lab)**<br><sub>IEEE-CIS, 590k transactions</sub> | PR-AUC | 0.993 → **0.052** | The behavioral features carry almost no signal on real fraud. |
| **[C + Ruby + Python fraud engine](https://github.com/Rxyxs/chile-polyglot-fraud-engine)**<br><sub>IEEE-CIS</sub> | PR-AUC | 1.000 → **0.098** | Two of its four rules never fire: their lists were invented. |
| **[Unsupervised graph AML](https://github.com/Rxyxs/fraud-detection-techniques-lab)**<br><sub>Elliptic, 204k Bitcoin transactions</sub> | ROC-AUC | 0.893 → **0.17–0.33** | Illicit flows are typical, not anomalous: it falls below random. |
| **[Blast fragmentation](https://github.com/Rxyxs/chile-mining-grade-blast-quality-dotnet)**<br><sub>97 published blasts, unseen mine</sub> | R² | 0.957 → **−0.59** | A random split lets it recognise the site; at a new mine it is worse than the mean. |
| **[Order-flow detector (C++)](https://github.com/Rxyxs/lithium-orderbook-imbalance-cpp)**<br><sub>IEX and Binance</sub> | Alerts (target 0.27%) | 0.02% → **1.4–24%** | Real tails are far heavier than the assumed Student-t. |
| **[19 anomaly detectors](https://github.com/Rxyxs/paysim-anomaly-detection-benchmark)**<br><sub>ULB and IEEE-CIS</sub> | Baseline ROC-AUC | 0.383 → **0.931** | The 'below chance' baseline was a simulator artifact; the ranking barely transfers. |
| **[Multi-task maintenance network](https://github.com/Rxyxs/failure-prediction-signal-lab)**<br><sub>23,550 SCANIA trucks</sub> | AUC vs. LightGBM | ties → **0.62 vs. 0.71** | The shared network loses both tasks on real trucks, even after correcting the validation scale. |
| **[Credit risk lab](https://github.com/Rxyxs/credit-risk-scoring-lab)**<br><sub>Lending Club, 621k loans</sub> | AUC, scorecard vs. boosting | 0.733 vs. 0.716 → **0.647 vs. 0.660** | On the weak signal of a real book boosting wins; the monotonic constraint still costs nothing. |
| **[A/B experimentation](https://github.com/Rxyxs/chile-fintech-experimentation-lab)**<br><sub>Criteo, 14M users</sub> | Effect after CUPED adjustment | unchanged → **−24% to −39%** | SRM passes, but the pre-test features predict the arm: the file was rebalanced and adjustment corrects the estimate. |
| **[Last-mile logistics](https://github.com/Rxyxs/chile-spatial-logistics-opt)**<br><sub>OSRM, 86k road pairs</sub> | Route plan, km | 572 → **835 driven** | The simulated detour factor falls short: 19% of real trips exceed its maximum. |
| **[Hourly power demand (R)](https://github.com/Rxyxs/chile-energy-grid-forecasting-r)**<br><sub>CEN, 2 years of hourly demand</sub> | Hourly MAPE, TBATS vs. naive | 4.28% vs. 6.73% → **7.01% vs. 5.81%** | Without a calendar, Christmas and Fiestas Patrias sink the classical models; the naive forecast adapts within a day. |
| **[Hourly SEN price by bus](https://github.com/Rxyxs/chile-energy-grid-forecasting)**<br><sub>CEN daily reports, 4 years, 6 buses</sub> | Price WAPE, LightGBM | 8.77% → **18.71%** | Zeros in the north, regime shifts and a north-south split; at Puerto Montt it loses to persistence. |

## Projects by kind of problem

43 projects across 9 kinds of problem; click a category to open it, or see them all in the [portfolio](https://rxyxs.github.io/en/).

<details>
<summary><b>1. Forecasting what comes next</b> · 7 projects</summary>

| Project | What it solves and what it found | Stack |
|---|---|---|
| **[Retail demand (Favorita)](https://github.com/Rxyxs/retail-demand-forecasting-favorita)**<br><sub>real data · [page](https://rxyxs.github.io/retail-demand-forecasting-favorita/)</sub> | Forecast scored as a purchase decision: quantiles only pay above a ~3:1 cost ratio. | `lightgbm` `quantile-regression` `newsvendor` |
| **[Chilean bank delinquency (CMF)](https://github.com/Rxyxs/chile-banking-delinquency-cmf)**<br><sub>real data · [page](https://rxyxs.github.io/chile-banking-delinquency-cmf/)</sub> | Panel from 128 CMF Excel files. Stress test with lag and signs chosen without look-ahead: only consumer and commercial beat no change (0.73 and 0.85). Per-bank LightGBM does not; SHAP shows it learns the regime. | `stress-testing` `shap` `fastapi` |
| **[Chile's power grid, hourly](https://github.com/Rxyxs/chile-energy-grid-forecasting)**<br><sub>real data · [page](https://rxyxs.github.io/chile-energy-grid-forecasting/)</sub> | 4 years of real hourly data read from the vector charts of the grid coordinator's daily reports (0.04 USD/MWh residual). Price by bus: 17.88% WAPE vs 21.88% naive; blending with persistence fixes Puerto Montt. | `lightgbm` `pdf-extraction` `time-series` |
| **[Chile's power grid, in R](https://github.com/Rxyxs/chile-energy-grid-forecasting-r)**<br><sub>real data · [page](https://rxyxs.github.io/chile-energy-grid-forecasting-r/)</sub> | Real hourly SEN demand, solar and wind: LightGBM with a holiday calendar forecasts the next day at 2.48% MAPE vs 3.61% naive; ARIMA and TBATS lose over the holidays; real wind has half the volatility the reconstruction implied. | `r` `lightgbm` `forecasting` |
| **[Copper volatility](https://github.com/Rxyxs/copper-volatility-forecaster)**<br><sub>real data · [page](https://rxyxs.github.io/copper-volatility-forecaster/)</sub> | 14 years of real LME prices: GARCH(1,1) has the best QLIKE and only HAR-X, with the VIX and the dollar, ties it. CatBoost re-tuned in every fold does not beat it. | `garch` `catboost` `shap` |
| **[High-frequency volatility](https://github.com/Rxyxs/reading-market-turbulence)**<br><sub>real data · [page](https://rxyxs.github.io/reading-market-turbulence/)</sub> | 24.8M Binance trades: at 30 s, persistence (RMSPE 4.58) beats LightGBM and the neural net. | `high-frequency-trading` `lightgbm` `duckdb` |
| **[Customer lifetime value](https://github.com/Rxyxs/customer-lifetime-value)**<br><sub>real data · [page](https://rxyxs.github.io/customer-lifetime-value/)</sub> | BG/NBD and Gamma-Gamma coded from the likelihood. Predicting 26 weeks: **-2%** error on total purchases, against +68% for the naive rate and +24% for LightGBM. | `bg-nbd` `gamma-gamma` `retention` |

</details>

<details>
<summary><b>2. Catching fraud and anomalies</b> · 7 projects</summary>

| Project | What it solves and what it found | Stack |
|---|---|---|
| **[Fraud and AML lab](https://github.com/Rxyxs/fraud-detection-techniques-lab)**<br><sub>real data · [page](https://rxyxs.github.io/fraud-detection-techniques-lab/)</sub> | Four techniques, all with real data: the e-commerce pipeline drops from a synthetic PR-AUC of 0.993 to 0.052 on IEEE-CIS, and the unsupervised AML ensemble falls below random on Elliptic (ROC-AUC 0.17-0.33) because illicit flows are typical, not anomalous. | `fraud-detection` `aml` `xgboost` |
| **[16 detectors on mobile-money fraud](https://github.com/Rxyxs/paysim-anomaly-detection-benchmark)**<br><sub>real + simulated · [page](https://rxyxs.github.io/paysim-anomaly-detection-benchmark/)</sub> | 19 detectors on PaySim and on real fraud (ULB cards, IEEE-CIS e-commerce): the ranking barely transfers (Spearman 0.28-0.38) and on e-commerce no detector exceeds PR-AUC 0.22. | `isolation-forest` `local-outlier-factor` `imbalanced-data` |
| **[Public procurement anomalies](https://github.com/Rxyxs/chile-public-procurement-anomalies)**<br><sub>real data · [page](https://rxyxs.github.io/chile-public-procurement-anomalies/)</sub> | 13.7 M ChileCompra order lines: Compra Ágil orders pile up under the cap and the pile moved with the law, but there is little sign of split purchases. Isolation Forest finds 38.8% of planted anomalies reviewing 5%. | `public-procurement` `bunching` `isolation-forest` |
| **[Polyglot fraud engine](https://github.com/Rxyxs/chile-polyglot-fraud-engine)**<br><sub>real + simulated · [page](https://rxyxs.github.io/chile-polyglot-fraud-engine/)</sub> | The same C + Ruby + Python engine on 590,540 real transactions (IEEE-CIS): PR-AUC 0.098 against the synthetic 1.000, and its layers add nothing over the native features. | `c` `ruby` `prometheus` |
| **[Market tick anomalies (C++)](https://github.com/Rxyxs/market-tick-anomaly-engine-cpp)**<br><sub>real data</sub> | EWMA and CUSUM validated on the March 2020 crypto crash, at 7.26M ticks/s. | `cpp` `cusum` `ewma` |
| **[Lithium order-flow imbalance (C++)](https://github.com/Rxyxs/lithium-orderbook-imbalance-cpp)**<br><sub>real + simulated · [page](https://rxyxs.github.io/lithium-orderbook-imbalance-cpp/)</sub> | On real IEX and Binance tapes the detector alerts on 1.4-24% of windows, not 0.27%, and does not anticipate price; the Apr 2023 lithium news day was a volume event (12x), not an imbalance one. | `cpp` `order-flow` `market-microstructure` |
| **[Anomalies in sensor streams (NAB)](https://github.com/Rxyxs/iot-anomaly-benchmark)**<br><sub>real data · [page](https://rxyxs.github.io/iot-anomaly-benchmark/)</sub> | NAB scorer reimplemented and validated 9/9 against published results. Reporting only the onset of each excursion lifts a seasonal detector from 2.4 to 41; cross-validated it scores **42.4**, above the published Gaussian baseline. | `anomaly-detection` `time-series` `benchmark` |

</details>

<details>
<summary><b>3. Anticipating equipment failure</b> · 3 projects</summary>

| Project | What it solves and what it found | Stack |
|---|---|---|
| **[Predictive maintenance (4 datasets)](https://github.com/Rxyxs/heavy-truck-predictive-maintenance)**<br><sub>real data · [page](https://rxyxs.github.io/heavy-truck-predictive-maintenance/)</sub> | 4 public datasets (2 real Scania truck sets, a metro compressor, NASA's simulated turbofans), 8 model families and a Docker demo: SCANIA rescales each variable differently across train, validation and test (adversarial AUC 1.00); fixing it cuts predicted risk from 16.9% to 4.2% (2.7% actual). On APS, cost 9,150 vs the IDA 2016 winner's 9,920. | `predictive-maintenance` `distribution-shift` `deep-learning` |
| **[Failure from continuous signal](https://github.com/Rxyxs/failure-prediction-signal-lab)**<br><sub>real data</sub> | Bearings (NASA IMS), earthquakes (LANL) and 23,550 real SCANIA trucks: spectral boosting beats a CNN by 2.5×, and the multi-task network that tied on the synthetic fleet loses on real trucks, even after correcting the validation scale (AUC 0.62 vs 0.71). | `remaining-useful-life` `signal-processing` `fft` |
| **[SAG mill digital twin](https://github.com/Rxyxs/chile-mining-sag-energy-digital-twin)**<br><sub>real + simulated · [page](https://rxyxs.github.io/chile-mining-sag-energy-digital-twin/)</sub> | Kalman estimates ore hardness with 79% less error; energy priced with real CNE marginal costs (95 months). | `digital-twin` `kalman-filter` `lightgbm` |

</details>

<details>
<summary><b>4. Measuring causes and evaluating decisions</b> · 5 projects</summary>

| Project | What it solves and what it found | Stack |
|---|---|---|
| **[Mining fleet causal impact](https://github.com/Rxyxs/chile-mining-fleet-causal-impact)**<br><sub>real + simulated · [page](https://rxyxs.github.io/chile-mining-fleet-causal-impact/)</sub> | Uplift and staggered DiD; the ATT matches a reference implementation on a real panel. | `causal-inference` `econml` `uplift-modeling` |
| **[A/B experimentation](https://github.com/Rxyxs/chile-fintech-experimentation-lab)**<br><sub>real + simulated · [page](https://rxyxs.github.io/chile-fintech-experimentation-lab/)</sub> | Sample size, SRM, CUPED, multiple testing and an mSPRT you can check daily, verified in simulation and on Criteo's real 14M-user experiment: SRM passes, but covariate adjustment moves the effect by 39%. | `ab-testing` `cuped` `sequential-testing` |
| **[Pension funds](https://github.com/Rxyxs/chile-pension-fund-switching-cost)**<br><sub>real data · [page](https://rxyxs.github.io/chile-pension-fund-switching-cost/)</sub> | A regime signal that "earned" 1.4–2.3% a year ties a static mix on Sharpe out of sample. In real terms, 2021–23 fell 26%. | `duckdb` `counterfactual-analysis` `pensions` |
| **[Late deliveries on a marketplace (Olist)](https://github.com/Rxyxs/olist-delivery-delays)**<br><sub>real data · [page](https://rxyxs.github.io/olist-delivery-delays/)</sub> | 96k real orders. Arriving late causes **-1.97 review points** (AIPW), with most of the damage in the first week. Filtering out pre-delivery reviews would have dropped 74% of late orders. | `causal-inference` `aipw` `survival-analysis` |
| **[Grocery price elasticity](https://github.com/Rxyxs/retail-price-elasticity)**<br><sub>real data · [page](https://rxyxs.github.io/retail-price-elasticity/)</sub> | 580 products, 2,500 real households. Ignoring display and mailer overstates elasticity by 40%; double ML gives **-1.50**. A 10% discount only pays for itself above 50% gross margin, even for beer. | `double-machine-learning` `fixed-effects` `pricing` |

</details>

<details>
<summary><b>5. Optimizing operations</b> · 4 projects</summary>

| Project | What it solves and what it found | Stack |
|---|---|---|
| **[Flotation plant](https://github.com/Rxyxs/flotation-plant-silica-soft-sensor)**<br><sub>real data · [page](https://rxyxs.github.io/flotation-plant-silica-soft-sensor/)</sub> | Real iron-ore plant: R² 0.83 on a random split is -0.43 in time order; only recent lab results beat persistence, and four models prescribe opposite pH moves. | `soft-sensor` `walk-forward` `optimization` |
| **[Last-mile logistics](https://github.com/Rxyxs/chile-spatial-logistics-opt)**<br><sub>real + simulated · [page](https://rxyxs.github.io/chile-spatial-logistics-opt/)</sub> | Multi-depot routing with time windows on real population (Kontur rescaled to Censo 2017) and real roads (OSRM): a plan built on simulated distances is 46% longer once driven. | `or-tools` `vrptw` `h3` `osrm` |
| **[Churn as a business decision](https://github.com/Rxyxs/customer-churn-mlops-platform)**<br><sub>real data · [page](https://rxyxs.github.io/customer-churn-mlops-platform/)</sub> | 10,000 real bank customers: the complaints column was a leak (AUC 1.00 vs 0.85); a value-based threshold recovers US$189,930 contacting 42%, vs US$143,842 contacting everyone. | `mlflow` `fastapi` `docker` |
| **[Quality failures on a Bosch line](https://github.com/Rxyxs/bosch-line-quality)**<br><sub>real data · [page](https://rxyxs.github.io/bosch-line-quality/)</sub> | 1.18M real parts: failures come in lots (11x next to a failed part). Shuffled CV overstates (0.40 vs 0.21 on later parts). Inspecting the riskiest 5% catches **61%** of failures. | `lightgbm` `imbalanced-learning` `quality-control` |

</details>

<details>
<summary><b>6. Measuring and managing financial risk</b> · 4 projects</summary>

| Project | What it solves and what it found | Stack |
|---|---|---|
| **[Credit risk lab](https://github.com/Rxyxs/credit-risk-scoring-lab)**<br><sub>real + simulated · [page](https://rxyxs.github.io/credit-risk-scoring-lab/)</sub> | 26 techniques on simulated books (R+Python+C scorecard at 270.6M rows/s, IFRS 9 PD, shadow/canary/retraining lifecycle) and a 27th that tests them on 621k real Lending Club loans: the monotonic constraint is still free and the scorecard no longer wins. | `scorecard` `ifrs9` `mlops` |
| **[Systemic risk in Chile](https://github.com/Rxyxs/chile-fintech-systemic-risk)**<br><sub>real data · [page](https://rxyxs.github.io/chile-fintech-systemic-risk/)</sub> | Six languages on Central Bank data. The LSTM (51.0%) doesn't beat the majority class (53.6%). | `julia` `r` `cplusplus` |
| **[Crypto quant lab](https://github.com/Rxyxs/crypto-quant-techniques-lab)**<br><sub>real data · [page](https://rxyxs.github.io/crypto-quant-techniques-lab/)</sub> | Eight techniques. All five strategies lose after costs; spoofing detection works (0.92 precision). | `quantitative-finance` `cointegration` `nlp` |
| **[Copper Asian options (C++)](https://github.com/Rxyxs/copper-options-montecarlo-cpp)**<br><sub>pricing model · [page](https://rxyxs.github.io/copper-options-montecarlo-cpp/)</sub> | C++20 Monte Carlo under GBM, Schwartz and Heston: 9.64× on 16 threads and a real bias fixed. | `cpp20` `monte-carlo` `heston-model` |

</details>

<details>
<summary><b>7. Getting the data in order</b> · 4 projects</summary>

| Project | What it solves and what it found | Stack |
|---|---|---|
| **[Cleaning toolkit across 4 domains](https://github.com/Rxyxs/data-cleaning-toolkit)**<br><sub>real data · [page](https://rxyxs.github.io/data-cleaning-toolkit/)</sub> | One toolkit on Central Bank, COCHILCO and World Bank data; it caught a corrupted source value. | `data-quality` `pydantic` `pytest` |
| **[Mining data warehouse](https://github.com/Rxyxs/data-warehouse-analitico-mineria-chile)**<br><sub>real + simulated · [page](https://rxyxs.github.io/data-warehouse-analitico-mineria-chile/)</sub> | Real Cochilco yearbook 2000-2025 and real SEN marginal cost by bus in dbt + DuckDB: at the spot price copper mining's electricity fell from USD 518 to 262 per tonne (2022-2024); 131 tests, simulated site layer. | `dbt` `duckdb` `star-schema` |
| **[E-commerce lakehouse (110M events)](https://github.com/Rxyxs/ecommerce-lakehouse-duckdb)**<br><sub>real data · [page](https://rxyxs.github.io/ecommerce-lakehouse-duckdb/)</sub> | 110M real events in DuckDB: 48 hours of purchases are missing and cart tracking changes 6 times, so the funnel is measured per regime. | `duckdb` `polars` `pyspark` `parquet` |
| **[Chilean data, refreshed every day](https://github.com/Rxyxs/chile-macro-data-pipeline)**<br><sub>real data · [page](https://rxyxs.github.io/chile-macro-data-pipeline/)</sub> | dbt + DuckDB + GitHub Actions: nine public series (UF, dollar, copper, CPI, policy rate, IMACEC, unemployment, pension funds, CMF delinquency) are downloaded, tested and published every day; if mindicador is down, the UF and the dollar come from the SII. | `dbt` `duckdb` `github-actions` |

</details>

<details>
<summary><b>8. Classifying and estimating</b> · 4 projects</summary>

| Project | What it solves and what it found | Stack |
|---|---|---|
| **[E-commerce recommender](https://github.com/Rxyxs/ecommerce-recommender-rees46)**<br><sub>real data · [page](https://rxyxs.github.io/ecommerce-recommender-rees46/)</sub> | 85M real events: a LightGBM ranker lifts recall@20 from 0.244 to 0.395, but 71% of purchases are items never viewed before. | `lightgbm` `learning-to-rank` `duckdb` |
| **[Scientific classification](https://github.com/Rxyxs/scientific-classification-lab)**<br><sub>real data · [page](https://rxyxs.github.io/scientific-classification-lab/)</sub> | Higgs boson (AMS 3.64 vs 3.8–3.9 for the winners) and Kepler exoplanets (79.3% vs 49.8%). | `gradient-boosting` `pytorch` `astronomy` |
| **[Ore grade and fragmentation (.NET)](https://github.com/Rxyxs/chile-mining-grade-blast-quality-dotnet)**<br><sub>real + simulated · [page](https://rxyxs.github.io/chile-mining-grade-blast-quality-dotnet/)</sub> | ML.NET + ONNX in a desktop app; on 97 real published blasts the model explains 0.76 with a random split but -0.59 at a new mine, against the synthetic 0.957. | `csharp` `ml-net` `onnx` |
| **[30-day hospital readmission](https://github.com/Rxyxs/hospital-readmission-risk)**<br><sub>real data · [page](https://rxyxs.github.io/hospital-readmission-risk/)</sub> | 99k real hospital encounters. Counting future visits inflates AUC from 0.67 to **0.80**. Calibrated model with net benefit at 5-39% thresholds; no racial gap, but weaker for patients over 70. | `calibration` `decision-curve` `fairness` |

</details>

<details>
<summary><b>9. Text, language and images</b> · 5 projects</summary>

| Project | What it solves and what it found | Stack |
|---|---|---|
| **[Mining safety RAG](https://github.com/Rxyxs/rag-seguridad-minera-chile)**<br><sub>real regulation · [page](https://rxyxs.github.io/rag-seguridad-minera-chile/)</sub> | Hybrid search over DS 132; re-ranking lifts MRR from 0.920 to 0.981. | `rag` `hybrid-search` `cross-encoder` |
| **[Mining operations agent](https://github.com/Rxyxs/chile-mining-ops-agent)**<br><sub>real data · [page](https://rxyxs.github.io/chile-mining-ops-agent/)</sub> | Agent over real plant and ChileCompra data, measured on 100 queries with local Qwen: right tool 99 times, and reporting amounts in millions lifts grounded answers from 67 to 86. | `llm-agent` `tool-calling` `duckdb` |
| **[Local language model for industry](https://github.com/Rxyxs/slm-industrial-gateway)**<br><sub>real + simulated · [page](https://rxyxs.github.io/slm-industrial-gateway/)</sub> | Evaluated on 100 real flotation-plant cases: listing tool arguments cuts invalid calls from 69 to 16, and auditing the request gives 25 of 25 correct safety decisions. | `llama-cpp` `qlora` `guardrails` |
| **[YOLOv8 on a Raspberry Pi (thesis)](https://github.com/Rxyxs/yolov8-separable-convolutions)**<br><sub>real data (COCO) · [page](https://rxyxs.github.io/yolov8-separable-convolutions/)</sub> | 68% fewer parameters and ~10× faster on a Raspberry Pi, at mAP50 0.175 vs 0.212. | `yolov8` `computer-vision` `edge-computing` |
| **[Aircraft contrails in satellite imagery](https://github.com/Rxyxs/contrail-detection-goes16)**<br><sub>real data · [page](https://rxyxs.github.io/contrail-detection-goes16/)</sub> | Segmentation on GOES-16 without downloading 451 GB: remote reads of the Kaggle zip and OpenContrails. Upsampling the input 2x is worth +0.05 Dice; stacking frames hurts. **0.597** on Kaggle private. | `pytorch` `segmentation` `satellite-imagery` |

</details>

## Experience

**[Fuel control for a bus fleet](https://github.com/Rxyxs/bus-fleet-fuel-efficiency)** · <sub>real job, fictitious sample data</sub>  
Each of the 20 depots tracked fuel in its own Excel file. First I wrote a Python script that merges the sheets, compresses them into consolidated tables by depot, day and month, computes each bus's km per litre against its previous load and flags the ones outside their model's range. Then an AppSheet app that replaced the sheets: operators record loads, pump readings and tanks from their phone, and the app computes per-pump consumption, theoretical stock and AdBlue. Reviewing the code, I fixed three bugs: dates sorted wrongly across months, buses left without a range because of how the standard was written, and every bus's first load flagged by mistake.  
`python` `pandas` `appsheet` `excel` `data-cleaning`

## Open-source tool

**[datoschile: Chilean public data in one line](https://github.com/Rxyxs/datoschile)**  
A Python library that downloads Chile's reference data, clean and in a DataFrame: 17 official Central Bank series with no key (dollar, policy rate, IMACEC, GDP, unemployment, reserves), UF, UTM, CPI, copper and other metals from Cochilco, pension funds, CMF bank delinquency, legal holidays and business days. It fixes real source errors, like the dollar leaking into the UF in 2014, the CPI's four base changes (without chain-linking, 12-month inflation is off by up to 25.8 points) or mindicador's IMACEC, which keeps the first published figure and matches the current one on only 3.8% of months. It publishes an interactive dashboard that updates every week.

```python
import datoschile as dc

dc.resumen()                          # 9 indicadores con su fuente
dc.bcentral.serie("imacec")           # serie oficial, sin clave
dc.cochilco.cobre(desde=2024)         # cobre LME del día
dc.convertir.deflactar(1_000_000, "2015-01")
```

[Open the interactive dashboard](https://rxyxs.github.io/datoschile/)

## Stack

<table>
<tr><td><b>Languages</b></td><td><img src="https://img.shields.io/badge/Python-0D1117?style=flat-square&logo=python&logoColor=00FF66" alt="Python"> <img src="https://img.shields.io/badge/SQL-0D1117?style=flat-square&logo=postgresql&logoColor=00FF66" alt="SQL"> <img src="https://img.shields.io/badge/R-0D1117?style=flat-square&logo=r&logoColor=00FF66" alt="R"> <img src="https://img.shields.io/badge/C%2B%2B-0D1117?style=flat-square&logo=cplusplus&logoColor=00FF66" alt="C++"> <img src="https://img.shields.io/badge/C-0D1117?style=flat-square&logo=c&logoColor=00FF66" alt="C"> <img src="https://img.shields.io/badge/C%23-0D1117?style=flat-square&logo=dotnet&logoColor=00FF66" alt="C#"> <img src="https://img.shields.io/badge/Julia-0D1117?style=flat-square&logo=julia&logoColor=00FF66" alt="Julia"> <img src="https://img.shields.io/badge/Go-0D1117?style=flat-square&logo=go&logoColor=00FF66" alt="Go"> <img src="https://img.shields.io/badge/Ruby-0D1117?style=flat-square&logo=ruby&logoColor=00FF66" alt="Ruby"></td></tr>
<tr><td><b>Data</b></td><td><img src="https://img.shields.io/badge/pandas-0D1117?style=flat-square&logo=pandas&logoColor=00FF66" alt="pandas"> <img src="https://img.shields.io/badge/Polars-0D1117?style=flat-square&logo=polars&logoColor=00FF66" alt="Polars"> <img src="https://img.shields.io/badge/NumPy-0D1117?style=flat-square&logo=numpy&logoColor=00FF66" alt="NumPy"> <img src="https://img.shields.io/badge/DuckDB-0D1117?style=flat-square&logo=duckdb&logoColor=00FF66" alt="DuckDB"> <img src="https://img.shields.io/badge/dbt-0D1117?style=flat-square" alt="dbt"> <img src="https://img.shields.io/badge/Parquet-0D1117?style=flat-square&logo=apacheparquet&logoColor=00FF66" alt="Parquet"> <img src="https://img.shields.io/badge/Pydantic-0D1117?style=flat-square&logo=pydantic&logoColor=00FF66" alt="Pydantic"> <img src="https://img.shields.io/badge/Jupyter-0D1117?style=flat-square&logo=jupyter&logoColor=00FF66" alt="Jupyter"></td></tr>
<tr><td><b>ML & statistics</b></td><td><img src="https://img.shields.io/badge/scikit--learn-0D1117?style=flat-square&logo=scikitlearn&logoColor=00FF66" alt="scikit-learn"> <img src="https://img.shields.io/badge/LightGBM-0D1117?style=flat-square" alt="LightGBM"> <img src="https://img.shields.io/badge/XGBoost-0D1117?style=flat-square" alt="XGBoost"> <img src="https://img.shields.io/badge/CatBoost-0D1117?style=flat-square" alt="CatBoost"> <img src="https://img.shields.io/badge/PyTorch-0D1117?style=flat-square&logo=pytorch&logoColor=00FF66" alt="PyTorch"> <img src="https://img.shields.io/badge/SciPy-0D1117?style=flat-square&logo=scipy&logoColor=00FF66" alt="SciPy"> <img src="https://img.shields.io/badge/Optuna-0D1117?style=flat-square&logo=optuna&logoColor=00FF66" alt="Optuna"> <img src="https://img.shields.io/badge/Plotly-0D1117?style=flat-square&logo=plotly&logoColor=00FF66" alt="Plotly"></td></tr>
<tr><td><b>Language, vision & edge</b></td><td><img src="https://img.shields.io/badge/LangChain-0D1117?style=flat-square&logo=langchain&logoColor=00FF66" alt="LangChain"> <img src="https://img.shields.io/badge/Hugging%20Face-0D1117?style=flat-square&logo=huggingface&logoColor=00FF66" alt="Hugging Face"> <img src="https://img.shields.io/badge/Ultralytics%20YOLO-0D1117?style=flat-square&logo=ultralytics&logoColor=00FF66" alt="Ultralytics YOLO"> <img src="https://img.shields.io/badge/ONNX-0D1117?style=flat-square&logo=onnx&logoColor=00FF66" alt="ONNX"> <img src="https://img.shields.io/badge/Raspberry%20Pi-0D1117?style=flat-square&logo=raspberrypi&logoColor=00FF66" alt="Raspberry Pi"></td></tr>
<tr><td><b>Production</b></td><td><img src="https://img.shields.io/badge/FastAPI-0D1117?style=flat-square&logo=fastapi&logoColor=00FF66" alt="FastAPI"> <img src="https://img.shields.io/badge/Streamlit-0D1117?style=flat-square&logo=streamlit&logoColor=00FF66" alt="Streamlit"> <img src="https://img.shields.io/badge/MLflow-0D1117?style=flat-square&logo=mlflow&logoColor=00FF66" alt="MLflow"> <img src="https://img.shields.io/badge/Docker-0D1117?style=flat-square&logo=docker&logoColor=00FF66" alt="Docker"> <img src="https://img.shields.io/badge/GitHub%20Actions-0D1117?style=flat-square&logo=githubactions&logoColor=00FF66" alt="GitHub Actions"> <img src="https://img.shields.io/badge/pytest-0D1117?style=flat-square&logo=pytest&logoColor=00FF66" alt="pytest"> <img src="https://img.shields.io/badge/Prometheus-0D1117?style=flat-square&logo=prometheus&logoColor=00FF66" alt="Prometheus"> <img src="https://img.shields.io/badge/Grafana-0D1117?style=flat-square&logo=grafana&logoColor=00FF66" alt="Grafana"> <img src="https://img.shields.io/badge/Git-0D1117?style=flat-square&logo=git&logoColor=00FF66" alt="Git"> <img src="https://img.shields.io/badge/Linux-0D1117?style=flat-square&logo=linux&logoColor=00FF66" alt="Linux"></td></tr>
</table>

---

<div align="center">
<sub><a href="https://rxyxs.github.io/">Portfolio</a> · <a href="https://www.linkedin.com/in/pablo-reyes-pino">LinkedIn</a> · preyesp09@gmail.com · Santiago, Chile</sub>
</div>
