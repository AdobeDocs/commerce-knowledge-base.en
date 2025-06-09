---
title: Security update available for Adobe Commerce - [!DNL APSB25-50]
promoted: true
description: Apply an Isolated patch to remediate [!DNL critical and important vulnerabilities] for Adobe Commerce 2.4.9-alpha1, 2.4.8-p1, 2.4.7-p6, 2.4.6-p11, 2.4.5-p13, 2.4.4-p14, and earlier versions.
feature: Compliance, Security
role: Developer
---
# Security update available for Adobe Commerce - [!DNL APSB25-50]

On June 10, 2025, Adobe released a regularly scheduled security update for Adobe Commerce. This update resolves [[!DNL critical] and [!DNL important]](https://helpx.adobe.com/security/severity-ratings.html) vulnerabilities. Successful exploitation of these vulnerabilities could lead to security feature bypass, privilege escalation, and arbitrary code execution. 

More information can be found in the [Adobe Security Bulletin ([!DNL APSB25-50]) here](https://helpx.adobe.com/security/products/magento/apsb25-50.html).  

>[!NOTE]
>
>**To help ensure that the remediation for [!DNL CVE-2025-47110] listed in the security bulletin above, can be applied as promptly as possible, Adobe has also released an isolated patch that resolves both these vulnerabilities [!DNL CVE-2025-47110]. This allows merchants to apply the fix in isolation with fewer risks of delay due to potential integration issues.** 

**Please apply the latest security updates as soon as possible. If you fail to do so, you will be vulnerable to these security issues, and Adobe will have limited means to help remediate the issue further.**

You can read more about [our isolated patch deployment process here.](https://business.adobe.com/blog/introducing-enhanced-security-patch-deployment-and-communications-in-adobe-commerce)

>[!NOTE]
>
>For Adobe Commerce on Managed Services customers, your Customer Success Engineer can provide additional guidance on applying the patch.

>[!NOTE]
>
>Please contact Support Services if you encounter any issues applying the security patch/Isolated patch.
 
As a reminder, you can find [the latest Security updates available for Adobe Commerce here.](https://helpx.adobe.com/security/products/magento.html)

## Affected products and versions

Adobe Commerce (all deployment menthods):

* 2.4.9-alpha1 
* 2.4.8-p1 and earlier
* 2.4.7-p6 and earlier
* 2.4.6-p11 and earlier
* 2.4.5-p13 and earlier
* 2.4.4-p14 and earlier

## Issues

### I. CVE-2025-47110: Stored XSS via Server-Side Template Injection in Adobe Commerce 2.4.7-p4

<u>Affected products and versions</u>:

Adobe Commerce (all deployment menthods):

* 2.4.8
* 2.4.7-p6 and earlier
* 2.4.6-p11 and earlier
* 2.4.5-p13 and earlier
* 2.4.4-p14 and earlier

<u>Solution</u>:

For Adobe Commerce versions:

* 2.4.8
* 2.4.7, 2.4.7-p1, 2.4.7-p2, 2.4.7-p3, 2.4.7-p4, 2.4.7-p5, 2.4.7-p6 
* 2.4.6, 2.4.6-p1, 2.4.6-p2, 2.4.6-p3, 2.4.6-p4, 2.4.6-p5, 2.4.6-p6, 2.4.6-p7, 2.4.6-p8, 2.4.6-p10, 2.4.6-p11
* 2.4.5, 2.4.5-p1, 2.4.5-p2, 2.4.5-p3, 2.4.5-p4, 2.4.5-p5, 2.4.5-p6, 2.4.5-p7, 2.4.5-p8, 2.4.5-p9, 2.4.5-p10, 2.4.5-p11, 2.4.5-p12, 2.4.5-p13
* 2.4.4, 2.4.4-p1, 2.4.4-p2, 2.4.4-p3, 2.4.4-p4, 2.4.4-p5, 2.4.4-p6, 2.4.4-p7, 2.4.4-p8, 2.4.4-p9, 2.4.4-p10, 2.4.4-p11, 2.4.4-p12, 2.4.4-p13, 2.4.4-p14

**Apply the following isolated patch or upgrade to the latest security patch.**

* **[VULN-31609_2.4.X.patch](assets/VULN-31609_2.4.X_patch.zip)**

### II. VULN-31547: Reflected XSS in marketplace.magento.com + one-click ATO issue impacting IMS instances

<u>Affected products and versions</u>:

Adobe Commerce (all deployment menthods): 

* 2.4.9-alpha1 
* 2.4.8-p1 and earlier

<u>Solution</u>:

For Adobe Commerce versions:

* 2.4.9-alpha1
* 2.4.8, 2.4.8-p1

**Apply the following isolated patch or upgrade to the latest security patch.**

* **[VULN-31547_2.4.8.patch](assets/VULN-31547_2.4.8_patch.zip)**

## How to apply the Isolated patch

Unzip the file and see [How to apply a composer patch provided by Adobe](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/how-to/how-to-apply-a-composer-patch-provided-by-magento.html) in our support knowledge base for instructions.

## For Adobe Commerce on Cloud merchants only - How to tell whether the Isolated patches have been applied

Considering that it isn't possible to easily check if the issue was patched, you might want to check whether the [!DNL CVE-2025-24434] Isolated patch has been successfully applied. 

>[!NOTE]
>
><u>You can do this by taking the following steps, using the file `VULN-27015-2.4.7_COMPOSER.patch` **as an EXAMPLE**</u>:

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

* [Adobe Security Bulletin ([!DNL APSB25-50])](https://helpx.adobe.com/security/products/magento/apsb25-50.html)
* [The latest Security updates available for Adobe Commerce](https://helpx.adobe.com/security/products/magento.html)
