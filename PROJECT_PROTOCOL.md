# Project Protocol

## Title
Real-World Chemoimmunotherapy Use and Survival in Diffuse Large B-Cell Lymphoma

## Basis
This portfolio project is based on a clinical research project previously conducted by the research team. The public repository is a methodological reconstruction using synthetic data.

## Original study aims
1. Describe annual treatment patterns (CIT vs chemotherapy alone) among patients with DLBCL from 2013–2022.
2. Quantify the absolute survival advantage of CIT using adjusted RMST differences at 3 and 5 years.
3. Estimate the relative survival association using multivariable Cox proportional hazards models and assess a treatment-by-year interaction.
4. Assess robustness with a 30-day landmark sensitivity analysis.

## Design
Retrospective observational cohort.

## Exposure
First-course chemoimmunotherapy versus chemotherapy alone.

## Outcome
Overall survival, defined in the original project as time from diagnosis to death or last contact.

## Covariates described in the original project
Age; sex; race/ethnicity; stage; comorbidity; B symptoms; insurance; income; education; urbanicity; facility type.

## Planned public demonstration
Because NCDB patient-level data are restricted, this repository uses synthetic data and demonstrates:
- Annual treatment distribution
- Table 1 / baseline description
- Kaplan–Meier curves
- Multivariable Cox regression
- Treatment × year interaction
- 30-day landmark analysis
- RMST concept demonstration

## Interpretation principle
Because the original study is observational, estimated treatment effects are interpreted as adjusted associations rather than causal effects.

## Reproducibility / privacy statement
No restricted NCDB data or original private research code are included.
