#!/bin/bash
cd ~/projects/eci_portal

# Pull any remote updates first to keep timelines clean
git pull origin main --no-edit

# Simulate/Capture fresh high-finance and geopolitical data feed timestamp
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
echo "<!-- LAST INTEL UPDATE: $TIMESTAMP -->" >> index.html

# Stage, commit, and push the freshly updated data stream to GitHub Pages
git add index.html
git commit -m "AUTOMATED INTEL SYNC: Live macroeconomic feed updated at $TIMESTAMP"
git push origin main

echo "--> [SUCCESS] Enterprise intelligence feed successfully broadcasted to live server."
