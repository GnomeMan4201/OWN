<p align="center">
  <img src=".github/branding/logo.png" alt="OWN" width="340"/>
</p>

# OWN

**Adaptive offensive framework — feedback-driven payload mutation, behavior-profile targeting, and multi-phase campaign execution.**

[![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](#)

---

OWN is a multi-phase offensive framework built around an adaptive mutation loop. It probes a target, captures behavioral responses, matches them against loaded profiles, and mutates its next payload accordingly — each phase informed by what the last one learned.

It does not fire fixed signatures. It reads the environment and adapts.

Built to integrate with the badBANANA ecosystem (Blackglass_Suite, zer0DAYSlater, Decoy-Hunter).

---

## How it works
```
probe target
    ↓
capture network response (dpkt)
    ↓
match against behavior profiles
    ↓
log redirects + behavioral signals
    ↓
adaptive_mutator — generate payloads from redirect paths
    ↓
neural_mutator + obfuscator_engine — mutate and obfuscate
    ↓
chimera_injector — fire to highest-value targets from memory_engine
    ↓
repeat
```

Each cycle tightens the payload to the specific environment. The memory engine maintains a ranked target list across runs.

---

## Architecture
```
OWN_PACKAGE/
├── own.sh                      campaign entry point (Termux-native)
├── phases/
│   ├── ai_loop.py              core loop — pcap capture + profile matching + action dispatch
│   ├── adaptive_mutator.py     redirect-log driven payload mutation
│   ├── adaptive_probe.py       environment-aware initial probing
│   ├── chimera_injector.py     multi-target payload delivery via memory_engine
│   ├── neural_mutator.py       neural-guided payload variant generation
│   ├── memory_engine.py        cross-run target ranking and state
│   ├── obfuscator_engine.py    HTTP-level payload obfuscation
│   ├── auto_escalator.py       privilege escalation automation
│   ├── backdoor_seed.py        persistence seeding
│   ├── covert_exfil.py         stealth data exfiltration
│   ├── decoy_generator.py      fake artifact generation
│   ├── dns_beacon.py           DNS-based C2 beacon
│   ├── dns_poisoner.py         DNS cache manipulation
│   ├── entropy_harvester.py    entropy-based evasion
│   ├── fingerprint_cloner.py   host fingerprint spoofing
│   ├── firewall_poison.py      firewall rule manipulation
│   ├── ghost_probe.py          stealthy host probing
│   └── honeynet_probe.py       decoy/honeypot detection
└── core/
    └── behavior_profiles.json  trigger → action mappings loaded by ai_loop
```

---

## Behavior profiles

The `ai_loop` loads `behavior_profiles.json` — a set of keyword triggers mapped to response actions. When captured traffic matches a trigger, the configured action fires: alert, inject, escalate, or custom handler. Profiles are swappable at runtime.

---

## Install
```bash
git clone https://github.com/GnomeMan4201/OWN.git
cd OWN
pip install -r requirements.txt
./quickstart.sh
```

Termux:
```bash
bash OWN_PACKAGE/own.sh
```

---

## Legal

For authorized security research and controlled lab environments only. Unauthorized use is prohibited.

---

*OWN // badBANANA research // GnomeMan4201*
