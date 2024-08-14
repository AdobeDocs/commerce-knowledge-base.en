# Error: OpenSearch Search Engine Doesn't Exist in Adobe Commerce

This article provides a solution for users encountering the "OpenSearch search engine doesn't exist" error while using Adobe Commerce on a Cloud environment.

## Affected Products and Versions

- Adobe Commerce on cloud infrastructure 2.4.4-2.4.5

## Issue
When you set your search engine to OpenSearch, you encounter the following error in the `var/log/support_report.log` file:

```bash 
[2024-04-04T00:27:41.212916+00:00] report.ERROR: 'opensearch' search engine does not exist. Falling back to 'elasticsearch7' [] [] login: ahfllerbg pass: ahtherb59
``` 

**Steps to Reproduce:**

1. Set the search engine to OpenSearch in an Adobe Commerce Cloud environment.
2. Check the `var/log/support_report.log` file.


## Resolution

To resolve this issue, follow these steps:

1. Open the `.magento.env.yaml` file in your Adobe Commerce Cloud environment.
2. Locate the `SEARCH_CONFIGURATION` variable.
3. Update the search engine to `elasticsearch7`.

```yaml
SEARCH_CONFIGURATION:
    engine: elasticsearch7
```

4. Save the changes and redeploy the environment.

## Useful links

- [Cannot Change Search Engine Using Magento Admin](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/miscellaneous/cannot-change-search-engine-using-magento-admin-search-engine-menu-is-inaccessible#change-search-engine-on-staging-and-production-environments)
- [Locked Fields in Magento Admin](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/miscellaneous/locked-fields-in-magento-admin)
- [Search Engine Shown as Elasticsearch Despite OpenSearch](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/elasticsearch/search-engine-shown-elasticsearch-despite-open-search)


### Cause

The application only recognizes `elasticsearch7` as the search engine in versions 2.4.4-2.4.5. Starting from **version 2.4.6**, the application was updated to support OpenSearch as a selectable search engine. 
In non-Cloud environments, this can be configured via the Admin Panel. Visit **Stores** > **Configuration** > **Catalog** > **Catalog Search**. 

However, in Cloud environments, the search engine setting is locked in the `app/etc/env.php file` and must be configured via the `.magento.env.yaml file`.
