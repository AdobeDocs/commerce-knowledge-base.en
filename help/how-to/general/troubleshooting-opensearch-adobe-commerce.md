# OpenSearch Not Recognized, Falling Back to Elasticsearch7

Adobe Commerce uses Elasticsearch or OpenSearch as the catalog search engine. Both Elasticsearch and OpenSearch are agile and powerful search engines that help you search your stored data more efficiently. 

But in Adobe Commerce versions **2.4.4** to **2.4.5**, many users have experienced an issue with **OpenSearch** where the system does not recognize it as a valid search engine, and as a result, the system defaults to *Elasticsearch7*, which may not align with your intended configuration.

This article will help you troubleshoot your issue of OpenSearch not being recognized in your Adobe Commerce environment by providing you with a step-by-step process.

## Issue

When trying to set OpenSearch as the search engine in Adobe Commerce versions **2.4.4** to **2.4.5** on Adobe Commerce Cloud, the following error is recorded.

*var/log/support_report.log*:

**[2024-04-04T00:27:41.212916+00:00] report.ERROR: opensearch search engine doesn't exist. Falling back to elasticsearch7 [] []**

### Steps to reproduce

1. Navigate to **Stores > Configuration > Catalog> Catalog Search**.

2. Check the search engine setting, and you'll see it's set to *Elasticsearch7*.

## Affected Versions: 
Adobe Commerce 2.4.4-2.4.5 on Adobe Commerce Cloud.
## Cause

The configuration of Adobe Commerce is hard-coded to utilize *Elasticsearch7* as its search engine. Regardless of the **OpenSearch** service being used in the backend, the application only recognizes *Elasticsearch7* as its search engine.

In non-cloud environments running version 2.4.6 or later, **OpenSearch** can be selected as the search engine if you go to **Stores > Configuration > Catalog > Catalog Search**. 

**Note:** However, in Cloud environments, the search engine configuration is locked in the *app/etc/env.php file.*

## Solution

To resolve this issue, ensure that the search engine is set to *elasticsearch7* in your environment configuration.

### Steps to Resolve

1. Open the **.magento.env.yaml** file located in your Adobe Commerce Cloud environment.

2. Once the file is opened, update the **SEARCH_CONFIGURATION** variable and make sure that the search engine is set to *elasticsearch7*.

3. After updating the **.magento.env.yaml** file, deploy the changes to your environment.

