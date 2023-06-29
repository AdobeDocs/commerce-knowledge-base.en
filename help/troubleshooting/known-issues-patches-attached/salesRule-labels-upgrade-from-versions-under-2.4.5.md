---
title: '**[!UICONTROL salesRules]** labels issues when upgrade from versions < 2.4.5'
description: Apply a patch to deal with the **[!UICONTROL salesRules]** issues when upgrading from Adobe Commerce versions < 2.4.5.
---
# **[!UICONTROL salesRules]** labels issues when upgrade from versions < 2.4.5

The **[!UICONTROL salesRules]** label staging functionality was introduced in Adobe Commerce [2.4.5](/docs/commerce-operations/release/notes/adobe-commerce/2-4-5.html).
The change may potentially lead to issues when you upgrade from Adobe Commerce < 2.4.5 to any version >= 2.4.5. After the upgrade, there is a possibility that **[!UICONTROL salesRules]** labels are mismatched.
To address the problem, a patch should be applied right after the upgrade to a newer Adobe Commerce version.

## Affected products and versions

Adobe Commerce on cloud infrastructure < 2.4.5

## Patch

Use the following attached patch:

[ACSD-50625_2.4.5-P1.patch.zip](assets/ACSD-50625_2.4.5-p1.patch.zip)

## How to apply the patch

1. Follow the steps in [Perform an upgrade](https://experienceleague.adobe.com/docs/commerce-operations/upgrade-guide/implementation/perform-upgrade.html) in the Commerce guide.
1. Apply the attached patch prior to the **[!UICONTROL Update metadata]** phase. 
    (You can also apply the patch after you have completed the **[!UICONTROL Update metadata]** phase but then you need to run `bin/magento setup:upgrade`).
1. Proceed with the rest of the steps in [Perform an upgrade](https://experienceleague.adobe.com/docs/commerce-operations/upgrade-guide/implementation/perform-upgrade.html).
