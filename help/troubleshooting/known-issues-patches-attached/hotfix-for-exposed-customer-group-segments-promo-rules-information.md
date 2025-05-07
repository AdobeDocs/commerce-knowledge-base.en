---
title: Customer groups, segments, and promotional rule information exposed via GraphQL
description: This article provides a hotfix to prevent the exposure of customer groups, segments, and promotional rule information via GraphQL in Adobe Commerce.
feature: GraphQL
role: Admin, Developer
---

# Customer groups, segments, and promotional rule information exposed via GraphQL

This article provides a hotfix to prevent the exposure of customer group names, customer segments, and promotional rule information via GraphQL. The issue is scheduled to be fixed in Adobe Commerce 2.4.8-p1.

## Affected products and versions

* The patch is created for Adobe Commerce version 2.4.8
* Compatible with Adobe Commerce versions 2.4.8

## Issue

For **[!UICONTROL Storefront Personalization Drop-ins]**, new GraphQL mutations introduced to display basic information such as customer group names, segments, and cart or catalog rules, can expose sensitive data added in the names.

<u>Steps to reproduce</u>:

Case I: **[!UICONTROL Catalog Rule]**

    1. Navigate to *Admin* > **[!UICONTROL Marketing]** > **[!UICONTROL Catalog Price Rule]** > **[!UICONTROL Add New Rule]**.
    1. Define the rule conditions (for example, product attribute or category).
    1. Save and apply the rule.
    1. Ensure a product meets the rule conditions.
    1. Run the following GraphQL query to fetch all the rules:

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

Case II: **[!UICONTROL Cart Rule]**

    1. Navigate to *Admin* > **[!UICONTROL Marketing]** > **[!UICONTROL Cart Price Rule]** > **[!UICONTROL Add New Rule]**.
    1. Set conditions such as minimum cart value and customer group.
    1. Save and apply the rule.
    1. Add products to cart to trigger the rule.
    1. Use GraphQL to verify all the cart rules:

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

Case III: **[!UICONTROL Customer Group]**

    1. Navigate to Admin → Customers → Customer Groups.
    1. Verify that expected groups exist.
    1. Use GraphQL to fetch all groups:

        ```
        query {
            allCustomerGroups {
                name
            }
        }
        ```

    1. Verify customer/guest's group:

        ```
        query {
            customerGroup {
                name
            }
        }
        ```

Case IV: **[!UICONTROL Customer Segment]** (for Adobe Commerce only)

    1. Go to Admin → Customers → Customer Segments → Add Segment.
    1. Define customer-based conditions (e.g., order, cart contents).
    1. Assign applicable scope: Visitor, Registered, or Both.
    1. Ensure conditions match for a test customer.
    1. Use GraphQL to check all segments:

        ```
        query {
            allCustomerSegments {
                name
                apply_to
            }
        }
        ```

    1. Validate segments applied to a cart:

        ```
        query {
            customerSegments(cartId: "your-cart-id") {
                name
            }
        }
        ```

<u>Expected result</u>:

Names of customer groups, segments, and promotional rule information aren't exposed through GraphQL.

<u>Actual result</u>:

Names of customer groups, segments, and promotional rule information are exposed through GraphQL.

## Solution

Apply the attached patches depending on your Adobe Commerce version:

* For Adobe Commerce version 2.4.8:

    * LYNX-839_CE_2.4.8.patch
    * LYNX-839_EE_2.4.8.patch

* For Magento Open Source version 2.4.8:

    * LYNX-839_CE_2.4.8.patch
