---
description: Learn how to resolve Adobe Commerce defaulting to Elasticsearch7 when OpenSearch isn’t recognized as a search engine.
---

# Falling back to Elasticsearch7 despite OpenSearch configuration

This article explains how to fix the **Falling back to Elasticsearch7** error when OpenSearch is set as the search engine in Adobe Commerce due to a configuration limitation. 
 
## Affected versions

Adobe Commerce on cloud 2.4.4 - 2.4.5-p11

>**NOTE**  
>OpenSearch is available as a search engine starting from Adobe Commerce 2.4.6.

## Issue 
You set the search engine to OpenSearch, but the system shows this error in `var/log/support_report.log`:  
``[2024-04-04T00:27:41.212916+00:00] report.ERROR: opensearch search engine doesn't exist. Falling back to elasticsearch7 [] []``

### Steps to reproduce

1. Verify OpenSearch is installed.  
2. Go to **Stores > Configuration > Catalog > Catalog Search** and set the search engine to OpenSearch.
3. Check the search engine. It will show Elasticsearch7.
4. Open the `var/log/support_report.log` file and find the error message:
**OpenSearch search engine doesn't exist. Falling back to Elasticsearch7.**


## Resolution

Update the `SEARCH_CONFIGURATION` variable in the `.magento.env.yaml` file and set the engine to elasticsearch7.

## Cause 

Adobe Commerce supports OpenSearch, but versions 2.4.4 – 2.4.5 default to Elasticsearch7 due to system limitations.

Starting in version 2.4.6, OpenSearch can be selected in **Stores > Configuration > Catalog > Catalog Search** in non-cloud environments.

Note: In cloud environments, the search engine setting is locked in the `app/etc/env.php` file and cannot be changed. As a result, in earlier versions, the application defaults to Elasticsearch7, even if OpenSearch is configured.