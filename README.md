IPPI — Identity Privilege Path Inspector

IPPI finds privilege escalation paths that traditional scanners ignore.

Most IAM tools list permissions.
IPPI shows how identities overlap until someone becomes admin.

Why IPPI Exists

Cloud breaches rarely start with “Owner access”.

They start with:

a forgotten Service Account

a deleted identity

a legacy Editor role

impersonation paths nobody mapped

IPPI answers one question:

“Who can become what — and how?”

What IPPI Does (and what it does NOT)

IPPI does:

Read-only IAM analysis

Finds high-signal privilege paths

Outputs human-readable evidence

Produces JSON for audits

IPPI does NOT:

Scan ports

Check CVEs

Perform exploitation

Modify anything

Example Finding

📂 samples/discovery.json
📸 samples/terminal_output.png

This is a real-world pattern:

Deleted Service Account

Still bound to Editor

Hidden privilege overlap

Who This Is For

Cloud Security Engineers

IAM Auditors

Red & Blue Teams

CTOs who want signal, not noise

Vision & Roadmap

IPPI is intentionally small.

Future ideas (not promises):

Privilege path visualization

Blast radius estimation

Natural language explanations for non-security stakeholders

Support the Project

IPPI is free for everyone.

If this tool saved you time, reduced risk, or helped an audit:
you can support development via GitHub Sponsors.

No paywall. No locked features.
