---
title: 'Falling back to [!DNL Elasticsearch7] when search engine set to [!DNL Opensearch]'
description: This article provides a solution for the issue when a *Falling back to [!DNL Elasticsearch7]* error occurs when the search engine is set to [!DNL OpenSearch] in Adobe Commerce.
feature: Search
role: Developer
---
# Falling back to [!DNL Elasticsearch7] when search engine set to [!DNL Opensearch]

This article provides a solution for the issue when a *Falling back to [!DNL Elasticsearch7]* error occurs whenn the search engine is set to [!DNL OpenSearch] in Adobe Commerce.

## Affected versions

Adobe Commerce on cloud infrastructure 2.4.4 - 2.4.5

>[!NOTE]
>
>[!DNL OpenSearch] is available as a search engine starting from Adobe Commerce 2.4.6.

## Issue

You set your **search engine** to **[!DNL OpenSearch]**, but see this type of error in the `var/log/support_report.log` file:

```[2024-04-04T00:27:41.212916+00:00] report.ERROR: opensearch search engine doesn't exist. Falling back to elasticsearch7 [] []```

<u>Steps to reproduce</u>:

1. Verify that [!DNL OpenSearch] is installed by running this command: `curl 127.0.0.1:9200`<br>
   If it indicates *1.2.4*, then [!DNL OpenSearch] is already installed.
1. Go to **[!UICONTROL Stores]** > **[!UICONTROL Configuration]** > **[!UICONTROL Catalog]** > **[!UICONTROL Catalog Search]**.
1. Check the search engine. It will show [!DNL Elasticsearch7].

## Cause

Even though your version does support [!DNL OpenSearch], the application will only recognize/accept [!DNL Elasticsearch7] as the search engine.

Starting in Adobe Commerce version 2.4.6, the application was updated to allow [!DNL OpenSearch] to be selected as the search engine.
If you go to **[!UICONTROL Stores]** > **[!UICONTROL Configuration]** > **[!UICONTROL Catalog]** > **[!UICONTROL Catalog Search]** in a non-cloud environment, you will be able to see this option.
(Note: in a cloud environment, this field can't be changed because the search engine is locked in the `app/etc/env.php` file.)

## Solution

Update the `SEARCH_CONFIGURATION` variable in the `.magento.env.yaml` file, and ensure that the **search engine** is set to *[!DNL elasticsearch7]*.

## Related reading

[Set up OpenSearch service](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/configure/service/opensearch.html) in the Commerce on Cloud Infrastructure guide.
 
