---
title: Installation xdebug maximum function nesting level error
description: This article provides a fix for the xdebug maximum function nesting level error during installation.
exl-id: 1f64a9bb-59a7-41df-92a4-890d9d32bcbe
feature: Install
role: Developer
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: 6388cf7b-8a81-5248-a1e4-7bb57bbe250f
    internal-label: Install
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Installation xdebug maximum function nesting level error

This article provides a fix for the xdebug maximum function nesting level error during installation.

## Details

During Adobe Commerce installation, a message similar to the following displays:

 `PHP Fatal error: Maximum function nesting level of '100' reached, aborting! in <path>/ClassLoader.php`

It is strongly recommended that you DO NOT USE `xdebug` on a Production environment!

## Solution

There is a known issue with `xdebug` that can affect Adobe Commerce installations or access to the storefront or Commerce Admin after installation.

For details, see [Known issue with xdebug](/help/troubleshooting/miscellaneous/known-issues-that-affect-installation.md) in our support knowledge base.
