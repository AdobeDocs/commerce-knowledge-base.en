
# Elasticsearch appears as the search engine despite OpenSearch being configured

This article provides a solution for the issue where Elasticsearch remains the displayed search engine in Adobe Commerce on Cloud, despite OpenSearch being configured as the search engine.

In this article:
- [Affected Versions](#affected-versions)
- [Issue](#issue)
- [Cause](#cause)
- [Solution](#solution)
     - [Check selected search engine](#check-selected-search-engine)
     - [Update the Search Configuration Variable](#update-the-search-configuration-variable)
- [Related documentation](#related-documentation) 

## Affected Versions
* Adobe Commerce on cloud 2.4.4 - 2.4.5

## Issue 

When configuring the search engine to OpenSearch, the following error appears in `var/log/support_report.log`:
```
[2024-04-04T00:27:41.212916+00:00] report.ERROR: opensearch search engine doesn't exist. Falling back to elasticsearch7 [] []
```
## Cause

While versions 2.4.4 to 2.4.5 support OpenSearch, the application only recognizes Elasticsearch7 as the search engine. In version 2.4.6, the ability to configure OpenSearch directly was added, but in Adobe Commerce Cloud environments, this setting remains locked in the `app/etc/env.php file`.
> **Note:** OpenSearch is available as a search engine only starting from Adobe Commerce 2.4.6
## Solution

### Check selected search engine

1. Log in to the **Admin** as an Administrator.
2. On the left-side of the Admin sidebar, click on **Stores**.
3. Under **Settings**, choose **Configuration**.
4. Navigate to the panel on the left under Catalog, and choose **Catalog**.
![media_164c1b56c392bb64697a04560429c4de131af948c](https://github.com/user-attachments/assets/04367845-1440-4648-851b-cbef8b472316)

5. Expand the **Catalog Search** section.
6. Check  **Search Engine**.
![Screenshot 2025-01-17 115924 png](https://github.com/user-attachments/assets/eae18d23-fff0-4d19-a525-d04702e4441e)

8. Set the **Search Engine** to elasticsearch.
![Screenshot 2025-01-17 120401](https://github.com/user-attachments/assets/ecf4db6f-0ce8-4200-88a0-7fdb0a04d2d6)

> **Note:** In a cloud environment, this setting cannot be modified as the search engine is locked in the `app/etc/env.php` file, and hence the `SEARCH_CONFIGURATION` variable in the `.magento.env.yaml` file must be updated.

### Update the Search Configuration Variable
 
To update the search engine used on your Staging and Production environments, change the `SEARCH_CONFIGURATION` environment variable in your `.magento.env.yaml` file on your local environment, then push changes to the Integration and Staging/Production environments for the changes to take effect.

Perform the below steps to update the `SEARCH_CONFIGURATION` Variable,

1. Open the `.magento.env.yaml` file.
2. Locate the `SEARCH_CONFIGURATION` variable.
3. Make sure that the `SEARCH_CONFIGURATION` variable in the `.magento.env.yaml` file looks as follows:
```yaml
stage:
  deploy:
   SEARCH_CONFIGURATION:
     engine: elasticsearch7
     elasticsearch_server_hostname: hostname
     elasticsearch_server_port: '12345'
     elasticsearch_index_prefix: magento
     elasticsearch_server_timeout: '15'
```
4. Save the file.
5. Push the changes into production environment.

## Related documentation
* [Enable Elasticsearch on Cloud](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/how-to/enable-elasticsearch-on-cloud)
* [Elasticsearch service not running](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/elasticsearch/elasticsearch-service-not-running)
