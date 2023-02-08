---
title: Search engine shows [!DNL Elasticsearch] despite [!DNL OpenSearch] installation
description: 'This topic describes how to fix the issue where the search engine is shown as [!DNL Elasticsearch] even after installing or upgrading to [!DNL OpenSearch].'
---
# Search engine shows [!DNL Elasticsearch] despite [!DNL OpenSearch] installation

This topic describes how to fix the issue where the search engine is shown as [!DNL Elasticsearch] even after installing or upgrading to [!DNL OpenSearch].

## Affected versions

Adobe Commerce on cloud (all versions)

## Issue

The search engine continues to show [!DNL Elasticsearch7] even after installing/upgrading to [!DNL OpenSearch].

<u>Steps to reproduce</u>:

1. Go to **[!UICONTROL Stores]** > **[!UICONTROL Configuration]** > **[!UICONTROL Catalog]** > **[!UICONTROL Catalog Search]**.
1. Check the search engine. It will show [!DNL Elasticsearch7].

## Cause

Adobe Commerce is hard-coded to specify [!DNL Elasticsearch] as the search engine.

## Solution

To verify if [!DNL OpenSearch] has been installed, run the following command:

1. Use this command on server: `curl 127.0.0.1:9200`. It should return [!DNL OpenSearch] with its version.
1. Use the following command on the Magento-cloud CLI: `magento-cloud relationships -p <project_id>`. After using the command, locate [!DNL OpenSearch].

## Related reading

[Set up OpenSearch service](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/configure/service/opensearch.html) in the Commerce on Cloud Infrastructure guide.



