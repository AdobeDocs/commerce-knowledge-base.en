---
title: 'ACSD-48627: out-of-stock configurable product causes an error'
description: Apply the ACSD-48627 patch to fix the Adobe Commerce issue where the out-of-stock configurable product causes an error when sending a GraphQL request to get cart details.
---
# ACSD-48627: out-of-stock configurable product causes an error

The ACSD-48627 patch fixes the issue where the out-of-stock configurable product causes an error when sending a GraphQL request to get cart details. This patch is available when the [[!DNL Quality Patches Tool (QPT)]](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.1.25 is installed. The patch ID is ACSD-48627. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.6. 

## Affected products and versions

**The patch is created for Adobe Commerce version:**

* Adobe Commerce (all deployment methods) xxx

**Compatible with Adobe Commerce versions:**

* Adobe Commerce (all deployment methods) xxx

>[!NOTE]
>
>The patch might become applicable to other versions with new [!DNL Quality Patches Tool] releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [QPT landing page](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html). Use the patch ID as a search keyword to locate the patch.

## Issue

Out-of-stock configurable product causes an error when sending a GraphQL request to get cart details.

<u>Steps to reproduce</u>:

1. Create a customer account.
1. Add some products to the cart including a configurable product (ID = 436).
1. Go to the admin backend, and edit the configurable product by setting all children product qty to 0.
1. The configurable product will become out of stock as all the child products are out of stock.
1. Check the `catalog_product_index_price` table, the record with this product is empty.
1. Make GraphQL request to get the customer token.

    ```GraphQL
    mutation {
        generateCustomerToken(
            email: "test@example.com"
            password: "xxxx"
            ) {
                token
                }
                }
    ```

1. Make GraphQL request to get cartId.

    ```GraphQL
    Headers: Authentication => Bearer [customer token in step 6]
    ```

    ```GraphQL
    {
        customerCart {
            id
            items {
                id
                product {
                    name
                    sku
                    }
                    quantity
                    }
                    }
                    }
    ```

1. Make a GraphQL request to get the cart details.

    ```GraphQL
    Headers: Authentication => Bearer [customer token in step 6]
    ```

    ```GraphQL
    query GetCartDetails($cartId: String!) {
        cart(cart_id: $cartId) {
            id
            ...CartPageFragment
            __typename
            }
            }
            fragment CartPageFragment on Cart {
                id
                total_quantity
                ...AppliedCouponsFragment
                ...ProductListingFragment
                ...PriceSummaryFragment
                __typename
                }
                fragment AppliedCouponsFragment on Cart {
                    id
                    applied_coupons {
                        code
                        __typename
                        }
                        __typename
                        }
                        fragment ProductListingFragment on Cart {
                            id
                            items {
                                uid
                                product {
                                    uid
                                    name
                                    sku
                                    url_key
                                    url_suffix
                                    thumbnail {
                                        url
                                        __typename
                                        }
                                        small_image {
                                            url
                                            __typename
                                            }
                                            stock_status
                                            price_range {
                                                minimum_price {
                                                
                                                final_price {
                                                    currency
                                                    value
                                                    __typename
                                                    }
                                                    regular_price {
                                                        currency
                                                        value
                                                        __typename
                                                        }
                                                        __typename
                                                        }
                                                        __typename
                                                        }
                                                        stock_status
                                                        ... on ConfigurableProduct {
                                                            variants {
                                                                attributes {
                                                                    uid
                                                                    __typename
                                                                    }
                                                                    product {
                                                                        uid
                                                                        small_image {
                                                                            url
                                                                            __typename
                                                                            }
                                                                            stock_status
                                                                            __typename
                                                                            }
                                                                            __typename
                                                                            }
                                                                            __typename
                                                                            }
                                                                            __typename
                                                                            }
                                                                            prices {
                                                                                price {
                                                                                    currency
                                                                                    value
                                                                                    __typename
                                                                                    }
                                                                                    __typename
                                                                                    }
                                                                                    quantity
                                                                                    ... on
                                                                                    ConfigurableCartItem {
                                                                                        configurable_options {
                                                                                            id
                                                                                            configurable_product_option_uid
                                                                                            option_label
                                                                                            configurable_product_option_value_uid
                                                                                            value_label
                                                                                            __typename
                                                                                            }
                                                                                            __typename
                                                                                            }
                                                                                            __typename
                                                                                            }
                                                                                            __typename
                                                                                            }
                                                                                            fragment PriceSummaryFragment on Cart {
                                                                                                id
                                                                                                items {
                                                                                                    uid
                                                                                                    quantity
                                                                                                    __typename
                                                                                                    }
                                                                                                    ...ShippingSummaryFragment
                                                                                                    prices {
                                                                                                        ...TaxSummaryFragment
                                                                                                        ...DiscountSummaryFragment
                                                                                                        ...GrandTotalFragment
                                                                                                        subtotal_excluding_tax {
                                                                                                            currency
                                                                                                            value
                                                                                                            __typename
                                                                                                            }
                                                                                                            subtotal_including_tax {
                                                                                                                currency
                                                                                                                value
                                                                                                                __typename
                                                                                                                }
                                                                                                                __typename
                                                                                                                }
                                                                                                                __typename
                                                                                                                }
                                                                                                                fragment DiscountSummaryFragment on
                                                                                                                CartPrices {
                                                                                                                    discounts {
                                                                                                                        amount {
                                                                                                                            currency
                                                                                                                            value
                                                                                                                            __typename
                                                                                                                            }
                                                                                                                            label
                                                                                                                            __typename
                                                                                                                            }
                                                                                                                            __typename
                                                                                                                            }
                                                                                                                            fragment GrandTotalFragment on CartPrices {
                                                                                                                                grand_total {
                                                                                                                                    currency
                                                                                                                                    value
                                                                                                                                    __typename
                                                                                                                                    }
                                                                                                                                    __typename
                                                                                                                                    }
                                                                                                                                    fragment ShippingSummaryFragment on Cart {
                                                                                                                                        id
                                                                                                                                        shipping_addresses {
                                                                                                                                            selected_shipping_method {
                                                                                                                                                amount {
                                                                                                                                                    currency
                                                                                                                                                    value
                                                                                                                                                    __typename
                                                                                                                                                    }
                                                                                                                                                    __typename
                                                                                                                                                    }
                                                                                                                                                    street
                                                                                                                                                    __typename
                                                                                                                                                    }
                                                                                                                                                    __typename
                                                                                                                                                    }
                                                                                                                                                    fragment TaxSummaryFragment on CartPrices {
                                                                                                                                                        applied_taxes {
                                                                                                                                                            amount {
                                                                                                                                                                currency
                                                                                                                                                                value
                                                                                                                                                                __typename
                                                                                                                                                                }
                                                                                                                                                                __typename
                                                                                                                                                                }
                                                                                                                                                                __typename
                                                                                                                                                                }
    ```

<u>Expected results</u>:


