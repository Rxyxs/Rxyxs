[Español](https://github.com/Rxyxs) · **English**

![Banner](assets/banner.png)

<div align="center">

# Pablo Reyes

**Data Scientist · Universidad Mayor · Santiago, Chile**

<a href="https://rxyxs.github.io/"><img src="https://img.shields.io/badge/Portfolio-0D1117?style=for-the-badge&logo=githubpages&logoColor=00FF66" alt="Portfolio"></a>
<a href="https://www.linkedin.com/in/pablo-reyes-pino"><img src="https://img.shields.io/badge/LinkedIn-0D1117?style=for-the-badge&logo=linkedin&logoColor=00FF66" alt="LinkedIn"></a>
<a href="mailto:preyesp09@gmail.com"><img src="https://img.shields.io/badge/Email-0D1117?style=for-the-badge&logo=gmail&logoColor=00FF66" alt="Email"></a>

</div>

---

This profile collects work and personal projects organized **by the kind of problem they solve**: forecasting, catching anomalies, anticipating failures, measuring causes, optimizing, managing risk, getting data in order, and working with text and images. The point is to show the different ways a data scientist can help an organization, in mining, energy, finance, retail or pensions.

The same rules apply throughout: the code runs end to end, the numbers come from that run, nearly every repo has tests and CI, and negative results are published like positive ones.

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
<h3><a href="https://github.com/Rxyxs/chile-fintech-experimentation-lab">A/B experimentation lab</a></h3>
<sub>Monte Carlo · <a href="https://rxyxs.github.io/chile-fintech-experimentation-lab/">page</a></sub>
<p>Checking an A/B test every day inflates the false-positive rate from 5% to <b>24.2%</b>, and the Bayesian rule usually assumed "safe" barely helps (<b>20.5%</b>).</p>
<code>ab-testing</code> <code>cuped</code> <code>sequential-testing</code>
</td>
</tr>
</table>

## Open-source tool

**[cordillera: Chilean public data in one line](https://github.com/Rxyxs/cordillera)**  
A Python library to download the UF, dollar, copper, pension fund unit values and CMF bank delinquency, clean and in a DataFrame. It fixes real source errors, like the dollar leaking into the UF in 2014 or the CMF Excel files' three layouts, and checks every week that the sources haven't changed.

```python
import cordillera as co

co.indicadores.uf(desde=2020)
co.pensiones.indice(fondos="A", desde=2008, real=True)
co.cmf.morosidad(solo_sistema=True)
```

## Experience

**[Fuel control for a bus fleet](https://github.com/Rxyxs/bus-fleet-fuel-efficiency)** · <sub>real job, fictitious sample data</sub>  
Each of the 17 depots tracked fuel in its own Excel file. First I wrote a Python script that merges the sheets, computes each bus's km per litre against its previous load and flags the ones outside their model's range. Then an AppSheet app that replaced the sheets: operators record loads, pump readings and tanks from their phone, and the app computes per-pump consumption, theoretical stock and AdBlue. Reviewing the code, I fixed three bugs: dates sorted wrongly across months, buses left without a range because of how the standard was written, and every bus's first load flagged by mistake.  
`python` `pandas` `appsheet` `excel` `data-cleaning`

## Projects by kind of problem

34 projects across 9 kinds of problem; click a category to open it, or see them all in the [portfolio](https://rxyxs.github.io/en/).

<details>
<summary><b>1. Forecasting what comes next</b> · 6 projects</summary>

| Project | What it solves and what it found | Stack |
|---|---|---|
| **[Retail demand (Favorita)](https://github.com/Rxyxs/retail-demand-forecasting-favorita)**<br><sub>real data · [page](https://rxyxs.github.io/retail-demand-forecasting-favorita/)</sub> | Forecast scored as a purchase decision: quantiles only pay above a ~3:1 cost ratio. | `lightgbm` `quantile-regression` `newsvendor` |
| **[Chilean bank delinquency (CMF)](https://github.com/Rxyxs/chile-banking-delinquency-cmf)**<br><sub>real data · [page](https://rxyxs.github.io/chile-banking-delinquency-cmf/)</sub> | Panel from 128 CMF Excel files. Only ARIMA at 3 months beats naive; adding unemployment, policy rate and IMACEC makes it worse. | `time-series` `forecasting` `credit-risk` |
| **[Chile's power grid, hourly](https://github.com/Rxyxs/chile-energy-grid-forecasting)**<br><sub>simulated</sub> | Solar, wind, demand and marginal cost at 5 nodes. Solar: 3.64% WAPE vs 26.95% naive; on wind, naive wins. | `lightgbm` `optuna` `time-series` |
| **[Chile's power grid, in R](https://github.com/Rxyxs/chile-energy-grid-forecasting-r)**<br><sub>simulated · [page](https://rxyxs.github.io/chile-energy-grid-forecasting-r/)</sub> | TBATS: 2.47% MAPE vs 6.54% seasonal naive; ETS's edge only shows under rolling validation. | `r` `arima` `garch` |
| **[Copper volatility](https://github.com/Rxyxs/copper-volatility-forecaster)**<br><sub>real data · [page](https://rxyxs.github.io/copper-volatility-forecaster/)</sub> | 14 years of real LME prices: GARCH(1,1) has the best QLIKE and only HAR-X, with the VIX and the dollar, ties it. CatBoost re-tuned in every fold does not beat it. | `garch` `catboost` `shap` |
| **[High-frequency volatility](https://github.com/Rxyxs/reading-market-turbulence)**<br><sub>real data · [page](https://rxyxs.github.io/reading-market-turbulence/)</sub> | 24.8M Binance trades: at 30 s, persistence (RMSPE 4.58) beats LightGBM and the neural net. | `high-frequency-trading` `lightgbm` `duckdb` |

</details>

<details>
<summary><b>2. Catching fraud and anomalies</b> · 6 projects</summary>

| Project | What it solves and what it found | Stack |
|---|---|---|
| **[Fraud and AML lab](https://github.com/Rxyxs/fraud-detection-techniques-lab)**<br><sub>real + simulated · [page](https://rxyxs.github.io/fraud-detection-techniques-lab/)</sub> | ROC-AUC makes a model with 3.4× worse PR-AUC look almost equal (0.931 vs 0.965); label-free graph AML: ROC-AUC 0.893. | `fraud-detection` `aml` `xgboost` |
| **[16 detectors on mobile-money fraud](https://github.com/Rxyxs/paysim-anomaly-detection-benchmark)**<br><sub>simulated · [page](https://rxyxs.github.io/paysim-anomaly-detection-benchmark/)</sub> | The statistical baseline lands below chance (ROC-AUC 0.383) and ensembles don't win. 266 tests. | `isolation-forest` `local-outlier-factor` `imbalanced-data` |
| **[Anomalous mining procurement invoices](https://github.com/Rxyxs/mining-procurement-anomaly-engine)**<br><sub>simulated</sub> | Reviewing only 5% of invoices, the autoencoder finds 37.3% of anomalies: ~7.5× chance. | `autoencoder` `pytorch` `unsupervised-learning` |
| **[Polyglot fraud engine](https://github.com/Rxyxs/chile-polyglot-fraud-engine)**<br><sub>simulated · [page](https://rxyxs.github.io/chile-polyglot-fraud-engine/)</sub> | C + Ruby + Python, each layer profiled: 31 ns per call in C; 4.68 ms p50 end to end. | `c` `ruby` `prometheus` |
| **[Market tick anomalies (C++)](https://github.com/Rxyxs/market-tick-anomaly-engine-cpp)**<br><sub>real data</sub> | EWMA and CUSUM validated on the March 2020 crypto crash, at 7.26M ticks/s. | `cpp` `cusum` `ewma` |
| **[Lithium order-flow imbalance (C++)](https://github.com/Rxyxs/lithium-orderbook-imbalance-cpp)**<br><sub>simulated · [page](https://rxyxs.github.io/lithium-orderbook-imbalance-cpp/)</sub> | Zero false positives outside the injected shock across 43,200 windows. | `cpp` `order-flow` `market-microstructure` |

</details>

<details>
<summary><b>3. Anticipating equipment failure</b> · 3 projects</summary>

| Project | What it solves and what it found | Stack |
|---|---|---|
| **[Predictive maintenance (SCANIA)](https://github.com/Rxyxs/heavy-truck-predictive-maintenance)**<br><sub>real data · [page](https://rxyxs.github.io/heavy-truck-predictive-maintenance/)</sub> | 23,550 trucks: −31% official cost on test, but the saving runs out if a visit costs double, because the model overstates risk. | `predictive-maintenance` `survival-analysis` `shap` |
| **[Failure from continuous signal](https://github.com/Rxyxs/failure-prediction-signal-lab)**<br><sub>real + simulated</sub> | Bearings (NASA IMS) and seismic signal (LANL): spectral features with boosting beat a CNN by 2.7×. | `remaining-useful-life` `signal-processing` `fft` |
| **[SAG mill digital twin](https://github.com/Rxyxs/chile-mining-sag-energy-digital-twin)**<br><sub>simulated · [page](https://rxyxs.github.io/chile-mining-sag-energy-digital-twin/)</sub> | Kalman estimates ore hardness with 79% less error; 24 h energy forecast 27.6% better than Holt-Winters. | `digital-twin` `kalman-filter` `lightgbm` |

</details>

<details>
<summary><b>4. Measuring causes and evaluating decisions</b> · 3 projects</summary>

| Project | What it solves and what it found | Stack |
|---|---|---|
| **[Mining fleet causal impact](https://github.com/Rxyxs/chile-mining-fleet-causal-impact)**<br><sub>real + simulated · [page](https://rxyxs.github.io/chile-mining-fleet-causal-impact/)</sub> | Uplift and staggered DiD; the ATT matches a reference implementation on a real panel. | `causal-inference` `econml` `uplift-modeling` |
| **[A/B experimentation](https://github.com/Rxyxs/chile-fintech-experimentation-lab)**<br><sub>Monte Carlo · [page](https://rxyxs.github.io/chile-fintech-experimentation-lab/)</sub> | Sample size, SRM, CUPED and multiple testing, with a harness that checks each rule's error rate. | `ab-testing` `cuped` `power-analysis` |
| **[Pension funds](https://github.com/Rxyxs/chile-pension-fund-switching-cost)**<br><sub>real data · [page](https://rxyxs.github.io/chile-pension-fund-switching-cost/)</sub> | A regime signal that "earned" 1.4–2.3% a year ties a static mix on Sharpe out of sample. In real terms, 2021–23 fell 26%. | `duckdb` `counterfactual-analysis` `pensions` |

</details>

<details>
<summary><b>5. Optimizing operations</b> · 3 projects</summary>

| Project | What it solves and what it found | Stack |
|---|---|---|
| **[Copper flotation](https://github.com/Rxyxs/optimizacion-geometalurgica-flotacion-cobre)**<br><sub>simulated</sub> | Reagents and pH per block: +27.6 pp recovery on the 150 worst blocks, with two optimizers that agree. | `genetic-algorithm` `nsga-ii` `shap` |
| **[Last-mile logistics](https://github.com/Rxyxs/chile-spatial-logistics-opt)**<br><sub>real districts, simulated demand · [page](https://rxyxs.github.io/chile-spatial-logistics-opt/)</sub> | Multi-depot routing with time windows over real polygons: 0 of 173 zones unserved. | `or-tools` `vrptw` `h3` |
| **[Churn as a business decision](https://github.com/Rxyxs/customer-churn-mlops-platform)**<br><sub>simulated · [page](https://rxyxs.github.io/customer-churn-mlops-platform/)</sub> | Threshold by customer value: +US$75,847 contacting 78.6%, vs +US$42,717 contacting everyone. | `mlflow` `fastapi` `docker` |

</details>

<details>
<summary><b>6. Measuring and managing financial risk</b> · 4 projects</summary>

| Project | What it solves and what it found | Stack |
|---|---|---|
| **[Credit risk lab](https://github.com/Rxyxs/credit-risk-scoring-lab)**<br><sub>real macro, simulated portfolio · [page](https://rxyxs.github.io/credit-risk-scoring-lab/)</sub> | 26 techniques: R+Python+C scorecard at 270.6M rows/s, IFRS 9 PD, bias audit and a shadow/canary/retraining lifecycle. | `scorecard` `ifrs9` `mlops` |
| **[Systemic risk in Chile](https://github.com/Rxyxs/chile-fintech-systemic-risk)**<br><sub>real data · [page](https://rxyxs.github.io/chile-fintech-systemic-risk/)</sub> | Six languages on Central Bank data. The LSTM (51.0%) doesn't beat the majority class (53.6%). | `julia` `r` `cplusplus` |
| **[Crypto quant lab](https://github.com/Rxyxs/crypto-quant-techniques-lab)**<br><sub>real data · [page](https://rxyxs.github.io/crypto-quant-techniques-lab/)</sub> | Eight techniques. All five strategies lose after costs; spoofing detection works (0.92 precision). | `quantitative-finance` `cointegration` `nlp` |
| **[Copper Asian options (C++)](https://github.com/Rxyxs/copper-options-montecarlo-cpp)**<br><sub>pricing model · [page](https://rxyxs.github.io/copper-options-montecarlo-cpp/)</sub> | C++20 Monte Carlo under GBM, Schwartz and Heston: 9.64× on 16 threads and a real bias fixed. | `cpp20` `monte-carlo` `heston-model` |

</details>

<details>
<summary><b>7. Getting the data in order</b> · 3 projects</summary>

| Project | What it solves and what it found | Stack |
|---|---|---|
| **[Cleaning toolkit across 4 domains](https://github.com/Rxyxs/data-cleaning-toolkit)**<br><sub>real data · [page](https://rxyxs.github.io/data-cleaning-toolkit/)</sub> | One toolkit on Central Bank, COCHILCO and World Bank data; it caught a corrupted source value. | `data-quality` `pydantic` `pytest` |
| **[Mining data warehouse](https://github.com/Rxyxs/data-warehouse-analitico-mineria-chile)**<br><sub>simulated · [page](https://rxyxs.github.io/data-warehouse-analitico-mineria-chile/)</sub> | dbt + DuckDB from staging to marts, 83 quality tests and model-ready views. | `dbt` `duckdb` `star-schema` |
| **[E-commerce lakehouse](https://github.com/Rxyxs/ecommerce-lakehouse-duckdb)**<br><sub>simulated · [page](https://rxyxs.github.io/ecommerce-lakehouse-duckdb/)</sub> | Polars + DuckDB over Parquet; repeating the benchmark 7 times changed the conclusion. | `polars` `duckdb` `parquet` |

</details>

<details>
<summary><b>8. Classifying and estimating</b> · 2 projects</summary>

| Project | What it solves and what it found | Stack |
|---|---|---|
| **[Scientific classification](https://github.com/Rxyxs/scientific-classification-lab)**<br><sub>real data · [page](https://rxyxs.github.io/scientific-classification-lab/)</sub> | Higgs boson (AMS 3.64 vs 3.8–3.9 for the winners) and Kepler exoplanets (79.3% vs 49.8%). | `gradient-boosting` `pytorch` `astronomy` |
| **[Ore grade and fragmentation (.NET)](https://github.com/Rxyxs/chile-mining-grade-blast-quality-dotnet)**<br><sub>simulated · [page](https://rxyxs.github.io/chile-mining-grade-blast-quality-dotnet/)</sub> | ML.NET + ONNX in a desktop app: P80 at R² 0.957. | `csharp` `ml-net` `onnx` |

</details>

<details>
<summary><b>9. Text, language and images</b> · 4 projects</summary>

| Project | What it solves and what it found | Stack |
|---|---|---|
| **[Mining safety RAG](https://github.com/Rxyxs/rag-seguridad-minera-chile)**<br><sub>real regulation · [page](https://rxyxs.github.io/rag-seguridad-minera-chile/)</sub> | Hybrid search over DS 132; re-ranking lifts MRR from 0.920 to 0.981. | `rag` `hybrid-search` `cross-encoder` |
| **[Mining operations agent](https://github.com/Rxyxs/chile-mining-ops-agent)**<br><sub>simulated · [page](https://rxyxs.github.io/chile-mining-ops-agent/)</sub> | An LLM that answers by calling tools (SQL, scoring, anomalies) instead of making up numbers. | `llm-agent` `tool-calling` `duckdb` |
| **[Local language model for industry](https://github.com/Rxyxs/slm-industrial-gateway)**<br><sub>simulated · [page](https://rxyxs.github.io/slm-industrial-gateway/)</sub> | Offline inference, guardrails and QLoRA; the base model makes up arguments in 94 of 100 prompts. | `llama-cpp` `qlora` `guardrails` |
| **[YOLOv8 on a Raspberry Pi (thesis)](https://github.com/Rxyxs/yolov8-separable-convolutions)**<br><sub>real data (COCO) · [page](https://rxyxs.github.io/yolov8-separable-convolutions/)</sub> | 68% fewer parameters and ~10× faster on a Raspberry Pi, at mAP50 0.175 vs 0.212. | `yolov8` `computer-vision` `edge-computing` |

</details>

## Tools

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
