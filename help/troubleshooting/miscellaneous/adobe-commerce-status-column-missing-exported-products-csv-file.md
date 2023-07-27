---
title: Adobe Commerce status column missing exported products CSV file
description: This article provides a solution for the issue when you cannot locate the status column in the CSV file containing exported products.
exl-id: 3cbe1e6c-fc73-4331-add7-1ebcb28a4580
feature: Data Import/Export, Products
role: Developer
---
# Adobe Commerce status column missing exported products CSV file 

This article provides a solution for the issue when you cannot locate the status column (i.e., indicating whether the product is enabled or disabled) in the CSV file containing exported products. The status of the product is indicated by the [!UICONTROL product_online] column.

## Affected products and versions

Adobe Commerce (all deployment methods) all [supported versions](https://www.adobe.com/content/dam/cc/en/legal/terms/enterprise/pdfs/Adobe-Commerce-Software-Lifecycle-Policy.pdf)

## Issue

You are unable to locate the [!UICONTROL status] column in the CSV file containing exported products. So, for example, you export a CSV of all SKUs, with their status, but the table appears to be missing the [!UICONTROL status] column. 

<u>Steps to reproduce:</u>

1. In the Adobe Commerce Admin, select **[!UICONTROL System]**, under **[!UICONTROL Data Transfer]** select **[!UICONTROL Export]**.
1. In the **[!UICONTROL Export Settings]** section, select on the **[!UICONTROL Entity Type]** drop down **[!UICONTROL Products]**.
1. Search for **[!UICONTROL status]**, listed under **[!UICONTROL Attribute Code]**. You see that attribute code in the list of available attributes (**[!UICONTROL Enable Product]**).
1. Click on **[!UICONTROL Export]**.

<u>Expected result:</u>

In the CSV file that you just exported, you see a column labeled [!UICONTROL status].

<u>Actual result:</u>

You do not see a column labeled [!UICONTROL status] in the exported csv file.  

## Cause

The product's status attribute has been renamed in the CSV file. It is now the [!UICONTROL product_online] column.

## Solution

1. Select **[!UICONTROL System]**, under **[!UICONTROL Data Transfer]** select **[!UICONTROL Import]**.
1. Click **[!UICONTROL Download Sample File]**.
1. You can see the [!UICONTROL product_online] column in the CSV file.

## Related reading

* [Working with CSV files](https://docs.magento.com/user-guide/system/data-csv.html) in our user guide.
* [Product Export Attributes Reference](https://docs.magento.com/user-guide/system/data-attributes-product.html) in our user guide.
