---
title: Error when filtering orders in the Admin
description: This article provides a patch for the Adobe Commerce issue, where an error occurs when attempting to filter orders in the Admin by date, displaying the message "Integrity constraint violation 1052 Column 'created_at' where clause is ambiguous".
feature: Orders
role: Developer
exl-id: 64aa104e-3b01-4a26-a88a-6aef06d9239e
---
# Error when filtering orders in the Admin

This article provides a patch for the Adobe Commerce issue where an error occurs when attempting to filter orders in the Admin by date, displaying the message: *Integrity constraint violation: 1052 Column 'created_at' where clause is ambiguous*.

## Affected versions

* Adobe Commerce (all deployment methods) 2.4.4 - 2.4.7

## Issue 

Filtering orders in the Admin by date returns an error.

The exception.log shows:

```SQL
report.CRITICAL: PDOException: SQLSTATE[23000]: Integrity constraint violation: 1052 Column 'created_at' in where clause is ambiguous in /path/to/magento/vendor/magento/framework/DB/Statement/Pdo/Mysql.php:90
```

<u>Steps to reproduce:</u>

1. Go to **[!UICONTROL Admin]** > **[!UICONTROL Sales]** > **[!UICONTROL Orders]**.
   * Set **[!UICONTROL Purchase Date Ascending]** order in grid, OR
   * Set **[!UICONTROL Purchase Date Filter]** in filters.
  
1. An error appears: *Something went wrong with processing the default view and we have restored the filter to its original state.*

## Cause

There is an issue with the [!DNL PayPal Braintree] modules.

## Solution

To solve the issue, apply the patch attached to this article. To download it, scroll down to the end of the article and click the file name, or click the following link:

[bundle_3357_filter_order_in_admin_by_date_patch.zip](assets/bundle-3357-unable-to-filter-order-in-admin-by-date.zip)

The patch is compatible with all affected versions and editions.

## How to apply the patch

For instructions, see [How to apply a composer patch provided by Adobe](/help/how-to/general/how-to-apply-a-composer-patch-provided-by-magento.md) in the support knowledge base.
