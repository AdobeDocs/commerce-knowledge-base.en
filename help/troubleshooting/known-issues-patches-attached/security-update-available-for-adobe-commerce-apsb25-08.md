---
title: Security update available for Adobe Commerce - [!DNL APSB25-08]
promoted: true
description: Apply an Isolated patch to remediate [!DNL critical, important, and moderate vulnerabilities] for both Adobe Commerce and Magento Open Source 2.4.7-beta1, 2.4.7-p3, 2.4.6-p8, 2.4.5-p10, 2.4.4-p11, and earlier versions.
feature: Compliance, Security
role: Developer
exl-id: 567e6ad2-704e-461f-a54d-75f6bd96e996
---
# Security update available for Adobe Commerce - [!DNL APSB25-08]

On February 11, 2025, Adobe released a regularly scheduled security update for Adobe Commerce and Magento Open Source. This update resolves [[!DNL critical, important], and [!DNL moderate]](https://helpx.adobe.com/security/severity-ratings.html) vulnerabilities. Successful exploitation of these vulnerabilities could lead to arbitrary code execution, security feature bypass, and privilege escalation. More information can be found in the [Adobe Security Bulletin ([!DNL APSB25-08]) here](https://helpx.adobe.com/security/products/magento/apsb25-08.html).  

>[!NOTE]
>
>**To help ensure that the remediation for [!DNL CVE-2025-24434], listed in the security bulletin above, can be applied as promptly as possible, Adobe has also released an isolated patch that resolves [!DNL CVE-2025-24434]. This allows merchants to apply the fix in isolation with fewer risks of delay due to potential integration issues.** 

**Please apply the latest security updates as soon as possible. If you fail to do so, you will be vulnerable to these security issues, and Adobe will have limited means to help remediate the issue further.**

>[!NOTE]
>
>Please contact Support Services if you encounter any issues applying the security patch/Isolated patch.
 
## Affected products and versions

Adobe Commerce on Cloud infrastructure, Adobe Commerce on-premises, and Magento Open Source:

* 2.4.7-beta1 and earlier
* 2.4.7-p3 and earlier
* 2.4.6-p8 and earlier
* 2.4.5-p10 and earlier
* 2.4.4-p11 and earlier

## Solution for Adobe Commerce on Cloud and Adobe Commerce on-premises software

To help resolve the vulnerability for the affected products and versions, you must apply the [!DNL CVE-2025-24434] Isolated patch.

## Isolated Patch Details

Use the following attached Isolated patch:

[vuln-28982-composer-patch.zip](assets/vuln-28982-composer-patch.zip)

## How to apply the Isolated patch

Unzip the file and see [How to apply a composer patch provided by Adobe](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/how-to/how-to-apply-a-composer-patch-provided-by-magento.html) in our support knowledge base for instructions.

## For Adobe Commerce on Cloud merchants only - How to tell whether the Isolated patches have been applied

Considering that it isn't possible to easily check if the issue was patched, you might want to check whether the [!DNL CVE-2025-24434] Isolated patch has been successfully applied. 

>[!NOTE]
>
><u>You can do this by taking the following steps, using the file `VULN-27015-2.4.7_COMPOSER.patch` **as an example**</u>:

1. [Install the Quality Patches Tool](https://experienceleague.adobe.com/docs/commerce-operations/tools/quality-patches-tool/usage.html).
1. Run the command:<br>
 ![cve-2024-34102-tell-if-patch-applied-code](assets/cve-2024-34102-tell-if-patch-applied-code.png)
1. You should see output similar to this, where VULN-27015 returns the *Applied* status:

    ```bash
    ║ Id            │ Title                                                        │ Category        │ Origin                 │ Status      │ Details                                          ║ ║ N/A           │ ../m2-hotfixes/VULN-27015-2.4.7_COMPOSER_patch.patch      │ Other           │ Local                  │ Applied     │ Patch type: Custom                                
    ```

<!-- For Step 2:
     ```bash
    vendor/bin/magento-patches -n status |grep "27015\|Status"
     ```
-->

## Security updates

Security updates available for Adobe Commerce:

* [Adobe Security Bulletin ([!DNL APSB25-08])](https://helpx.adobe.com/security/products/magento/apsb25-08.html)
* [The latest Security updates available for Adobe Commerce](https://helpx.adobe.com/security/products/magento.html)
