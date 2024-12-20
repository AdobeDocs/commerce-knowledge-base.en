# Reverting to Elasticsearch7 when OpenSearch is set as the search engine in Adobe Commerce

This article explains how to resolve the issue when **OpenSearch** is set as the **search engine** in Adobe Commerce, but it reverts to **Elasticsearch7**.

## Affected versions

- Adobe Commerce on Cloud 2.4.4-2.4.5

## Issue

You have set your **search engine** to **OpenSearch**, but the following error appears in the `var/log/support_report.log` file:

```
[2024-04-04T00:27:41.212916+00:00] report.ERROR: opensearch search engine doesn't exist. Falling back to elasticsearch7 [] []
```

## Cause

Although Adobe Commerce versions 2.4.4 and 2.4.5 support **OpenSearch**, but the application only recognizes **Elasticsearch7** as the valid **search engine**.

**Note:** OpenSearch is available as a search engine starting from Adobe Commerce version 2.4.6.

## Solution

To resolve the issue, update the `SEARCH_CONFIGURATION` variable in the `.magento.env.yaml` file to specify **elasticsearch7** as the **search engine**. Follow these steps:

1. Open the `.magento.env.yaml` file in your application.
2. Locate the `SEARCH_CONFIGURATION` variable.
3. Set the **search engine** to **elasticsearch7**:

    ```yaml
    SEARCH_CONFIGURATION:
      engine: elasticsearch7
    ```

4. Save the file.
5. Deploy the updated configuration to your environment.

## Related articles

- [Adobe Commerce on cloud infrastructure](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/miscellaneous/cannot-change-search-engine-using-magento-admin-search-engine-menu-is-inaccessible#adobe-commerce-on-cloud-infrastructure)
- [Locked (grayed out) fields in Commerce Admin](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/miscellaneous/locked-fields-in-magento-admin)
- [Elasticsearch is shown as the search engine despite OpenSearch installation](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/elasticsearch/search-engine-shown-elasticsearch-despite-open-search)
