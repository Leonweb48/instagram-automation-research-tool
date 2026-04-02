# instagram-automation-research-tool
White-hat Instagram browser automation tool for cyber-security research (shared with Instagram Developers/Security team)
# Instagram Automation Research Tool (White-Hat)

**Purpose**: Demonstrate real-world browser-based automation risks on Instagram for cyber-security research.  
This tool will be shared directly with the Instagram Developers / Security team to help improve platform defenses.

## ⚠️ Ethical & Legal Warning
- This tool **violates Instagram’s Terms of Service**.
- Use **only** on accounts you own or have **explicit written permission** to test.
- Strictly for white-hat research and red-team demonstrations.

## Features
- Stealthy Playwright browser automation (human-like behavior, randomized fingerprints)
- Login, Like posts, Comment, Follow/Unfollow
- Rate limiting, proxy support, dry-run mode, detailed logging
- Multi-account support

## Setup & Run
1. `pip install -r requirements.txt`
2. `playwright install chromium`
3. Copy `.env.example` to `.env` and add your research credentials
4. Run commands: `python main.py login`, `python main.py like --post-url ...` etc.

## Recommendations for Instagram Security Team
- Detect via mouse entropy, typing cadence, scroll patterns, and action sequence anomalies.
- Enforce stronger device fingerprint binding and server-side rate limits.
- Increase challenge frequency for suspicious browser signatures.

Built for research purposes — April 2026.
