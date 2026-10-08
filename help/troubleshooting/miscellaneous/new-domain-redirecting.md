---
title: New domain is redirecting to default domain
description: This article provides a fix for the issue where the new domain redirects to the default domain in the existing or different environment.
exl-id: 88e9eb3f-9b82-4ca3-aa80-e49f360b3eb9
feature: Configuration
role: Developer
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: dac87252-6066-4d6e-a9d2-f6d84c323de7
    internal-label: Configuration
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# New domain is redirecting to default domain

This article provides a fix for the issue where the new domain redirects to the default domain in the existing or different environment.

## Affected products and versions

* Adobe Commerce on cloud pro infrastructure (all versions)

## Issue

The new domain is redirecting to the default domain in the current environment or the default domain of another environment.

## Cause

It happens when the Variables are not updated after adding a new domain or the wrong [!DNL Fastly] service has been configured in the environment.

## Solution

1. If the domain is redirecting within the same environment, make sure that you have configured the [Variables](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/configure-store/multiple-sites.html#modify-variables).
1. If the domain is redirecting to another environment, check whether you have configured the correct [!DNL Fastly] service by running the following command: `bin/magento fastly:conf:get -s`

>[!NOTE]
>
>You can find the [!DNL Fastly] API credentials by logging in to each environment (Staging/Production) and checking the `/mnt/shared/fastly_tokens.txt` file. For more information, see [configure [!DNL Fastly] services](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/cdn/setup-fastly/fastly-configuration.html) in the Commerce on Cloud Infrastructure Guide.

If both the above configurations are correct, submit a support ticket.

## Related reading

* [Checklist for setting up a new domain](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/how-to/checklist-for-setting-up-a-new-domain.html) in our support knowledge base.
