# Statistical Methods and Interpretation Notes

## 1. Study framework

This portfolio is based on a retrospective cohort study framework comparing **chemoimmunotherapy (CIT)** with **chemotherapy alone** in patients with diffuse large B-cell lymphoma (DLBCL).

## 2. Why the public repository uses synthetic data

The original NCDB patient-level data and team analysis outputs are not included in this public repository. Therefore, all tables and figures shown here are generated from a **synthetic demonstration dataset** constructed to preserve the overall clinical-statistical logic of the project while avoiding disclosure of restricted or unpublished research material.

## 3. Table 1 — Baseline characteristics

The baseline table is used to describe the composition of the treatment groups. It helps the reader understand how the CIT and chemotherapy-alone groups differ before time-to-event modeling.

## 4. Figure 1 — Treatment patterns and overall survival

Figure 1 combines three complementary views:

- **A. Kaplan–Meier overall survival with number at risk**
- **B. Annual treatment distribution**
- **C. Event structure by diagnosis year**

Together, these panels show the time-to-event pattern, the secular adoption of CIT, and the balance between death and censoring across diagnosis years.

## 5. Figure 2 — RMST and follow-up maturity

Restricted mean survival time (RMST) is used here as an **absolute survival summary** up to fixed time horizons (3 years and 5 years). This complements the hazard ratio from Cox regression. The follow-up maturity panel shows why later calendar years have shorter available follow-up.

## 6. Figure 3 — Year-specific Cox estimates

Year-specific multivariable Cox models estimate the adjusted association between treatment and overall survival within each diagnosis year. The same figure also shows the **overall treatment association** and the **treatment-by-year interaction**, which addresses whether the treatment association changes across calendar time.

## 7. Figure 4 — 30-day landmark sensitivity analysis

The landmark analysis tests whether very early events materially change the observed treatment association. In the portfolio, this is presented as a robustness check rather than a separate primary result.

## 8. Interpretation principle

Because the original study framework is **observational**, results should be interpreted as **adjusted associations**, not automatic causal treatment effects.
