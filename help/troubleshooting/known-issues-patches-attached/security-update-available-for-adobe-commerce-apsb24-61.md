---
title: Security update available for Adobe Commerce - [!DNL APSB24-61]
promoted: true
description: Apply an Isolated patch to remediate [!DNL CVE-2024-39397] for Adobe Commerce 2.4.7-p2, 2.4.6-p7, 2.4.5-p9, 2.4.4-p10, and earlier versions instances only running [!DNL Apache].
feature: Compliance, Security
role: Developer
---
# Security update available for Adobe Commerce - [!DNL APSB24-61]

On August 13, 2024, Adobe released a security update for Adobe Commerce, Magento Open Source, and Adobe Commerce Webhooks Plugin.
This update resolves [[!DNL critical, important], and [!DNL moderate]](https://helpx.adobe.com/security/severity-ratings.html) vulnerabilities.  Successful exploitation could lead to arbitrary code execution, arbitrary file system read, security feature bypass, and privilege escalation. The bulletin is [Adobe Security Bulletin ([!DNL APSB24-61])](https://helpx.adobe.com/security/products/magento/apsb24-61.html).  

>[!NOTE]
>
>**[!DNL CVE-2024-39397] is applicable only when using the Apache web server.** To help ensure that the remediation for this vulnerability can be applied as promptly as possible, Adobe has also released an isolated patch that resolves [!DNL CVE-2024-39397]. 

**Please apply the latest security updates as soon as possible. If you fail to do so, you will be vulnerable to these security issues, and Adobe will have limited means to help remediate.**

>[!NOTE]
>
>Please contact Support Services if you encounter any issues applying the security patch/Isolated patch.
 
## Affected products and versions

Adobe Commerce on Cloud, Adobe Commerce on-premises, and Magento Open Source:

* 2.4.7-p1 and earlier
* 2.4.6-p6 and earlier
* 2.4.5-p8 and earlier
* 2.4.4-p9 and earlier

Adobe Commerce Webhooks Plugin

## Solution for Adobe Commerce on Cloud, Adobe Commerce on-premise Software, and Magento Open Source 

To help resolve the vulnerability for the affected products and versions, you must apply the [!DNL CVE-2024-39397] isolated patch.

## Isolated Patch Details

Use the following attached Isolated patch:

* [acsd-60551-composer-patch.zip](assets/acsd-60551-composer-patch.zip)

## How to apply the isolated patch

Unzip the file and see [How to apply a composer patch provided by Adobe](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/how-to/how-to-apply-a-composer-patch-provided-by-magento.html) in our support knowledge base for instructions.

## For Adobe Commerce on Cloud merchants only - How to tell whether the isolated patches have been applied

Considering that it isn't possible to easily check if the issue was patched, you might want to check whether the [!DNL CVE-2024-39397] Isolated patch has been successfully applied. 

<u>You can do this by taking the following steps, using the file `VULN-27015-2.4.7_COMPOSER.patch` as an example</u>:

1. [Install the Quality Patches Tool](https://experienceleague.adobe.com/docs/commerce-operations/tools/quality-patches-tool/usage.html).
1. Run the command:<br>
 ![cve-2024-34102-tell-if-patch-applied-code](assets/cve-2024-34102-tell-if-patch-applied-code.png)

<!--
    ```bash
    vendor/bin/magento-patches -n status |grep "27015\|Status"
    ```
-->

1. You should see output similar to this, where VULN-27015 returns the *Applied* status:

    ```bash
    ║ Id            │ Title                                                        │ Category        │ Origin                 │ Status      │ Details                                          ║ ║ N/A           │ ../m2-hotfixes/VULN-27015-2.4.7_COMPOSER_patch.patch      │ Other           │ Local                  │ Applied     │ Patch type: Custom                                
    ```

## Security updates

Security updates available for Adobe Commerce:

* [Adobe Security Bulletin ([!DNL APSB24-61])](https://helpx.adobe.com/security/products/magento/apsb24-61.html)
