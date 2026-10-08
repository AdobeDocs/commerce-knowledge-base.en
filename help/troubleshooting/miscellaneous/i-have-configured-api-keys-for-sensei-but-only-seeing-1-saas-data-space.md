---
title: Unable to see multiple SaaS data spaces after configuring Adobe AI API keys
description: This article provides a solution for the issues where you only see one SaaS data space after you have configured the API keys for Adobe AI.
exl-id: e13041da-b122-4684-8287-42132931f47a
feature: REST, Saas, Observability
role: Developer
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: d3b92bef-63fa-5031-a925-d04d9362d616
    internal-label: Saas
  - id: 4239b8a6-e74f-567d-a7a5-b98b9ead0ea4
    internal-label: Observability
  - id: c4f010fa-1478-4300-a88d-706fbc036a7a
    internal-label: APIs and SDKs
subfeature_v2:
  - id: e0ca0e7a-9738-48d1-b98b-615468ab4aaf
    internal-label: REST API
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Unable to see multiple SaaS data spaces after configuring Adobe AI API keys

After configuring API keys for a Commerce service such as Adobe AI services (Product Recommendations or Live Search) or Payment Services for Adobe Commerce, you expect to see multiple SaaS data spaces in the Commerce Services Connector. Depending on product entitlement and deployment type, the connector displays only one SaaS data space, which is expected behavior.

## Affected products and versions

* Adobe Commerce (all deployment methods): all versions
* Magento Open Source: all versions
* Extension or technology (Fastly, New Relic, etc.), Adobe AI (Product Recommendations/Live Search)

## Issue

After configuring the Adobe AI API keys, the system shows only one SaaS data space.

## Cause

The number of available SaaS data spaces depends on the product entitlement tied to the Commerce account and the type of service being used.

## Solution

In general, the number of available SaaS data spaces depends on the Commerce license:

* Adobe Commerce: one production data space and two testing data spaces
* Magento Open Source: one production data space and no testing data spaces

For Payment Services, the default behavior is:

* Payment Services on Adobe Commerce (*Cloud or on-premises*) has three data spaces by default:
 * one production data space
 * two testing data spaces
* Payment Services on Magento Open Source has one data space by default

Customers who own multiple Cloud projects or on-premises (*live/production*) installations can also request additional production and testing data spaces for each project or instance by submitting a Support request.

Magento Open Source customers using Adobe Payment Services can also request an additional data space. Contact the Payments team for prior approval before submitting a Support request to add a testing data space.

>[!NOTE]
> * Do not use the same SaaS data space across multiple environments at the same time. If a production or testing data space is reused across environments, data can become mixed and may require cleanup.
> * Payment Services on Adobe Commerce (*Cloud/On‑Prem*) have three data spaces by default.
> * Payment Services on Magento Open Source have one data space by default.
> To request additional data spaces:
> * Magento Open Source customers using Adobe Payment Services can request an additional data space. Contact the Payments team for prior approval before submitting a Support request to obtain a testing data space.
> * Customers who own multiple Cloud projects or on‑premises (*live/production*) installations can also request additional production and testing data spaces for each project or instance by submitting a Support request.

## Realeted reading

[SaaS data space provisioning](https://experienceleague.adobe.com/en/docs/commerce/user-guides/integration-services/saas?lang=en#saas-data-space-provisioning)
