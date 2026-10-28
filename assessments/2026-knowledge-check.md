# 2026 Knowledge Check — Answer Key for Instructors / Self-study

The offline interactive quiz is in `dashboard/index.html`. This file provides a short written assessment for learners who prefer Markdown or printed notes.

## Questions
1. What must be confirmed before a security test begins?
2. Name three signals of excessive cloud permissions.
3. Why are container image scanning and runtime hardening different controls?
4. Give two mitigations for prompt injection or data leakage in an AI application.
5. List the major phases of incident response.
6. What belongs in a useful vulnerability finding?
7. Why should secrets never be committed to Git, even briefly?
8. How can you preserve evidence while minimizing privacy risk?
9. What is the purpose of a software bill of materials (SBOM)?
10. What makes a capstone ethically and technically defensible?

## Suggested answers
1. Written authorization, precise scope, permitted techniques, time window, contacts and stop conditions.
2. Wildcard permissions, unused admin identities, long-lived keys, public resources without a business need, lack of MFA for privileged roles.
3. Scanning detects known image/package issues; runtime hardening limits privileges and exposure if an issue exists.
4. Enforce authorization outside the model, treat retrieved content/output as untrusted, constrain tools, require approval for impactful actions, minimize and redact data.
5. Preparation, identification, containment, eradication, recovery and lessons learned.
6. Summary, affected asset, severity rationale, evidence, bounded reproduction, impact, remediation and retest.
7. Git history and clones can retain it; revoke/rotate exposed credentials and remove the secret safely from history if appropriate.
8. Collect only necessary artifacts, record provenance, preserve originals, restrict access and redact reports.
9. It inventories software components and supports vulnerability and provenance review.
10. Authorized scope, reproducible methods, minimal risk, trustworthy evidence, prioritized fixes and retesting.
