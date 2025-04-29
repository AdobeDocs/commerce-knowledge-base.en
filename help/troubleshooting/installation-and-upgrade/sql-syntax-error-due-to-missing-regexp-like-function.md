---
title: Upgrade to B2B 1.5.2 fails with SQL syntax error due to missing REGEXP_LIKE function
description: This article provides a hotfix for the issue where an SQL syntax error occurs due to the missing REGEXP_LIKE function when attempting to update the company_structure table.
feature: B2B, Upgrade
role: Admin, Developer
exl-id: c5fe316c-99e3-482e-80b5-25aaae371230
---
# Upgrade to B2B 1.5.2 fails with SQL syntax error due to missing REGEXP_LIKE function

>[!INFO]
>
>If you experience a performance issue when upgrading the `Magento_Company` module after updating to B2B 1.5.2, apply the attached [ACSD-65540_B2B_1.5.2_DEPENDENT_ACSD-65684_B2B_1.5.2.patch](assets/ACSD-65540_B2B_1.5.2_DEPENDENT_ACSD-65684_B2B_1.5.2.patch.zip).
>
>For more information, refer to [Performance issue in Magento_Company module upgrade after B2B 1.5.2 update](/help/troubleshooting/installation-and-upgrade/magento-company-module-upgrade-performance-issue.md) in our Adobe Commerce knowledge base.

This article provides a hotfix for the SQL syntax error that occurs due to the missing `REGEXP_LIKE` function when attempting to update the `company_structure` table.

## Affected products and versions

* Adobe Commerce (all deployment methods) 2.4.6-px + B2B 1.5.2 using [!DNL MariaDB] 10.6
* Adobe Commerce (all deployment methods) 2.4.7-px + B2B 1.5.2 using [!DNL MariaDB] 10.6

## Issue

Upgrading to B2B version 1.5.2 fails with an SQL syntax error due to the missing `REGEXP_LIKE` function when attempting to update the `company_structure` table.

<u>Prerequisites</u>:

* MariaDB 10.6
* Adobe Commerce 2.4.6x or 2.4.7x
* B2B version 1.5.0 or 1.5.1

<u>Steps to reproduce</u>:

1. Assign a company to a parent company to establish company hierarchy. Refer to [Manage the Company Hierarchy](https://experienceleague.adobe.com/en/docs/commerce-admin/b2b/company-management/manage-company-hierarchy) in the Adobe Commerce B2B guide for more information.
1. Upgrade B2B to the 1.5.2 version.

<u>Expected results</u>:

Upgrade completes successfully.

<u>Actual results</u>:

`bin/magento setup:upgrade` fails with the following error:

```
Unable to apply data patch Magento\Company\Setup\Patch\Data\SetCompanyForStructure for module Magento_Company. Original exception message: SQLSTATE[42000]: Syntax error or access violation: 1305 FUNCTION REGEXP_LIKE does not exist, query was: UPDATE `company_structure` SET `company_id` = ? WHERE (REGEXP_LIKE(path, '^123(/.+)?$'))
```

## Solution

To solve the issue, take the following steps:

1. Update the B2B module to the 1.5.2 version:

    ```
    composer require magento/module-b2b:1.5.2 --no-update
    composer update magento/module-b2b
    ```

1. Apply the attached [ACSD-65540_B2B_1.5.2.zip](assets/ACSD-65540_B2B_1.5.2.zip) patch. Refer to [How to apply a composer patch provided by Adobe](/help/how-to/general/how-to-apply-a-composer-patch-provided-by-magento.md) in our support knowledge base for instructions. 
1. Run `bin/magento setup:upgrade`.

### Apply a patch using Cloud Patches

For Adobe Commerce on Cloud infrastructures, follow the steps below:

1. Update the version of the `cloud-patches` module to 1.1.5:

    ```
    composer require magento/magento-cloud-patches:1.1.5 --no-update
    composer update magento/magento-cloud-patches
    ```

1. Commit and push the changes to initiate re-deploy. Refer to [Apply patches](https://experienceleague.adobe.com/en/docs/commerce-on-cloud/user-guide/develop/upgrade/apply-patches) in our Adobe Commerce on Cloud guide for instructions.
