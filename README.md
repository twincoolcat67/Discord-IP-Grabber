# Discord IP Logger

---

## Overview
This Python project generates a custom IP logger script that fetches detailed IP information about the machine it is run on and sends it to a Discord webhook. The generated logger collects IP data using various free IP info services, logs new IP addresses with timestamps, and sends nicely formatted embedded messages to Discord.

> **Important:** This project is **strictly for educational purposes only** and should only be tested on your own machines. Unauthorized use or deploying it to gather data from others without consent is illegal and unethical.

---

## Features

* Generates a unique Python logger script dynamically.
* Fetches comprehensive IP info: city, region, country, ISP, proxy/mobile status, timezone, and more.
* Saves logged IP info locally to avoid duplicate reporting.
* Sends data as an embedded message to a Discord webhook.
* Simple, colorized CLI interface using `pystyle`.
* Logs are stored in JSON format for easy inspection.

---

## Getting Started

### Prerequisites

* Python 3.7 or higher
* A Discord server with permissions to create webhooks
* Install required Python libraries:

```bash
pip install -r requirements.txt
```

### Installation

1. Clone this repository or download the script files.
2. Run the main script:

```bash
python main.py
```

3. When prompted, enter your Discord webhook URL.
4. The script generates a unique Python file inside the `built/` directory.
5. Run the generated script file to fetch your IP info and send it to Discord.

---

## Usage

* The initial script prompts for your Discord webhook URL.
* It creates a uniquely named logger script (`built/{random}.py`).
* Running the generated logger will:

  * Collect IP data.
  * Check if the IP has been logged before.
  * If new, send an embedded message to your Discord webhook.
  * Save the logged IP data locally in `log/ip_logs.json`.

---

## File Structure

```
/
├── built/                  # Generated logger scripts
├── log/                    # IP logs in JSON
├── main.py                 # Script to generate logger scripts (this project)
├── requirements.txt        # Python dependencies
└── README.md
```

---

## Dependencies

* [requests](https://pypi.org/project/requests/) — For HTTP requests to IP APIs and Discord webhook.
* [pystyle](https://pypi.org/project/pystyle/) — For colorful CLI output.

---

## Disclaimer & Ethics

This tool is intended for learning and experimentation only. Collecting IP or location data without explicit permission may violate privacy laws in your country.

Use responsibly. Only run this on machines you own or have explicit permission to test.

---


