---
title: 'Adobe Commerce Site-Wide Analysis Tool Report FAQ'
description: Learn about the Site-Wide Analysis Tool, a proactive self-service tool and central repository that includes detailed system insights and recommendations to ensure the security and operability of your Adobe Commerce installation.
---

This article provides a description of the Site-Wide Analysis Tool (SWAT) Report, generated automatically for Adobe Commerce on cloud infrastructure customers on a monthly or quarterly basis.

Note: In Adobe Commerce on cloud infrastructure v2.4.1 and higher, SWAT is available through the Commerce Admin Panel. Hence, SWAT Reports can be run directly by the Customer. For access details, please refer to the [Site-Wide Analysis Tool guide](https://experienceleague.adobe.com/docs/commerce-operations/tools/site-wide-analysis-tool/access.html).

## What is SWAT?

SWAT is a SaaS application that performs end-to-end 'point-in-time' customer site analysis (within the SWAT environment, not on the customer's site). All SWAT-related customer site information is collected on predetermined schedules from every 3 hours to once a day. This means that SWAT is constantly analyzing customer site data for Findings.

## What is a SWAT Report?

The SWAT Report is a list of findings (Issues) with self-service, best practice recommendations, that can be sent to customers in a PDF form through the Adobe Commerce support ticket system.

## What information in included in a SWAT Report?

The site information, provided in the SWAT report, includes:

* Finding
* Overview, including a ‘Priority’ for order of implementation fix
* Finding Description
* Pre-condition(s), if any
* Site Impact(s)
* Root Cause(s)
* Recommendation(s)
* Exception logs
* Log exception info
* Date of last occurrence
* Number of times the exception occurs
* Who receives the automated monthly SWAT reports?

Currently, those customers with a low SWAT Health Index (at or below the currently set performance threshold), will receive a monthly SWAT Report for their Production environment through the support ticket system.

## Who receives the automated quarterly SWAT reports?

All customers, irrespective of the SWAT Health Index, will receive a quarterly SWAT Report for their Production environment through the support ticket system.

## How are Reports delivered?

SWAT reports are delivered automatically via the Adobe Commerce support ticket system either monthly or quarterly. SWAT reports can also be generated manually from the SWAT Dashboard and saved to your desktop. These SWAT reports can then be emailed as attachments.
