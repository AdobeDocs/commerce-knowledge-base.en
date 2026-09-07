---
title: Security update available for Adobe Commerce - APSB26-146
description: Adobe has released Security Bulletin APSB26-146 addressing CVE-2026-75650, a zero-day vulnerability in Adobe Commerce. Learn how to apply the hotfix and rotate credentials.
autotag-review: '2026-09-07T17:27:44.037Z'
TQID: 'https://experienceleague.adobe.com/ADVRRn85--ZgWtPdi4qA49fsDPVW976N4MYWp26taho'
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: ba9e5be9-7de1-4f71-a5d2-baead0e425ee
    internal-label: Security
  - id: bd989d82-1e15-4534-88db-f1f51dd77ffa
    internal-label: Accounts
  - id: c32adafa-ed01-4b31-997e-2413013911b0
    internal-label: Integrations
topic_v2:
  - id: d095671a-1355-40aa-8b5f-06c33c68080b
    internal-label: Security
---

# Security update available for Adobe Commerce - APSB26-146

>[!IMPORTANT]
>
>This is an urgent update related to CVE-2026-75650. Adobe is aware that CVE-2026-75650 has been exploited in the wild targeting Adobe Commerce merchants.

On September 5, 2026, Adobe became aware, through an independent security researcher, of a zero-day vulnerability in Adobe Commerce that could allow an unauthenticated attacker to execute arbitrary code on an affected installation (CVE-2026-75650).

Adobe has released Security Bulletin APSB26-146, which addresses this vulnerability. The bulletin is available here:

<https://helpx.adobe.com/security/products/magento/apsb26-146.html>

In this article you will find how to implement the hotfix for this issue for the current and earlier versions of Adobe Commerce and Magento Open Source.

## Description

Affected products and versions:

* 2.4.9-2026-aug and earlier
* 2.4.8-2026-aug and earlier
* 2.4.7-2026-aug and earlier
* 2.4.6-2026-aug and earlier
* 2.4.5-2026-aug and earlier
* 2.4.4-2026-aug and earlier

## Resolution

### Solution for Adobe Commerce on Cloud, Adobe Commerce on-premise, and Magento Open Source

To help resolve the vulnerability for the affected products and versions, you must apply the VULN-39341 patch (dependent on your version) and rotate your encryption keys.

### Hotfix details

Apply the following hotfix to the affected product version:

* [Download the Hotfix VULN-39341-composer-patches.zip](https://repo.magento.com/patch/VULN-39341-composer-patches.zip)

### How to apply the hotfix

Unzip the file and see [How to apply a composer patch provided by Adobe](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/how-to/how-to-apply-a-composer-patch-provided-by-magento) in our support knowledge base for instructions.

### For Adobe Commerce on Cloud merchants only - how to tell whether patches have been applied

Considering that it isn't possible to easily determine if the issue was patched, it's recommended that you check whether the CVE-2026-75650 hotfix has been successfully applied.

You can do this by taking the following steps, using the file `VULN-39341_Hotfix_COMPOSER.patch` as an example:

* [Install the Quality Patches Tool](https://experienceleague.adobe.com/en/docs/commerce-operations/tools/quality-patches-tool/usage).
* Run the command:

  `vendor/bin/magento-patches -n status | grep "39341\|Status"`

* You should see output similar to this, where this example VULN-39341 returns the Applied status:

  | ID | Title | Category | Origin | Status | Detail |
  |---|---|---|---|---|---|
  | N/A | …/m2-hotfixes/VULN-39341_Hotfix_COMPOSER.patch | Other | Local | Applied | Patch type: Custom |

### Rotate the credentials after applying the patch

To fully remediate this issue, rotate not only your encryption key but all credentials that may have been encrypted or exposed using it, including server, API, and integration credentials.

>[!NOTE]
>
>Because the encryption key is used to encrypt integration tokens, payment gateway credentials, and system-privileged automation tokens, rotating the encryption key alone does not invalidate credentials that may already have been exposed. All associated credentials should be rotated at their source (e.g., at the payment gateway or third-party service), not only within Commerce.

Steps to rotate credentials:

1. Apply the hotfix.
1. Enable maintenance mode.
1. Disable cron execution (Commerce on Cloud command: vendor/bin/ece-tools cron:disable).
1. [Rotate your encryption keys](https://experienceleague.adobe.com/en/docs/commerce-admin/systems/security/encryption-key?lang=en).
1. Rotate all Admin panel user passwords.
1. Deactivate and regenerate all REST/SOAP/GraphQL integration tokens (**System** > **Extensions** > **Integrations**).
1. Rotate OAuth client secrets for any connected third-party applications.
1. Rotate payment gateway API credentials at the provider level (Stripe, Braintree, Adyen, PayPal, etc.).
1. Rotate database credentials.
1. Rotate SSH/deploy keys and any cron or system-privileged service account credentials.
1. Rotate API keys for shipping, tax, and other integrated third-party extensions.
1. Flush the cache.
1. Enable cron execution (Commerce on Cloud command: vendor/bin/ece-tools cron:enable).
1. Disable maintenance mode.


### Security updates

Security updates available for Adobe Commerce:

* Adobe Security Bulletin (APSB26-146)
* [The latest Security updates available for Adobe Commerce](https://helpx.adobe.com/security/products/magento.html)

### Related reading

[Enable or disable maintenance mode](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/tutorials/maintenance-mode?lang=en) in the Adobe Commerce Installation Guide
