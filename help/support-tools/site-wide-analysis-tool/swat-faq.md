---
title: Adobe Commerce Site-Wide Analysis Tool Report FAQ
description: Learn about the Site-Wide Analysis Tool, a proactive self-service tool and central repository that includes detailed system insights and recommendations to ensure the security and operability of your Adobe Commerce installation.
exl-id: 7c843d55-9e2c-4b18-8859-0ebad0ae28cf
feature: "Best Practices, Saas, Support, Tools and External Services"
role: Admin
---
# Adobe Commerce Site-Wide Analysis Tool Report FAQ

This article provides a description of the Site-Wide Analysis Tool Report, generated automatically for Adobe Commerce on cloud infrastructure customers on a monthly or quarterly basis.

>[!NOTE]
>
>In Adobe Commerce on cloud infrastructure v2.4.1 and higher, Site-Wide Analysis Tool is available through the Commerce Admin Panel. Hence, Site-Wide Analysis Tool Reports can be run directly by the Customer. For access details, please refer to the [Site-Wide Analysis Tool guide](https://experienceleague.adobe.com/docs/commerce-operations/tools/site-wide-analysis-tool/access.html).

## What is Site-Wide Analysis Tool?

Site-Wide Analysis Tool is a SaaS application that performs end-to-end 'point-in-time' customer site analysis (within the Site-Wide Analysis Tool environment, not on the customer's site). All Site-Wide Analysis Tool-related customer site information is collected on predetermined schedules from every 3 hours to once a day. This means that Site-Wide Analysis Tool is constantly analyzing customer site data for findings.

## What is a Site-Wide Analysis Tool Report?

The Site-Wide Analysis Tool Report is a list of findings (issues) with self-service, best practice recommendations, that can be sent to customers in a PDF form through the Adobe Commerce support ticket system.

## What information is included in a Site-Wide Analysis Tool Report?

The site information, provided in the Site-Wide Analysis Tool report, includes:

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
 
## Who receives the automated monthly Site-Wide Analysis Tool reports?

Currently, those customers with a low Site-Wide Analysis Tool Health Index (at or below the currently set performance threshold), will receive a monthly Site-Wide Analysis Tool Report for their Production environment through the support ticket system.

## Who receives the automated quarterly Site-Wide Analysis Tool reports?

All customers, irrespective of the Site-Wide Analysis Tool Health Index, will receive a quarterly Site-Wide Analysis Tool Report for their Production environment through the support ticket system.

## How are Reports delivered?

Site-Wide Analysis Tool reports are delivered automatically via the Adobe Commerce support ticket system monthly or quarterly. Site-Wide Analysis Tool reports can also be generated manually from the Site-Wide Analysis Tool Dashboard and saved to your desktop. These Site-Wide Analysis Tool reports can then be emailed as attachments.
