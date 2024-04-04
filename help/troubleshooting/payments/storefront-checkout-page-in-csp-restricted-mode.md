---
title: Troubleshoot storefront checkout page in [!UICONTROL CSP] restricted mode
description: This article explains errors you may experience while viewing checkout page in CSP restricted mode, and provides solutions to fix those errors.
feature: Checkout,Security,Orders,Payments
role: Developer
---

# Troubleshoot storefront checkout page in [!UICONTROL CSP] restricted mode

This article provides explanations and fixes for the Adobe Commerce 2.4.7 issues while viewing the checkout page in **[!UICONTROL CSP restricted mode]**, with the "*Refused to execute inline script because it violates the following Content Security Policy directive: "script-src ...*" error message in the browser console log.

## Affected products and versions

Adobe Commerce on cloud infrastructure, Adobe Commerce on-premises, and Magento Open Source:

* 2.4.7
* 2.4.6-pX
* 2.4.5-pX
* 2.4.4-pX

## Issue - Storefront Checkout page is broken or isn't able to load

The **storefont checkout** page is broken or isn't able to load, with the "*Refused to execute inline script because it violates the following Content Security Policy directive: "script-src ...*" error message in the browser console log.

<u>Steps to reproduce</u>:

1. Go to the storefront.
1. Add a product to the cart and proceed to the checkout.

<u>Expected results</u>:

The checkout page fully loads normally.

<u>Actual results</u>:

The checkout page is blank or is missing components. The following [!DNL JS] error is displayed in the browser console log: "*Refused to execute inline script because it violates the following Content Security Policy directive: "script-src ...*"

### Cause

In Adobe Commerce and Magento Open Source version 2.4.7 and later, **[!UICONTROL CSP]** is configured in `restrict-mode`, by default, for payment pages in the storefront and admin areas, and in `report-only` mode for all other pages.
The corresponding **[!UICONTROL CSP]** header does not contain the `unsafe-inline` keyword inside the `script-src` directive for payment pages. Also, only [!DNL whitelisted] inline scripts are allowed.

### Solution

Users might see browser errors due to certain scripts being blocked because of **[!UICONTROL CSP]**:

`Refused to execute inline script because it violates the following Content Security Policy directive: "script-src`

<u>To fix this issue, you must either</u>:

1. [[!DNL Whitelist]](https://developer.adobe.com/commerce/php/development/security/content-security-policies/#whitelist-an-inline-script-or-style) the blocked scripts using the `SecureHtmlRenderer` class.
1. Use the `CSPNonceProvider` class to allow scripts to be executed.
    Adobe Commerce and Magento Open Source 2.4.7 and later include a **[!UICONTROL Content Security Policy (CSP)]** [!DNL nonce] provider to facilitate the generation of unique [!DNL nonce] strings for each request.  These [!DNL nonce] strings are then attached to the [!UICONTROL CSP] header.
    
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

Payment method is missing or isn't working on the **storefront checkout** page, with the "*Refused to execute inline script because it violates the following Content Security Policy directive: "script-src ...*" error message in the browser console log.

<u>Steps to reproduce</u>:

1. Go to the storefront.
2. Add a product to the cart and proceed to the checkout.
3. Select a payment method.

<u>Expected results</u>:

You are able to select a payment method and proceed to place an order successfully.

<u>Actual results</u>:

The payment method is missing or isn't working. The following [!DNL JS] error is displayed in the browser console log: "*Refused to execute inline script because it violates the following Content Security Policy directive: "script-src ...*"

### Cause

In Adobe Commerce and Magento Open Source version 2.4.7 and later, **[!UICONTROL CSP]** is configured in `restrict-mode`, by default, for payment pages in the storefront and admin areas, and in `report-only` mode for all other pages.
The corresponding **[!UICONTROL CSP]** header does not contain the `unsafe-inline` keyword inside the `script-src` directive for payment pages. Also, only [!DNL whitelisted] inline scripts are allowed.

### Solution

Users might see browser errors due to certain scripts being blocked because of **[!UICONTROL CSP]**:

`Refused to execute inline script because it violates the following Content Security Policy directive: "script-src`

<u>To fix this issue, you must either</u>:

1. [[!DNL Whitelist]](https://developer.adobe.com/commerce/php/development/security/content-security-policies/#whitelist-an-inline-script-or-style) the blocked scripts using the `SecureHtmlRenderer` class.
1. Use the `CSPNonceProvider` class to allow scripts to be executed.
    Adobe Commerce and Magento Open Source 2.4.7 and later include a **[!UICONTROL Content Security Policy (CSP)]** [!DNL nonce] provider to facilitate the generation of unique [!DNL nonce] strings for each request.  These [!DNL nonce] strings are then attached to the [!UICONTROL CSP] header.
    
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

## Issue - Customer can't place an order

A customer isn't able to place an order, with the "*Refused to execute inline script because it violates the following Content Security Policy directive: "script-src ...*" error message in the browser console log.

<u>Steps to reproduce</u>:

1. Go to the storefront.
2. Add a product to the cart and proceed to the checkout.
3. Select a payment method.
4. Click **Place Order**.

<u>Expected results</u>:

You're able to place an order successfully.

<u>Actual results</u>:

You're not able to place an order. The following [!DNL JS] error is displayed in the browser console log: "*Refused to execute inline script because it violates the following Content Security Policy directive: "script-src ...*"

### Cause

In Adobe Commerce and Magento Open Source version 2.4.7 and later, **[!UICONTROL CSP]** is configured in `restrict-mode`, by default, for payment pages in the storefront and admin areas, and in `report-only` mode for all other pages.
The corresponding **[!UICONTROL CSP]** header does not contain the `unsafe-inline` keyword inside the `script-src` directive for payment pages. Also, only [!DNL whitelisted] inline scripts are allowed.

### Solution

Users might see browser errors due to certain scripts being blocked because of **[!UICONTROL CSP]**:

`Refused to execute inline script because it violates the following Content Security Policy directive: "script-src`

<u>To fix this issue, you must either</u>:

1. [[!DNL Whitelist]](https://developer.adobe.com/commerce/php/development/security/content-security-policies/#whitelist-an-inline-script-or-style) the blocked scripts using the `SecureHtmlRenderer` class.
1. Use the `CSPNonceProvider` class to allow scripts to be executed.
    Adobe Commerce and Magento Open Source 2.4.7 and later include a **[!UICONTROL Content Security Policy (CSP)]** [!DNL nonce] provider to facilitate the generation of unique [!DNL nonce] strings for each request.  These [!DNL nonce] strings are then attached to the [!UICONTROL CSP] header.
    
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
