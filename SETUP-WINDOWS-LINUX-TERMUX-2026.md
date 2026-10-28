# Setup Guide: Windows, Linux and Termux (2026)

This guide uses Python's standard library for the included exercises; no paid software or third-party Python packages are required.

## Windows 11 / PowerShell
1. Install Python 3 from the official Python website or Microsoft Store, if it is not already installed.
2. Open PowerShell in the extracted course folder.
3. Check Python:

```powershell
py --version
```

4. Run the synthetic-log parser:

```powershell
py labs/parse_auth_events.py
```

5. Run tests:

```powershell
py -m unittest discover -s labs -p "test_*.py" -v
```

## Linux / Parrot / Kali
From the extracted course directory:

```bash
python3 --version
python3 labs/parse_auth_events.py
python3 -m unittest discover -s labs -p 'test_*.py' -v
```

Use your distribution's official package manager to install Python if needed. Do not run every course command as root.

## Android Termux
Install Termux from a trusted official distribution source. Then:

```bash
pkg update
pkg install python
cd ~/storage/shared
```

Change directory to wherever you extracted the course ZIP. If the archive is in Downloads, use your actual path; do not copy a path blindly. Then run:

```bash
python labs/parse_auth_events.py
python -m unittest discover -s labs -p 'test_*.py' -v
```

Android storage permissions and paths differ by setup. `termux-setup-storage` may be needed to access shared storage.

## Run the local-only header lab
Terminal 1:

```bash
python labs/local_header_lab.py
```

Terminal 2:

```bash
python labs/audit_local_headers.py
```

The demo server binds only to `127.0.0.1`. The checker rejects hostnames and non-loopback IP addresses. Stop the server with Ctrl+C when finished.

## Troubleshooting
- `python` not found: try `py` on Windows or `python3` on Linux.
- `No module named ...`: run commands from the course root; these labs use the standard library.
- Port 8765 is busy: stop the other local process before starting this lab. Do not expose the training server to your LAN.
- Do not run commands you do not understand on a production system.
