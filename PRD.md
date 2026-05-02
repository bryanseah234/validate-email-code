# PRD: emailvalidate

## Overview
A Python CLI script that bulk-validates a list of email addresses using three-layer verification: format checking, DNS MX record lookup, and SMTP handshake. Splits input into valid and invalid output files. Target user: marketers or developers who need to clean an email list before a send campaign.

## Goals
- Accept a flat list of email addresses (one per line in `emails.txt`)
- Validate each address via format, DNS, and SMTP checks
- Write results to `true emails.txt` and `false emails.txt`
- Show a progress bar during processing

## Non-Goals
- Web UI or API endpoint
- Deduplication of input list
- Handling email formats other than plain `user@domain.tld`
- Rate limiting / bulk SMTP throttling
- Output formats other than plaintext

## User Stories
- As a marketer, I have a CSV export of 10,000 emails and want to remove invalid ones before a campaign.
- As a developer, I want to test which addresses in a collected list actually have working mail servers.

## Tech Stack
- **Language**: Python 3.x
- **Libraries**: `py3-validate-email` (pip), `tqdm` (pip)
- **Runtime**: any OS with Python 3 and internet access

## Architecture
```
emailvalidate/
├── validateemail.py   # main script
├── emails.txt         # input file (user-provided)
├── true emails.txt    # output: valid addresses
└── false emails.txt   # output: invalid addresses
```

Single-file script:
1. Read `emails.txt` line by line
2. For each address, call `validate_email()` with format + DNS + SMTP flags
3. Append to appropriate output file
4. Update `tqdm` progress bar

## Features (detailed)

### Format Validation
- Checks email conforms to RFC format (local@domain.tld)
- Acceptance criteria: malformed strings return `False`

### DNS Validation
- Looks up MX records for the email's domain
- Timeout: 3 seconds
- Acceptance criteria: domains with no MX records return `False`

### SMTP Validation
- Opens SMTP connection and checks if the mailbox exists
- Timeout: 3 seconds
- Does not send actual email
- Acceptance criteria: non-existent mailboxes return `False`

### Progress Display
- `tqdm` progress bar showing current index and total count
- Handles `KeyboardInterrupt` gracefully — closes bar on Ctrl+C

## Data / Config
| File | Purpose |
|------|---------|
| `emails.txt` | Input — one email per line, UTF-8 |
| `true emails.txt` | Output — addresses that passed all checks |
| `false emails.txt` | Output — addresses that failed any check |

No config file needed — all parameters are hardcoded in script constants.

## Deployment / Run
```bash
pip install py3-validate-email tqdm
# place your email list in emails.txt
python validateemail.py
```

## Constraints & Notes
- **Speed**: SMTP checks are slow (~3s per address); 10k emails ≈ 8+ hours single-threaded
- **Blacklist**: `check_blacklist=False` — disposable email domains are not filtered
- **SMTP accuracy**: some valid servers reject SMTP probes (false negatives expected)
- **Network required**: DNS and SMTP checks need internet access
