IPPI — Identity Privilege Path Inspector
IPPI (Identity Privilege Path Identification) is more than a tool; it is a specialized security framework for mapping deterministic privilege escalation in complex Cloud environments. It serves as the foundation for a unified identity reasoning ecosystem.

IPPI finds privilege escalation paths that traditional scanners ignore. Most IAM tools list permissions; IPPI shows how identities overlap until someone becomes admin.

Why IPPI Exists
Cloud breaches rarely start with “Owner access”. They start with:

A forgotten Service Account

A deleted identity

A legacy Editor role

Impersonation paths nobody mapped

IPPI answers one question: “Who can become what — and how?”

What IPPI Does (and what it does NOT)
IPPI does:

Methodology-Driven Analysis: Implements the IPPI framework to identify identity pivots.

Read-only IAM analysis: Safe for production environments.

High-signal discovery: Finds privilege paths, not just misconfigurations.

Audit-Ready Evidence: Produces JSON artifacts for downstream reasoning tools.

IPPI does NOT:

Scan ports / Check CVEs

Perform exploitation

Modify any cloud resources

Example Finding
📂 samples/discovery.json Evidence. This is a real-world pattern:

Deleted Service Account

Still bound to Editor

Hidden privilege overlap

Who This Is For
Cloud Security Engineers & IAM Auditors

Red & Blue Teams

CTOs who want signal, not noise

The IPPI Ecosystem & Roadmap
IPPI is the core detection engine. It is designed to work in tandem with:

Cloud-IAM-Trust-Simulator: For modeling theoretical trust transitivity.

Cloud-IAM-Drift-Architect: For synthesizing findings into architectural risk reports.

Future ideas:

Privilege path visualization

Blast radius estimation

Natural language explanations for non-security stakeholders

Support the Project
IPPI is free for everyone. If this tool saved you time, reduced risk, or helped an audit, you can support development via GitHub Sponsors.

No paywall. No locked features.
