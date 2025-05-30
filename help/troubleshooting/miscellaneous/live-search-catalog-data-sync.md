---
title: Live search catalog not synchronized
description: This article provides solutions for the Adobe Commerce issue where your catalog data is not synchronized correctly when using the Live Search extension.
exl-id: cd2e602f-b2c7-4ecf-874f-ec5f99ae1900
feature: Catalog Management, Search
role: Developer
---
# Live search catalog not synchronized

This article provides solutions for the Adobe Commerce issue where your catalog data is not synchronized correctly when using the Live Search extension.

## Affected products and versions

* Adobe Commerce 2.4.x with Live Search extension installed

## Issue

Your catalog data is not synchronized correctly, or a new product was added but does not appear in search results. You may also get the following error in the `var/log/exception.log`:

`Magento_LiveSearch: An error occurred in search backend. {"result":{"errors":[{"message":"Exception while fetching data (/productSearch) : No index was found for this request"}]}}`

>[!NOTE]
>
>The table names `catalog_data_exporter_products` and `catalog_data_exporter_product_attributes` are now called `cde_products_feed` and `cde_product_attributes_feed` as of [!DNL Live Search] version 4.2.1. For merchants on versions prior to 4.2.1, look for the data in the old table names, `catalog_data_exporter_products` and `catalog_data_exporter_product_attributes`.

<u>Steps to reproduce</u>

1. Configure and connect Live Search for your Adobe Commerce instance as described in [Install Live Search > Configure API keys](https://experienceleague.adobe.com/docs/commerce-merchant-services/live-search/onboard/install.html#configure-api-keys) in our user documentation.
1. After 30 minutes, verify the exported catalog data as described in [Install Live Search > Verify export](https://experienceleague.adobe.com/docs/commerce-merchant-services/live-search/onboard/install.html#verify-export) in our user documentation.
1. After 30 minutes, test the connection as described in [Install Live Search > Test the connection](https://experienceleague.adobe.com/docs/commerce-merchant-services/live-search/onboard/install.html#test-connection) in our user documentation.

Or

1. Add a new product to the catalog.
1. Try running a search query using the product name or other searchable attributes after 15-20 minutes from the time Magento indexer + cron have run to sync data to backend service.

<u>Expected result</u>

* Exported catalog data can be verified
* Connection is successful
* New product appears in search results.

<u>Actual result</u>

Exported catalog cannot be verified and/or connection is not established because the API key has changed.

## Solution

There are several things you might do to try and fix the catalog syncing issues.

### Wait for changes to be applied

Once you configure and connect, it can take over 30 minutes for the index in ES (Elasticsearch) to be created and search results to be returned. Subsequent one-off product updates are expected to be indexed within a few minutes.

### Sync product data for a specific SKU

If your product data is not synced correctly for a specific SKU, do the following:

1. Use the following [!DNL SQL] query and verify that you have the data you expect in the `feed_data` column. Also, make a note of the `modified_at` timestamp.

    ```sql
    SELECT * FROM cde_products_feed WHERE json_extract(feed_data, '$.sku') = '<your_sku>' AND json_extract(feed_data, '$.storeViewCode') = '<your_ store_view_code>';
    ```

    For example:

    ```sql
    SELECT * FROM cde_products_feed WHERE json_extract(feed_data, '$.sku') = '24-MB04' AND json_extract(feed_data, '$.storeViewCode') = 'default';
    ```

1. If you do not see the correct data, try to reindex using the following command and rerun the [!DNL SQL] query in step 1 to verify the data:

    ```bash
    bin/magento indexer:reindex cde_products_feed
    ```

1. If you still do not see the correct data, [create a Support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket).

### Check timestamp of last product export

1. If you see the correct data in `cde_products_feed`, use the following [!DNL SQL] query to check the timestamp of the last export. It should be after the `modified_at` timestamp:

    ```sql
    select * from scopes_website_data_exporter;
    ```

1. If the timestamp is older, you can either wait for the next cron run or trigger it yourself using the following command:

    ```bash
    bin/magento cron:run --group=saas_data_exporter
    ```

1. Wait for `<>` time (time for incremental updates). If you still do not see your data, [create a Support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket).

### Sync specific attribute code

If your product attribute data isn't synced correctly for a specific attribute code, do the following:

1. Use the following [!DNL SQL] query and verify that you have the data you expect in the `feed_data` column. Also, make a note of the `modified_at` timestamp.

    ```sql
    select * from cde_product_attributes_feed where json_extract(feed_data, '$.attributeCode') = '<your_attribute_code>' and store_view_code = '<your_ store_view_code>';
    ```

1. If you do not see the correct data, use the following command to reindex and then rerun the [!DNL SQL] query in step 1 to verify the data.

    ```bash
    bin/magento indexer:reindex cde_product_attributes_feed
    ```

1. If you still do not see the correct data, [create a Support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket).

### Check timestamp of last product attribute export

If you see the correct data in `cde_product_attributes_feed`:

1. Use the following [!DNL SQL] query to check the timestamp of the last export. It should be after the `modified_at` timestamp.

    ```sql
    select * from scopes_website_data_exporter;
    ```

1. If the timestamp is older, you can either wait for the next cron run or trigger it yourself using the following command:

    ```bash
    bin/magento cron:run --group=saas_data_exporter
    ```

1. Wait for 15-20 minutes (time for incremental updates). If you still do not see your data, please [create a Support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket).

### Sync after API configuration change

(Known issue) If you have changed your API configuration, which results in a change in your Data Space ID and find that your catalog changes are no longer syncing, run the following commands to resync the feeds:

```
bin/magento saas:resync --feed productattributes --cleanup-feed
bin/magento saas:resync --feed products --cleanup-feed
bin/magento saas:resync --feed scopesCustomerGroup --cleanup-feed
bin/magento saas:resync --feed scopesWebsite --cleanup-feed
bin/magento saas:resync --feed prices --cleanup-feed
bin/magento saas:resync --feed productOverrides --cleanup-feed
bin/magento saas:resync --feed variants --cleanup-feed
bin/magento saas:resync --feed categories --cleanup-feed
bin/magento saas:resync --feed categoryPermissions --cleanup-feed
```

[Submit a support request](https://experienceleague.adobe.com/home?support-tab=home#support) to request reindex of the Live Search index. In the issue description, include your Data Space/Environment ID found in the admin panel under **[!UICONTROL System]** >  **[!UICONTROL Services]** > **[!UICONTROL Commerce Services Connector]**.

>[!IMPORTANT]
>Using the `--cleanup-feed` option in other cases can cause data loss and data sync issues.  Only use it when you have a new, empty environment,  after the Adobe team has completed a data space cleanup operation, or when you run the `saas:resync` command with the [--dry-run](https://experienceleague.adobe.com/en/docs/commerce/saas-data-export/data-export-cli-commands#--dry-run) option. Using the `--cleanup-feed` option in other cases can cause data loss and data sync issues.

## Related reading

* [Onboard Live Search](https://experienceleague.adobe.com/docs/commerce-merchant-services/live-search/onboard/onboarding-overview.html) in our user documentation
* [Review logs and troubleshoot Adobe Commerce SaaS data export and synchronization](https://experienceleague.adobe.com/en/docs/commerce-merchant-services/saas-data-export/troubleshooting-logging) in Adobe Commerce SaaS Data Export Guide
* [Best practices for modifying database tables](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/development/modifying-core-and-third-party-tables#why-adobe-recommends-avoiding-modifications) in the Commerce Implementation Playbook
