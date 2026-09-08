# ECI-SL SOVEREIGN EDGE: STANDARD OPERATING PROCEDURES (SOP)
**Project Root:** `~/ECI_NEXUS/projects/eci_sl_public/`
**Classification:** Air-Gapped / Zero-Cost Edge Architecture
**Aesthetic Baseline:** Institutional Luxury (Bone/Parchment #EAE6DF, Charcoal #2A2A2A, Gold #C5A861, Electric Blue #0070FF)

---

## 1. Local Server Management & Background Binding
To maintain an active local preview without blocking your terminal workflow, the Python HTTP server runs detached via background process management.

* **Start / Restart Server:**
    ```bash
    cd ~/ECI_NEXUS/projects/eci_sl_public
    fuser -k 8044/tcp 2>/dev/null
    nohup python3 -m http.server 8044 > server.log 2>&1 &
    ```
* **Access Local Preview:**
    Open browser at: `http://localhost:8044/index_light.html`

---

## 2. Visual Palette & Typography Standards
* **Background (Bone/Parchment):** `#EAE6DF` (Reduced glare, elite Swiss institutional tone).
* **Primary Text (Charcoal):** `#2A2A2A` (Maximum authority and legibility).
* **Dividers / Accents (Gold):** `#C5A861` (Structured layout separation).
* **Telemetry / Status (Electric Blue):** `#0070FF` / `#00F0FF` (Active LED indicators and hover states).
* **Typography:** 'Cinzel' (Sophisticated headers) paired with 'Inter' (Clean, calm body text).

---

## 3. Architecture & File Tree Hygiene
* `index_light.html`: The core public-facing static edge template (Home, Services, Macro Intercept Feed, Secure Intake Form).
* `server.log`: Execution and request logs for local diagnostics.
* `HOWTO_BOOKLET.md`: This exact procedure log, ensuring total continuity across sessions.

---

## 4. Zero-Cost Edge Deployment Protocol
When ready to push this local asset to the public web (Vercel / GitHub Pages) while keeping your proprietary backend (`localhost:8501`) air-gapped:
1. Initialize local git tracking: `git init && git add -A`
2. Commit stable state: `git commit -m "Deploy ECI-SL Sovereign Edge v1.0"`
3. Push to remote edge repository for instant global CDN propagation.

## 5. STRATEGIC DIRECTIVE: SEP 04, 2026 (Logged via AI Intercept)
* **Legal Posture:** ECI SL does NOT provide financial, trading, or legal "advice." We provide "Mathematical Verification" and "Algorithmic Telemetry." We are software architects, not licensed brokers.
* **SIAI Expansion:** Sovereign AI is for everyone. From agricultural yield prediction (fishermen, farmers) to creative IP management (music producers) to high-stakes trade finance. We create the need where it is unseen.
* **Multi-Vector DD:** Due Diligence scripts must be expanded into multiple specific variants (MT760, UCP600, SBLC, Contract Law, Corporate M&A).
* **Data Flow (A to B):** Raw Data (Public APIs / PDF ingest) -> Air-Gapped Local Linux Node (Validation/Processing) -> JSON/Markdown -> Public Edge (Vercel/GitHub Pages).

## 6. ARCHITECTURE EXPANSION: THE SECONDARY LAYER & INTAKE
* **The Arriver's Journey:** Home -> Legal Firewall -> Dual-Core Matrix (Institutional vs Universal SIAI) -> Secondary Sector Pages -> Intake/CIS.
* **Secondary Layer (Sub-pages):** Specific market matrices (e.g., SBLC, Agriculture, Music IP) will reside on secondary pages. These pages will host interactive data-entry fields and direct CIS (Client Information Sheet) downloads.
* **Intake Form Masking:** Public intake forms route to `hello.eci@outlook.com` using a hashed headless endpoint (e.g., Formsubmit). The raw email is NEVER exposed in the HTML source code.
* **CIS Integration:** Every service vector must have a downloadable, rigorously structured CIS PDF or Markdown equivalent.

## 7. SESSION STOP & RESUME PROTOCOL
When terminating a session, the operator will issue this command to the AI:
**"INITIATE SESSION STOP. Summarize current architectural state, file tree, and locked directives. Generate the exact prompt I must paste upon return to seamlessly resume ECI-SL development."**

## 8. PERSISTENT LOCAL DAEMON (systemd)
* **Objective:** Make `http://localhost:8044` permanently bookmarkable across reboots.
* **Mechanism:** A user-level systemd service (`ecisl-public.service`) forces the Linux kernel to automatically launch the Python HTTP server on boot.
* **Commands:**
  * Check status: `systemctl --user status ecisl-public.service`
  * Stop server: `systemctl --user stop ecisl-public.service`
  * Restart server: `systemctl --user restart ecisl-public.service`

## 9. SECONDARY LAYER EXPANSION (SEP 05, 2026)
* **Matrix 01:** Trade Finance (`matrix_trade_finance.html`)
* **Matrix 02:** Agriculture & Resources (`matrix_agriculture.html`)
* **Matrix 03:** Music IP & Creators (`matrix_music_ip.html`)
* **Matrix 04:** Sole Traders & Startups (`matrix_sole_traders.html`)

## 9. SECONDARY LAYER EXPANSION (SEP 05, 2026)
* **Matrix 01:** Trade Finance (`matrix_trade_finance.html`)
* **Matrix 02:** Agriculture & Resources (`matrix_agriculture.html`)
* **Matrix 03:** Music IP & Creators (`matrix_music_ip.html`)
* **Matrix 04:** Sole Traders & Startups (`matrix_sole_traders.html`)
* **Matrix 05:** Logistics & Freight Forwarding (`matrix_logistics.html`)
* **Matrix 06:** Commercial Real Estate (`matrix_real_estate.html`)
* **Matrix 07:** Corporate Treasury (`matrix_treasury.html`)
* **Matrix 08:** Philanthropy & Trusts (`matrix_philanthropy.html`)

**STATUS:** All 8 primary market sector matrices successfully compiled, styled, and logged.

## 10. MASTER INDEX ARCHITECTURE (TWO-TIERED TACTICAL GRID)
* **Core Philosophy Shift:** Explicitly reframed ECI SL away from "number crunching" to "multi-domain text, legal, and operational intelligence."
* **Tier 1:** Dominant institutional anchor for Core A (Trade Finance / Capital Structuring).
* **Tier 2:** Clean 7-sector micro-grid for Core B (Agriculture, Music IP, Sole Traders, Logistics, Real Estate, Treasury, Philanthropy).
* **Routing:** All 8 sector cards link directly to their respective secondary nodes (`matrix_*.html`).
* **Operator's Guide:** Compiled `guide.html` detailing the 4-phase engagement protocol.

## 11. THE 1505 CERTAINTY ENGINE & BRANDING (SEP 05, 2026)
* **Backend Logic:** Created `eci_engine.py` to execute deterministic structural verification, rule parsing, and cryptographic hash generation for sector payloads.
* **Branding:** Upgrading visual hierarchy with SVG insignia crests and unified iconography across all nodes.
* **Streamlit Control Panel:** Created `eci_dashboard.py` for administrative case handling, payload ingestion, and live certainty verification.
