---
title: Issues after disabling a module
description: This article provides a solution for module functionality issues after having disabled module output in the Commerce Admin.
exl-id: 517f6993-f09e-4a94-8c57-175ecf9a98a8
feature: Extensions
role: Developer
---
# Issues after disabling a module

This article provides a solution for module functionality issues after having disabled module output in the Commerce Admin.

## Affected products and versions

* Adobe Commerce on cloud infrastructure 2.1.X or earlier
* Adobe Commerce on-premises 2.1.X or earlier

## Issue

Having disabled module output in the Commerce Admin, under **Stores** > **Settings** > **Configuration** > ADVANCED > **Advanced**, you might start seeing issues related to the module functionality.

## Cause

Disabling a module output under **Stores** > **Settings** > **Configuration** > ADVANCED > **Advanced** disables only the output (HTML, JS), but it does not disable the functionality of this module.

## Solution

If you need to disable module functionality, disable the module as described in [Enable or disable modules](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/tutorials/manage-modules) in our developer documentation.

The module output disabling functionality was removed starting from version 2.2.0.
