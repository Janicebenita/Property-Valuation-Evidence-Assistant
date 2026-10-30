# Property Valuation Evidence Assistant Explainability

## Decision and Reasoning Process

The agent's decision support selects potentially relevant comparables using declared similarity and recency rules. Its reasoning explains inclusion, exclusion, differences, possible adjustments, and confidence limitations.

## Inputs and Data Sources Used

Input data includes subject-property details, authorized transaction records, listing history, and professional assumptions. The date, coverage, and reliability of every data source are recorded when available.

## Outputs and Supporting Evidence

The output contains a comparable table, factor analysis, indicative range, and unresolved questions. Supporting evidence remains linked to the relevant transaction or property record.

## Limits, Constraints, and Known Issues

A limitation is that historical or advertised prices may not represent current market value. The agent is constrained from issuing a certified appraisal, investment guarantee, lending decision, or legal opinion.

## Uncertainty and Human Review

Uncertainty is explicitly stated when evidence is limited or market conditions are volatile. A qualified professional must review the analysis and determine any formal valuation.

## Implementation in This Repository

The repository's implementation is the OpenGAP package formed by `agent.yaml`, `SOUL.md`, this explainability document, and `README.md`. The manifest defines the property and comparable-evidence inputs and requires an evidence-linked, uncertainty-aware summary rather than a certified value.

No live market-data feed, appraisal model, lender integration, or transaction action is present. A compatible host must retain the supplied evidence and present the result to a qualified human for any formal valuation or financial decision.
