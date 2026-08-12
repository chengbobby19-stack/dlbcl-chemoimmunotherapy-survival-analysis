"""
Generate the public synthetic DLBCL demonstration dataset.

This script does NOT reproduce NCDB patient-level data.
It creates non-identifiable synthetic data that preserves the overall
clinical-statistical structure used in the public portfolio figures.
"""
import numpy as np
import pandas as pd

def generate_synthetic_dlbcl(seed=20260812):
    rng = np.random.default_rng(seed)
    years = np.arange(2013, 2022)
    rows = []

    for year in years:
        n = int(rng.integers(520, 680))
        age = np.clip(rng.normal(67.5, 10.5, n), 20, 90)
        sex = rng.choice(["Male","Female"], n, p=[0.56,0.44])
        race = rng.choice(
            ["NHW","NHB","Hispanic","NHAPI","Other/Unknown"],
            n, p=[0.77,0.07,0.08,0.03,0.05]
        )
        insured = rng.choice(["Insured","Uninsured"], n, p=[0.975,0.025])
        stage = rng.choice(["I","II","III","IV"], n, p=[0.12,0.18,0.24,0.46])
        comorbidity = rng.choice([0,1], n, p=[0.70,0.30])
        b_symptoms = rng.choice([0,1], n, p=[0.63,0.37])

        base_p = 0.60 + 0.04*(year-2013)
        p_cit = (
            base_p
            - 0.0025*(age-67.5)
            - 0.04*comorbidity
            + 0.01*(stage=="IV")
        )
        p_cit = np.clip(p_cit, 0.05, 0.97)
        cit = rng.binomial(1, p_cit, n)

        treat_beta = -0.17 - 0.025*(year-2013)
        lp = (
            treat_beta*cit
            + 0.020*(age-67.5)
            + 0.22*(sex=="Male")
            + 0.18*(stage=="III")
            + 0.42*(stage=="IV")
            + 0.30*comorbidity
            + 0.17*b_symptoms
        )
        base_rate = 1/52.0 * (0.985 ** (year-2013))
        event_time = rng.exponential(1/(base_rate*np.exp(lp)))

        diagnosis_month = rng.integers(0,12,n)
        admin_censor = (2024-year)*12 - diagnosis_month
        random_dropout = rng.uniform(0.60,1.00,n) * admin_censor
        censor_time = np.minimum(admin_censor, random_dropout)

        observed = np.minimum(event_time, censor_time)
        death = (event_time <= censor_time).astype(int)

        for i in range(n):
            rows.append({
                "diagnosis_year": year,
                "age": round(float(age[i]),1),
                "sex": sex[i],
                "race_ethnicity": race[i],
                "insurance_status": insured[i],
                "ann_arbor_stage": stage[i],
                "comorbidity_ge1": int(comorbidity[i]),
                "b_symptoms": int(b_symptoms[i]),
                "treatment": "Chemoimmunotherapy" if cit[i]==1 else "Chemotherapy alone",
                "survival_months": round(float(observed[i]),2),
                "death": int(death[i]),
            })

    return pd.DataFrame(rows)

if __name__ == "__main__":
    generate_synthetic_dlbcl().to_csv("../data/synthetic_dlbcl_demo.csv", index=False)
