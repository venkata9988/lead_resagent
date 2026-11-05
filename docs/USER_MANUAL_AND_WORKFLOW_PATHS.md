# ProspectPulse: Complete Operational Guide & End-to-End Workflow Paths

This manual traces every user path through **ProspectPulse**, detailing the exact clicks, state changes, and automated agent behaviors across all four views and five interactive modals.

---

## Architecture Overview & Navigation Map

```
                  ┌─────────────────────────────────────────┐
                  │          ProspectPulse Header           │
                  │  [Logo] [Overview] [Agent] [Lists] [CRM]│
                  │  [n8n Export]  [Plan Badge]  [VS Profile]│
                  └────────────────────┬────────────────────┘
                                       │
         ┌──────────────────┬──────────┴──────────┬──────────────────┐
         ▼                  ▼                     ▼                  ▼
┌─────────────────┐ ┌───────────────┐ ┌─────────────────┐ ┌─────────────────┐
│ View 1:         │ │ View 2:       │ │ View 3:         │ │ View 4:         │
│ Overview &      │ │ AI SDR Agent  │ │ Lead Lists &    │ │ Sales Pipeline  │
│ Pricing Plans   │ │ Workspace     │ │ Target Segments │ │ Kanban CRM      │
└─────────────────┘ └───────────────┘ └─────────────────┘ └─────────────────┘
```

---

## Path 1: Public Marketing & Subscription Activation

### Step 1: Navigating to the Platform
- **Action**: Open `src/frontend/index.html` in any modern web browser or click the top logo **"ProspectPulse"** / **"Overview"** tab.
- **Expected Result**: Displays the main landing page highlighting the headline: *"Replace a $50,000/yr SDR with an Autonomous AI Sales Agent"*.

### Step 2: Plan Selection & Checkout
1. Scroll down to the **Transparent Pricing** section or click **"Upgrade: $34/mo"** in the top navigation bar.
2. Select either:
   - **Starter SDR ($34/mo)**: Click **"Start 7-Day Free Trial"**.
   - **Agency & Scale ($99/mo)**: Click **"Activate Agency Plan"**.
3. **Modal Opens**: The **Checkout Modal** appears with pre-filled fields for Work Email and Agency Name.
4. **Billing Toggle**: Click **"Annual (Save 20%)"** or **"Monthly Billing"**.
5. Click **"Activate Free Trial Now"**:
   - The modal closes.
   - The header plan badge updates to `Starter Pro ($34/mo) Active` or `Agency Plan Active`.
   - The view automatically transitions to the **AI SDR Agent Workspace**.

---

## Path 2: Administrator Profile & System Health Verification

- **Action**: Click the circular **"VS"** avatar badge located in the top-right corner of the header.
- **Expected Result**:
  - The **Profile & Workspace Drawer** opens.
  - Displays Administrator Name (**Venkata Siva**), active plan tier, and credits used (**284 / 300 Leads**).
  - Confirms system status: **FastAPI Agent Backend (Port 8000 OK)** and **n8n Webhook Sync (Connected)**.
  - Provides a direct link to the GitHub repository: `https://github.com/venkata9988/lead_resagent`.
  - Click **"Manage Subscription"** to change plans, or **"Close"** to dismiss.

---

## Path 3: Autonomous AI Reconnaissance (SDR Studio)

### Path 3A: Selecting Pre-Loaded Industry Accounts
1. Navigate to the **"AI SDR Agent"** tab.
2. In the **Prospect Review Queue** on the left, click any target company:
   - **Acme Health Partners** (Healthcare • Series B Urgent Care expansion)
   - **NovaPay Solutions** (FinTech • ISO 20022 compliance migration)
   - **Kestrel Outdoor Goods** (Retail • 3,000 SKU headless commerce surge)
   - **Aether Telecom Systems** (Middleware • Apache Kafka event streaming)
3. **Expected State**:
   - The selected card receives a green border (`border-2 border-emerald-500`).
   - The search inputs at the top automatically sync to that company's domain, contact name, and role.
   - The right-hand pane loads the **Executive Research Dossier**:
     * Grounding Score (e.g. `98 / 100 PASS`).
     * Detected Buying Trigger description.
     * Detected Tech Stack chips (e.g. *Stripe, PostgreSQL, MuleSoft, AWS Cloud*).
     * Personalized **LinkedIn Connection Note** (<250 characters) with a working **"Copy"** button.
     * Non-cliché **Cold Email Sequence** (<85 words) with subject line and a working **"Copy"** button.

### Path 3B: Running Recon on a Custom Domain
1. In the top search bar, enter any custom domain (e.g. `biohealthsystems.com`), a contact name, and select a sector.
2. Click the green button **"Run Autonomous Recon"**:
   - The button pulses: `Analyzing Signals...` ➔ `Recon Complete`.
   - A fresh, custom dossier is generated and added to the review queue without reverting to default leads.

### Path 3C: Approving & Dispatching Outreach
1. Review the generated LinkedIn note and email draft.
2. Click the green button **"Approve & Dispatch"**:
   - The button changes to a confirmed state: `Dispatched to Staging Queue`.
   - The badge in the left queue updates to **`Dispatched ✓`** with an emerald border.
   - The account is automatically synced to **Stage 3 (Contacted)** in the Pipeline CRM.

### Path 3D: Moving Directly to CRM
1. Click **"Move to Pipeline CRM"**:
   - If the account is already in the pipeline, it alerts you of its current stage.
   - If new, it registers the deal into **Stage 2: AI Enriched**.
   - Transitions directly to the **Pipeline CRM** board.

---

## Path 4: Lead Lists, CSV Ingestion & Bulk Operations

### Path 4A: Exploring Pre-Configured Target Segments
1. Navigate to the **"Lead Lists"** tab.
2. Click any of the three pre-built segment cards:
   - **Healthcare**: Urgent Care & Regional Clinics (42 Leads)
   - **FinTech**: Payment Rails & ISO 20022 (28 Leads)
   - **Retail**: Shopify Plus Scalebrands (65 Leads)
3. **Expected State**:
   - Smoothly scrolls to the **Prospects Table** below.
   - Displays real contacts with buying signals and tech stacks.
4. **Action per Row**:
   - Click **"Run AI Recon ➔"** on any row (e.g. *Rachel Adams* or *Julian Scott*).
   - Instantly jumps into the **AI SDR Workspace**, adds that contact to the left queue, and generates their personalized pitch.

### Path 4B: Bulk AI Scraping & Enrichment
1. With any segment active in the table, click the top button **"Enrich Entire List"**.
2. **Expected State**:
   - The button shows a progress spinner: `AI Scraping Accounts...`.
   - All rows in the table update their status badges to `100% Enriched ✓`.
   - A notification toast confirms that all accounts are grounded and ready for outreach.

### Path 4C: Importing Custom CSV Datasets
1. Click the white button **"Import CSV"** at the top right of the Lead Lists view.
2. In the modal:
   - **Option 1**: Drag and drop or browse to select `sample_leads_50.csv`.
   - **Option 2**: Click the green button **"Load 50 Leads"** for instant demo data.
3. **Expected State**:
   - The modal closes.
   - A new segment card appears in the grid: **`sample_leads_50.csv (50 Leads)`**.
   - The table populates with all 50 prospects.
   - All data is saved in `localStorage`, persisting even if you switch tabs or refresh the page.

### Path 4D: Creating a Custom Target Segment
1. Click the green button **"Create New List"**.
2. Enter:
   - **Segment Name**: e.g. *Q4 Enterprise Cloud Infrastructure*
   - **Industry Sector**: e.g. *Middleware & Enterprise IT*
   - **Primary Buying Trigger**: e.g. *Kafka event streaming migration*
3. Click **"Save Segment"**:
   - A new card is prepended into the top grid with a purple border and animated indicator.
   - The table below populates with targeted Enterprise IT accounts.

---

## Path 5: Outbound Sales Pipeline & CRM Board

### Path 5A: Advancing Deals Across the 5 Kanban Stages
1. Navigate to the **"Pipeline CRM"** tab.
2. Review the 5 balanced columns:
   - **1. Discovered**
   - **2. AI Enriched**
   - **3. Contacted**
   - **4. Meeting Booked**
   - **5. Closed Won**
3. **Advancing Deals**:
   - Click **"Advance ➔"** on Apex Logistics in Column 1 ➔ Moves to Column 2 (*AI Enriched*).
   - Click **"Advance ➔"** on NovaPay Solutions in Column 2 ➔ Moves to Column 3 (*Contacted*).
   - Click **"Advance ➔"** on Acme Health Partners in Column 3 ➔ Moves to Column 4 (*Meeting Booked*).
   - Click **"Close Deal ➔"** on Kestrel Outdoor Goods in Column 4 ➔ Moves to Column 5 (*Closed Won*) with a **Won ✓** badge.
4. **Live Metrics**:
   - Column counter badges update dynamically.
   - **Total Pipeline ($)** and **Active Meetings Booked** recalculate automatically.

### Path 5B: Inspecting Closed Deals & Winning Pitch Formulas
1. In Column 5 (*Closed Won*):
   - **Direct 1-Click Jump**: Click directly on the purple **"Won ✓"** badge or **"Signed via Agent Pitch"** pill to jump straight into the AI SDR Workspace with that company's dossier loaded.
   - **Detailed Deal Inspector**: Click the body of the card to open the **Deal & Pitch Inspector Modal**:
     * Shows annual contract value (e.g. `$45,000 / yr`).
     * Displays detected tech stack chips.
     * Previews the winning pitch formula that closed the deal.
     * Click **"Open Full Dossier in Studio ➔"** to jump into the full workspace.

### Path 5C: Adding a Manual Deal
1. Click the green button **"+ Add Deal"** at the top right of the CRM board.
2. Enter Company Name, Target Contact, Deal Value ($), Stage, and Trigger note.
3. Click **"Create Deal"**:
   - The card appears in the selected column immediately.
   - The **Total Pipeline** dollar total increases accordingly.

---

## Path 6: External CRM & Webhook Dispatch (n8n / Zapier)

1. Click **"n8n Export"** in the top navigation bar.
2. The **Webhook Export Modal** opens with:
   - Default webhook URL: `https://n8n.yourdomain.com/webhook/lead-intake`
   - Pre-formatted JSON payload matching the Pydantic `NormalizedLeadSignal` schema.
3. Click **"Send Payload"**:
   - Simulates live HTTP POST dispatch.
   - Displays confirmation: `Sent to n8n!`.
   - Shows a notification toast confirming the payload was delivered.
