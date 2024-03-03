# Testing

[Click here to go back to the README.md file](README.md)

## Overview

This document outlines the testing process for the Sleep Healthily website. The testing process includes manual testing, performance testing and code validation. The testing process was carried out on Google Chrome, Mozilla Firefox, and Safari on MacBook.

## Table of Contents

- [Validation](#validation)
  - [HTML](#html)
  - [CSS](#css)
  - [JavaScript](#javascript)
  - [Python and Django (Pep 8)](#python-and-django-pep-8)
- [Performance](#performance)
  - [Mobile Performance](#mobile-performance)
  - [Desktop Performance](#desktop-performance)
- [Manual Testing](#manual-testing)
- [Incomplete known bugs and UX improvements](#incomplete-known-bugs-and-ux-improvements)

## Validation

### HTML

I use the [W3C Markup Validation Service](https://validator.w3.org/) to validate my HTML code.

With Django, theres a lot of syntax that doesn't play well with the HTML Validator, such as `{% url 'homepage' %}` or `{{ variable|filter }}`.

Normally, I validate by using [validate by uri](https://validator.w3.org/#validate_by_uri) by passing in my deployed URL. However, many pages on this site require a user to be logged-in and authenticated, and will not work using this method, due to the fact that the HTML Validator (W3C) doesn't have access to login to the pages.

In order to properly validate my HTML pages for authenticated pages, I followed these steps:

- Navigate to the deployed pages that require authentication
- Right-click anywhere on the page, and select **View Page Source** (usually `CTRL+U` or `⌘+U` on Mac).
- This will display the entire compiled code.
- Copy everything, and use the [validate by input](https://validator.w3.org/#validate_by_input) method.
- Repeat this process for every page that requires a user to be logged-in/authenticated.

| Page             | W3C URL                                                                                                                                             | Screenshot                                                                         | Notes                                                                 |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| Homepage         | [Link](https://validator.w3.org/nu/?doc=https://sleep-healthily-12a12155ea31.herokuapp.com/)                                                        | ![Homepage Validation](documentation/validation/html/homepage.png)                 | Pass                                                                  |
| About            | NA                                                                                                                                                  | ![About Validation](documentation/validation/html/about.png)                       | Pass                                                                  |
| Blog Add         | NA                                                                                                                                                  | ![Blog Add Validation](documentation/validation/html/blog-add.png)                 | Errors are standard when using summernote on frontend                 |
| Blog Edit        | NA                                                                                                                                                  | ![Blog Edit Validation](documentation/validation/html/blog-edit.png)               | Errors are standard when using summernote on frontend                 |
| Blog Post Detail | [Link](https://validator.w3.org/nu/?doc=https://sleep-healthily-12a12155ea31.herokuapp.com/blog/3)                                                  | ![Blog Post Detail Validation](documentation/validation/html/blog-post-detail.png) | Pass                                                                  |
| Blog Posts       | [Link](https://validator.w3.org/nu/?doc=https://sleep-healthily-12a12155ea31.herokuapp.com/blog/)                                                   | ![Blog Posts Validation](documentation/validation/html/blog-posts.png)             | Pass                                                                  |
| Cart             | NA                                                                                                                                                  | ![Cart Validation](documentation/validation/html/cart.png)                         | Pass                                                                  |
| Checkout         | NA                                                                                                                                                  | ![Checkout Validation](documentation/validation/html/checkout.png)                 | Pass                                                                  |
| Contact          | [Link](https://validator.w3.org/nu/?doc=https://sleep-healthily-12a12155ea31.herokuapp.com/contact/)                                                | ![Contact Validation](documentation/validation/html/contact.png)                   | Pass                                                                  |
| Edit Product     | NA                                                                                                                                                  | ![Edit Product Validation](documentation/validation/html/edit-product.png)         | Duplicate error ID when using Custom Clearable input from CI Tutorial |
| Login            | [Link](https://validator.w3.org/nu/?doc=https://sleep-healthily-12a12155ea31.herokuapp.com/accounts/login/)                                         | ![Login Validation](documentation/validation/html/login.png)                       | Pass                                                                  |
| Order Summary    | [Link](https://validator.w3.org/nu/?doc=https://sleep-healthily-12a12155ea31.herokuapp.com/profile/order_history/CC9047E992AD47BE89ADE92CC30ABD34/) | ![Order Summary Validation](documentation/validation/html/order-summary.png)       | Scope error due to Bootstrap 4 syntax                                 |
| Product Detail   | [Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsleep-healthily-12a12155ea31.herokuapp.com%2Fproducts%2F4%2F)                                 | ![Product Detail Validation](documentation/validation/html/product-detail.png)     | Pass                                                                  |
| Products         | [Link](https://validator.w3.org/nu/?doc=https://sleep-healthily-12a12155ea31.herokuapp.com/products/)                                               | ![Products Validation](documentation/validation/html/products.png)                 | Pass                                                                  |
| Signup           | [Link](https://validator.w3.org/nu/?doc=https://sleep-healthily-12a12155ea31.herokuapp.com/accounts/signup/)                                        | ![Signup Validation](documentation/validation/html/signup.png)                     | Pass                                                                  |

### CSS

I use the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) to validate my CSS code. You can [click here to see the validated CSS code without any errors](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fsleep-healthily-12a12155ea31.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en).

### JavaScript

I used [JSHint](https://jshint.com/) to validate my JavaScript code. Here is a table of the validated code, which shows the file validated, a screenshot and a description of any warnings:

| File        | Screenshot                                                               | Description                                                                       |
| ----------- | ------------------------------------------------------------------------ | --------------------------------------------------------------------------------- |
| `script.js` | ![Sleep healthily script](documentation/validation/js/jshint-script.png) | Optional chaining warning because online validator can't recognise I'm using ES11 |

### Python and Django (Pep 8)

I used the [Code Institute PEP8 Validator](https://pep8ci.herokuapp.com/) to check that my Python code is PEP8 compliant. I validated any files that were either modified or created by me. Here is a table of the validated code, which shows the file validated, a screenshot, and a description of any warnings:

| File                        | Screenshot                                                                              | Description                                                                                   |
| --------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| sleep_healthily/settings.py | ![sleep_healthily-settings](documentation/validation/pep8/sleep-healthily-settings.png) | There are 4 errors that come from standard settings.py lines. It is advised not to edit them. |
| cart/contexts.py            | ![cart-contexts](documentation/validation/pep8/cart-contexts.png)                       | Pass                                                                                          |
| blog/admin.py               | ![blog-admin](documentation/validation/pep8/blog-admin.png)                             | Pass                                                                                          |
| blog/contexts.py            | ![blog-contexts](documentation/validation/pep8/blog-contexts.png)                       | Pass                                                                                          |
| blog/forms.py               | ![blog-forms](documentation/validation/pep8/blog-forms.png)                             | Pass                                                                                          |
| blog/models.py              | ![blog-models](documentation/validation/pep8/blog-models.png)                           | Pass                                                                                          |
| blog/urls.py                | ![blog-urls](documentation/validation/pep8/blog-urls.png)                               | Pass                                                                                          |
| blog/views.py               | ![blog-views](documentation/validation/pep8/blog-views.png)                             | Pass                                                                                          |
| cart/views.py               | ![car-views](documentation/validation/pep8/car-views.png)                               | Pass                                                                                          |
| cart/urls.py                | ![cart-urls](documentation/validation/pep8/cart-urls.png)                               | Pass                                                                                          |
| checkout/admin.py           | ![checkout-admin](documentation/validation/pep8/checkout-admin.png)                     | Pass                                                                                          |
| checkout/forms.py           | ![checkout-forms](documentation/validation/pep8/checkout-forms.png)                     | Pass                                                                                          |
| checkout/models.py          | ![checkout-models](documentation/validation/pep8/checkout-models.png)                   | Pass                                                                                          |
| checkout/signals.py         | ![checkout-signals](documentation/validation/pep8/checkout-signals.png)                 | Pass                                                                                          |
| checkout/urls.py            | ![checkout-urls](documentation/validation/pep8/checkout-urls.png)                       | Pass                                                                                          |
| checkout/views.py           | ![checkout-views](documentation/validation/pep8/checkout-views.png)                     | Pass                                                                                          |
| checkout/webhook_handler.py | ![checkout-webhook_handler](documentation/validation/pep8/checkout-webhook_handler.png) | Pass                                                                                          |
| checkout/webhooks.py        | ![checkout-webhooks](documentation/validation/pep8/checkout-webhooks.png)               | Pass                                                                                          |
| home/urls.py                | ![home-urls](documentation/validation/pep8/home-urls.png)                               | Pass                                                                                          |
| home/views.py               | ![home-views](documentation/validation/pep8/home-views.png)                             | Pass                                                                                          |
| product/admin.py            | ![product-admin](documentation/validation/pep8/product-admin.png)                       | Pass                                                                                          |
| product/forms.py            | ![product-forms](documentation/validation/pep8/product-forms.png)                       | Pass                                                                                          |
| product/helper_tags.py      | ![product-helper_tags](documentation/validation/pep8/product-helper_tags.png)           | Pass                                                                                          |
| product/models.py           | ![product-models](documentation/validation/pep8/product-models.png)                     | Pass                                                                                          |
| product/urls.py             | ![product-urls](documentation/validation/pep8/product-urls.png)                         | Pass                                                                                          |
| product/views.py            | ![product-views](documentation/validation/pep8/product-views.png)                       | Pass                                                                                          |
| product/widgets.py          | ![product-widgets](documentation/validation/pep8/product-widgets.png)                   | Pass                                                                                          |
| profiles/admin.py           | ![profiles-admin](documentation/validation/pep8/profiles-admin.png)                     | Pass                                                                                          |
| profiles/forms.py           | ![profiles-forms](documentation/validation/pep8/profiles-forms.png)                     | Pass                                                                                          |
| profiles/models.py          | ![profiles-models](documentation/validation/pep8/profiles-models.png)                   | Pass                                                                                          |
| profiles/urls.py            | ![profiles-urls](documentation/validation/pep8/profiles-urls.png)                       | Pass                                                                                          |
| profiles/views.py           | ![profiles-views](documentation/validation/pep8/profiles-views.png)                     | Pass                                                                                          |
| review/admin.py             | ![review-admin](documentation/validation/pep8/review-admin.png)                         | Pass                                                                                          |
| review/forms.py             | ![review-forms](documentation/validation/pep8/review-forms.png)                         | Pass                                                                                          |
| review/models.py            | ![review-models](documentation/validation/pep8/review-models.png)                       | Pass                                                                                          |
| review/urls.py              | ![review-urls](documentation/validation/pep8/review-urls.png)                           | Pass                                                                                          |
| review/views.py             | ![review-views](documentation/validation/pep8/review-views.png)                         | Pass                                                                                          |
| sleep_healthily/urls.py     | ![sleep-healthily-urls](documentation/validation/pep8/sleep-healthily-urls.png)         | Pass                                                                                          |
| sleep_healthily/views.py    | ![sleep-healthily-views](documentation/validation/pep8/sleep-healthily-views.png)       | Pass                                                                                          |

## Performance

Performance metrics were gathered using Google's PageSpeed Insights to ensure the website operates efficiently on both mobile and desktop devices. Below are the performance results with Lighthouse screenshots from the `documentation/performance` directory.

### Mobile Performance

| Page            | Lighthouse Screenshot                                                           | Comments                                                                                       |
| --------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Homepage        | ![Homepage Mobile](documentation/performance/mobile-homepage.png)               | Minor warnings                                                                                 |
| Blog Detail     | ![Blog Detail Mobile](documentation/performance/mobile-blog-detail.png)         | Minor warnings                                                                                 |
| Blog Posts      | ![Blog Posts Mobile](documentation/performance/mobile-blog-posts.png)           | Minor warnings                                                                                 |
| Login           | ![Login Mobile](documentation/performance/mobile-login.png)                     | Minor warnings                                                                                 |
| Order Summary   | ![Order Summary Mobile](documentation/performance/mobile-order-summary.png)     | Minor warnings                                                                                 |
| Privacy Policy  | ![Privacy Policy Mobile](documentation/performance/mobile-privacy-policy.png)   | Warnings caused by using Termly code - leaving as is so that it doesn't disrupt the formatting |
| Product Detail  | ![Product Mobile](documentation/performance/mobile-product.png)                 | Minor warnings                                                                                 |
| Products        | ![Products Mobile](documentation/performance/mobile-products.png)               | Minor warnings                                                                                 |
| Search          | ![Search Mobile](documentation/performance/mobile-search.png)                   | Minor warnings                                                                                 |
| Shipping Policy | ![Shipping Policy Mobile](documentation/performance/mobile-shipping-policy.png) | Warnings caused by using Termly code - leaving as is so that it doesn't disrupt the formatting |
| Signup          | ![Signup Mobile](documentation/performance/mobile-signup.png)                   | Minor warnings                                                                                 |

### Desktop Performance

| Page            | Lighthouse Screenshot                                                             | Comments       |
| --------------- | --------------------------------------------------------------------------------- | -------------- |
| Homepage        | ![Homepage Desktop](documentation/performance/desktop-homepage.png)               | Minor warnings |
| Blog Detail     | ![Blog Detail Desktop](documentation/performance/desktop-blog-detail.png)         | No warnings    |
| Blog Posts      | ![Blog Posts Desktop](documentation/performance/desktop-blog-posts.png)           | Minor warnings |
| Login           | ![Login Desktop](documentation/performance/desktop-login.png)                     | No warnings    |
| Order Summary   | ![Order Summary Desktop](documentation/performance/desktop-order-summary.png)     | Minor warnings |
| Privacy Policy  | ![Privacy Policy Desktop](documentation/performance/desktop-privacy-policy.png)   | Minor warnings |
| Product Detail  | ![Product Detail Desktop](documentation/performance/desktop-product-detail.png)   | Minor warnings |
| Products        | ![Products Desktop](documentation/performance/desktop-products.png)               | Minor warnings |
| Search          | ![Search Desktop](documentation/performance/desktop-search.png)                   | Minor warnings |
| Shipping Policy | ![Shipping Policy Desktop](documentation/performance/desktop-shipping-policy.png) | No warnings    |
| Signup          | ![Signup Desktop](documentation/performance/desktop-signup.png)                   | No warnings    |

## Manual Testing

I carried out manual testing according to my user stories. I carried the tests out on Google Chrome, Mozilla Firefox, and Safari on MacBook.

| User story - As a user, I can...                                                                                             | Notes  | Chrome | Firefox | Safari |
| ---------------------------------------------------------------------------------------------------------------------------- | ------ | :----: | :-----: | :----: |
| **create an account** to **access personalised features and save my preferences**.                                           | Passed |   ✅   |   ✅    |   ✅   |
| **log into my account** to **access my personal settings and history, or prefill my details at checkout**.                   | Passed |   ✅   |   ✅    |   ✅   |
| **log out of my account** to **ensure my account is secure when I'm not using it**.                                          | Passed |   ✅   |   ✅    |   ✅   |
| **update my account/profile** to **keep my personal information up to date for checking out**.                               | Passed |   ✅   |   ✅    |   ✅   |
| **delete my account** to **remove my personal data from the platform**.                                                      | Passed |   ✅   |   ✅    |   ✅   |
| **access and view my user profile** to **see my personal information, order history, and manage my account settings**.       | Passed |   ✅   |   ✅    |   ✅   |
| **view a summary of my orders** to **keep track of my purchases** (as a **registered customer**).                            | Passed |   ✅   |   ✅    |   ✅   |
| **add products to a wishlist** to **save them for future consideration or purchase**.                                        | Passed |   ✅   |   ✅    |   ✅   |
| **create new products** to **offer more choices to customers** (as a **staff member**).                                      | Passed |   ✅   |   ✅    |   ✅   |
| **update product details** to **ensure all information about the products is current and accurate** (as a **staff member**). | Passed |   ✅   |   ✅    |   ✅   |
| **delete products** to **remove items that are no longer available or relevant** (as a **staff member**).                    | Passed |   ✅   |   ✅    |   ✅   |
| **add products to my cart** to **purchase them** (as a **customer**).                                                        | Passed |   ✅   |   ✅    |   ✅   |
| **remove products from my cart** to **manage items before finalizing my purchase** (as a **customer**).                      | Passed |   ✅   |   ✅    |   ✅   |
| **see an order summary in the cart** to **review my order before completing the purchase** (as a **customer**).              | Passed |   ✅   |   ✅    |   ✅   |
| **complete the checkout process and pay** to **finalise my order** (as a **customer**).                                      | Passed |   ✅   |   ✅    |   ✅   |
| **create reviews for products** to **share my experience with others** (as a **registered customer**).                       | Passed |   ✅   |   ✅    |   ✅   |
| **update my reviews** to **modify my feedback if my opinion changes** (as a **registered customer**).                        | Passed |   ✅   |   ✅    |   ✅   |
| **delete my reviews** to **remove my feedback if I no longer wish it to be displayed** (as a **registered customer**).       | Passed |   ✅   |   ✅    |   ✅   |
| **create blog posts** to **provide valuable content to customers and visitors** (as a **staff member**).                     | Passed |   ✅   |   ✅    |   ✅   |
| **update blog posts** to **keep the content current and relevant** (as a **staff member**).                                  | Passed |   ✅   |   ✅    |   ✅   |
| **delete blog posts** to **remove outdated or irrelevant content** (as a **staff member**).                                  | Passed |   ✅   |   ✅    |   ✅   |
| **create comments on blog posts** to **engage in discussions and share my thoughts** (as a **registered customer**).         | Passed |   ✅   |   ✅    |   ✅   |
| **update my comments** to **change my input or correct mistakes** (as a **registered customer**).                            | Passed |   ✅   |   ✅    |   ✅   |
| **delete my comments** to remove my input if I change my mind (as a registered customer).                                    | Passed |   ✅   |   ✅    |   ✅   |

## Incomplete known bugs and UX improvements

The below are known bugs and possible areas of UX improvement I came across during testing.

1. Order note is not addable even though the field exists on the model. I explained this a bit more in the [project board issue](https://github.com/users/stephendawsondev/projects/6/views/1?pane=issue&itemId=54188655), but basically it turned out to be too complex to implement with the way I set it up. I removed the text input from the cart to mitigate this issue, but will revisit in the future.
