![Portada](assets/banner.png)

<p align="center">
<a href="https://www.linkedin.com/in/pablo-reyes-pino"><img src="https://img.shields.io/badge/LinkedIn-0D1117?style=for-the-badge&logo=linkedin&logoColor=00FF66" alt="LinkedIn"></a>
<a href="mailto:preyesp09@gmail.com"><img src="https://img.shields.io/badge/Email-0D1117?style=for-the-badge&logo=gmail&logoColor=00FF66" alt="Email"></a>
<img src="https://img.shields.io/badge/Santiago%2C%20Chile-0D1117?style=for-the-badge&logo=googlemaps&logoColor=00FF66" alt="Ubicación: Santiago, Chile">
</p>

<p align="center">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&pause=1000&color=00FF66&center=true&vCenter=true&width=520&lines=Pronosticar;Detectar+anomal%C3%ADas;Medir+causas;Optimizar+decisiones;Forecast;Detect+anomalies;Measure+causes;Optimize+decisions">
</p>

<div align="center">

[ Versión en Español ](#-español) &nbsp;|&nbsp; [ English Version ](#-english)

</div>

---

<a name="-español"></a>
# ¡Hola! Soy Pablo Reyes
### Científico de Datos · Universidad Mayor · Santiago, Chile

Soy Científico de Datos titulado de la Universidad Mayor. Este perfil reúne trabajo y proyectos propios, y está ordenado a propósito **por el tipo de problema que resuelve cada uno**, no por herramienta: pronosticar, detectar lo anómalo, anticipar fallas, medir qué causó qué, decidir mejor, gestionar riesgo, ordenar los datos y trabajar con texto e imágenes. La idea es mostrar la amplitud de formas en que un científico de datos puede ayudar a una organización — en minería, energía, finanzas, retail o pensiones.

En todos sigo las mismas reglas: el código corre de principio a fin, las cifras salen de esa corrida, casi todos los repos tienen tests y CI, y los resultados negativos se publican igual que los positivos. Cada proyecto indica si usa **datos reales** o **simulados**.

## Para empezar

**[Cambiarse de fondo de pensiones en pánico](https://github.com/Rxyxs/chile-pension-fund-switching-cost)** · *datos reales* — 24 años de valores cuota diarios de la Superintendencia de Pensiones. Cambiarse al fondo E justo en el piso de una caída pierde plata en **97%** de 2.000 historias simuladas; pero el piso solo se conoce después. Con una regla que alguien podría seguir de verdad (salir al cruzar −15%), pierde en **59%**: casi una moneda al aire. [Página](https://rxyxs.github.io/chile-pension-fund-switching-cost/).

**[Impacto causal en una flota minera](https://github.com/Rxyxs/chile-mining-fleet-causal-impact)** · *simulado + real* — ¿funcionó el programa de mantenimiento, y en qué camiones? Cinco estimadores validados contra un efecto verdadero conocido. Con sensores reales de 60.000 camiones Scania, **el DRLearner por defecto colapsa (r = −0,01)**; se aisló la causa y una etapa final Ridge lo recupera a 0,61–0,79. [Página](https://rxyxs.github.io/chile-mining-fleet-causal-impact/).

**[Forecasting de demanda como decisión de inventario](https://github.com/Rxyxs/retail-demand-forecasting-favorita)** · *datos reales* — 3.000.888 filas de ventas de supermercado. Un cuarto de la "demanda cero" eran **locales que aún no abrían**, y el modelo con mejor métrica deja quiebre de stock en **41%** de los días-local. [Página](https://rxyxs.github.io/retail-demand-forecasting-favorita/).

**[Laboratorio de experimentación A/B](https://github.com/Rxyxs/chile-fintech-experimentation-lab)** · *simulación Monte Carlo* — revisar un test A/B todos los días infla el falso positivo de 5% a **24,2%**, y la regla bayesiana que se suele asumir "segura" casi no ayuda (**20,5%**).

## Experiencia

* **[Rendimiento de combustible de una flota de buses](https://github.com/Rxyxs/Trabajo-Vule)** · *trabajo para una empresa de buses* — cada terminal registraba sus cargas de combustible en su propio Excel. La herramienta los une, calcula los km por litro de cada bus contra su lectura anterior (aunque haya cargado en otro terminal) y marca las cargas fuera del rango de su modelo y norma, en un reporte con fórmulas vivas. Al revisarla encontré y corregí un bug: ordenaba las fechas como texto y calculaba mal los km cuando las cargas cruzaban un cambio de mes.<br>`pandas` `openpyxl` `excel` `data-cleaning`

## Proyectos por tipo de problema

### 1. Pronosticar lo que viene

* **[Demanda retail (Favorita)](https://github.com/Rxyxs/retail-demand-forecasting-favorita)** · *real* — pronóstico evaluado como decisión de compra, no solo como métrica: el enfoque por cuantiles solo conviene sobre una razón de costos ~3:1.<br>`demand-forecasting` `lightgbm` `quantile-regression` `newsvendor`
* **[Morosidad bancaria en Chile (CMF)](https://github.com/Rxyxs/chile-banking-delinquency-cmf)** · *real* — panel armado desde 128 Excel de la CMF en tres formatos (2016–2026). Solo ARIMA a 3 meses le gana al pronóstico ingenuo, y agregar desempleo, TPM e IMACEC lo empeora. [Página](https://rxyxs.github.io/chile-banking-delinquency-cmf/).<br>`time-series` `forecasting` `credit-risk` `data-engineering`
* **[Sistema Eléctrico Nacional, horario](https://github.com/Rxyxs/chile-energy-grid-forecasting)** · *simulado* — solar, eólica, demanda y costo marginal en 5 barras con LightGBM. Solar: WAPE 3,64% contra 26,95% del ingenuo; en eólica el ingenuo gana, y se explica por qué.<br>`lightgbm` `optuna` `time-series` `streamlit`
* **[Sistema Eléctrico Nacional, en R](https://github.com/Rxyxs/chile-energy-grid-forecasting-r)** · *simulado* — ARIMA, SARIMAX, TBATS, ETS y GARCH. TBATS: MAPE 2,47% contra 6,54% del ingenuo estacional; la ventaja de ETS solo aparece con validación cruzada rolling.<br>`r` `arima` `garch` `tidyverts`
* **[Volatilidad del cobre](https://github.com/Rxyxs/copper-volatility-forecaster)** · *simulado* — CatBoost+Optuna contra GARCH(1,1) y HAR-RV: **gana GARCH**, y se explica la razón estructural.<br>`garch` `catboost` `optuna` `shap`
* **[Volatilidad de alta frecuencia](https://github.com/Rxyxs/reading-market-turbulence)** · *real* — 24,8 millones de trades de Binance. A 30 segundos, la persistencia (RMSPE 4,58) le gana a LightGBM y a la red neuronal.<br>`high-frequency-trading` `lightgbm` `duckdb` `fastapi`

### 2. Detectar fraude y anomalías

* **[Laboratorio de fraude y AML](https://github.com/Rxyxs/fraud-detection-techniques-lab)** · *real + simulado* — cuatro técnicas. Sobre 284.807 transacciones reales, el ROC-AUC hace parecer casi igual (0,931 vs 0,965) un modelo cuyo PR-AUC es 3,4 veces peor; y AML por grafos **sin etiquetas** llega a ROC-AUC 0,893.<br>`fraud-detection` `aml` `xgboost` `anomaly-detection`
* **[16 detectores sobre fraude móvil (PaySim)](https://github.com/Rxyxs/Proyectos_ML_anomalias)** · *simulado* — el baseline estadístico simple queda **bajo el azar** (ROC-AUC 0,383) y los ensambles no ganan. 266 tests.<br>`isolation-forest` `local-outlier-factor` `imbalanced-data` `paysim`
* **[Facturas anómalas en compras mineras](https://github.com/Rxyxs/mining-procurement-anomaly-engine)** · *simulado* — autoencoder en PyTorch: revisando solo el 5% de las facturas encuentra el 37,3% de las anómalas, ~7,5 veces el azar.<br>`autoencoder` `pytorch` `unsupervised-learning` `procurement`
* **[Motor de fraude políglota](https://github.com/Rxyxs/chile-polyglot-fraud-engine)** · *simulado* — C + Ruby + Python con cada capa perfilada: el módulo C toma 31 ns por llamada; la solicitud completa, 4,68 ms p50.<br>`c` `ruby` `shared-memory-ipc` `prometheus`
* **[Anomalías en ticks de mercado (C++)](https://github.com/Rxyxs/market-tick-anomaly-engine-cpp)** · *real* — EWMA y CUSUM validados contra el crash cripto de marzo 2020, a 7,26 millones de ticks por segundo.<br>`cpp` `cusum` `ewma` `real-market-data`
* **[Desbalance de order flow en litio (C++)](https://github.com/Rxyxs/lithium-orderbook-imbalance-cpp)** · *simulado* — cero falsos positivos fuera del shock inyectado en 43.200 ventanas.<br>`cpp` `order-flow` `market-microstructure` `zero-dependencies`

### 3. Anticipar fallas de equipos

* **[Mantenimiento predictivo en camiones (SCANIA)](https://github.com/Rxyxs/heavy-truck-predictive-maintenance)** · *real* — 23.550 camiones. La regla de costo esperado baja el costo oficial del reto 31% en test, pero el ahorro se agota si la visita a taller cuesta el doble, porque el modelo exagera el riesgo. [Página](https://rxyxs.github.io/heavy-truck-predictive-maintenance/).<br>`predictive-maintenance` `survival-analysis` `cost-sensitive-learning` `shap`
* **[Falla desde señal continua](https://github.com/Rxyxs/failure-prediction-signal-lab)** · *real + simulado* — vibración de rodamientos (NASA IMS) y señal sísmica (LANL): en LANL, features espectrales con boosting le ganan 2,7 veces a una CNN sobre la señal cruda.<br>`remaining-useful-life` `signal-processing` `fft` `pytorch`
* **[Gemelo digital de molino SAG](https://github.com/Rxyxs/chile-mining-sag-energy-digital-twin)** · *simulado* — filtro de Kalman para estimar la dureza del mineral (79% menos error que el sensor) y pronóstico de energía a 24 h un 27,6% mejor que Holt-Winters.<br>`digital-twin` `kalman-filter` `sensor-fusion` `lightgbm`

### 4. Medir causas y evaluar decisiones

* **[Impacto causal en flota minera](https://github.com/Rxyxs/chile-mining-fleet-causal-impact)** · *simulado + real* — uplift y diferencias-en-diferencias escalonado; el ATT coincide con una implementación de referencia independiente en un panel real.<br>`causal-inference` `econml` `uplift-modeling` `difference-in-differences`
* **[Experimentación A/B](https://github.com/Rxyxs/chile-fintech-experimentation-lab)** · *Monte Carlo* — tamaño muestral, SRM, CUPED y corrección por comparaciones múltiples, con un arnés que comprueba si cada regla controla el error que promete.<br>`ab-testing` `cuped` `power-analysis` `sequential-testing`
* **[Fondos de pensiones](https://github.com/Rxyxs/chile-pension-fund-switching-cost)** · *real* — una señal de régimen que "ganaba" 1,4–2,3% al año pierde 0,2% al año fuera de muestra. En UF, 2021–23 fue una caída de 26%, no de 14,6%.<br>`duckdb` `counterfactual-analysis` `behavioral-finance` `pensions`

### 5. Optimizar operaciones

* **[Flotación de cobre](https://github.com/Rxyxs/optimizacion-geometalurgica-flotacion-cobre)** · *simulado* — recomienda reactivos y pH por bloque: +27,6 puntos de recuperación en los 150 peores bloques dentro del presupuesto, con dos optimizadores que coinciden entre sí.<br>`genetic-algorithm` `nsga-ii` `multi-objective-optimization` `shap`
* **[Logística de última milla](https://github.com/Rxyxs/chile-spatial-logistics-opt)** · *simulado sobre comunas reales* — ruteo multi-depósito con ventanas horarias (OR-Tools) sobre polígonos reales de comunas: 0 de 173 zonas sin atender.<br>`or-tools` `vrptw` `h3` `geopandas`
* **[Churn con decisión de negocio](https://github.com/Rxyxs/customer-churn-mlops-platform)** · *simulado* — el umbral se elige por valor de cliente: +US$75.847 contactando al 78,6%, contra +US$42.717 contactando a todos.<br>`mlflow` `mlops` `fastapi` `docker`

### 6. Medir y gestionar riesgo financiero

* **[Laboratorio de riesgo crediticio](https://github.com/Rxyxs/credit-risk-scoring-lab)** · *macro real, cartera simulada* — 26 técnicas: scorecard R+Python+C (270,6 millones de filas por segundo), PD de vida completa para IFRS 9, auditoría de sesgo y el ciclo completo de un modelo en producción (shadow, canary, reentrenamiento).<br>`scorecard` `ifrs9` `r` `mlops`
* **[Riesgo sistémico en Chile](https://github.com/Rxyxs/chile-fintech-systemic-risk)** · *real* — seis lenguajes sobre datos del Banco Central. El LSTM (51,0%) no le gana a la clase mayoritaria (53,6%); la volatilidad, en cambio, es muy persistente.<br>`julia` `r` `cplusplus` `systemic-risk`
* **[Laboratorio cuantitativo cripto](https://github.com/Rxyxs/crypto-quant-techniques-lab)** · *real* — ocho técnicas. Las cinco estrategias pierden plata después de costos y la regla más simple le gana a LightGBM; la detección de spoofing es el resultado claramente positivo (precisión 0,92).<br>`quantitative-finance` `cointegration` `portfolio-optimization` `nlp`
* **[Opciones asiáticas sobre cobre (C++)](https://github.com/Rxyxs/copper-options-montecarlo-cpp)** · *modelo* — Monte Carlo en C++20 bajo GBM, Schwartz y Heston: 9,64× con 16 hilos y un sesgo real de la variable de control encontrado y corregido.<br>`cpp20` `monte-carlo` `heston-model` `variance-reduction`

### 7. Ordenar y preparar los datos

* **[Toolkit de limpieza en 4 dominios](https://github.com/Rxyxs/Limpieza_Datos)** · *real* — el mismo toolkit sobre Banco Central, COCHILCO y Banco Mundial; detectó un dato corrupto en la fuente. 223 tests.<br>`data-quality` `pydantic` `schema-validation` `pytest`
* **[Data warehouse minero](https://github.com/Rxyxs/data-warehouse-analitico-mineria-chile)** · *simulado* — dbt + DuckDB, de staging a marts, con 83 tests de calidad y vistas listas para modelar.<br>`dbt` `duckdb` `star-schema` `analytics-engineering`
* **[Lakehouse de e-commerce](https://github.com/Rxyxs/ecommerce-lakehouse-duckdb)** · *simulado* — Polars + DuckDB sobre Parquet particionado; repetir el benchmark 7 veces cambió la conclusión.<br>`polars` `duckdb` `parquet` `lakehouse`

### 8. Clasificar y estimar

* **[Clasificación científica](https://github.com/Rxyxs/scientific-classification-lab)** · *real* — bosón de Higgs (AMS 3,64 contra 3,8–3,9 de los ganadores de Kaggle) y exoplanetas Kepler (79,3% contra 49,8% del baseline).<br>`gradient-boosting` `pytorch` `particle-physics` `astronomy`
* **[Ley de mineral y fragmentación (.NET)](https://github.com/Rxyxs/chile-mining-grade-blast-quality-dotnet)** · *simulado* — ML.NET + ONNX en app de escritorio: P80 con R² 0,957.<br>`csharp` `ml-net` `onnx` `wpf`

### 9. Texto, lenguaje e imágenes

* **[RAG de seguridad minera](https://github.com/Rxyxs/rag-seguridad-minera-chile)** · *normativa real* — búsqueda híbrida sobre el DS 132; el re-ranking sube el MRR de 0,920 a 0,981.<br>`rag` `hybrid-search` `cross-encoder` `bm25`
* **[Agente de operaciones mineras](https://github.com/Rxyxs/chile-mining-ops-agent)** · *simulado* — un LLM que responde llamando herramientas (SQL, scoring, anomalías) en vez de inventar números.<br>`llm-agent` `tool-calling` `duckdb`
* **[Modelo de lenguaje local para industria](https://github.com/Rxyxs/slm-industrial-gateway)** · *simulado* — inferencia sin internet, guardrails y fine-tuning QLoRA; la evaluación muestra que el modelo base inventa nombres de argumentos en 94 de 100 prompts — justo lo que el fine-tuning viene a corregir.<br>`llama-cpp` `qlora` `guardrails` `local-inference`
* **[YOLOv8 en Raspberry Pi — tesis de título](https://github.com/Rxyxs/yolov8-separable-convolutions)** · *real (COCO)* — convoluciones separables: 68% menos parámetros y ~10× más rápido en Raspberry Pi, a cambio de mAP50 0,175 contra 0,212.<br>`yolov8` `computer-vision` `edge-computing` `raspberry-pi`

## Herramientas

**Lenguajes**

![Python](https://img.shields.io/badge/Python-0D1117?style=flat-square&logo=python&logoColor=00FF66)
![SQL](https://img.shields.io/badge/SQL-0D1117?style=flat-square&logo=postgresql&logoColor=00FF66)
![R](https://img.shields.io/badge/R-0D1117?style=flat-square&logo=r&logoColor=00FF66)
![C++](https://img.shields.io/badge/C%2B%2B-0D1117?style=flat-square&logo=cplusplus&logoColor=00FF66)
![C](https://img.shields.io/badge/C-0D1117?style=flat-square&logo=c&logoColor=00FF66)
![C#](https://img.shields.io/badge/C%23-0D1117?style=flat-square&logo=dotnet&logoColor=00FF66)
![Julia](https://img.shields.io/badge/Julia-0D1117?style=flat-square&logo=julia&logoColor=00FF66)
![Go](https://img.shields.io/badge/Go-0D1117?style=flat-square&logo=go&logoColor=00FF66)
![Ruby](https://img.shields.io/badge/Ruby-0D1117?style=flat-square&logo=ruby&logoColor=00FF66)

**Datos**

![pandas](https://img.shields.io/badge/pandas-0D1117?style=flat-square&logo=pandas&logoColor=00FF66)
![Polars](https://img.shields.io/badge/Polars-0D1117?style=flat-square&logo=polars&logoColor=00FF66)
![NumPy](https://img.shields.io/badge/NumPy-0D1117?style=flat-square&logo=numpy&logoColor=00FF66)
![DuckDB](https://img.shields.io/badge/DuckDB-0D1117?style=flat-square&logo=duckdb&logoColor=00FF66)
![dbt](https://img.shields.io/badge/dbt-0D1117?style=flat-square)
![Apache Parquet](https://img.shields.io/badge/Apache%20Parquet-0D1117?style=flat-square&logo=apacheparquet&logoColor=00FF66)
![Pydantic](https://img.shields.io/badge/Pydantic-0D1117?style=flat-square&logo=pydantic&logoColor=00FF66)
![Jupyter](https://img.shields.io/badge/Jupyter-0D1117?style=flat-square&logo=jupyter&logoColor=00FF66)

**Machine learning y estadística**

![scikit-learn](https://img.shields.io/badge/scikit--learn-0D1117?style=flat-square&logo=scikitlearn&logoColor=00FF66)
![LightGBM](https://img.shields.io/badge/LightGBM-0D1117?style=flat-square)
![XGBoost](https://img.shields.io/badge/XGBoost-0D1117?style=flat-square)
![CatBoost](https://img.shields.io/badge/CatBoost-0D1117?style=flat-square)
![PyTorch](https://img.shields.io/badge/PyTorch-0D1117?style=flat-square&logo=pytorch&logoColor=00FF66)
![SciPy](https://img.shields.io/badge/SciPy-0D1117?style=flat-square&logo=scipy&logoColor=00FF66)
![Optuna](https://img.shields.io/badge/Optuna-0D1117?style=flat-square&logo=optuna&logoColor=00FF66)
![Plotly](https://img.shields.io/badge/Plotly-0D1117?style=flat-square&logo=plotly&logoColor=00FF66)

**Lenguaje, visión y edge**

![LangChain](https://img.shields.io/badge/LangChain-0D1117?style=flat-square&logo=langchain&logoColor=00FF66)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-0D1117?style=flat-square&logo=huggingface&logoColor=00FF66)
![Ultralytics YOLO](https://img.shields.io/badge/Ultralytics%20YOLO-0D1117?style=flat-square&logo=ultralytics&logoColor=00FF66)
![ONNX](https://img.shields.io/badge/ONNX-0D1117?style=flat-square&logo=onnx&logoColor=00FF66)
![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-0D1117?style=flat-square&logo=raspberrypi&logoColor=00FF66)

**Producción**

![FastAPI](https://img.shields.io/badge/FastAPI-0D1117?style=flat-square&logo=fastapi&logoColor=00FF66)
![Streamlit](https://img.shields.io/badge/Streamlit-0D1117?style=flat-square&logo=streamlit&logoColor=00FF66)
![MLflow](https://img.shields.io/badge/MLflow-0D1117?style=flat-square&logo=mlflow&logoColor=00FF66)
![Docker](https://img.shields.io/badge/Docker-0D1117?style=flat-square&logo=docker&logoColor=00FF66)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-0D1117?style=flat-square&logo=githubactions&logoColor=00FF66)
![pytest](https://img.shields.io/badge/pytest-0D1117?style=flat-square&logo=pytest&logoColor=00FF66)
![Prometheus](https://img.shields.io/badge/Prometheus-0D1117?style=flat-square&logo=prometheus&logoColor=00FF66)
![Grafana](https://img.shields.io/badge/Grafana-0D1117?style=flat-square&logo=grafana&logoColor=00FF66)
![Git](https://img.shields.io/badge/Git-0D1117?style=flat-square&logo=git&logoColor=00FF66)
![Linux](https://img.shields.io/badge/Linux-0D1117?style=flat-square&logo=linux&logoColor=00FF66)

## Contacto

[LinkedIn](https://www.linkedin.com/in/pablo-reyes-pino) · preyesp09@gmail.com · Santiago, Chile

---

<a name="-english"></a>
# Hi, I'm Pablo Reyes
### Data Scientist · Universidad Mayor · Santiago, Chile

I'm a Data Scientist with a degree from Universidad Mayor. This profile collects work and personal projects, and it is organized on purpose **by the kind of problem each one solves**, not by tool: forecasting, catching what's anomalous, anticipating failures, measuring what caused what, making better decisions, managing risk, getting data in order, and working with text and images. The point is to show the range of ways a data scientist can help an organization — in mining, energy, finance, retail or pensions.

The same rules apply throughout: the code runs end to end, the numbers come from that run, nearly every repo has tests and CI, and negative results are published like positive ones. Each project states whether it uses **real** or **simulated** data.

## Start here

**[Panic-switching pension funds](https://github.com/Rxyxs/chile-pension-fund-switching-cost)** · *real data* — 24 years of daily unit values from Chile's pension regulator. Switching to Fund E right at the bottom of a crash loses money in **97%** of 2,000 simulated histories; but the bottom is only known afterwards. With a rule someone could actually follow (exit when the loss crosses −15%), it loses in **59%**: close to a coin flip. [Page](https://rxyxs.github.io/chile-pension-fund-switching-cost/).

**[Causal impact in a mining fleet](https://github.com/Rxyxs/chile-mining-fleet-causal-impact)** · *simulated + real* — did the maintenance program work, and on which trucks? Five estimators validated against a known true effect. On real sensor data from 60,000 Scania trucks, **the default DRLearner collapses (r = −0.01)**; the cause was isolated and a Ridge final stage recovers it to 0.61–0.79. [Page](https://rxyxs.github.io/chile-mining-fleet-causal-impact/).

**[Demand forecasting as an inventory decision](https://github.com/Rxyxs/retail-demand-forecasting-favorita)** · *real data* — 3,000,888 rows of grocery sales. A quarter of the "zero demand" was **stores that had not opened yet**, and the model with the best metric leaves a stockout on **41%** of store-days. [Page](https://rxyxs.github.io/retail-demand-forecasting-favorita/).

**[A/B experimentation lab](https://github.com/Rxyxs/chile-fintech-experimentation-lab)** · *Monte Carlo simulation* — checking an A/B test every day inflates the false-positive rate from 5% to **24.2%**, and the Bayesian rule usually assumed "safe" barely helps (**20.5%**).

## Experience

* **[Fuel efficiency for a bus fleet](https://github.com/Rxyxs/Trabajo-Vule)** · *work for a bus company* — each depot logged its fuel loads in its own Excel file. The tool merges them, computes each bus's km per litre against its previous reading (even if it refuelled at another depot) and flags loads outside the range for its model and emissions standard, in a report with live formulas. While reviewing it I found and fixed a bug: it sorted dates as text and miscomputed km whenever loads crossed a month boundary.<br>`pandas` `openpyxl` `excel` `data-cleaning`

## Projects by kind of problem

### 1. Forecasting what comes next

* **[Retail demand (Favorita)](https://github.com/Rxyxs/retail-demand-forecasting-favorita)** · *real* — the forecast is scored as a purchase decision, not only as a metric: the quantile approach only pays above a ~3:1 cost ratio.<br>`demand-forecasting` `lightgbm` `quantile-regression` `newsvendor`
* **[Chilean bank delinquency (CMF)](https://github.com/Rxyxs/chile-banking-delinquency-cmf)** · *real* — a panel built from 128 CMF Excel files in three layouts (2016–2026). Only ARIMA at 3 months beats the naive forecast, and adding unemployment, policy rate and IMACEC makes it worse. [Page](https://rxyxs.github.io/chile-banking-delinquency-cmf/).<br>`time-series` `forecasting` `credit-risk` `data-engineering`
* **[Chile's power grid, hourly](https://github.com/Rxyxs/chile-energy-grid-forecasting)** · *simulated* — solar, wind, demand and marginal cost at 5 nodes with LightGBM. Solar: 3.64% WAPE against 26.95% for the naive forecast; on wind the naive forecast wins, and the README explains why.<br>`lightgbm` `optuna` `time-series` `streamlit`
* **[Chile's power grid, in R](https://github.com/Rxyxs/chile-energy-grid-forecasting-r)** · *simulated* — ARIMA, SARIMAX, TBATS, ETS and GARCH. TBATS: 2.47% MAPE against 6.54% for seasonal naive; ETS's advantage only shows up under rolling cross-validation.<br>`r` `arima` `garch` `tidyverts`
* **[Copper volatility](https://github.com/Rxyxs/copper-volatility-forecaster)** · *simulated* — CatBoost+Optuna against GARCH(1,1) and HAR-RV: **GARCH wins**, and the structural reason is explained.<br>`garch` `catboost` `optuna` `shap`
* **[High-frequency volatility](https://github.com/Rxyxs/reading-market-turbulence)** · *real* — 24.8 million Binance trades. At 30 seconds, persistence (RMSPE 4.58) beats both LightGBM and the neural network.<br>`high-frequency-trading` `lightgbm` `duckdb` `fastapi`

### 2. Catching fraud and anomalies

* **[Fraud and AML lab](https://github.com/Rxyxs/fraud-detection-techniques-lab)** · *real + simulated* — four techniques. On 284,807 real transactions, ROC-AUC makes a model look almost as good (0.931 vs 0.965) when its PR-AUC is 3.4 times worse; and graph-based AML **with no labels** reaches ROC-AUC 0.893.<br>`fraud-detection` `aml` `xgboost` `anomaly-detection`
* **[16 detectors on mobile-money fraud (PaySim)](https://github.com/Rxyxs/Proyectos_ML_anomalias)** · *simulated* — the simple statistical baseline lands **below chance** (ROC-AUC 0.383) and the ensembles don't win. 266 tests.<br>`isolation-forest` `local-outlier-factor` `imbalanced-data` `paysim`
* **[Anomalous invoices in mining procurement](https://github.com/Rxyxs/mining-procurement-anomaly-engine)** · *simulated* — a PyTorch autoencoder: reviewing only 5% of invoices finds 37.3% of the anomalous ones, ~7.5 times chance.<br>`autoencoder` `pytorch` `unsupervised-learning` `procurement`
* **[Polyglot fraud engine](https://github.com/Rxyxs/chile-polyglot-fraud-engine)** · *simulated* — C + Ruby + Python with each layer profiled: the C module takes 31 ns per call; the full request, 4.68 ms p50.<br>`c` `ruby` `shared-memory-ipc` `prometheus`
* **[Market tick anomalies (C++)](https://github.com/Rxyxs/market-tick-anomaly-engine-cpp)** · *real* — EWMA and CUSUM validated against the March 2020 crypto crash, at 7.26 million ticks per second.<br>`cpp` `cusum` `ewma` `real-market-data`
* **[Lithium order-flow imbalance (C++)](https://github.com/Rxyxs/lithium-orderbook-imbalance-cpp)** · *simulated* — zero false positives outside the injected shock across 43,200 windows.<br>`cpp` `order-flow` `market-microstructure` `zero-dependencies`

### 3. Anticipating equipment failure

* **[Predictive maintenance on trucks (SCANIA)](https://github.com/Rxyxs/heavy-truck-predictive-maintenance)** · *real* — 23,550 trucks. The expected-cost rule cuts the challenge's official cost by 31% on test, but the saving runs out if a workshop visit costs twice as much, because the model overstates the risk. [Page](https://rxyxs.github.io/heavy-truck-predictive-maintenance/).<br>`predictive-maintenance` `survival-analysis` `cost-sensitive-learning` `shap`
* **[Failure from continuous signal](https://github.com/Rxyxs/failure-prediction-signal-lab)** · *real + simulated* — bearing vibration (NASA IMS) and seismic signal (LANL): on LANL, spectral features with boosting beat a CNN on the raw signal by 2.7×.<br>`remaining-useful-life` `signal-processing` `fft` `pytorch`
* **[SAG mill digital twin](https://github.com/Rxyxs/chile-mining-sag-energy-digital-twin)** · *simulated* — a Kalman filter to estimate ore hardness (79% less error than the sensor) and a 24-hour energy forecast 27.6% better than Holt-Winters.<br>`digital-twin` `kalman-filter` `sensor-fusion` `lightgbm`

### 4. Measuring causes and evaluating decisions

* **[Mining fleet causal impact](https://github.com/Rxyxs/chile-mining-fleet-causal-impact)** · *simulated + real* — uplift and staggered difference-in-differences; the ATT matches an independent reference implementation on a real panel.<br>`causal-inference` `econml` `uplift-modeling` `difference-in-differences`
* **[A/B experimentation](https://github.com/Rxyxs/chile-fintech-experimentation-lab)** · *Monte Carlo* — sample size, SRM, CUPED and multiple-comparison correction, with a harness that checks whether each rule controls the error it promises.<br>`ab-testing` `cuped` `power-analysis` `sequential-testing`
* **[Pension funds](https://github.com/Rxyxs/chile-pension-fund-switching-cost)** · *real* — a regime signal that "earned" 1.4–2.3% a year loses 0.2% a year out of sample. In inflation-indexed terms, 2021–23 was a 26% drop, not 14.6%.<br>`duckdb` `counterfactual-analysis` `behavioral-finance` `pensions`

### 5. Optimizing operations

* **[Copper flotation](https://github.com/Rxyxs/optimizacion-geometalurgica-flotacion-cobre)** · *simulated* — recommends reagents and pH per block: +27.6 recovery points on the 150 worst blocks within budget, with two optimizers that agree with each other.<br>`genetic-algorithm` `nsga-ii` `multi-objective-optimization` `shap`
* **[Last-mile logistics](https://github.com/Rxyxs/chile-spatial-logistics-opt)** · *simulated on real districts* — multi-depot routing with time windows (OR-Tools) over real district polygons: 0 of 173 zones left unserved.<br>`or-tools` `vrptw` `h3` `geopandas`
* **[Churn as a business decision](https://github.com/Rxyxs/customer-churn-mlops-platform)** · *simulated* — the threshold is chosen by customer value: +US$75,847 contacting 78.6%, against +US$42,717 contacting everyone.<br>`mlflow` `mlops` `fastapi` `docker`

### 6. Measuring and managing financial risk

* **[Credit risk lab](https://github.com/Rxyxs/credit-risk-scoring-lab)** · *real macro, simulated portfolio* — 26 techniques: an R+Python+C scorecard (270.6 million rows per second), lifetime PD for IFRS 9, a bias audit, and the full lifecycle of a production model (shadow, canary, retraining).<br>`scorecard` `ifrs9` `r` `mlops`
* **[Systemic risk in Chile](https://github.com/Rxyxs/chile-fintech-systemic-risk)** · *real* — six languages over Central Bank data. The LSTM (51.0%) does not beat the majority class (53.6%); volatility, on the other hand, is highly persistent.<br>`julia` `r` `cplusplus` `systemic-risk`
* **[Crypto quant lab](https://github.com/Rxyxs/crypto-quant-techniques-lab)** · *real* — eight techniques. All five strategies lose money after costs and the simplest rule beats LightGBM; spoofing detection is the clearly positive result (0.92 precision).<br>`quantitative-finance` `cointegration` `portfolio-optimization` `nlp`
* **[Copper Asian options (C++)](https://github.com/Rxyxs/copper-options-montecarlo-cpp)** · *model* — C++20 Monte Carlo under GBM, Schwartz and Heston: 9.64× on 16 threads, and a real control-variate bias found and fixed.<br>`cpp20` `monte-carlo` `heston-model` `variance-reduction`

### 7. Getting the data in order

* **[Cleaning toolkit across 4 domains](https://github.com/Rxyxs/Limpieza_Datos)** · *real* — the same toolkit on Central Bank, COCHILCO and World Bank data; it caught a corrupted value at the source. 223 tests.<br>`data-quality` `pydantic` `schema-validation` `pytest`
* **[Mining data warehouse](https://github.com/Rxyxs/data-warehouse-analitico-mineria-chile)** · *simulated* — dbt + DuckDB from staging to marts, with 83 quality tests and model-ready views.<br>`dbt` `duckdb` `star-schema` `analytics-engineering`
* **[E-commerce lakehouse](https://github.com/Rxyxs/ecommerce-lakehouse-duckdb)** · *simulated* — Polars + DuckDB over partitioned Parquet; repeating the benchmark 7 times changed the conclusion.<br>`polars` `duckdb` `parquet` `lakehouse`

### 8. Classifying and estimating

* **[Scientific classification](https://github.com/Rxyxs/scientific-classification-lab)** · *real* — Higgs boson (AMS 3.64 against 3.8–3.9 for the Kaggle winners) and Kepler exoplanets (79.3% against a 49.8% baseline).<br>`gradient-boosting` `pytorch` `particle-physics` `astronomy`
* **[Ore grade and fragmentation (.NET)](https://github.com/Rxyxs/chile-mining-grade-blast-quality-dotnet)** · *simulated* — ML.NET + ONNX in a desktop app: P80 at R² 0.957.<br>`csharp` `ml-net` `onnx` `wpf`

### 9. Text, language and images

* **[Mining safety RAG](https://github.com/Rxyxs/rag-seguridad-minera-chile)** · *real regulation* — hybrid search over Chile's DS 132; re-ranking lifts MRR from 0.920 to 0.981.<br>`rag` `hybrid-search` `cross-encoder` `bm25`
* **[Mining operations agent](https://github.com/Rxyxs/chile-mining-ops-agent)** · *simulated* — an LLM that answers by calling tools (SQL, scoring, anomalies) instead of making up numbers.<br>`llm-agent` `tool-calling` `duckdb`
* **[Local language model for industry](https://github.com/Rxyxs/slm-industrial-gateway)** · *simulated* — offline inference, guardrails and QLoRA fine-tuning; the evaluation shows the base model makes up argument names in 94 of 100 prompts — exactly what the fine-tuning is there to fix.<br>`llama-cpp` `qlora` `guardrails` `local-inference`
* **[YOLOv8 on a Raspberry Pi — undergraduate thesis](https://github.com/Rxyxs/yolov8-separable-convolutions)** · *real (COCO)* — separable convolutions: 68% fewer parameters and ~10× faster on a Raspberry Pi, at the cost of mAP50 0.175 against 0.212.<br>`yolov8` `computer-vision` `edge-computing` `raspberry-pi`

## Tools

**Languages**

![Python](https://img.shields.io/badge/Python-0D1117?style=flat-square&logo=python&logoColor=00FF66)
![SQL](https://img.shields.io/badge/SQL-0D1117?style=flat-square&logo=postgresql&logoColor=00FF66)
![R](https://img.shields.io/badge/R-0D1117?style=flat-square&logo=r&logoColor=00FF66)
![C++](https://img.shields.io/badge/C%2B%2B-0D1117?style=flat-square&logo=cplusplus&logoColor=00FF66)
![C](https://img.shields.io/badge/C-0D1117?style=flat-square&logo=c&logoColor=00FF66)
![C#](https://img.shields.io/badge/C%23-0D1117?style=flat-square&logo=dotnet&logoColor=00FF66)
![Julia](https://img.shields.io/badge/Julia-0D1117?style=flat-square&logo=julia&logoColor=00FF66)
![Go](https://img.shields.io/badge/Go-0D1117?style=flat-square&logo=go&logoColor=00FF66)
![Ruby](https://img.shields.io/badge/Ruby-0D1117?style=flat-square&logo=ruby&logoColor=00FF66)

**Data**

![pandas](https://img.shields.io/badge/pandas-0D1117?style=flat-square&logo=pandas&logoColor=00FF66)
![Polars](https://img.shields.io/badge/Polars-0D1117?style=flat-square&logo=polars&logoColor=00FF66)
![NumPy](https://img.shields.io/badge/NumPy-0D1117?style=flat-square&logo=numpy&logoColor=00FF66)
![DuckDB](https://img.shields.io/badge/DuckDB-0D1117?style=flat-square&logo=duckdb&logoColor=00FF66)
![dbt](https://img.shields.io/badge/dbt-0D1117?style=flat-square)
![Apache Parquet](https://img.shields.io/badge/Apache%20Parquet-0D1117?style=flat-square&logo=apacheparquet&logoColor=00FF66)
![Pydantic](https://img.shields.io/badge/Pydantic-0D1117?style=flat-square&logo=pydantic&logoColor=00FF66)
![Jupyter](https://img.shields.io/badge/Jupyter-0D1117?style=flat-square&logo=jupyter&logoColor=00FF66)

**Machine learning & statistics**

![scikit-learn](https://img.shields.io/badge/scikit--learn-0D1117?style=flat-square&logo=scikitlearn&logoColor=00FF66)
![LightGBM](https://img.shields.io/badge/LightGBM-0D1117?style=flat-square)
![XGBoost](https://img.shields.io/badge/XGBoost-0D1117?style=flat-square)
![CatBoost](https://img.shields.io/badge/CatBoost-0D1117?style=flat-square)
![PyTorch](https://img.shields.io/badge/PyTorch-0D1117?style=flat-square&logo=pytorch&logoColor=00FF66)
![SciPy](https://img.shields.io/badge/SciPy-0D1117?style=flat-square&logo=scipy&logoColor=00FF66)
![Optuna](https://img.shields.io/badge/Optuna-0D1117?style=flat-square&logo=optuna&logoColor=00FF66)
![Plotly](https://img.shields.io/badge/Plotly-0D1117?style=flat-square&logo=plotly&logoColor=00FF66)

**Language, vision & edge**

![LangChain](https://img.shields.io/badge/LangChain-0D1117?style=flat-square&logo=langchain&logoColor=00FF66)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-0D1117?style=flat-square&logo=huggingface&logoColor=00FF66)
![Ultralytics YOLO](https://img.shields.io/badge/Ultralytics%20YOLO-0D1117?style=flat-square&logo=ultralytics&logoColor=00FF66)
![ONNX](https://img.shields.io/badge/ONNX-0D1117?style=flat-square&logo=onnx&logoColor=00FF66)
![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-0D1117?style=flat-square&logo=raspberrypi&logoColor=00FF66)

**Production**

![FastAPI](https://img.shields.io/badge/FastAPI-0D1117?style=flat-square&logo=fastapi&logoColor=00FF66)
![Streamlit](https://img.shields.io/badge/Streamlit-0D1117?style=flat-square&logo=streamlit&logoColor=00FF66)
![MLflow](https://img.shields.io/badge/MLflow-0D1117?style=flat-square&logo=mlflow&logoColor=00FF66)
![Docker](https://img.shields.io/badge/Docker-0D1117?style=flat-square&logo=docker&logoColor=00FF66)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-0D1117?style=flat-square&logo=githubactions&logoColor=00FF66)
![pytest](https://img.shields.io/badge/pytest-0D1117?style=flat-square&logo=pytest&logoColor=00FF66)
![Prometheus](https://img.shields.io/badge/Prometheus-0D1117?style=flat-square&logo=prometheus&logoColor=00FF66)
![Grafana](https://img.shields.io/badge/Grafana-0D1117?style=flat-square&logo=grafana&logoColor=00FF66)
![Git](https://img.shields.io/badge/Git-0D1117?style=flat-square&logo=git&logoColor=00FF66)
![Linux](https://img.shields.io/badge/Linux-0D1117?style=flat-square&logo=linux&logoColor=00FF66)

## Contact

[LinkedIn](https://www.linkedin.com/in/pablo-reyes-pino) · preyesp09@gmail.com · Santiago, Chile
