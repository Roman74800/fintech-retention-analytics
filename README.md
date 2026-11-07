# Fintech Customer Retention Analytics

**Portfolio project | Synthetic data | Python + PostgreSQL**

## Business question
How does monthly retention change across signup cohorts, and which acquisition channels bring more engaged customers?

## Deliverables
- Reproducible synthetic dataset of 5,000 customers and monthly activity
- Cohort retention heatmap (M0–M11, where observable)
- Average transaction volume by acquisition channel
- PostgreSQL cohort query with distinct-user counts

## Quick start
```bash
pip install -r requirements.txt
python generate_data.py
jupyter notebook notebooks/analysis.ipynb
```
Run the notebook from the project root (or from `notebooks/`). CSV files are included.

## Metric definitions
- **M1 retention**: customers active one calendar month after signup / all customers in signup cohort.
- **M0 retention**: active customers in signup month / all customers in cohort.
- **Transaction volume**: simulated monthly RUB volume among active customers.

## Caveats
The dataset is generated with a probabilistic retention decay model; it is **not real bank data**. Observed retention differences are descriptive, not causal. Recent cohorts have fewer observable months. No personal data is used.

## Suggested extensions
Segment retention by channel, estimate confidence intervals, and compare cohort-weighted vs user-weighted averages.
