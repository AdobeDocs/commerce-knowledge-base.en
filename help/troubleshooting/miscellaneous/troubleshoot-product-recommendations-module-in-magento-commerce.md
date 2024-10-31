---
title: Troubleshoot the [!UICONTROL Product Recommendations] module in Adobe Commerce
description: This article talks about troubleshooting suggestions for the [!UICONTROL Product Recommendations] module in Adobe Commerce.
exl-id: 431ee31e-eb5b-400c-9c99-cc86613453d7
feature: Cache, Compliance, Extensions, Marketing Tools, Personalization, Products, Recommendations
role: Developer
---
# Troubleshoot the [!UICONTROL Product Recommendations] module in Adobe Commerce

This article talks about troubleshooting suggestions for the

```php
magento/product-recommendations
```

module and its dependency

```php
saas-export
```

module since you need both modules operating in order to use the [!UICONTROL Product Recommendations] tool in Adobe Commerce.

## Affected products and versions

* Adobe Commerce 2.4.4 - 2.4.7

## Troubleshoot product-recommendations module

If you have configured the

```php
magento/product-recommendations
```

module correctly, (Check [[!UICONTROL Product Recommendations - Install and Configure]](https://experienceleague.adobe.com/en/docs/commerce-merchant-services/product-recommendations/getting-started/install-configure) in our developer documentation.) but you aren't seeing any recommendations, try the following:

* It's possible that the module hasn't had enough time to collect behavioral data. Allow the system to run for 24 hours so it can start collecting data. Consider deploying a recommendation type that does not require any behavioral data, such as "*More like this*".

* If you aren't seeing the recommendations that you configured, it's possible there isn't yet sufficient data to build recommendations for the user.

* Ensure the [!DNL SaaS] Data Space or [!DNL API] Key are valid. If you get an error after specifying your [!DNL SaaS] Data Space or your [!DNL API] key during the product recommendations initialization, check to make sure you have entered the [[!DNL SaaS] Data Space and [!DNL API] key](https://experienceleague.adobe.com/en/docs/commerce-admin/config/services/saas) (in our user guide) correctly. To ensure the [!DNL MageID] and [!DNL API] key are linked, the user who owns the [!DNL MageID], typically the user who owns the Adobe Commerce license, needs to be the same user who generates the [!DNL API] key. If you must change the [!DNL MageID] that was used, [submit a Support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket).

>[!NOTE]
>
>If [**[!UICONTROL Cookie Restriction Mode]**](https://experienceleague.adobe.com/en/docs/commerce-admin/start/compliance/privacy/compliance-cookie-law) (in our user guide) is *enabled*, Adobe Commerce doesn't collect behavioral data until the shopper consents. If **[!UICONTROL Cookie Restriction Mode]** is *disabled*, Adobe Commerce collects behavioral data by default.

## Catalog [!DNL SaaS] Export module

For issues related to the Catalog [!DNL SaaS] Export (

```php
saas-export
```

) module:

1. Confirm the [[!DNL cron]](https://experienceleague.adobe.com/en/docs/commerce-operations/configuration-guide/cli/configure-cron-jobs) (in our developer documentation) jobs are running.
1. Confirm the [[!UICONTROL indexers]](https://experienceleague.adobe.com/en/docs/commerce-operations/configuration-guide/cli/manage-indexers) (in our developer documentation) are running and the    ```php    Product Feed    ```    [!UICONTROL indexer] is set to    ```php    Update by Schedule    ```    .
1. Confirm the modules are *enabled*. The    ```php    saas-export    ```    metapackage installs the following modules, all of which must be *enabled*:    ```php    "magento/module-catalog-data-exporter"      "magento/module-catalog-inventory-data-exporter"      "magento/module-catalog-url-rewrite-data-exporter"      "magento/module-configurable-product-data-exporter"      "magento/module-data-exporter"      "magento/module-saas-catalog"    ```
1. Check the [logs](https://experienceleague.adobe.com/en/docs/commerce-operations/configuration-guide/cli/enable-logging) (in our developer documentation). Make sure there are no errors associated with the above modules.
1. Refresh the [!UICONTROL Configuration cache]. Go to **System** > **Tools** > **Cache Management**, and clear the [!UICONTROL Configuration cache].
1. Confirm there is data in the `cde_products_products_feed` database table.

   >[!NOTE]
   >
   >If you can't find that table, check the `catalog_data_exporter_products` table. The table name was changed in the [!DNL Data Export] version 103.3.0 release.

## Events

 [Verify Event Collection](https://experienceleague.adobe.com/en/docs/commerce-merchant-services/product-recommendations/getting-started/verify), in our developer documentation, describes the behavioral events that are sent to Adobe Commerce.

## Related reading

* [Product Recommendations Administrator Development](https://experienceleague.adobe.com/en/docs/commerce-merchant-services/product-recommendations/developer/development-overview) in our developer documentation
* [Introduction to Product Recommendations](https://experienceleague.adobe.com/en/docs/commerce-merchant-services/product-recommendations/overview) in the Product Recommendations Guide
* [Create Product Recommendations](https://experienceleague.adobe.com/en/docs/commerce-merchant-services/product-recommendations/admin/create) in the Product Recommendations Guide
* [Review logs and troubleshoot](https://experienceleague.adobe.com/en/docs/commerce-merchant-services/saas-data-export/troubleshooting-logging) in the [!DNL SaaS] Data Export Guide
* [[!DNL SaaS] Data Export Extension Release Notes](https://experienceleague.adobe.com/en/docs/commerce-merchant-services/saas-data-export/release-notes) in the Adobe Commerce Data Export Guide for [!DNL SaaS] Services
* [Best practices for modifying database tables](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/development/modifying-core-and-third-party-tables#why-adobe-recommends-avoiding-modifications) in the Commerce Implementation Playbook

