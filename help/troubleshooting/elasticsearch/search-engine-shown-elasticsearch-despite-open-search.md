---
title: '[!DNL Elasticsearch] is shown as the search engine despite [!DNL OpenSearch] installation'
description: This article provides a solution for the issue where [!DNL Elasticsearch] is still shown as the search engine for Adobe Commerce on cloud even after installing or upgrading to [!DNL OpenSearch].
exl-id: cdd8a35d-da6f-46d3-b732-65626487c9bb
---
# [!DNL Elasticsearch] is shown as the search engine despite [!DNL OpenSearch] installation

This article provides a solution for the issue where [!DNL Elasticsearch] is still shown as the search engine for Adobe Commerce on cloud even after installing or upgrading to [!DNL OpenSearch].

## Affected versions

Adobe Commerce on cloud (all versions)

## Issue

[!DNL Elasticsearch] is still shown as the search engine for Adobe Commerce on cloud even after installing or upgrading to [!DNL OpenSearch].

<u>Steps to reproduce</u>:

1. Go to **[!UICONTROL Stores]** > **[!UICONTROL Configuration]** > **[!UICONTROL Catalog]** > **[!UICONTROL Catalog Search]**.
1. Check the search engine. It will show [!DNL Elasticsearch7].

## Cause

Adobe Commerce is hard-coded to specify [!DNL Elasticsearch7] as the search engine.

## Solution

To verify if [!DNL OpenSearch] has been installed, run the following command:

**Method 1**:

* Run the following command on server: `curl 127.0.0.1:9200`. It should return [!DNL OpenSearch] with its version.

**Method 2**:

* Use the following command on the Magento-cloud CLI: `magento-cloud relationships -p <project_id>`. After using the command, locate [!DNL OpenSearch].

## Related reading

[Set up OpenSearch service](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/configure/service/opensearch.html) in the Commerce on Cloud Infrastructure guide.
