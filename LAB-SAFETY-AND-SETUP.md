# Lab Safety and Setup (Windows, Linux, Termux)

## Rules before starting
1. Only test systems you own or have explicit written permission to assess.
2. Keep vulnerable VMs on host-only or isolated networks; avoid bridged networking for intentionally vulnerable targets.
3. Use snapshots and synthetic data.
4. Never scan public IP ranges or third-party networks without explicit authorization.
5. Do not store passwords, private keys, API tokens, or real client evidence in this repository.
6. Confirm resource use and costs before enabling cloud resources.

## Windows host
- Use a standard user account for everyday work.
- Keep Windows, browser, hypervisor, and security tools updated from official sources.
- Prefer an isolated VM network for labs.
- Take a clean snapshot before each exercise and revert afterward.

## Linux host or VM
- Use distro-supported packages where possible.
- Keep a package inventory and record versions in notes.
- Use Python virtual environments; avoid `sudo pip`.
- Do not pipe an unreviewed remote script directly into a privileged shell.

## Android / Termux
- Treat the phone as a learning client, not a substitute for an isolated vulnerable target.
- Keep the main phone non-root if that is your preference.
- Do not run intrusive scans against mobile networks, shared Wi-Fi, or public hosts.
- Use `pkg update` and review package changes before accepting them; package availability differs by repository and architecture.
- Never paste secrets into AI chats or terminal screenshots.

## Teardown checklist
- [ ] Stop lab containers/VMs.
- [ ] Revert snapshots or delete temporary resources.
- [ ] Remove dummy credentials and test data.
- [ ] Verify no cloud resources are still running.
- [ ] Archive sanitized notes and findings.
