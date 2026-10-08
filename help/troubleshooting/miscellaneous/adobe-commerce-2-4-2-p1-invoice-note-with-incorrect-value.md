---
title: 'Adobe Commerce 2.4.2-p1: invoice note with an incorrect value'
description: This article describes a known Adobe Commerce 2.4.2-p1 issue where an invoice note with incorrect value is generated when the customer group is changed while creating the order. This issue is fixed in version 2.4.3.
exl-id: bde90251-625f-4c9d-8e5a-9a2019656125
feature: Customer Service, Invoices
role: Developer
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: 591c578b-908e-5b79-a9d3-931dfe60c24c
    internal-label: Invoices
  - id: da76473c-f99b-5ad0-9b14-896aed473f8a
    internal-label: Services
subfeature_v2:
  - id: deedbb4d-f1b7-58ea-a34a-de1f481f9d4c
    internal-label: Customer Service
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Adobe Commerce 2.4.2-p1: invoice note with an incorrect value

This article describes a known Adobe Commerce 2.4.2-p1 issue where an invoice note with incorrect value is generated when the customer group is changed while creating the order. This issue is fixed in version 2.4.3.

## Affected products and versions

* Adobe Commerce on-premises 2.4.2-p1
* Adobe Commerce on cloud infrastructure 2.4.2-p1

## Issue

When the customer group is changed at the time of creating the order, the invoice is generated with an incorrect invoice note.

<u>Steps to reproduce</u>:

1. Create a **Test Customer Account** and add it to the **Retail Customer Group**.
1. Create a **New Order** for the test customer, add **Product** and **Address**.
1. Select **Shipping Method**.
1. In the **Account Information** section, change customer group from **Retailer** to **Government**.
1. Click **Place Order**.
1. Click **Invoice** > **Submit Invoice**.

<u>Expected results</u>:

The following note should appear under the **Notes for this order**  section: "Vertex Invoice sent successfully. Amount: $0.00."

<u>Actual results</u>:

The following note appears under the **Notes for this order** section: "Vertex Invoice sent successfully. Amount: $3.23."

## Solution

This issue is fixed in version 2.4.3.
