---
title: '[!DNL Elasticsearch] is shown as the search engine despite [!DNL OpenSearch] installation'
description: This article provides a solution for the issue where [!DNL Elasticsearch] is still shown as the search engine for Adobe Commerce on cloud even after installing or upgrading to [!DNL OpenSearch].
exl-id: cdd8a35d-da6f-46d3-b732-65626487c9bb
feature: Install
---
# [!DNL Elasticsearch] is shown as the search engine despite [!DNL OpenSearch] installation

This article provides a solution for the issue where [!DNL Elasticsearch] is still shown as the search engine for Adobe Commerce on cloud even after installing or upgrading to [!DNL OpenSearch].

## Affected versions

Adobe Commerce on cloud 2.4.4 - 2.4.5-p11

>[!NOTE]
>
>[!DNL OpenSearch] is available as a search engine starting from Adobe Commerce 2.4.6.

## Issue

[!DNL Elasticsearch] is still shown as the search engine for Adobe Commerce on cloud even after installing or upgrading to [!DNL OpenSearch].

<u>Steps to reproduce</u>:

1. Go to **[!UICONTROL Stores]** > **[!UICONTROL Configuration]** > **[!UICONTROL Catalog]** > **[!UICONTROL Catalog Search]**.
1. Check the search engine. It will show [!DNL Elasticsearch7].

## Cause

[!DNL Elasticsearch7] is hard-coded in Adobe Commerce to be the search engine used in these versions. Even though there isn't an [!DNL Opensearch] module included in the code, Adobe Commerce is able to make use of the underlying [!DNL Opensearch] service.

This is not to be confused with the installed version of the service. The application only recognizes [!DNL Elasticsearch7] as the search engine but not [!DNL OpenSearch], even though it uses the underlying [!DNL OpenSearch] service as the engine in the backend.

## Solution

To verify if [!DNL OpenSearch] has been installed, run the following command:

**Method 1**:

* Run the following command on server: `curl 127.0.0.1:9200`. It should return [!DNL OpenSearch] with its version.

Example:

```
$ curl 127.0.0.1:9200
{
  "name" : $clusterName,
  "cluster_name" : "opensearch_stg",
  "cluster_uuid" : $clusterUuid,
  "version" : {
    "distribution" : "opensearch",
    "number" : "1.2.4",
    "build_type" : "deb",
    "build_hash" : "44ccdbaed5fe5a8b02d99a611857a671b6dd909d",
    "build_date" : "2022-11-08T09:23:45.993372Z",
    "build_snapshot" : false,
    "lucene_version" : "8.10.1",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "The OpenSearch Project: https://opensearch.org/"
}
```

**Method 2**:

* Use the following command on the Magento-cloud CLI: `magento-cloud relationships -p <project_id>`. After using the command, locate [!DNL OpenSearch].

## Related reading

[Set up OpenSearch service](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/configure/service/opensearch.html) in the Commerce on Cloud Infrastructure guide.
