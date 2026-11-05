# Full Page Navigation UI Test Plan

This document details the automated and manual verification suite for ProspectPulse, covering global page routing, dynamic pricing UI elements, payment gateway checkout experience, and post-purchase billing fulfillment.

---

## 1. Global Navigation & Page Routing

*   [x] **Cross-Page State Retention:** 
    *   *Path:* Navigate across `Overview (Home)` ➔ `AI SDR Agent` ➔ `Lead Lists` ➔ `Pipeline CRM`.
    *   *Verification:* Page transitions execute instantly in under 150ms. User state (e.g., active lead `novapay`, 50 imported CSV leads in `sample_leads_50.csv`, active Kanban stage positions, and active plan credentials) persists continuously without session drop or data loss.
*   [x] **Footer & Quick Links:** 
    *   *Path:* Click every quick link in the footer (`Privacy Policy`, `Terms of Service`, `Affiliate Program`, `Contact Support`).
    *   *Verification:* All links trigger dedicated responsive modals with zero 404 errors, providing full legal disclosures and support channels.
*   [x] **Breadcrumb Tracking:** 
    *   *Path:* Navigate deep into sub-modules (e.g., `Lead Lists` ➔ `Shopify Plus Scalebrands` or `AI SDR Agent` ➔ `Prospect Dossier`).
    *   *Verification:* Active breadcrumbs (`Lead Lists > Retail > Shopify Plus Scalebrands`) render dynamically, allowing one-click navigation back to parent categories.
*   [x] **Deep Linking Recovery:** 
    *   *Path:* Open direct hash URLs (`#view=crm`, `#modal=checkout&tier=agency`, `#view=agent&lead=retail`, `#modal=profile`).
    *   *Verification:* Application hash router directly restores the requested view and modal state on fresh page loads.

---

## 2. Dynamic Pricing Page UI Elements

*   [x] **Monthly / Annual Plan Toggle:** 
    *   *Path:* Flip subscription toggle between "Monthly" and "Annual" on the pricing grid.
    *   *Verification:* Instant price recalculation: Starter SDR updates from `$34/mo` to `$27/mo` (billed yearly), and Agency & Scale updates from `$99/mo` to `$79/mo` (billed yearly) with dynamic "Save 20%" badges.
*   [x] **Currency Switcher:** 
    *   *Path:* Toggle currency dropdown between `USD ($)`, `EUR (€)`, `GBP (£)`, and `INR (₹)`.
    *   *Verification:* Currency symbols and converted price tiers update globally across the landing page pricing cards and checkout order summaries.
*   [x] **Plan Selection Handshake:** 
    *   *Path:* Click "Start 7-Day Free Trial" on Starter SDR ($34/mo) vs. "Activate Agency Plan" on Agency & Scale ($99/mo).
    *   *Verification:* Checkout modal opens with the exact variant selected, matching tier badges, correct feature limits (300 vs 1,500 leads), and corresponding order summary values.

---

## 3. Payment Gateway & Checkout Experience

*   [x] **Stripe / Credit Card Form Validation:** 
    *   *Path:* Input incomplete card numbers (< 16 digits), expired dates, or invalid CVV codes.
    *   *Verification:* Real-time inline field validation highlights invalid inputs in red, displays contextual error notices, and disables the submit button until valid.
*   [x] **Alternative Payment Triggers:** 
    *   *Path:* Click alternative payment methods: `Google Pay`, `Apple Pay`, or `PayPal`.
    *   *Verification:* Initializes secure 1-click payment overlay with zero window freezing.
*   [x] **Promo / Coupon Code Box:** 
    *   *Path:* Enter valid promo code (e.g. `WELCOME10` or `PROSPECT20`) and click "Apply".
    *   *Verification:* Subtotal recalculates instantly with percentage discount applied and a green success notification. Invalid codes trigger an immediate "Invalid or expired promo code" alert.
*   [x] **Loading Spinners & Double-Click Protection:** 
    *   *Path:* Click "Activate Subscription / Start Trial".
    *   *Verification:* Submit button is immediately disabled (`pointer-events: none`), renders an animated loading spinner (`Authorizing Payment Method...`), and prevents duplicate requests.

---

## 4. Post-Purchase Fulfillment & Billing History

*   [x] **Success Page Redirect & Transaction Receipt:** 
    *   *Path:* Complete test transaction authorization.
    *   *Verification:* Modal transitions to a verified transaction receipt screen displaying unique Receipt ID (`INV-2026-XXXXX`), card on file (`Visa ending in 4242`), and direct `[Download Invoice PDF]` action.
*   [x] **Instant Tier Provisioning:** 
    *   *Path:* Inspect user header badges and profile modal immediately post-purchase.
    *   *Verification:* Header badges instantly switch to `Starter Pro ($34/mo) Active` / `Plan: Active`, and profile subscription changes to `Stripe Verified` with zero page reload required.
*   [x] **Invoice Matrix & Receipts:** 
    *   *Path:* Navigate to `Settings` ➔ `Billing & Invoices` drawer.
    *   *Verification:* A chronological billing table displays transaction date, plan description, amount charged, `Paid` status pill, and one-click PDF download triggers.
*   [x] **Subscription Management Controls:** 
    *   *Path:* Access `Manage Subscription` in the profile drawer.
    *   *Verification:* "Update Payment Method" and "Cancel Subscription" options are fully clickable, allowing plan changes or cancellation with instant confirmation.
