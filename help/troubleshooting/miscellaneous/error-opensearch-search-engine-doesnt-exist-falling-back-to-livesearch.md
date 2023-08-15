---
title: "Error "[!DNL opensearch] search engine doesn't exist. Falling back to [!DNL livesearch].""
description: This article provides a solution to the issue where you see the error, `Error- [!DNL opensearch] search engine doesn't exist. Falling back to [!DNL livesearch].`, in Adobe Commerce on cloud infrastructure.
feature: Deploy, Search
role: Developer
---

# Error "[!DNL opensearch] search engine doesn't exist. Falling back to [!DNL livesearch]."

This article provides a solution to the issue where you see the error: *Error: [!DNL opensearch] search engine doesn't exist. Falling back to [!DNL livesearch].* in Adobe Commerce on cloud infrastructure.

## Affected products and versions

* Adobe Commerce on cloud infrastructure, all versions

## Issue

The following message is shown in the logs (and observable in [!DNL New Relic]): 
*Error: [!DNL opensearch] search engine doesn't exist. Falling back to [!DNL livesearch].*

## Solution

1. Modify the `.magento.env.yaml` file.
1. Locate the following lines:

    ```yaml
      deploy:
    ...
        SEARCH_CONFIGURATION:
          engine: opensearch
    ```

1. If you don't have these lines, add them to the `.magento.env.yaml` file.
1. If these lines exist, **modify the engine** from *[!DNL opensearch]* to *[!DNL livesearch]*.
1. Commit the change and then redeploy.

## Related reading

* [Install [!DNL Live Search]](https://experienceleague.adobe.com/docs/commerce-merchant-services/live-search/onboard/install.html) in our Live Search Guide
