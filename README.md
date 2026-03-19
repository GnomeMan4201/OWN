<p align="center">
  <img src=".github/branding/logo.png" alt="OWN" width="340"/>
</p>

# OWN

**Autonomous offensive framework — adaptive mutation, covert C2, and multi-phase payload delivery.**

[![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](#)

---

OWN is a modular offensive research framework built around an AI-driven mutation loop. It runs multi-phase campaigns that adapt based on environmental feedback — probing, mutating, persisting, and exfiltrating without fixed signatures.

Built to integrate with the badBANANA ecosystem (Blackglass_Suite, zer0DAYSlater, Decoy-Hunter).

---

## Architecture
```
OWN_PACKAGE/phases/
  adaptive_mutator.py     payload mutation with feedback loop
  adaptive_probe.py       environment-aware probing
  ai_loop.py              core AI-driven campaign controller
  auto_escalator.py       privilege escalation automation
  backdoor_seed.py        persistence seeding
  chimera_injector.py     multi-vector payload injector
  covert_exfil.py         stealth data exfiltration
  decoy_generator.py      fake artifact generation
  dns_beacon.py           DNS-based C2 beacon
  dns_poisoner.py         DNS cache manipulation
  entropy_harvester.py    entropy-based evasion
  fingerprint_cloner.py   host fingerprint spoofing
  firewall_poison.py      firewall rule manipulation
  ghost_probe.py          stealthy host probing
  honeynet_probe.py       decoy/honeypot detection
  neural_mutator.py       neural-guided payload mutation
```

---

## Install
```bash
git clone https://github.com/GnomeMan4201/OWN.git
cd OWN
pip install -r requirements.txt
./quickstart.sh
```

---

## Legal

For authorized security research and controlled lab environments only. Unauthorized use is prohibited.

---

*OWN // badBANANA research // GnomeMan4201*
