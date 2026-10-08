---
title: How to bypass WAF for GraphQL requests
description: This article explains how to bypass WAF for GraphQL requests.
feature: GraphQL
exl-id: 3a0f2c22-f976-4596-b6a9-4634be1ea4c3
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: c32adafa-ed01-4b31-997e-2413013911b0
    internal-label: Integrations
subfeature_v2:
  - id: e396cff5-f586-484c-89f0-7f1da3308f92
    internal-label: GraphQL
---
# How to bypass WAF for GraphQL requests

This article explains how to bypass WAF for GraphQL requests when the [!DNL Fastly] WAF is blocking your GraphQL requests.

## Affected products and versions 

Adobe Commerce on cloud infrastructure (all versions)

## Cause

Due to the inherent nature of GraphQL requests, there can be a lot of repeated characters that can trigger false positive blocking of the requests by the [!DNL Fastly] WAF.

## Solution

1. Bypass the WAF for these requests by adding a custom snippet through the [!DNL Fastly] Magento module:

    type: recv
    priority: 15
    content:
    
    ```
    if( req.url.path ~ "^/graphql" ) {
        set req.http.bypasswaf = "1";
    }
    ```

1. Click on **[!UICONTROL Upload VCL to Fastly]**.

## Related reading

* [Web Application Firewall (WAF)](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/cdn/fastly-waf-service) in Commerce on Cloud Infrastructure guide.
* [Getting started with custom VCL](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/cdn/custom-vcl-snippets/fastly-vcl-custom-snippets) in Commerce on Cloud Infrastructure guide.
