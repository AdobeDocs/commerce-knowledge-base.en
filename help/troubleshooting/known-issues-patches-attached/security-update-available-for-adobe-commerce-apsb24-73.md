---
title: Security update available for Adobe Commerce - [!DNL APSB24-73]
promoted: true
description: Apply an Isolated patch to remediate [!DNL critical, important, and moderate vulnerabilities] for Adobe Commerce 2.4.7-p3, 2.4.6-p8, 2.4.5-p10,  2.4.4-p11, and earlier versions instances only running [!DNL B2B] module.
feature: Compliance, Security
role: Developer
---
# Security update available for Adobe Commerce - [!DNL APSB24-73]

On October 08, 2024, Adobe released a regularly scheduled security update for Adobe Commerce, Magento Open Source, and [!DNL Adobe Commerce Webhooks Plugin].
This update resolves [[!DNL critical, important], and [!DNL moderate]](https://helpx.adobe.com/security/severity-ratings.html) vulnerabilities. Successful exploitation could lead to arbitrary code execution, arbitrary file system read, security feature bypass, and privilege escalation. The bulletin is [Adobe Security Bulletin ([!DNL APSB24-73])](https://helpx.adobe.com/security/products/magento/apsb24-73.html).  

>[!NOTE]
>
>**[!DNL CVE-2024-45115], listed in the security bulletin above, is applicable only when using the [!DNL B2B] module.** To help ensure that the remediation for this vulnerability can be applied as promptly as possible, Adobe has also released an Isolated patch that resolves [!DNL CVE-2024-45115]. 

**Please apply the latest security updates as soon as possible. If you fail to do so, you will be vulnerable to these security issues, and Adobe will have limited means to help remediate.**

>[!NOTE]
>
>Please contact Support Services if you encounter any issues applying the security patch/Isolated patch.
 
## Affected products and versions

Adobe Commerce on Cloud, Adobe Commerce on-premises, and Magento Open Source:

* 2.4.7-p3 and earlier
* 2.4.6-p8 and earlier
* 2.4.5-p10 and earlier
* 2.4.4-p11 and earlier

## Solution for Adobe Commerce on Cloud, Adobe Commerce on-premises Software, and Magento Open Source 

To help resolve the vulnerability for the affected products and versions, you must apply the [!DNL CVE-2024-45115] Isolated patch.

## Isolated Patch Details

Use the following attached Isolated patch:

[vuln-25610-composer-patch.zip](assets/vuln-25610-composer-patch.zip)

## How to apply the Isolated patch

Unzip the file and see [How to apply a composer patch provided by Adobe](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/how-to/how-to-apply-a-composer-patch-provided-by-magento.html) in our support knowledge base for instructions.

## For Adobe Commerce on Cloud merchants only - How to tell whether the Isolated patches have been applied

Considering that it isn't possible to easily check if the issue was patched, you might want to check whether the [!DNL CVE-2024-45115] Isolated patch has been successfully applied. 

<u>You can do this by taking the following steps, using the file `VULN-27015-2.4.7_COMPOSER.patch` **as an example**</u>:

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

* [Adobe Security Bulletin ([!DNL APSB24-73])](https://helpx.adobe.com/security/products/magento/apsb24-73.html)
