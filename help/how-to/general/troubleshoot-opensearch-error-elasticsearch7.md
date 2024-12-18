# Resolving OpenSearch Error in Adobe Commerce cloud Versions 2.4.4-2.4.5

This article provides a solution to resolve the error that occurs when using the **OpenSearch** search engine in **Adobe Commerce Cloud Versions 2.4.4-2.4.5**.

## Description

The **error** occurs when you attempt to set the **search engine** to **OpenSearch**.

_Error Details_
- **file name**: var/log/support_report.log
- **Error**: OpenSearch engine doesn't exist. Falling back to Elasticsearch7.

_Steps to Reproduce_
1.	Go to **Stores > Configuration > Catalog > Catalog Search.**
2.	The search engine is updated to **Elasticsearch7**.

_Affected Products and Versions_
- Adobe Commerce Cloud 2.4.4-2.4.5


## Solution

Steps to resolve the search engine issue:
1.	Open **.magento.env.yaml** file.
2.	Locate **SEARCH_CONFIGURATION** variable.
3.	Update search engine to **Elasticsearch7**.
4.	Save the file.

_Useful Links_

•	[Cannot change search engine using Magento Admin](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/miscellaneous/cannot-change-search-engine-using-magento-admin-search-engine-menu-is-inaccessible#adobe-commerce-on-cloud-infrastructure)

•	[Located fields in Commerce Admin]( https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/miscellaneous/locked-fields-in-magento-adminA)

•	[ElasticSearch shown as the Search engine despite OpenSearch installation]( https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/elasticsearch/search-engine-shown-elasticsearch-despite-open-search)

### Cause

The Adobe Commerce 2.4.4 and 2.4.5 clearly support **OpenSearch**, but the application only recognizes **Elasticsearch7** as its configured search engine.
>**Note:** Adobe Commerce Version 2.4.6 supports the *OpenSearch* search engine.
