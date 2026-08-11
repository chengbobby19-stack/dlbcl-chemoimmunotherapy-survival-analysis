
"""
Synthetic demonstration data for a GitHub portfolio project.

IMPORTANT:
- This file does NOT reproduce NCDB patient-level data.
- It does NOT contain original research code.
- It only creates non-identifiable synthetic data with a structure similar to
  the variables described in the user's prior DLBCL chemoimmunotherapy project.
"""
import numpy as np
import pandas as pd

def generate_synthetic_dlbcl(n=2500, seed=20260811):
    rng = np.random.default_rng(seed)
    year = rng.integers(2013, 2023, n)
    age = np.clip(rng.normal(68, 11, n), 20, 90).round(0)
    sex = rng.choice(["Female","Male"], n, p=[0.45,0.55])
    stage = rng.choice(["I-II","III-IV"], n, p=[0.42,0.58])
    comorbidity = rng.choice([0,1], n, p=[0.69,0.31])
    b_symptoms = rng.choice([0,1], n, p=[0.64,0.36])
    insurance = rng.choice(["Private","Medicare","Medicaid/Other"], n, p=[0.34,0.52,0.14])
    facility = rng.choice(["Academic/Research","Community"], n, p=[0.46,0.54])

    logit = (-0.3 + 0.28*(year-2013) -0.025*(age-68)
             -0.25*comorbidity +0.15*(facility=="Academic/Research"))
    p_cit = 1/(1+np.exp(-logit))
    cit = rng.binomial(1, p_cit, n)

    linpred = (-0.35*cit +0.025*(age-68) +0.42*(stage=="III-IV")
               +0.35*comorbidity +0.22*b_symptoms)
    event_time = rng.exponential(1/((1/55)*np.exp(linpred)))
    censor_time = rng.uniform(12, 84, n)
    time = np.minimum(event_time, censor_time)
    death = (event_time <= censor_time).astype(int)

    return pd.DataFrame({
        "diagnosis_year": year,
        "age": age.astype(int),
        "sex": sex,
        "stage": stage,
        "comorbidity_ge1": comorbidity,
        "b_symptoms": b_symptoms,
        "insurance": insurance,
        "facility_type": facility,
        "treatment": np.where(cit==1, "Chemoimmunotherapy", "Chemotherapy alone"),
        "survival_months": np.round(time,2),
        "death": death
    })

if __name__ == "__main__":
    generate_synthetic_dlbcl().to_csv("../data/synthetic_dlbcl_demo.csv", index=False)
