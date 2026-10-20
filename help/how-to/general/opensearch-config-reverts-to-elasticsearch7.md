---
description: Learn how to resolve an issue where Adobe Commerce uses Elasticsearch7 even when OpenSearch is selected as the search engine.
---

# OpenSearch configuration falls back to Elasticsearch7

This article describes how to address the **fallback to Elasticsearch7** issue that occurs when OpenSearch is chosen as the search engine in Adobe Commerce, but the application cannot recognize it due to configuration constraints.

## Affected versions

Adobe Commerce on cloud infrastructure  
Versions **2.4.4 – 2.4.5-p11**

> **Note**  
> Beginning with Adobe Commerce **2.4.6**, OpenSearch becomes available for selection in non-Cloud environments.

## Issue

After configuring OpenSearch as the search engine, the following message appears in the `var/log/support_report.log` file:`[2024-04-04T00:27:41.212916+00:00] report.ERROR: opensearch search engine doesn't exist. Falling back to elasticsearch7 [] []`

### Steps to reproduce

1. Ensure that OpenSearch is available in your environment.  
2. Navigate to **Stores > Configuration > Catalog > Catalog Search** and attempt to switch the search engine to OpenSearch.  
3. Review the search engine field — it continues to show **Elasticsearch7**.  
4. Open the `var/log/support_report.log` file and locate the fallback error entry:
   **opensearch search engine doesn't exist. Falling back to elasticsearch7.**

## Resolution

To resolve this behavior, update the deployment configuration so that the search engine is explicitly set to Elasticsearch7.

Modify your `.magento.env.yaml` file and update the `SEARCH_CONFIGURATION` variable to use: `elasticsearch7`

Redeploy the Cloud environment after applying the change.

## Cause

Although Adobe Commerce 2.4.4 – 2.4.5 includes OpenSearch support at the application level, Cloud-based installations during these versions still rely on **Elasticsearch7** as the only supported search engine.

From Adobe Commerce **2.4.6** onward, OpenSearch can be selected within **Catalog Search** settings in non-Cloud setups.  
In Cloud environments, however, the search engine option is locked because its value is managed within: `app/etc/env.php`

As a result, in earlier versions the system defaults back to Elasticsearch7 even when OpenSearch is configured.
