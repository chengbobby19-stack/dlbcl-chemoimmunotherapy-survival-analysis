# Statistical Methods and Interpretation Notes

This file is for my own preparation before discussing the project with a biostatistics mentor.

## 1. Annual treatment distribution
**Question:** Did real-world use of CIT change over calendar time?

I should be able to explain:
- why treatment utilization is summarized by diagnosis year;
- why this is descriptive rather than causal;
- how changing treatment adoption can motivate year-specific outcome analyses.

## 2. Kaplan–Meier (KM) survival analysis
**Purpose:** Describe unadjusted overall survival over time.

I should be able to explain:
- censoring;
- survival probability;
- why KM is unadjusted;
- what a log-rank comparison does and does not prove.

## 3. Cox proportional hazards regression
**Purpose:** Estimate the association between treatment and the instantaneous hazard of death while adjusting for measured covariates.

I should be able to explain:
- hazard ratio (HR);
- HR < 1 vs HR > 1;
- adjustment for baseline covariates;
- why an adjusted HR in an observational study is still not automatically causal.

## 4. Treatment × year interaction
**Purpose:** Test whether the relative association between CIT and survival changed across calendar years.

I should be able to explain:
- main effect vs interaction;
- why the interaction addresses a different question from the overall treatment HR.

## 5. Restricted Mean Survival Time (RMST)
**Purpose:** Provide an absolute, clinically interpretable summary of survival up to a fixed time horizon.

I should be able to explain:
- RMST as the area under the survival curve up to tau;
- why RMST complements the hazard ratio;
- why 36- and 60-month horizons were clinically useful in the original project.

**Important:** The original presentation states that RMST was adjusted but does not specify the exact estimator. I should not claim a specific adjustment method unless I verify it from the original analysis code/specification.

## 6. 30-day landmark sensitivity analysis
**Purpose:** Examine whether very early post-diagnosis deaths materially affect the observed treatment-survival association.

I should be able to explain:
- the landmark concept;
- restriction to patients alive/followed at the landmark;
- why sensitivity analyses test robustness rather than create a second primary conclusion.

## 7. Association vs causation
Because the study is retrospective and observational:
- measured confounding can be adjusted;
- unmeasured confounding can remain;
- treatment selection is not randomized;
- conclusions should be phrased as associations.

## 8. My project statement
A concise explanation I can give:

> This GitHub project is a reproducibility-focused reconstruction of a DLBCL real-world survival project I previously worked on. I use synthetic data because the original NCDB patient-level data are restricted. The goal is to demonstrate the statistical workflow I understand—treatment-pattern description, Kaplan–Meier analysis, Cox regression, calendar-time interaction, RMST interpretation, and landmark sensitivity analysis—without presenting restricted data or claiming to reproduce the original study results.
