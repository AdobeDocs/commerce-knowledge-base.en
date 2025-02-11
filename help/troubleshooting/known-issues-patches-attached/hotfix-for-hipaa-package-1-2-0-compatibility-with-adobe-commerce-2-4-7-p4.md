---
title: Adobe Commerce 2.4.7-p4 [!DNL HIPAA] 1.2.0 compatibility package Hotfix
description: 'This article provides a hotfix to add compatibility for a new [!DNL HIPAA] package 1.2.0 with Adobe Commerce on Cloud infrastructure 2.4.7-p4'
feature: Install, Upgrade
role: Developer
---
# Adobe Commerce 2.4.7-p4 [!DNL HIPAA] 1.2.0 compatibility package Hotfix

This article provides a hotfix to add compatibility for a new [!DNL HIPAA] package 1.2.0 with Adobe Commerce on Cloud infrastructure 2.4.7-p4.

The issue will be fixed in the scope of the version 2.4.7-p5 release.

## Affected versions and products

Adobe Commerce on Cloud infrastructure 2.4.7-p4 and earlier

## Issue

The issue is caused by the [!DNL HIPAA] package 1.1.0 is not compatible with Adobe Commerce 2.4.7x release line.

## Solution

Through this hotfix, merchants who are running Adobe Commerce on Cloud infrastructure 2.4.7-p4 will able to use the [!DNL HIPAA] package 1.2.0.

>[!NOTE]
>
>**[!DNL HIPAA] 1.2.0 is compatible with Adobe Commerce 2.4.7-p5 only. If you want to add compatibility with [!DNL HIPAA] 1.2.0 to Adobe Commerce 2.4.7-p4, please install the provided patch.<br><u>If you aren't on Adobe Commerce 2.4.7-p4, you must first upgrade to Adobe Commerce 2.4.7-p4 in order to use this patch</u>.**

In order to fix the issue for Adobe Commerce on Cloud infrastructure 2.4.7-p4, you should apply the patch:

 [ac-13382--patch-for-hipaa-2-4-7-p4-composer-patch.zip](assets/ac-13382--patch-for-hipaa-2-4-7-p4-composer-patch.zip)

## How to apply the patch

Unzip the file and see [How to apply a composer patch provided by Adobe](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/how-to/how-to-apply-a-composer-patch-provided-by-magento.html) in our support knowledge base for instructions.

## For Adobe Commerce on Cloud merchants only - How to tell whether the patch has been applied

Considering that it isn't possible to easily check if the issue was patched, you might want to check whether the patch has been successfully applied. 

>[!NOTE]
>
><u>You can do this by taking the following steps, using the file `VULN-27015-2.4.7_COMPOSER.patch` **as an Example**</u>:

1. [Install the Quality Patches Tool](https://experienceleague.adobe.com/docs/commerce-operations/tools/quality-patches-tool/usage.html).
1. Run the command:<br>
 ![cve-2024-34102-tell-if-patch-applied-code](assets/cve-2024-34102-tell-if-patch-applied-code.png)
1. You should see output similar to this, **<u>where the Example used here, VULN-27015</u>**, returns the *Applied* status:

    ```bash
    ║ Id            │ Title                                                        │ Category        │ Origin                 │ Status      │ Details                                          ║ ║ N/A           │ ../m2-hotfixes/VULN-27015-2.4.7_COMPOSER_patch.patch      │ Other           │ Local                  │ Applied     │ Patch type: Custom                                
    ```

<!-- For Step 2:
     ```bash
    vendor/bin/magento-patches -n status |grep "27015\|Status"
     ```
-->
