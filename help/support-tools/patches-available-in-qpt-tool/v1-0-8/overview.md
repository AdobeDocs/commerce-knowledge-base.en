---
title: 'Overview: [!DNL Quality Patches Tool] (QPT) v1.0.8'
description: This sub-section provides a detailed description of the issues fixed by the patches available in [!DNL Quality Patches Tool] (QPT) v1.0.8.
exl-id: 6cd3eabe-067f-4e80-b17f-561290499261
---
# [!DNL Quality Patches Tool] (QPT) v1.0.8 overview

This sub-section provides a detailed description of the issues fixed by the patches available in [!DNL Quality Patches Tool] (QPT) v1.0.8.

QPT v1.0.8 includes the following patches:

1. **MDVA-28357**: Replaces the standard analyzer with a custom analyzer with keyword tokenizer for the SKU field in the [!DNL ElasticSearch] index to make wildcard search queries work with SKUs containing a hyphen ("-").
1. **MDVA-29954**: Fixes the issue where the *New Company Registration Request* and *You've been linked to a company* emails are sent from the wrong address.
1. **MDVA-30112**: Fixes the issue where if the number of orders exceeds the *bunch-size* value, Adobe Commerce considers the orders with *pending* status as inconsistencies.
1. **MDVA-30963**: Fixes the issue where products filtering results set to only contain values specified for *All store views* scope in the Admin, include products with values overridden on the store view level.
1. **MDVA-31150**: Fixes the issue where the store credit and gift card balances are not returned by the GET Invoice Rest API call, when the invoice was posted by Rest API call and the order was partially paid by store credit and gift card accounts.
1. **MDVA-31242**: Fixes the issue where a wrong currency sign is displayed in [!UICONTROL Credit Memo] grid.
1. **MDVA-31295**: Fixes the issue where reward points are not calculated when a partial order is completed and items are taxed.

Use the menu on the left to navigate to a specific patch page.
