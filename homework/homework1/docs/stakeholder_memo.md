# Project Title: Real-time Risk Monitoring System for IRDM
**Stage:** Problem Framing & Scoping (Stage 01)
## Problem Statement
Uncertainty and volatilily recently surge in the IRDM(Interest Rate Derivative Maket) given the instability inherent in the recent policies made by the current administration, such as the tariff shiftments and cutting in energy. The risk management department needs to identify the portfolios that may breach VaR threshold in advance to adjust the heading strategy and reduce the penalty and capital occupancy. The current end-of-day VaR system can't respond to the immediate policy shock, causing potential massive loss in terms of regulatory compilance and capital costs. It's therefore necessary to construct a real-time monitoring system capable of capturing the policy-driven impacts and provides early warnings of sharp increase in risk exposure.

## Stakeholder & User
**Decision Maker**:
+   CRO (Chief Risk Officer):
      + Oversees the firm's overall risk management framework and ensures compilance with regulatory capital and exposure limits.
+ CIO/CTO (Chief Information Officer/Chief Technology Officer) 
    +  Who manages the entire technological structure relating to the business.
+ Head of Compilance    
    + Ensuring all trading activities and risk processes meet internal policies and external regulatory requirements.
+ Head of Trading   
    + Manages the trading desk's strategies and wnsures alignment between trading decisions and risk controls.
+ Head of Market Risk
    + Leads the team monitoring market risk metrics such as VaR, sentisitivities, and stress test results.

**Users**:
  + Front-desk Trader 
    + Who executes trades, position management, and portfolio adjustments in response to market movements and risk alerts.
  + Risk Quantitative Analyst
    + Develops, calibrates, and maintains risk models, performing quantitative analysis to support decision-making.
  
**Timing & Workflow context**:
+ The system shold provides a close monitoring to the market; when a policy is issued, the system should analyze the potential IR(Impulse Response) and give the simulation with VaR and risk indicators updated
+ If a risk measure falls into a setting range, trigger alarm, informing the trading and risk management team.

## Useful Answer & Decision

**Properties**: Descriptive + Predictive
**Metrics**: 
  + The estimated VaR in the next 24-hour window with RMSE <= 5%
  + The recall rate >= 90%
  + Auxiliary Indices
    + Macro Uncertainty & Panic Fctors (e.g. EPU (Economic Policy Uncertainty Index), VIX, Fiscal Policy Sentiment Index ...)
    + Interest Rate & Credit Factors (e.g. MOVE Index, Yield Curve Slope, ...)
    + Financial Market Indices (e.g. SP500, DXY ...)

**Artifact to Deliver**:
  + Deployable API intercepting the policy signals.
  + Visualizable tools offering descriptive statistics including Heat Map and so on.
  + Automatic break points checker.
  + Back track tools for efficiency analysis and system-generated risk report.

## Assumptions & Constraints
  + **Assumptions**:
      + Historical trada data, intraday market data, policy event feeds (signallized) will remain accessible with latency <= 5 mins.
      + High-performance computing strcuture able to deliver VaR recalculations within 40s.
      + Regulatory guidelines permit the use of certain policy-sensitive data (e.g., counterparty exposures) within the risk model.
 + **Constraints**:
      + Limited budget restricts expansion of computing resources
      + Risk metrics must be updated within 1 hour of a relevant policy announcement.
      + All data storage and processing must remain within domestic data centers, in compliance with Basel standards and local regulations.
      + System deployment must be completed before the quarter-end regulatory review.
  
## Known Unknowns / Risks
**Data quality**: 
  + The alternative-data involved in the decisioning process may come from many data sources and have inconsistencies per se. The problem deteriorates especially when dealing with unstructured data and signalize them.
  + Can use multiple sources to crossvalidate the efficacy of the data, ensuring the completeness. When huge disparity is detected on some indices, mark them for artificial check later.

**User Adoption**:
  + Even if the system can accurately predict risks, whether traders and risk managers take corresponding intraday actions depends on their trust in the system, existing operating habits, and performance evaluation criteria. Some users may rely more on their own experience and be unwilling to fully depend on model-generated alerts. 
  + After deployment, the match rate between triggered alerts and actual position adjustments should be tracked. A user feedback channel should be established to collect traders’ opinions on the accuracy and interpretability of alerts, and to iteratively improve the model and its visualizations.
  
## Lifecycle Mapping
Goal → Stage → Deliverable
- Disecting the problem; locating the core issues and technicalitys; setting up basic development process; considering possible major risks → Problem Framing & Scoping (Stage 01) → Blueprint of the Project (including: Problem Statement; Stakeholder & User Delineation; Useful Answer & Decision; Assumptions & Constraints; known Unknowns / Risks; lifecycle mapping; Repo Plan)
- ...
## Repo Plan
**Repo Structure:**

    + /data/ - Stores project datasets, including raw data (e.g., historical interest rate data, derivatives transaction records, policy event feeds) and processed data.

    + /src/ - Contains source code for data processing, feature engineering, model training, prediction APIs, and visualization modules.

    + /notebooks/ - Holds Jupyter Notebooks for exploratory data analysis, experiments, and prototype visualizations.

    + /docs/ - Project documentation, including requirements, design documents, meeting notes, compliance records, and test reports.

**Cadence for Updates:**

    + /data/ - Updated in real time or hourly to reflect market data and policy events.

    + /src/ - Updated weekly or whenever new features or model improvements are implemented.

    + /notebooks/ - Updated after each new experiment or analysis is completed.

    + /docs/ - Updated after any requirements changes, compliance reviews, or major project milestones.