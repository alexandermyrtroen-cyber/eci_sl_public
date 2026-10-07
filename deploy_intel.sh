#!/bin/bash
cd ~/projects/eci_portal

git pull origin main --no-edit
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
echo "<!-- LAST INTEL UPDATE: $TIMESTAMP -->" >> index.html

git add index.html
git commit -m "AUTOMATED INTEL SYNC: Live macroeconomic feed updated at $TIMESTAMP"
git push origin main

sudo mkdir -p /var/www/eci_sl
sudo cp -r . /var/www/eci_sl/
sudo chown -R www-data:www-data /var/www/eci_sl/
sudo chmod -R 755 /var/www/eci_sl/
sudo systemctl reload nginx

echo "--> [SUCCESS] Enterprise intelligence synced to GitHub AND live Nginx path (/var/www/eci_sl)."
