![Portada](assets/banner.png)

<p align="center">
<a href="https://www.linkedin.com/in/pablo-reyes-pino"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"></a>
<a href="mailto:preyesp09@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white"></a>
</p>

<p align="center">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&pause=1000&color=39FF14&center=true&vCenter=true&width=650&lines=29+proyectos%2C+reproducibles+de+punta+a+punta;Causal+Inference+%C2%B7+Quant+%C2%B7+Ingenier%C3%ADa+Polig+lota;Baselines+honestos+%C2%B7+sin+fuga+de+datos+%C2%B7+sin+mocks">
</p>

<div align="center">

[ Versión en Español ](#-español) &nbsp;|&nbsp; [ English Version ](#-english)

</div>

---

<a name="-español"></a>
# ¡Hola! Soy Pablo Reyes
### Data Scientist / ML Engineer | Python · R · SQL · C++ · C# · Ruby · Julia

Científico de Datos titulado de la Universidad Mayor, especializado en **analítica industrial para minería, energía y finanzas cuantitativas**. Construyo soluciones *end-to-end* — ETL, modelos predictivos y causales, motores de optimización, APIs en producción — con el mismo estándar con el que se evalúa código de producción, no un notebook de portafolio: reproducibilidad, tests automatizados, prevención de fuga de datos y resultados honestos, incluidos los negativos.

Cada repo corre completo con un solo comando (`python -m src.pipeline` o equivalente), reporta los números de esa corrida — no de una versión anterior — y documenta en el propio README los bugs reales que aparecieron en el camino.

## Stack Tecnológico

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![R](https://img.shields.io/badge/R-276DC3?style=flat-square&logo=r&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=postgresql&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white)
![C#](https://img.shields.io/badge/C%23-239120?style=flat-square&logo=csharp&logoColor=white)
![Julia](https://img.shields.io/badge/Julia-9558B2?style=flat-square&logo=julia&logoColor=white)
![Ruby](https://img.shields.io/badge/Ruby-CC342D?style=flat-square&logo=ruby&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-EB5E28?style=flat-square)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![dbt](https://img.shields.io/badge/dbt-FF694B?style=flat-square&logo=dbt&logoColor=white)
![DuckDB](https://img.shields.io/badge/DuckDB-FFF000?style=flat-square&logo=duckdb&logoColor=black)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=flat-square&logo=powerbi&logoColor=black)

## Minería & Energía

Analítica industrial aplicada a operaciones mineras y energéticas de alta escala.

* **[Optimización Geometalúrgica en Flotación (Cu/Mo)](https://github.com/Rxyxs/optimizacion-geometalurgica-flotacion-cobre):** Ensamble XGBoost+CatBoost sin fuga temporal, dos motores de optimización (Algoritmo Genético + `scipy.optimize`) validados cruzados entre sí **[Mejora de recuperación +2.4%]**.
* **[Impacto Causal en Flota Minera](https://github.com/Rxyxs/chile-mining-fleet-causal-impact):** Estimación del impacto causal real de mantenimiento predictivo mediante *Doubly Robust Learners* (DRLearner) y *Causal Forest*, con análisis de sensibilidad de tendencias paralelas para el estimador de diferencias-en-diferencias **[Reducción de downtime estimado ~14%; 41 tests]**.
* **[Gemelo Digital SAG (Eficiencia Energética)](https://github.com/Rxyxs/chile-mining-sag-energy-digital-twin):** *Kalman Filter* para *soft-sensing* de dureza de mineral + modelos de supervivencia (CoxPH) para estimación de RUL y optimización prescriptiva de *setpoints* **[Ahorro de energía en molienda ~8.5%]**.
* **[Data Warehouse Analítico de Minería](https://github.com/Rxyxs/data-warehouse-analitico-mineria-chile):** Arquitectura dbt + DuckDB (staging → marts, 83 tests de calidad) unificando flotación, mantenimiento CAEX y seguridad **[Latencia de consulta <50ms]**.
* **[Mantenimiento Predictivo y RUL](https://github.com/Rxyxs/chile-mining-predictive-maintenance):** Redes neuronales multitarea en PyTorch y análisis de supervivencia (CoxPH) para predicción de Vida Útil Restante de flota CAEX **[MAE < 12 hrs en predicción RUL; 47 tests]**.
* **[Calidad de Tronadura/Ley (.NET)](https://github.com/Rxyxs/chile-mining-grade-blast-quality-dotnet):** Pipeline ML.NET en C# comparando SDCA vs. FastTree para predecir calidad de ley post-tronadura **[R² = 0.860 SDCA vs. 0.833 FastTree]**.
* **[Pronóstico de Red Eléctrica (Costo Marginal)](https://github.com/Rxyxs/chile-energy-grid-forecasting):** Comparación baseline/ensamble/MLP PyTorch (loss Huber) con activación Swish ganadora sobre LightGBM y XGBoost **[WAPE = 5.42% MLP vs. 6.26% LightGBM vs. 7.06% XGBoost]**.
* **[Pronóstico de Red Eléctrica en R](https://github.com/Rxyxs/chile-energy-grid-forecasting-r):** Variante en R del pronóstico de costo marginal, comparando cuatro enfoques estadísticos (ARIMA/SARIMAX/TBATS/ETS/GARCH) con validación cruzada rolling.
* **[Detección de Anomalías en Procurement Minero](https://github.com/Rxyxs/mining-procurement-anomaly-engine):** Z-score + Isolation Forest + Autoencoder PyTorch para detectar compras y proveedores anómalos en la cadena de suministro minera.
* **[RAG de Seguridad Minera Chile](https://github.com/Rxyxs/rag-seguridad-minera-chile):** Sistema de recuperación aumentada híbrida (BM25 + embeddings densos) con reranker cross-encoder sobre normativa chilena de seguridad minera.
* **[Optimización Espacial de Logística](https://github.com/Rxyxs/chile-spatial-logistics-opt):** Optimización de rutas (VRP) alimentada por un módulo de predicción de demanda comparando Ridge/RF/MLP como insumo del ruteo.

## Fraude, AML & Riesgo Crediticio

* **[Laboratorio de Detección de Fraude & AML](https://github.com/Rxyxs/fraud-detection-techniques-lab):** Cuatro técnicas en un repo, cada una en su carpeta con pipeline propio — pipeline multi-lenguaje sobre 568k transacciones reales (LogReg+SMOTE, CatBoost, XGBoost, MLP PyTorch con Focal Loss, validación adversaria de splits, calibración de umbral por matriz de costo, export a ONNX), *scoring* de fraude e-commerce en tiempo real, AML no supervisado sobre grafos temporales (NetworkX) con explicabilidad SHAP en vivo, y Autoencoder/VAE/Deep SVDD frente a XGBoost supervisado **[Reducción de costo = 44.7% vs. umbral 0.5; latencia p99 < 15ms]**.
* **[Laboratorio de Scoring de Riesgo Crediticio](https://github.com/Rxyxs/credit-risk-scoring-lab):** Ocho técnicas, cada una con pipeline de un comando y su propia suite de tests (**194 tests** en las técnicas 03-08) — scorecard políglota R+Python+C, interoperabilidad bidireccional R↔Python (`reticulate`/`rpy2`), Cox PH implementado desde cero (Breslow/Efron, Newton-Raphson amortiguado, test PH de Schoenfeld) para estructura temporal de PD bajo IFRS 9, muestreo de Gibbs jerárquico sobre aumentación Pólya-Gamma, restricciones monotónicas auditadas por contrafactuales + decisión conformal de Mondrian, *binning* óptimo resuelto por programación dinámica exacta, auditoría de sesgo en préstamo justo (reconstruir género desde las propias features del modelo, AUC 0.768), y DP-SGD con contador RDP desde cero validado por ataque de membresía **[AUC test = 0.733 scorecard R vs. 0.715 MLP]**.
* **[Motor de Fraude Políglota](https://github.com/Rxyxs/chile-polyglot-fraud-engine):** Arquitectura híbrida de baja latencia — C para el *hot-path* de *scoring* vía feature store en memoria mapeada, Ruby como motor de reglas, Python para la inferencia ML — con cada capa perfilada por separado (Prometheus/Grafana) para identificar el cuello de botella real **[Feature store ~568k req/s; capa Ruby ~12-14k req/s; 60 tests en C+RSpec+pytest]**.
* **[Riesgo Sistémico Fintech Chile (Políglota)](https://github.com/Rxyxs/chile-fintech-systemic-risk):** Arquitectura de 6 lenguajes sobre el mercado financiero chileno — ETL Python+DuckDB con indicadores reales del Banco Central, PD con XGBoost+SHAP, LSTM PyTorch, econometría en R (cointegración/Granger/GARCH), clustering en Julia, motor Monte Carlo C++/OpenMP para VaR, y microservicio Go sirviendo las predicciones ya calculadas **[1M trayectorias Monte Carlo en 14.4ms; hallazgo honesto: el LSTM (51.2%) no supera el baseline de clase mayoritaria (53.6%)]**.
* **[Detección de Fraude Bancario (PaySim)](https://github.com/Rxyxs/Proyectos_ML_anomalias):** Isolation Forest/LOF vs. baseline MAD-z vs. Autoencoder PyTorch sobre transacciones simuladas PaySim.

## Quant & Trading Sistemático

* **[Laboratorio Quant Cripto](https://github.com/Rxyxs/crypto-quant-techniques-lab):** Ocho técnicas cuantitativas sobre datos reales de Binance, cada una en su carpeta — clasificación de dirección con deep learning (Dense NN y Conv1D-Attention), impacto de precio y liquidez (Ridge/XGBoost/MLP Huber), pares cointegrados con Engle-Granger y *hedge ratio* dinámico por Filtro de Kalman, optimización de portafolio media-varianza, detección de régimen por clustering, *screening* de sentimiento con FinBERT vs. TF-IDF, detección de *spoofing* en libro de órdenes, y framework de backtesting con persistencia en DuckDB **[Sharpe Ratio = 1.84 backtested en el par cointegrado]**.
* **[Costo de Cambiarse de Fondo de Pensiones](https://github.com/Rxyxs/chile-pension-fund-switching-cost):** Cuánto cuesta realmente cambiarse de fondo en pánico durante una caída, medido sobre datos diarios reales de la Superintendencia de Pensiones (2002-2026, ~278k filas).
* **[Pricing de Opciones Monte Carlo en C++](https://github.com/Rxyxs/copper-options-montecarlo-cpp):** Motor Monte Carlo multi-hilo en C++20 (OpenMP) usando el modelo de reversión a la media de Schwartz (1997) para valoración de opciones asiáticas sobre cobre **[1M trayectorias en <250ms]**.
* **[Leyendo la Turbulencia del Mercado](https://github.com/Rxyxs/reading-market-turbulence):** Forecasting de volatilidad realizada sobre 24.8M trades reales de Binance (BTC/ETH), MLP con embeddings de activo, hallazgo honesto: el baseline de persistencia le gana a los modelos en el horizonte de 30s **[RMSPE = 4.58 baseline]**.
* **[Pronosticador de Volatilidad del Cobre](https://github.com/Rxyxs/copper-volatility-forecaster):** Forecasting de volatilidad realizada del cobre con MLP PyTorch (Huber + RMSPE) sobre baseline estadístico.
* **[Desequilibrio de Order Book de Litio (C++)](https://github.com/Rxyxs/lithium-orderbook-imbalance-cpp):** Motor C++ de bajo overhead para desequilibrio de libro de órdenes **[95/95 tests pasando]**.
* **[Motor de Anomalías en Ticks de Mercado (C++)](https://github.com/Rxyxs/market-tick-anomaly-engine-cpp):** Detección de anomalías en ticks con EWMA-zscore, CUSUM y ensamble **[Throughput ~7.26M ticks/seg]**.

## Ciencia de Datos Aplicada

* **[Laboratorio de Experimentación Fintech (A/B Testing)](https://github.com/Rxyxs/chile-fintech-experimentation-lab):** Toolkit de diseño y análisis de experimentos — cálculo de tamaño de muestra, detección de Sample Ratio Mismatch, reducción de varianza con CUPED, corrección BH-FDR entre métricas de guardrail, chequeo de efecto de novedad — validado con un arnés de calibración Monte Carlo que mide si cada regla de detención controla de verdad la tasa de error que promete **[Hallazgo honesto: el peeking diario ingenuo infla el falso-positivo de 5% nominal a 24.2%, y una regla de detención bayesiana asumida "segura" casi no mejora (20.5%); 29 tests, ninguno mockeado]**.
* **[Limpieza_Datos: Toolkit + 4 Dominios Reales](https://github.com/Rxyxs/Limpieza_Datos):** Toolkit reusable de limpieza y modelamiento (`src/toolkit/`, 18 módulos) probado sin cambios contra 4 bases de datos públicas reales e independientes — finanzas (Banco Central de Chile), minería del cobre (COCHILCO), agricultura (Banco Mundial), y un Excel de 80MB del Banco Mundial transformado en un data warehouse real (DuckDB). Cada modelo entrena un mínimo de 100 épocas reales, **190 tests** (148 unitarios + smoke tests reales por dominio, ninguno mockeado), y tres bugs reales encontrados y corregidos en el camino: un dato corrupto en la fuente detectado por un detector de saltos de nivel por mediana móvil, y dos colapsos *dying ReLU* distintos (R² de hasta -8746 antes del fix). El propio toolkit audita los cuatro dominios: `drift.target_shift` reproduce el R² negativo del baseline hasta la cuarta decimal en dos de ellos, y `keys`/`leakage` verifican integridad referencial y fuga de datos con evidencia determinística, no con umbrales arbitrarios.
* **[Laboratorio de Clasificación Científica](https://github.com/Rxyxs/scientific-classification-lab):** Dos problemas de clasificación en ciencias físicas — eventos de colisión ATLAS/CERN (818k eventos, imputación con causa física por multiplicidad de jets, CatBoost/LightGBM/PyTorch optimizados para la métrica AMS del challenge original) y tránsitos de exoplanetas Kepler (9.564 objetos vía la API pública del NASA Exoplanet Archive, XGBoost+SHAP vs. ablación PyTorch ReLU/GELU/Swish) **[AMS = 3.58 honesto vs. 3.8-3.9 del leaderboard histórico; Accuracy = 79.3% XGBoost vs. 49.8% baseline en Kepler]**.
* **[Laboratorio de Predicción de Falla desde Señal](https://github.com/Rxyxs/failure-prediction-signal-lab):** Tres dominios de predicción de tiempo hasta falla desde señal continua — RUL multitarea de flota minera, vibración real de rodamientos (NASA/IMS, 3 bancos run-to-failure, FFT + features espectrales, GroupKFold leave-one-experiment-out) y señal acústica sísmica (LANL) **[MAE = 21.6% de vida restante en rodamientos, tras corregir un bug real de escala temporal]**.

## Agentes & LLM

* **[Agente de Operaciones Mineras (Tool-Calling)](https://github.com/Rxyxs/chile-mining-ops-agent):** Agente con el SDK de OpenAI que despacha herramientas Python reales (consultas a warehouse DuckDB, scoring de riesgo, detección de anomalías) en vez de responder desde texto libre, con gráficos de evaluación reales (ROC/PR, scores de anomalía) generados a partir de las mismas tools **[43/43 tests, incl. dispatch con cliente OpenAI mockeado]**.

## Deep Learning & Edge AI

* **[Eficiencia de YOLOv8 en Edge AI (Tesis)](https://github.com/Rxyxs/yolov8-separable-convolutions):** Rediseño del *head* de YOLOv8 con *Depthwise Separable Convolutions*, entrenado desde cero sobre COCO2017 y medido en GPU, CPU y Raspberry Pi 4 bajo el mismo protocolo — **68% menos parámetros (3.99M → 1.26M)** y **~10x más rápido en Raspberry Pi** **[0.68 vs. 0.07 FPS y 1.48s vs. 13.93s por imagen en RPi 4; costo honesto: mAP50 0.175 vs. 0.212]**.
* **[Plataforma MLOps de Churn](https://github.com/Rxyxs/customer-churn-mlops-platform):** Predicción de churn con LightGBM + MLflow, calibración de umbral por costo/LTV en vez de por AUC a secas, API de inferencia FastAPI y simulador de ROI en Streamlit, validado en un holdout nunca visto durante entrenamiento ni optimización de umbral **[Contactar a todos: +US$42,717 · umbral óptimo del modelo: +US$75,847 contactando solo 78.6% — casi el doble de retorno, con menos gente contactada]**.

## Contacto

* **Ubicación:** Santiago, Chile
* **LinkedIn:** [linkedin.com/in/pablo-reyes-pino](https://www.linkedin.com/in/pablo-reyes-pino)
* **Email:** preyesp09@gmail.com

---

<a name="-english"></a>
# Hi there! I'm Pablo Reyes
### Data Scientist / ML Engineer | Python · R · SQL · C++ · C# · Ruby · Julia

Data Scientist graduated from Universidad Mayor, specialized in **industrial analytics for mining, energy, and quantitative finance**. I build end-to-end solutions — ETL, predictive and causal models, optimization engines, production APIs — held to the standard used to evaluate production code, not a portfolio notebook: reproducibility, automated tests, leakage prevention, and honestly reported results, negative ones included.

Every repo runs end to end from a single command (`python -m src.pipeline` or equivalent), reports the numbers from that run — not from an earlier one — and documents the real bugs found along the way in the README itself.

## Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![R](https://img.shields.io/badge/R-276DC3?style=flat-square&logo=r&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=postgresql&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white)
![C#](https://img.shields.io/badge/C%23-239120?style=flat-square&logo=csharp&logoColor=white)
![Julia](https://img.shields.io/badge/Julia-9558B2?style=flat-square&logo=julia&logoColor=white)
![Ruby](https://img.shields.io/badge/Ruby-CC342D?style=flat-square&logo=ruby&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-EB5E28?style=flat-square)
![scikit--learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![dbt](https://img.shields.io/badge/dbt-FF694B?style=flat-square&logo=dbt&logoColor=white)
![DuckDB](https://img.shields.io/badge/DuckDB-FFF000?style=flat-square&logo=duckdb&logoColor=black)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=flat-square&logo=powerbi&logoColor=black)

## Mining & Energy

My core specialization — industrial analytics applied to real Chilean mining and energy operations.

* **[Geometallurgical Flotation Optimization (Cu/Mo)](https://github.com/Rxyxs/optimizacion-geometalurgica-flotacion-cobre):** Leak-free XGBoost+CatBoost ensemble, two optimization engines (Genetic Algorithm + `scipy.optimize`) cross-validated against each other **[+2.4% recovery]**.
* **[Mining Fleet Causal Impact](https://github.com/Rxyxs/chile-mining-fleet-causal-impact):** Real causal impact — not just correlation — of a predictive-maintenance program: Doubly Robust Learners, Causal Forest, and a dedicated sensitivity analysis for the difference-in-differences estimator's parallel-trends assumption **[~14% estimated downtime reduction; 41 tests]**.
* **[SAG Digital Twin (Energy Efficiency)](https://github.com/Rxyxs/chile-mining-sag-energy-digital-twin):** Kalman Filter for ore-hardness soft-sensing + survival analysis (CoxPH) for RUL estimation and prescriptive setpoint optimization **[~8.5% grinding energy savings]**.
* **[Mining Analytics Data Warehouse](https://github.com/Rxyxs/data-warehouse-analitico-mineria-chile):** dbt + DuckDB architecture (staging → marts, 83 data-quality tests), unifying flotation, CAEX maintenance, and safety data **[<50ms query latency]**.
* **[Predictive Maintenance & RUL](https://github.com/Rxyxs/chile-mining-predictive-maintenance):** Multi-task PyTorch neural networks and survival analysis (CoxPH) for haul-truck Remaining Useful Life **[MAE < 12 hrs on RUL prediction; 47 tests]**.
* **[Blast/Grade Quality (.NET)](https://github.com/Rxyxs/chile-mining-grade-blast-quality-dotnet):** ML.NET pipeline in C# comparing SDCA vs. FastTree to predict post-blast ore grade quality **[R² = 0.860 SDCA vs. 0.833 FastTree]**.
* **[Power Grid Forecasting (Marginal Cost)](https://github.com/Rxyxs/chile-energy-grid-forecasting):** Baseline/ensemble/PyTorch MLP comparison (Huber loss) with Swish winning over LightGBM and XGBoost **[WAPE = 5.42% MLP vs. 6.26% LightGBM vs. 7.06% XGBoost]**.
* **[Power Grid Forecasting in R](https://github.com/Rxyxs/chile-energy-grid-forecasting-r):** R variant of the marginal-cost forecast, comparing four statistical approaches (ARIMA/SARIMAX/TBATS/ETS/GARCH) with rolling cross-validation.
* **[Mining Procurement Anomaly Engine](https://github.com/Rxyxs/mining-procurement-anomaly-engine):** Z-score + Isolation Forest + PyTorch Autoencoder to flag anomalous purchases and suppliers in the mining supply chain.
* **[Chile Mining Safety RAG](https://github.com/Rxyxs/rag-seguridad-minera-chile):** Hybrid retrieval (BM25 + dense embeddings) with a cross-encoder reranker over Chilean mining safety regulations.
* **[Spatial Logistics Optimization](https://github.com/Rxyxs/chile-spatial-logistics-opt):** Vehicle routing optimization (VRP) fed by a demand-forecasting module comparing Ridge/RF/MLP as routing input.

## Fraud, AML & Credit Risk

* **[Fraud & AML Detection Lab](https://github.com/Rxyxs/fraud-detection-techniques-lab):** Four techniques in one repo, each in its own folder with its own pipeline — a multi-language pipeline over 568k real transactions (LogReg+SMOTE, CatBoost, XGBoost, PyTorch MLP with Focal Loss, adversarial split validation, cost-matrix threshold calibration, ONNX export), real-time e-commerce fraud scoring, unsupervised AML over temporal graphs (NetworkX) with live SHAP explainability, and Autoencoder/VAE/Deep SVDD against supervised XGBoost **[44.7% cost reduction vs. a 0.5 threshold; p99 latency < 15ms]**.
* **[Credit Risk Scoring Lab](https://github.com/Rxyxs/credit-risk-scoring-lab):** Eight techniques, each with a one-command pipeline and its own test suite (**194 tests** across techniques 03-08) — polyglot R+Python+C scorecard, bidirectional R↔Python interop (`reticulate`/`rpy2`), Cox PH implemented from scratch (Breslow/Efron, damped Newton-Raphson, Schoenfeld PH test) for an IFRS 9 PD term structure, hierarchical Bayesian Gibbs sampling on Pólya-Gamma augmentation, monotonic constraints audited by counterfactual perturbation + Mondrian conformal decisioning, optimal binning solved by exact dynamic programming, a fair-lending bias audit (gender reconstructed from the model's own features at AUC 0.768), and DP-SGD with a from-scratch RDP accountant validated by a membership-inference attack **[Test AUC = 0.733 R scorecard vs. 0.715 MLP]**.
* **[Polyglot Fraud Engine](https://github.com/Rxyxs/chile-polyglot-fraud-engine):** Low-latency hybrid architecture — C for the scoring hot-path via a memory-mapped feature store, Ruby as the rules engine, Python for ML inference — with each layer profiled independently (Prometheus/Grafana) to find the real bottleneck **[Feature store ~568k req/s; Ruby rules layer ~12-14k req/s; 60 tests across C+RSpec+pytest]**.
* **[Chile Fintech Systemic Risk (Polyglot)](https://github.com/Rxyxs/chile-fintech-systemic-risk):** 6-language architecture over the Chilean financial market — Python+DuckDB ETL on real Central Bank indicators, XGBoost+SHAP PD model, PyTorch LSTM, R econometrics (cointegration/Granger/GARCH), Julia clustering, a C++/OpenMP Monte Carlo VaR engine, and a Go microservice serving the precomputed predictions **[1M Monte Carlo paths in 14.4ms; honest finding: the LSTM (51.2%) doesn't beat the majority-class baseline (53.6%)]**.
* **[Bank Fraud Detection (PaySim)](https://github.com/Rxyxs/Proyectos_ML_anomalias):** Isolation Forest/LOF vs. MAD-z baseline vs. PyTorch Autoencoder over simulated PaySim transactions.

## Quant & Systematic Trading

* **[Crypto Quant Techniques Lab](https://github.com/Rxyxs/crypto-quant-techniques-lab):** Eight quantitative techniques over real Binance data, each in its own folder — direction classification with deep learning (Dense NN and Conv1D-Attention), liquidity and price impact (Ridge/XGBoost/Huber MLP), cointegrated pairs with Engle-Granger and a Kalman-filtered dynamic hedge ratio, mean-variance portfolio optimization, regime detection by clustering, sentiment screening with FinBERT vs. TF-IDF, order-book spoofing detection, and a backtesting framework persisting to DuckDB **[Sharpe Ratio = 1.84 backtested on the cointegrated pair]**.
* **[Pension Fund Switching Cost](https://github.com/Rxyxs/chile-pension-fund-switching-cost):** What panic-switching pension funds during a drawdown actually costs, measured on real daily data from Chile's Superintendencia de Pensiones (2002-2026, ~278k rows).
* **[Monte Carlo Options Pricing in C++](https://github.com/Rxyxs/copper-options-montecarlo-cpp):** Multi-threaded Monte Carlo engine in C++20 (OpenMP), Schwartz (1997) mean-reverting model for copper Asian options **[1M paths in <250ms]**.
* **[Reading Market Turbulence](https://github.com/Rxyxs/reading-market-turbulence):** Realized volatility forecasting on 24.8M real Binance trades (BTC/ETH), MLP with symbol embeddings, honest finding: the persistence baseline beats the models at a 30s horizon **[RMSPE = 4.58 baseline]**.
* **[Copper Volatility Forecaster](https://github.com/Rxyxs/copper-volatility-forecaster):** Realized copper volatility forecasting with a PyTorch MLP (Huber + RMSPE) against a statistical baseline.
* **[Lithium Order Book Imbalance (C++)](https://github.com/Rxyxs/lithium-orderbook-imbalance-cpp):** Low-overhead C++ engine for order book imbalance **[95/95 tests passing]**.
* **[Market Tick Anomaly Engine (C++)](https://github.com/Rxyxs/market-tick-anomaly-engine-cpp):** Tick-level anomaly detection with EWMA-zscore, CUSUM, and ensemble **[~7.26M ticks/sec throughput]**.

## Applied Data Science

* **[Fintech Experimentation Lab (A/B Testing)](https://github.com/Rxyxs/chile-fintech-experimentation-lab):** An experiment design-and-analysis toolkit — sample-size calculation, Sample Ratio Mismatch detection, CUPED variance reduction, BH-FDR correction across guardrail metrics, a novelty-effect check — validated with a Monte Carlo calibration harness that measures whether each stopping rule actually controls the error rate it claims to **[Honest finding: naive daily peeking inflates the false-positive rate from a nominal 5% to 24.2%, and a Bayesian stopping rule assumed "safe" barely helps (20.5%); 29 tests, none mocked]**.
* **[Limpieza_Datos: Toolkit + 4 Real Domains](https://github.com/Rxyxs/Limpieza_Datos):** A reusable cleaning-and-modeling toolkit (`src/toolkit/`, 18 modules) proven unchanged against 4 real, independent public datasets — Chilean finance (Banco Central de Chile), copper mining (COCHILCO), agriculture (World Bank), and an 80MB World Bank Excel turned into a real DuckDB warehouse. Every model trains a minimum of 100 real epochs, **190 tests** (148 unit tests plus real per-domain smoke tests, none mocked), and three real bugs found and fixed along the way: a corrupted source value caught by a rolling-median level-jump detector, and two distinct "dying ReLU" collapses (R² as low as -8746 before the fix). The toolkit audits all four domains on its own: `drift.target_shift` reproduces the baseline's negative R² to four decimal places in two of them, and `keys`/`leakage` verify referential integrity and data leakage on deterministic evidence, not arbitrary thresholds.
* **[Scientific Classification Lab](https://github.com/Rxyxs/scientific-classification-lab):** Two classification problems from the physical sciences — ATLAS/CERN collision events (818k events, physically-caused missing-value imputation by jet multiplicity, CatBoost/LightGBM/PyTorch optimized for the challenge's own AMS metric) and Kepler exoplanet transits (9,564 objects via NASA's public Exoplanet Archive API, XGBoost+SHAP vs. a PyTorch ReLU/GELU/Swish ablation) **[AMS = 3.58 honest vs. 3.8-3.9 on the historical leaderboard; 79.3% accuracy XGBoost vs. 49.8% baseline on Kepler]**.
* **[Failure Prediction from Signal Lab](https://github.com/Rxyxs/failure-prediction-signal-lab):** Three domains of time-to-failure prediction from continuous signal — multi-task mining-fleet RUL, real bearing vibration (NASA/IMS, 3 run-to-failure rigs, FFT + spectral features, leave-one-experiment-out GroupKFold), and acoustic seismic signal (LANL) **[MAE = 21.6% of remaining life on bearings, after fixing a real time-scale bug]**.

## Agents & LLM

* **[Mining Ops Tool-Calling Agent](https://github.com/Rxyxs/chile-mining-ops-agent):** OpenAI SDK agent that dispatches real Python tools (DuckDB warehouse queries, credit-risk scoring, anomaly detection) instead of answering from free text, with real evaluation plots (ROC/PR, anomaly scores) generated from those same tools **[43/43 tests, incl. tool dispatch with a mocked OpenAI client]**.

## Deep Learning & Edge AI

* **[YOLOv8 Edge AI Efficiency Benchmark (Thesis)](https://github.com/Rxyxs/yolov8-separable-convolutions):** Redesigned the YOLOv8 Head with Depthwise Separable Convolutions, trained from scratch on COCO2017 and benchmarked on GPU, CPU and Raspberry Pi 4 under one protocol — **68% fewer parameters (3.99M → 1.26M)** and **~10x faster on Raspberry Pi** **[0.68 vs. 0.07 FPS and 1.48s vs. 13.93s per image on the RPi 4; honest cost: mAP50 0.175 vs. 0.212]**.
* **[Customer Churn MLOps Platform](https://github.com/Rxyxs/customer-churn-mlops-platform):** Churn prediction with LightGBM + MLflow, cost/LTV-weighted threshold calibration instead of a bare AUC cutoff, FastAPI inference, and a Streamlit ROI simulator — evaluated on a holdout never seen during training or threshold optimization **[Contact everyone: +$42,717 · model's optimal threshold: +$75,847 while contacting only 78.6% — nearly double the return, to fewer people]**.

## Connect with Me

* **Location:** Santiago, Chile
* **LinkedIn:** [linkedin.com/in/pablo-reyes-pino](https://www.linkedin.com/in/pablo-reyes-pino)
* **Email:** preyesp09@gmail.com

---
