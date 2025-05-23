---
title: Customer group names, segments, and promotional rule information exposed via [!DNL GraphQL]
description: This article provides a hotfix to prevent the exposure of customer group names, customer segments, and promotional rule information via [!DNL GraphQL].
feature: GraphQL
role: Admin, Developer
exl-id: 96cd2608-25db-4dac-a5f8-6437a54e3134
---
# Customer group names, segments, and promotional rule information exposed via [!DNL GraphQL]

This article provides a hotfix to prevent the exposure of customer group names, customer segments, and promotional rule information via [!DNL GraphQL]. The issue is scheduled to be fixed in Adobe Commerce 2.4.8-p1.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

* Adobe Commerce (all deployment methods) 2.4.8

**Compatible with Adobe Commerce versions:**

* Adobe Commerce (all deployment methods) 2.4.8

## Issue

For [!UICONTROL Storefront Personalization Drop-ins], new [!DNL GraphQL] mutations were introduced to display basic information like customer group names, segments, cart, and catalog rules. However, this can expose sensitive data such as offer details or coupon codes, if included in the names.

### Steps to reproduce

#### Case I: [!UICONTROL Catalog Rule]

1. On the *Admin* sidebar, go to **[!UICONTROL Marketing]** > **[!UICONTROL Catalog Price Rule]** > **[!UICONTROL Add New Rule]**.
1. Define the rule conditions (for example, product attribute or category).
1. Save and apply the rule.
1. Ensure a product meets the rule conditions.
1. Run the following [!DNL GraphQL] query to fetch all the rules:

    ```
    query {
        allCatalogRules {
            name
        }
    }
    ```
    
1. Query a product to verify if the rule applies:

    ```
    query {
        products(filter: { sku: { eq: "product-sku" } }) {
            items {
                name
                rules {
                    name
                }
            }
        }
    }
    ```

#### Case II: [!UICONTROL Cart Rule]

1. On the *Admin* sidebar, go to **[!UICONTROL Marketing]** > **[!UICONTROL Cart Price Rule]** > **[!UICONTROL Add New Rule]**.
1. Set conditions such as minimum cart value and customer group.
1. Save and apply the rule.
1. Add products to cart to trigger the rule.
1. Use [!DNL GraphQL] to verify all the cart rules:

    ```
    query {
        allCartRules {
            name
        }
    }
    ```

1. Check if rules are applied to the active cart:

    ```
    query {
        cart(cart_id: "your-cart-id") {
            rules {
                name
            }
        }
    }
    ```

#### Case III: [!UICONTROL Customer Group]

1. On the *Admin* sidebar, go to **[!UICONTROL Customers]** > **[!UICONTROL Customer Groups]**.
1. Verify that the expected groups exist.
1. Use [!DNL GraphQL] to fetch all groups:

    ```
    query {
        allCustomerGroups {
            name
        }
    }
    ```

1. Verify the customer/guest's group:

    ```
    query {
        customerGroup {
            name
        }
    }
    ```

#### Case IV: [!UICONTROL Customer Segment] (for Adobe Commerce only)

1. On the *Admin* sidebar, go to **[!UICONTROL Customers]** > **[!UICONTROL Customer Segments]** → **[!UICONTROL Add Segment]**.
1. Define customer-based conditions (for example, order, cart contents).
1. Assign applicable scope: *[!UICONTROL Visitor]*, *[!UICONTROL Registered]*, or both.
1. Ensure that the conditions match a test customer.
1. Use [!DNL GraphQL] to check all segments:

    ```
    query {
        allCustomerSegments {
            name
            apply_to
        }
    }
    ```

1. Validate the segments applied to a cart:

    ```
    query {
        customerSegments(cartId: "your-cart-id") {
            name
        }
    }
    ```

<u>Expected result</u>:

Names of customer groups, segments, and promotional rule information aren't exposed through [!DNL GraphQL].

<u>Actual result</u>:

Names of customer groups, segments, and promotional rule information are exposed through [!DNL GraphQL].

## Solution

Apply the attached patches depending on your Adobe Commerce version:

* For Adobe Commerce version 2.4.8:

    * [LYNX-839_CE_2.4.8.patch](assets/LYNX-839_CE_2.4.8.patch.zip)
    * [LYNX-839_EE_2.4.8.patch](assets/LYNX-839_EE_2.4.8.patch.zip)

* For [!DNL Magento] Open Source version 2.4.8:

    * [LYNX-839_CE_2.4.8.patch](assets/LYNX-839_CE_2.4.8.patch.zip)
