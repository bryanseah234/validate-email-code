# Validate Email Code

A Python script to bulk validate email addresses using format, DNS, and SMTP checks.

## Description

This project provides a simple yet powerful email validation tool that reads email addresses from a text file and validates each one through multiple verification methods. It checks email format, DNS records, and SMTP server responses to determine if an email address is valid. Results are separated into two output files for valid and invalid emails.

## Features

- Bulk email validation from text file input
- Multi-layer validation (format, DNS, and SMTP checks)
- Progress bar visualization using tqdm
- Automatic separation of valid and invalid emails into separate output files
- Configurable timeout settings for DNS and SMTP checks

## Technologies Used

- Python 3
- py3-validate-email - Email validation library
- tqdm - Progress bar library

## Installation

```bash
# Clone the repository
git clone https://github.com/bryanseah234/validate-email-code.git

# Navigate to project directory
cd validate-email-code

# Install dependencies
pip install py3-validate-email tqdm
```

## Usage

```bash
# Run the validation script
python validateemail.py
```

### Instructions:
1. Create a text file named `emails.txt` in the same directory as the script
2. Add email addresses to validate (one per line)
3. Run the script using the command above
4. Check the output:
   - `true emails.txt` - Contains valid email addresses
   - `false emails.txt` - Contains invalid email addresses

## Disclaimer

1. FOR EDUCATIONAL PURPOSES ONLY
2. USE AT YOUR OWN DISCRETION

## License

MIT License

---

**Author:** <a href="https://github.com/bryanseah234">bryanseah234</a>
