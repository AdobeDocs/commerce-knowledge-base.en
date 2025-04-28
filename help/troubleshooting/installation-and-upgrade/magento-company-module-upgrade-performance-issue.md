---
title: Performance issue in Magento_Company module upgrade after B2B 1.5.2 update
description: This article provides a hotfix for the performance issue in the Magento_Company module upgrade after the B2B 1.5.2 update, addressing the excessively long processing time for large datasets in the company_structure table.
feature: B2B, Upgrade
role: Admin, Developer
---
# Performance issue in Magento_Company module upgrade after B2B 1.5.2 update

This article provides a hotfix for the performance issue in the `Magento_Company` module upgrade after the B2B 1.5.2 update, addressing the excessively long processing time for large datasets (~100,000+ records) in the `company_structure` table.

## Affected products and versions

* Adobe Commerce (all deployment methods) 2.4.6-px + B2B 1.5.2
* Adobe Commerce (all deployment methods) 2.4.7-px + B2B 1.5.2
* Adobe Commerce (all deployment methods) 2.4.8 + B2B 1.5.2

## Issue

Upgrading the `Magento_Company` module after updating to B2B 1.5.2 takes an excessively long time when processing a large number of records (~100,000+) in the `company_structure` table.

<u>Prerequisites</u>:

* ACSD-65540_B2B_1.5.2.patch should be installed.
* Adobe Commerce 2.4.6 - 2.4.8
* B2B version 1.5.0, 1.5.1, or B2B 1.5.2 with the ACSD-65540 patch applied

<u>Steps to reproduce</u>:

1. Assign a company to a parent company to establish company hierarchy. Refer to [Manage the Company Hierarchy](https://experienceleague.adobe.com/en/docs/commerce-admin/b2b/company-management/manage-company-hierarchy) in the Adobe Commerce B2B guide for more information.
1. Upgrade B2B to the 1.5.2 version.

<u>Expected results</u>:

Upgrade completes successfully.

<u>Actual results</u>:

Upgrading the `Magento_Company` module takes a long time to complete if there are many records in the `company_structure` table.

## Solution

To solve the issue, take the following steps:

1. Update the B2B module to the 1.5.2 version:

    ```
    composer require magento/module-b2b:1.5.2 --no-update
    composer update magento/module-b2b
    ```

1. Apply the [ACSD-65540_B2B_1.5.2.patch](/help/troubleshooting/installation-and-upgrade/assets/ACSD-65540_B2B_1.5.2.zip).

1. Apply the attached [ACSD-65540_B2B_1.5.2_DEPENDENT_ACSD-65684_B2B_1.5.2.patch](/help/troubleshooting/installation-and-upgrade/assets/ACSD-65540_B2B_1.5.2_DEPENDENT_ACSD-65684_B2B_1.5.2.patch.zip) in our support knowledge base for instructions. 
1. Run `bin/magento setup:upgrade` after applying the patch.

### How to apply the patch

Unzip the file and see [How to apply a composer patch provided by Adobe](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/how-to/how-to-apply-a-composer-patch-provided-by-magento) in our support knowledge base for instructions.

### Apply a patch using Cloud Patches

For Adobe Commerce on Cloud merchants, follow the steps below:

1. Update the version of the cloud-patches module to 1.1.5 to install the ACSD-65540 patch distributed as MCLOUD-13605.

>[!NOTE]
>
>To check if the patch is already installed run:
>   ```
>   ./vendor/bin/magento-patches -n status | grep MCLOUD-13605
>   ```


    ```
    composer require magento/magento-cloud-patches:1.1.5 --no-update
    composer update magento/magento-cloud-patches
    ```

1. Add the ACSD-65540_B2B_1.5.2_DEPENDENT_ACSD-65684_B2B_1.5.2.patch to the m2-hotfixes directory.
1. Commit and push the changes to initiate redeployment and `bin/magento setup:upgrade`. Refer to [Apply patches](https://experienceleague.adobe.com/en/docs/commerce-on-cloud/user-guide/develop/upgrade/apply-patches) in our Adobe Commerce on Cloud guide for instructions.

## Related reading

* [Upgrade to B2B 1.5.2 fails with SQL syntax error due to missing REGEXP_LIKE function](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/installation-and-upgrade/sql-syntax-error-due-to-missing-regexp-like-function)
