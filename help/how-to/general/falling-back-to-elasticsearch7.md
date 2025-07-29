# Falling back to Elasticsearch7 when OpenSearch is set as the search engine in Adobe Commerce

This article explains how to resolve the issue where Adobe Commerce reverts to **Elasticsearch7** when **OpenSearch** is set as the **search engine**.

## Affected versions

Adobe Commerce on cloud 2.4.4 - 2.4.5

>**NOTE**  
>OpenSearch is available as a search engine starting from Adobe Commerce 2.4.6.
>
## Issue

You have set your **search engine** to **OpenSearch**, but the system shows following error in the `var/log/support_report.log` file:

```
[2024-04-04T00:27:41.212916+00:00] report.ERROR: opensearch search engine doesn't exist. Falling back to elasticsearch7 [] []
```

### Steps to reproduce:

1. Verify OpenSearch is installed.  
2. Go to **Stores > Configuration > Catalog > Catalog Search** and set the search engine to **OpenSearch**.
3. Check the search engine. It will show Elasticsearch7.
4. Open the `var/log/support_report.log` file and find the error message:
**OpenSearch search engine doesn't exist. Falling back to Elasticsearch7.**



## Cause

Although Adobe Commerce versions 2.4.4 and 2.4.5 support **OpenSearch**, but the application only recognizes **Elasticsearch7** as the valid **search engine** due to limitations.


Starting with version 2.4.6, you can select **OpenSearch** in **Stores > Configuration > Catalog > Catalog Search** on non-cloud environments.

Note: In cloud environment, the search engine setting is locked in the `app/etc/env.php` file and cannot be changed.



## Solution

Update the `SEARCH_CONFIGURATION` variable in the `.magento.env.yaml` file, and set the **search engine** to *elasticsearch7*.


## Related articles
- [Adobe Commerce on cloud infrastructure](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/miscellaneous/cannot-change-search-engine-using-magento-admin-search-engine-menu-is-inaccessible#adobe-commerce-on-cloud-infrastructure)
- [Elasticsearch is shown as the search engine despite OpenSearch installation](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/elasticsearch/search-engine-shown-elasticsearch-despite-open-search)
