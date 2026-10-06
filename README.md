🇨🇱 **Español** · 🇺🇸 [English](https://github.com/Rxyxs/Rxyxs/blob/main/README.en.md)

![Portada](assets/banner.png)

<div align="center">

# Pablo Reyes

**Científico de Datos · Universidad Mayor · Santiago, Chile**

<a href="https://www.linkedin.com/in/pablo-reyes-pino"><img src="https://img.shields.io/badge/LinkedIn-0D1117?style=for-the-badge&logo=linkedin&logoColor=00FF66" alt="LinkedIn"></a>
<a href="mailto:preyesp09@gmail.com"><img src="https://img.shields.io/badge/Email-0D1117?style=for-the-badge&logo=gmail&logoColor=00FF66" alt="Email"></a>

</div>

---

Este perfil reúne trabajo y proyectos propios ordenados **por el tipo de problema que resuelven**: pronosticar, detectar lo anómalo, anticipar fallas, medir causas, optimizar, gestionar riesgo, ordenar datos y trabajar con texto e imágenes. La idea es mostrar las distintas formas en que un científico de datos puede ayudar a una organización, en minería, energía, finanzas, retail o pensiones.

En todos sigo las mismas reglas: el código corre de principio a fin, las cifras salen de esa corrida, casi todos tienen tests y CI, y los resultados negativos se publican igual que los positivos.

## Proyectos destacados

<table>
<tr>
<td width="50%" valign="top">
<h3><a href="https://github.com/Rxyxs/chile-pension-fund-switching-cost">Cambiarse de fondo de pensiones en pánico</a></h3>
<sub>datos reales · <a href="https://rxyxs.github.io/chile-pension-fund-switching-cost/">página</a></sub>
<p>24 años de valores cuota diarios. Cambiarse al fondo E en el piso de una caída pierde plata en <b>97%</b> de 2.000 historias; con una regla que alguien podría seguir de verdad, en <b>59%</b>: casi una moneda al aire.</p>
<code>duckdb</code> <code>counterfactual-analysis</code> <code>behavioral-finance</code>
</td>
<td width="50%" valign="top">
<h3><a href="https://github.com/Rxyxs/chile-mining-fleet-causal-impact">Impacto causal en una flota minera</a></h3>
<sub>real + simulado · <a href="https://rxyxs.github.io/chile-mining-fleet-causal-impact/">página</a></sub>
<p>¿Funcionó el programa de mantenimiento, y en qué camiones? Con sensores reales de 60.000 camiones Scania, <b>el DRLearner por defecto colapsa (r = −0,01)</b>; se aisló la causa y se recupera a 0,61–0,79.</p>
<code>causal-inference</code> <code>econml</code> <code>difference-in-differences</code>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<h3><a href="https://github.com/Rxyxs/retail-demand-forecasting-favorita">Demanda retail como decisión de inventario</a></h3>
<sub>datos reales · <a href="https://rxyxs.github.io/retail-demand-forecasting-favorita/">página</a></sub>
<p>3.000.888 filas de ventas. Un cuarto de la "demanda cero" eran <b>locales que aún no abrían</b>, y el modelo con mejor métrica deja quiebre de stock en <b>41%</b> de los días-local.</p>
<code>demand-forecasting</code> <code>lightgbm</code> <code>quantile-regression</code>
</td>
<td width="50%" valign="top">
<h3><a href="https://github.com/Rxyxs/chile-fintech-experimentation-lab">Laboratorio de experimentación A/B</a></h3>
<sub>Monte Carlo</sub>
<p>Revisar un test A/B todos los días infla el falso positivo de 5% a <b>24,2%</b>, y la regla bayesiana que se suele asumir "segura" casi no ayuda (<b>20,5%</b>).</p>
<code>ab-testing</code> <code>cuped</code> <code>sequential-testing</code>
</td>
</tr>
</table>

## Experiencia

**[Rendimiento de combustible de una flota de buses](https://github.com/Rxyxs/Trabajo-Vule)** · <sub>trabajo real, datos de ejemplo ficticios</sub>  
Cada terminal registraba sus cargas de combustible en su propio Excel. La herramienta los une, calcula los km por litro de cada bus contra su lectura anterior (aunque haya cargado en otro terminal) y marca las cargas fuera del rango de su modelo y norma, en un reporte con fórmulas vivas. Al revisarla corregí un bug que calculaba mal los km cuando las cargas cruzaban un cambio de mes.  
`pandas` `openpyxl` `excel` `data-cleaning`

## Proyectos por tipo de problema

34 proyectos en 9 tipos de problema. Cada uno indica si usa datos reales o simulados; haz clic en una categoría para abrirla.

<details>
<summary><b>1. Pronosticar lo que viene</b> · 6 proyectos</summary>

| Proyecto | Qué resuelve y qué encontró | Stack |
|---|---|---|
| **[Demanda retail (Favorita)](https://github.com/Rxyxs/retail-demand-forecasting-favorita)**<br><sub>datos reales · [página](https://rxyxs.github.io/retail-demand-forecasting-favorita/)</sub> | Pronóstico evaluado como decisión de compra: los cuantiles solo convienen sobre una razón de costos ~3:1. | `lightgbm` `quantile-regression` `newsvendor` |
| **[Morosidad bancaria en Chile (CMF)](https://github.com/Rxyxs/chile-banking-delinquency-cmf)**<br><sub>datos reales · [página](https://rxyxs.github.io/chile-banking-delinquency-cmf/)</sub> | Panel desde 128 Excel de la CMF. Solo ARIMA a 3 meses le gana al ingenuo; sumar desempleo, TPM e IMACEC lo empeora. | `time-series` `forecasting` `credit-risk` |
| **[Sistema Eléctrico Nacional, horario](https://github.com/Rxyxs/chile-energy-grid-forecasting)**<br><sub>simulado</sub> | Solar, eólica, demanda y costo marginal en 5 barras. Solar: WAPE 3,64% vs 26,95% del ingenuo; en eólica gana el ingenuo. | `lightgbm` `optuna` `time-series` |
| **[Sistema Eléctrico Nacional, en R](https://github.com/Rxyxs/chile-energy-grid-forecasting-r)**<br><sub>simulado</sub> | TBATS: MAPE 2,47% vs 6,54% del ingenuo estacional; la ventaja de ETS solo aparece con validación rolling. | `r` `arima` `garch` |
| **[Volatilidad del cobre](https://github.com/Rxyxs/copper-volatility-forecaster)**<br><sub>simulado</sub> | CatBoost+Optuna contra GARCH(1,1) y HAR-RV: gana GARCH, y se explica por qué. | `garch` `catboost` `shap` |
| **[Volatilidad de alta frecuencia](https://github.com/Rxyxs/reading-market-turbulence)**<br><sub>datos reales</sub> | 24,8 M de trades de Binance: a 30 s, la persistencia (RMSPE 4,58) le gana a LightGBM y a la red neuronal. | `high-frequency-trading` `lightgbm` `duckdb` |

</details>

<details>
<summary><b>2. Detectar fraude y anomalías</b> · 6 proyectos</summary>

| Proyecto | Qué resuelve y qué encontró | Stack |
|---|---|---|
| **[Laboratorio de fraude y AML](https://github.com/Rxyxs/fraud-detection-techniques-lab)**<br><sub>real + simulado</sub> | El ROC-AUC hace parecer casi igual (0,931 vs 0,965) un modelo con PR-AUC 3,4× peor; AML por grafos sin etiquetas: ROC-AUC 0,893. | `fraud-detection` `aml` `xgboost` |
| **[16 detectores sobre fraude móvil](https://github.com/Rxyxs/Proyectos_ML_anomalias)**<br><sub>simulado</sub> | El baseline estadístico queda bajo el azar (ROC-AUC 0,383) y los ensambles no ganan. 266 tests. | `isolation-forest` `local-outlier-factor` `imbalanced-data` |
| **[Facturas anómalas en compras mineras](https://github.com/Rxyxs/mining-procurement-anomaly-engine)**<br><sub>simulado</sub> | Revisando solo el 5% de las facturas, el autoencoder encuentra el 37,3% de las anómalas: ~7,5× el azar. | `autoencoder` `pytorch` `unsupervised-learning` |
| **[Motor de fraude políglota](https://github.com/Rxyxs/chile-polyglot-fraud-engine)**<br><sub>simulado</sub> | C + Ruby + Python, cada capa perfilada: 31 ns por llamada en C; 4,68 ms p50 la solicitud completa. | `c` `ruby` `prometheus` |
| **[Anomalías en ticks de mercado (C++)](https://github.com/Rxyxs/market-tick-anomaly-engine-cpp)**<br><sub>datos reales</sub> | EWMA y CUSUM validados contra el crash cripto de marzo 2020, a 7,26 M ticks/s. | `cpp` `cusum` `ewma` |
| **[Order flow en acciones de litio (C++)](https://github.com/Rxyxs/lithium-orderbook-imbalance-cpp)**<br><sub>simulado</sub> | Cero falsos positivos fuera del shock inyectado en 43.200 ventanas. | `cpp` `order-flow` `market-microstructure` |

</details>

<details>
<summary><b>3. Anticipar fallas de equipos</b> · 3 proyectos</summary>

| Proyecto | Qué resuelve y qué encontró | Stack |
|---|---|---|
| **[Mantenimiento predictivo (SCANIA)](https://github.com/Rxyxs/heavy-truck-predictive-maintenance)**<br><sub>datos reales · [página](https://rxyxs.github.io/heavy-truck-predictive-maintenance/)</sub> | 23.550 camiones: −31% del costo oficial en test, pero el ahorro se agota si la visita cuesta el doble, porque el modelo exagera el riesgo. | `predictive-maintenance` `survival-analysis` `shap` |
| **[Falla desde señal continua](https://github.com/Rxyxs/failure-prediction-signal-lab)**<br><sub>real + simulado</sub> | Rodamientos (NASA IMS) y señal sísmica (LANL): features espectrales con boosting le ganan 2,7× a una CNN. | `remaining-useful-life` `signal-processing` `fft` |
| **[Gemelo digital de molino SAG](https://github.com/Rxyxs/chile-mining-sag-energy-digital-twin)**<br><sub>simulado</sub> | Kalman estima la dureza del mineral con 79% menos error; energía a 24 h un 27,6% mejor que Holt-Winters. | `digital-twin` `kalman-filter` `lightgbm` |

</details>

<details>
<summary><b>4. Medir causas y evaluar decisiones</b> · 3 proyectos</summary>

| Proyecto | Qué resuelve y qué encontró | Stack |
|---|---|---|
| **[Impacto causal en flota minera](https://github.com/Rxyxs/chile-mining-fleet-causal-impact)**<br><sub>real + simulado · [página](https://rxyxs.github.io/chile-mining-fleet-causal-impact/)</sub> | Uplift y DiD escalonado; el ATT coincide con una implementación de referencia en un panel real. | `causal-inference` `econml` `uplift-modeling` |
| **[Experimentación A/B](https://github.com/Rxyxs/chile-fintech-experimentation-lab)**<br><sub>Monte Carlo</sub> | Tamaño muestral, SRM, CUPED y comparaciones múltiples, con un arnés que verifica el error de cada regla. | `ab-testing` `cuped` `power-analysis` |
| **[Fondos de pensiones](https://github.com/Rxyxs/chile-pension-fund-switching-cost)**<br><sub>datos reales · [página](https://rxyxs.github.io/chile-pension-fund-switching-cost/)</sub> | Una señal de régimen que "ganaba" 1,4–2,3% al año pierde 0,2% fuera de muestra. En UF, 2021–23 cayó 26%. | `duckdb` `counterfactual-analysis` `pensions` |

</details>

<details>
<summary><b>5. Optimizar operaciones</b> · 3 proyectos</summary>

| Proyecto | Qué resuelve y qué encontró | Stack |
|---|---|---|
| **[Flotación de cobre](https://github.com/Rxyxs/optimizacion-geometalurgica-flotacion-cobre)**<br><sub>simulado</sub> | Reactivos y pH por bloque: +27,6 pp de recuperación en los 150 peores bloques, con dos optimizadores que coinciden. | `genetic-algorithm` `nsga-ii` `shap` |
| **[Logística de última milla](https://github.com/Rxyxs/chile-spatial-logistics-opt)**<br><sub>comunas reales, demanda simulada</sub> | Ruteo multi-depósito con ventanas horarias sobre polígonos reales: 0 de 173 zonas sin atender. | `or-tools` `vrptw` `h3` |
| **[Churn como decisión de negocio](https://github.com/Rxyxs/customer-churn-mlops-platform)**<br><sub>simulado</sub> | Umbral por valor de cliente: +US$75.847 contactando al 78,6%, vs +US$42.717 contactando a todos. | `mlflow` `fastapi` `docker` |

</details>

<details>
<summary><b>6. Medir y gestionar riesgo financiero</b> · 4 proyectos</summary>

| Proyecto | Qué resuelve y qué encontró | Stack |
|---|---|---|
| **[Laboratorio de riesgo crediticio](https://github.com/Rxyxs/credit-risk-scoring-lab)**<br><sub>macro real, cartera simulada</sub> | 26 técnicas: scorecard R+Python+C a 270,6 M filas/s, PD para IFRS 9, auditoría de sesgo y ciclo shadow/canary/reentrenamiento. | `scorecard` `ifrs9` `mlops` |
| **[Riesgo sistémico en Chile](https://github.com/Rxyxs/chile-fintech-systemic-risk)**<br><sub>datos reales</sub> | Seis lenguajes sobre datos del Banco Central. El LSTM (51,0%) no le gana a la clase mayoritaria (53,6%). | `julia` `r` `cplusplus` |
| **[Laboratorio cuantitativo cripto](https://github.com/Rxyxs/crypto-quant-techniques-lab)**<br><sub>datos reales</sub> | Ocho técnicas. Las cinco estrategias pierden tras costos; la detección de spoofing sí funciona (precisión 0,92). | `quantitative-finance` `cointegration` `nlp` |
| **[Opciones asiáticas sobre cobre (C++)](https://github.com/Rxyxs/copper-options-montecarlo-cpp)**<br><sub>modelo de precios</sub> | Monte Carlo C++20 bajo GBM, Schwartz y Heston: 9,64× con 16 hilos y un sesgo real corregido. | `cpp20` `monte-carlo` `heston-model` |

</details>

<details>
<summary><b>7. Ordenar y preparar los datos</b> · 3 proyectos</summary>

| Proyecto | Qué resuelve y qué encontró | Stack |
|---|---|---|
| **[Toolkit de limpieza en 4 dominios](https://github.com/Rxyxs/Limpieza_Datos)**<br><sub>datos reales</sub> | El mismo toolkit sobre Banco Central, COCHILCO y Banco Mundial; detectó un dato corrupto en la fuente. | `data-quality` `pydantic` `pytest` |
| **[Data warehouse minero](https://github.com/Rxyxs/data-warehouse-analitico-mineria-chile)**<br><sub>simulado</sub> | dbt + DuckDB de staging a marts, 83 tests de calidad y vistas listas para modelar. | `dbt` `duckdb` `star-schema` |
| **[Lakehouse de e-commerce](https://github.com/Rxyxs/ecommerce-lakehouse-duckdb)**<br><sub>simulado</sub> | Polars + DuckDB sobre Parquet; repetir el benchmark 7 veces cambió la conclusión. | `polars` `duckdb` `parquet` |

</details>

<details>
<summary><b>8. Clasificar y estimar</b> · 2 proyectos</summary>

| Proyecto | Qué resuelve y qué encontró | Stack |
|---|---|---|
| **[Clasificación científica](https://github.com/Rxyxs/scientific-classification-lab)**<br><sub>datos reales</sub> | Bosón de Higgs (AMS 3,64 vs 3,8–3,9 de los ganadores) y exoplanetas Kepler (79,3% vs 49,8%). | `gradient-boosting` `pytorch` `astronomy` |
| **[Ley y fragmentación (.NET)](https://github.com/Rxyxs/chile-mining-grade-blast-quality-dotnet)**<br><sub>simulado</sub> | ML.NET + ONNX en app de escritorio: P80 con R² 0,957. | `csharp` `ml-net` `onnx` |

</details>

<details>
<summary><b>9. Texto, lenguaje e imágenes</b> · 4 proyectos</summary>

| Proyecto | Qué resuelve y qué encontró | Stack |
|---|---|---|
| **[RAG de seguridad minera](https://github.com/Rxyxs/rag-seguridad-minera-chile)**<br><sub>normativa real</sub> | Búsqueda híbrida sobre el DS 132; el re-ranking sube el MRR de 0,920 a 0,981. | `rag` `hybrid-search` `cross-encoder` |
| **[Agente de operaciones mineras](https://github.com/Rxyxs/chile-mining-ops-agent)**<br><sub>simulado</sub> | Un LLM que responde llamando herramientas (SQL, scoring, anomalías) en vez de inventar números. | `llm-agent` `tool-calling` `duckdb` |
| **[Modelo de lenguaje local para industria](https://github.com/Rxyxs/slm-industrial-gateway)**<br><sub>simulado</sub> | Inferencia sin internet, guardrails y QLoRA; el modelo base inventa argumentos en 94 de 100 prompts. | `llama-cpp` `qlora` `guardrails` |
| **[YOLOv8 en Raspberry Pi (tesis)](https://github.com/Rxyxs/yolov8-separable-convolutions)**<br><sub>datos reales (COCO)</sub> | 68% menos parámetros y ~10× más rápido en Raspberry Pi, a cambio de mAP50 0,175 vs 0,212. | `yolov8` `computer-vision` `edge-computing` |

</details>

## Herramientas

<table>
<tr><td><b>Lenguajes</b></td><td><img src="https://img.shields.io/badge/Python-0D1117?style=flat-square&logo=python&logoColor=00FF66" alt="Python"> <img src="https://img.shields.io/badge/SQL-0D1117?style=flat-square&logo=postgresql&logoColor=00FF66" alt="SQL"> <img src="https://img.shields.io/badge/R-0D1117?style=flat-square&logo=r&logoColor=00FF66" alt="R"> <img src="https://img.shields.io/badge/C%2B%2B-0D1117?style=flat-square&logo=cplusplus&logoColor=00FF66" alt="C++"> <img src="https://img.shields.io/badge/C-0D1117?style=flat-square&logo=c&logoColor=00FF66" alt="C"> <img src="https://img.shields.io/badge/C%23-0D1117?style=flat-square&logo=dotnet&logoColor=00FF66" alt="C#"> <img src="https://img.shields.io/badge/Julia-0D1117?style=flat-square&logo=julia&logoColor=00FF66" alt="Julia"> <img src="https://img.shields.io/badge/Go-0D1117?style=flat-square&logo=go&logoColor=00FF66" alt="Go"> <img src="https://img.shields.io/badge/Ruby-0D1117?style=flat-square&logo=ruby&logoColor=00FF66" alt="Ruby"></td></tr>
<tr><td><b>Datos</b></td><td><img src="https://img.shields.io/badge/pandas-0D1117?style=flat-square&logo=pandas&logoColor=00FF66" alt="pandas"> <img src="https://img.shields.io/badge/Polars-0D1117?style=flat-square&logo=polars&logoColor=00FF66" alt="Polars"> <img src="https://img.shields.io/badge/NumPy-0D1117?style=flat-square&logo=numpy&logoColor=00FF66" alt="NumPy"> <img src="https://img.shields.io/badge/DuckDB-0D1117?style=flat-square&logo=duckdb&logoColor=00FF66" alt="DuckDB"> <img src="https://img.shields.io/badge/dbt-0D1117?style=flat-square" alt="dbt"> <img src="https://img.shields.io/badge/Parquet-0D1117?style=flat-square&logo=apacheparquet&logoColor=00FF66" alt="Parquet"> <img src="https://img.shields.io/badge/Pydantic-0D1117?style=flat-square&logo=pydantic&logoColor=00FF66" alt="Pydantic"> <img src="https://img.shields.io/badge/Jupyter-0D1117?style=flat-square&logo=jupyter&logoColor=00FF66" alt="Jupyter"></td></tr>
<tr><td><b>ML y estadística</b></td><td><img src="https://img.shields.io/badge/scikit--learn-0D1117?style=flat-square&logo=scikitlearn&logoColor=00FF66" alt="scikit-learn"> <img src="https://img.shields.io/badge/LightGBM-0D1117?style=flat-square" alt="LightGBM"> <img src="https://img.shields.io/badge/XGBoost-0D1117?style=flat-square" alt="XGBoost"> <img src="https://img.shields.io/badge/CatBoost-0D1117?style=flat-square" alt="CatBoost"> <img src="https://img.shields.io/badge/PyTorch-0D1117?style=flat-square&logo=pytorch&logoColor=00FF66" alt="PyTorch"> <img src="https://img.shields.io/badge/SciPy-0D1117?style=flat-square&logo=scipy&logoColor=00FF66" alt="SciPy"> <img src="https://img.shields.io/badge/Optuna-0D1117?style=flat-square&logo=optuna&logoColor=00FF66" alt="Optuna"> <img src="https://img.shields.io/badge/Plotly-0D1117?style=flat-square&logo=plotly&logoColor=00FF66" alt="Plotly"></td></tr>
<tr><td><b>Lenguaje, visión y edge</b></td><td><img src="https://img.shields.io/badge/LangChain-0D1117?style=flat-square&logo=langchain&logoColor=00FF66" alt="LangChain"> <img src="https://img.shields.io/badge/Hugging%20Face-0D1117?style=flat-square&logo=huggingface&logoColor=00FF66" alt="Hugging Face"> <img src="https://img.shields.io/badge/Ultralytics%20YOLO-0D1117?style=flat-square&logo=ultralytics&logoColor=00FF66" alt="Ultralytics YOLO"> <img src="https://img.shields.io/badge/ONNX-0D1117?style=flat-square&logo=onnx&logoColor=00FF66" alt="ONNX"> <img src="https://img.shields.io/badge/Raspberry%20Pi-0D1117?style=flat-square&logo=raspberrypi&logoColor=00FF66" alt="Raspberry Pi"></td></tr>
<tr><td><b>Producción</b></td><td><img src="https://img.shields.io/badge/FastAPI-0D1117?style=flat-square&logo=fastapi&logoColor=00FF66" alt="FastAPI"> <img src="https://img.shields.io/badge/Streamlit-0D1117?style=flat-square&logo=streamlit&logoColor=00FF66" alt="Streamlit"> <img src="https://img.shields.io/badge/MLflow-0D1117?style=flat-square&logo=mlflow&logoColor=00FF66" alt="MLflow"> <img src="https://img.shields.io/badge/Docker-0D1117?style=flat-square&logo=docker&logoColor=00FF66" alt="Docker"> <img src="https://img.shields.io/badge/GitHub%20Actions-0D1117?style=flat-square&logo=githubactions&logoColor=00FF66" alt="GitHub Actions"> <img src="https://img.shields.io/badge/pytest-0D1117?style=flat-square&logo=pytest&logoColor=00FF66" alt="pytest"> <img src="https://img.shields.io/badge/Prometheus-0D1117?style=flat-square&logo=prometheus&logoColor=00FF66" alt="Prometheus"> <img src="https://img.shields.io/badge/Grafana-0D1117?style=flat-square&logo=grafana&logoColor=00FF66" alt="Grafana"> <img src="https://img.shields.io/badge/Git-0D1117?style=flat-square&logo=git&logoColor=00FF66" alt="Git"> <img src="https://img.shields.io/badge/Linux-0D1117?style=flat-square&logo=linux&logoColor=00FF66" alt="Linux"></td></tr>
</table>

---

<div align="center">
<sub><a href="https://www.linkedin.com/in/pablo-reyes-pino">LinkedIn</a> · preyesp09@gmail.com · Santiago, Chile</sub>
</div>
