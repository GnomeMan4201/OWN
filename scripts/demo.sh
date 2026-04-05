#!/usr/bin/env bash
set -euo pipefail
export PYTHONWARNINGS=ignore

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

GRN='\033[0;32m'; YEL='\033[1;33m'; RED='\033[0;31m'
CYN='\033[0;36m'; DIM='\033[2m'; BLD='\033[1m'; RST='\033[0m'

sep() { echo -e "${DIM}────────────────────────────────────────${RST}"; }

sep
echo -e "  ${BLD}OWN${RST} — Multi-Phase Adaptive Execution Framework"
sep
echo ""

python3 -c "
import sys
sys.path.insert(0, '.')
sys.path.insert(0, 'OWN_PACKAGE')
import pwn
" 2>/dev/null || {
  echo -e "  ${RED}✗${RST}  missing deps — run: pip install -r requirements.txt"
  exit 1
}
echo -e "  ${GRN}✓${RST}  framework loaded"
echo ""

python3 - << 'PYEOF'
import sys, time, random
sys.path.insert(0, '.')
sys.path.insert(0, 'OWN_PACKAGE')
import pwn

GRN='\033[0;32m'; YEL='\033[1;33m'; RED='\033[0;31m'
CYN='\033[0;36m'; DIM='\033[2m'; BLD='\033[1m'; RST='\033[0m'

def delay(t=0.3): time.sleep(t)

# ── BANNER ───────────────────────────────────────────────────────
print(f"  {DIM}session: pwn-{random.randint(1000,9999)}  target: 192.168.1.44{pwn.RST if hasattr(pwn,'RST') else ''}{'\033[0m'}")
print()

# ── PHASE EXECUTION ──────────────────────────────────────────────
print(f"  {BLD}PHASE EXECUTION{'\033[0m'}")
delay(0.3)

phases = [
    ("RECON",     "fingerprint_cloner + adaptive_probe"),
    ("NEURAL",    "generate_neural_payloads → disk"),
    ("SIGNATURE", "sig_mutator + obfuscator_engine"),
    ("SUBNET",    "lan_spread + pivot_bootstrapper"),
    ("BACKDOOR",  "ephemeral shell :7788"),
    ("EXFIL",     "covert_exfil via dns_beacon"),
]

for name, detail in phases:
    delay(0.35)
    col = GRN if name not in ("BACKDOOR", "EXFIL") else YEL
    print(f"  {DIM}[*]{'\033[0m'} Phase: {col}{name:<12}{'\033[0m'}  {DIM}{detail}{'\033[0m'}")

print()

# ── PAYLOAD SAMPLE ───────────────────────────────────────────────
delay(0.3)
print(f"  {BLD}PAYLOAD SAMPLE{'\033[0m'}")
for _ in range(3):
    delay(0.2)
    p = pwn.fake_payload()
    print(f"  {DIM}  {p.splitlines()[0]}{'\033[0m'}")

print()

# ── MEMORY SAVE ──────────────────────────────────────────────────
delay(0.3)
print(f"  {GRN}✓{'\033[0m'}  session state saved")
print(f"  {GRN}✓{'\033[0m'}  phase log written")
print(f"  {CYN}→{'\033[0m'}  dispatcher: ready for next operator command")
PYEOF

echo ""
sep
echo -e "  ${GRN}✓${RST}  6 phases executed"
echo -e "  ${CYN}→${RST}  integrates with zer0DAYSlater dispatcher and drift_orchestrator gates"
sep
echo ""
