---
title: Troubleshoot create order page in [!UICONTROL CSP] restricted mode
description: This article explains errors creating an order on the Admin side when CSP restricted mode is Enabled, and provides solutions to fix those errors.
feature: Checkout,Security,Orders,Payments
role: Developer
exl-id: c1a0886a-df1f-418a-9e4d-562b28a0d8b3
---
# Troubleshoot create order page in [!UICONTROL CSP] restricted mode

This article provides explanations and fixes for the Adobe Commerce 2.4.7 issues while creating an order on the Admin side with **[!UICONTROL CSP restricted mode]** is *Enabled*, with the "*Refused to execute inline script because it violates the following Content Security Policy directive: "script-src ...*" error message in the browser console log.

## Affected products and versions

Adobe Commerce on cloud infrastructure, Adobe Commerce on-premises, and Magento Open Source:

* 2.4.7
* 2.4.6-pX
* 2.4.5-pX
* 2.4.4-pX

## Issue - Admin **create order** page is broken or isn't able to load

The Admin **create order** page is broken or isn't able to load, with the "*Refused to execute inline script because it violates the following Content Security Policy directive: "script-src ...*" error message in the browser console log.

<u>Steps to reproduce</u>:

1. Go to **[!UICONTROL Sales]** > **[!UICONTROL Orders]**.
1. Create a new order.

<u>Expected results</u>:

The Admin **create order** page fully loads normally.

<u>Actual results</u>:

The Admin **create order** page is blank or missing components. The following [!DNL JS] error is displayed in the browser console log: "*Refused to execute inline script because it violates the following Content Security Policy directive: "script-src ...*"

### Cause

In Adobe Commerce and Magento Open Source version 2.4.7 and later, **[!UICONTROL CSP]** is configured in `restrict-mode`, by default, for payment pages in the storefront and admin areas, and in `report-only` mode for all other pages.
The corresponding **[!UICONTROL CSP]** header does not contain the `unsafe-inline` keyword inside the `script-src` directive for payment pages. Also, only [!DNL whitelisted] inline scripts are allowed.

### Solution

Users might see browser errors due to certain scripts being blocked because of [!UICONTROL CSP]:

`Refused to execute inline script because it violates the following [!UICONTROL Content Security Policy] directive: "script-src`

<u>To fix this issue, you must either</u>:

1. [[!DNL Whitelist]](https://developer.adobe.com/commerce/php/development/security/content-security-policies/#whitelist-an-inline-script-or-style) the blocked scripts using the `SecureHtmlRenderer` class.
1. Use the `CSPNonceProvider` class to allow scripts to be executed.
    Adobe Commerce and Magento Open Source 2.4.7 and later include a **[!UICONTROL Content Security Policy (CSP)]** [!DNL nonce] provider to facilitate the generation of unique [!DNL nonce] strings for each request. These [!DNL nonce] strings are then attached to the [!UICONTROL CSP] header.
    
    Use the `generateNonce` function in `Magento\Csp\Helper\CspNonceProvider` to obtain a [!DNL nonce] string.
    
    ```php
    use Magento\Csp\Helper\CspNonceProvider;
    
    class MyClass
    {
    
        /**
         * @var CspNonceProvider
         */
        private $cspNonceProvider;
    
        /**
         * @param CspNonceProvider $cspNonceProvider
         */
        public function __construct(CspNonceProvider $cspNonceProvider)
        {
            $this->cspNonceProvider = $cspNonceProvider
        }
    
        /**
         * Get CSP Nonce
         *
         * @return String
         */
        public function getNonce(): string
        {
            return $this->cspNonceProvider->generateNonce();
        }
    }
    ```
   
1. [Add a [!DNL hash]](https://developer.adobe.com/commerce/php/development/security/content-security-policies/#using-inline-scripts-and-styles-is-discouraged-in-favor-of-ui-components-and-classes) to your module's `csp_whitelist.xml` file.

## Issue - Payment method is missing or isn't working

Payment method is missing or not working on the Admin **order create page**, with the "*Refused to execute inline script because it violates the following Content Security Policy directive: "script-src ...*" error message in the browser console log.

<u>Steps to reproduce</u>:

1. Go to **[!UICONTROL Sales]** > **[!UICONTROL Orders]**.
1. Create a new order.
1. Create a new customer.
1. Enter the customer details.
1. Enter the order details (products, shipping method).
1. Select a payment method.

<u>Expected results</u>:

You are able to select a payment method and proceed to place an order successfully.

<u>Actual results</u>:

The payment method is missing or not working. The following [!DNL JS] error is displayed in the browser console log: "*Refused to execute inline script because it violates the following Content Security Policy directive: "script-src ...*".

### Cause

In Adobe Commerce and Magento Open Source version 2.4.7 and later, **[!UICONTROL CSP]** is configured in `restrict-mode`, by default, for payment pages in the storefront and admin areas, and in `report-only` mode for all other pages.
The corresponding **[!UICONTROL CSP]** header does not contain the `unsafe-inline` keyword inside the `script-src` directive for payment pages. Also, only [!DNL whitelisted] inline scripts are allowed.

### Solution

Users might see browser errors due to certain scripts being blocked because of **[!UICONTROL CSP]**:

`Refused to execute inline script because it violates the following [!UICONTROL Content Security Policy] directive: "script-src`

<u>To fix this issue, you must either</u>:

1. [[!DNL Whitelist]](https://developer.adobe.com/commerce/php/development/security/content-security-policies/#whitelist-an-inline-script-or-style) the blocked scripts using the `SecureHtmlRenderer` class.
1. Use the `CSPNonceProvider` class to allow scripts to be executed.
    Adobe Commerce and Magento Open Source 2.4.7 and later include a **[!UICONTROL Content Security Policy (CSP)]** [!DNL nonce] provider to facilitate the generation of unique [!DNL nonce] strings for each request. These [!DNL nonce] strings are then attached to the [!UICONTROL CSP] header.
    
    Use the `generateNonce` function in `Magento\Csp\Helper\CspNonceProvider` to obtain a [!DNL nonce] string.
    
    ```php
    use Magento\Csp\Helper\CspNonceProvider;
    
    class MyClass
    {
    
        /**
         * @var CspNonceProvider
         */
        private $cspNonceProvider;
    
        /**
         * @param CspNonceProvider $cspNonceProvider
         */
        public function __construct(CspNonceProvider $cspNonceProvider)
        {
            $this->cspNonceProvider = $cspNonceProvider
        }
    
        /**
         * Get CSP Nonce
         *
         * @return String
         */
        public function getNonce(): string
        {
            return $this->cspNonceProvider->generateNonce();
        }
    }
    ```
  
1. [add a [!DNL hash]](https://developer.adobe.com/commerce/php/development/security/content-security-policies/#using-inline-scripts-and-styles-is-discouraged-in-favor-of-ui-components-and-classes) to your module's `csp_whitelist.xml` file.

## Issue - Admin can't place an order

An admin can't submit an order on the Admin **create order page**, with the "*Refused to execute inline script because it violates the following Content Security Policy directive: "script-src ...*" error message in the browser console log.

<u>Steps to reproduce</u>:

1. Go to **[!UICONTROL Sales]** > **[!UICONTROL Orders]**.
1. Create a new order.
1. Create a new customer.
1. Enter the customer details.
1. Enter the order details (products, shipping method).
1. Select a payment method.
1. Submit the order.

<u>Expected results</u>:

You're able to submit an order successfully.

<u>Actual results</u>:

You're not able to submit an order. The following [!DNL JS] error is displayed in the browser console log: "*Refused to execute inline script because it violates the following Content Security Policy directive: "script-src ...*"

### Cause

In Adobe Commerce and Magento Open Source version 2.4.7 and later, **[!UICONTROL CSP]** is configured in `restrict-mode`, by default, for payment pages in the storefront and admin areas, and in `report-only` mode for all other pages.
The corresponding **[!UICONTROL CSP]** header does not contain the `unsafe-inline` keyword inside the `script-src` directive for payment pages. Also, only [!DNL whitelisted] inline scripts are allowed.

### Solution

Users might see browser errors due to certain scripts being blocked because of **[!UICONTROL CSP]**:

`Refused to execute inline script because it violates the following [!UICONTROL Content Security Policy] directive: "script-src`

<u>To fix this issue, you must either</u>:

1. [[!DNL Whitelist]](https://developer.adobe.com/commerce/php/development/security/content-security-policies/#whitelist-an-inline-script-or-style) the blocked scripts using the `SecureHtmlRenderer` class.
1. Use the `CSPNonceProvider` class to allow scripts to be executed.
    Adobe Commerce and Magento Open Source 2.4.7 and later include a **[!UICONTROL Content Security Policy (CSP)]** [!DNL nonce] provider to facilitate the generation of unique [!DNL nonce] strings for each request. These [!DNL nonce] strings are then attached to the [!UICONTROL CSP] header.
    
    Use the `generateNonce` function in `Magento\Csp\Helper\CspNonceProvider` to obtain a [!DNL nonce] string.
    
    ```php
    use Magento\Csp\Helper\CspNonceProvider;
    
    class MyClass
    {
    
        /**
         * @var CspNonceProvider
         */
        private $cspNonceProvider;
    
        /**
         * @param CspNonceProvider $cspNonceProvider
         */
        public function __construct(CspNonceProvider $cspNonceProvider)
        {
            $this->cspNonceProvider = $cspNonceProvider
        }
    
        /**
         * Get CSP Nonce
         *
         * @return String
         */
        public function getNonce(): string
        {
            return $this->cspNonceProvider->generateNonce();
        }
    }
    ```
  
1. [Add a [!DNL hash]](https://developer.adobe.com/commerce/php/development/security/content-security-policies/#using-inline-scripts-and-styles-is-discouraged-in-favor-of-ui-components-and-classes) to your module's `csp_whitelist.xml` file.
