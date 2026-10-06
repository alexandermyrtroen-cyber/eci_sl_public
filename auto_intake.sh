#!/bin/bash
SECTORS=("01_TRADE_FINANCE" "02_LOGISTICS" "03_AGRICULTURE" "04_TREASURY" "05_REAL_ESTATE" "06_SOLE_TRADERS" "07_PHILANTHROPY" "08_MUSIC")
for sector in "${SECTORS[@]}"; do
    echo "$sector" | python3 /home/alexander/ECI_NEXUS/projects/eci_sl_public/eci_intake.py --populate-workshops
done
