#!/usr/bin/env python3
import sys
import json
import os
from eci_engine import verify_structural_integrity

def write_certificate(sector_code, payload_data, report):
    cert_filename = f"certificate_{sector_code.lower()}_{report['certainty_signature'][:8]}.html"
    cert_path = os.path.join("/home/alexander/ECI_NEXUS/projects/eci_sl_public", cert_filename)
    
    # 1. The exact ECI SL Vector Emblem injected into the document header
    crest_svg = '<svg class="w-12 h-12 text-[#C5A861] inline-block mr-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>'
    
    # 2. The explicit Sub-matrix findings dynamically printed line-by-line
    sub_rules_html = "".join([f'<li class="border-b border-[#333333] py-2 text-cyan-400 font-bold">> STRUCTURAL SUB-RULE [{rule}] : VERIFIED</li>' for rule in report['rules_evaluated']])

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ECI SL | Cryptographic Certificate of Certainty</title>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700&family=Inter:wght@300;400;600&family=JetBrains+Mono&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-[#0a0a0a] text-[#EAE6DF] font-sans antialiased p-12">
    <div class="max-w-4xl mx-auto bg-[#111111] p-12 border border-[#C5A861] shadow-2xl relative">
        
        <!-- INSTITUTIONAL BRANDING HEADER -->
        <div class="flex justify-between items-start border-b border-[#333333] pb-6 mb-8">
            <div class="flex items-center">
                {crest_svg}
                <div>
                    <h1 class="font-serif text-4xl font-bold tracking-widest text-[#EAE6DF]">ECI SL</h1>
                    <p class="font-mono text-xs text-[#C5A861] uppercase tracking-wider mt-1">Sovereign Intelligence & Certainty Engine</p>
                </div>
            </div>
            <div class="text-right font-mono text-xs text-[#0070FF]">
                <p class="font-bold tracking-widest border border-[#0070FF] px-2 py-1 inline-block mb-2 bg-[#0070FF]/10">STATUS: MATHEMATICALLY CERTAIN</p>
                <p class="text-gray-400">{report['timestamp']}</p>
            </div>
        </div>

        <!-- INGESTED PAYLOAD DATA -->
        <div class="grid grid-cols-2 gap-8 mb-8 font-light text-sm text-[#CCCCCC]">
            <div>
                <span class="font-mono text-[10px] uppercase tracking-widest text-[#C5A861]">Sector Matrix</span>
                <p class="font-serif font-semibold text-xl mt-1 text-white">{report['sector']}</p>
            </div>
            <div>
                <span class="font-mono text-[10px] uppercase tracking-widest text-[#C5A861]">Entity Payload</span>
                <p class="font-mono text-[11px] mt-1 bg-black p-3 border border-[#333333] break-all">{payload_data}</p>
            </div>
        </div>

        <!-- FINDINGS & SUB-MATRICES -->
        <div class="mb-8">
            <span class="font-mono text-[10px] uppercase tracking-widest text-[#C5A861] mb-2 block">Findings & Sub-Matrix Parsing</span>
            <div class="bg-black p-5 border border-[#333333] font-mono text-[11px]">
                <p class="text-gray-500 mb-3">// Executing deterministic evaluation across sub-matrices...</p>
                <ul class="space-y-1">
                    {sub_rules_html}
                </ul>
            </div>
        </div>

        <!-- SHA-256 CRYPTOGRAPHIC PROOF -->
        <div>
            <span class="font-mono text-[10px] uppercase tracking-widest text-[#C5A861] mb-2 block">Cryptographic Signature (SHA-256)</span>
            <p class="font-mono text-xs mt-1 text-[#0070FF] break-all bg-black border border-[#333333] p-4 text-center">{report['certainty_signature']}</p>
        </div>

        <!-- ENFORCEMENT DECLARATION -->
        <div class="pt-6 mt-10 border-t border-[#333333] text-[9px] text-gray-500 font-mono text-center uppercase tracking-widest">
            {report['declarative_posture']} | Air-Gapped Verification: Ubuntu Acer ECI-muscle
        </div>
    </div>
</body>
</html>
"""
    with open(cert_path, "w", encoding="utf-8") as cf:
        cf.write(html_content)
    return cert_filename

print("\n\033[33m[ ECI SL // TERMINAL COMMAND CONSOLE ]\033[0m")
print("------------------------------------------")

sector = input("Enter Sector Code (e.g., 01_TRADE_FINANCE): ").strip().upper()
entity = input("Enter Principal Entity Name: ").strip()
payload_val = input("Enter Declared Metric (e.g., €45M MT760, 1000 Hectares): ").strip()

payload_data = {"entity": entity, "declared_metric": payload_val, "node": "Ubuntu Acer ECI-muscle"}

print("\n[!] INGESTING PAYLOAD AND EXECUTING DETERMINISTIC AUDIT...")
report = verify_structural_integrity(sector, payload_data)

if report['status'] == 'MATHEMATICALLY_CERTAIN':
    cert_file = write_certificate(sector, json.dumps(payload_data), report)
    print(f"\n\033[32m[PASS] Mathematical Certainty Achieved.\033[0m")
    print(f"\033[36m[SUCCESS] Institutional certificate compiled: {cert_file}\033[0m\n")
else:
    print("\n\033[31m[FAIL] Structural integrity compromised. Reject payload.\033[0m\n")
