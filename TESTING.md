# Testing

[Click here to go back to the README.md file](README.md)

## Overview

Overview of testing goes here

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

| Page             | W3C URL | Screenshot | Notes |
| ---------------- | ------- | ---------- | ----- |
| Homepage         |         |            |       |
| Collections page |         |            |       |

### CSS

I use the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) to validate my CSS code.

### JavaScript

I used [JSHint](https://jshint.com/) to validate my JavaScript code. Here is a table of the validated code, which shows the file validated, a screenshot and a description of any warnings:

| File        | Screenshot | Description |
| ----------- | ---------- | ----------- |
| `script.js` |            |             |

### Python and Django (Pep 8)

I used the [Code Institute PEP8 Validator](https://pep8ci.herokuapp.com/) to check that my Python code is PEP8 compliant. I validated any files that were either modified or created by me. Here is a table of the validated code, which shows the file validated, a screenshot, and a description of any warnings:

| File                        | Screenshot                                                                         | Description                                                                                   |
| --------------------------- | ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| sleep_healthily/settings.py | ![sleep_healthily-settings](documentation/validation/sleep-healthily-settings.png) | There are 4 errors that come from standard settings.py lines. It is advised not to edit them. |
| cart/contexts.py            | ![cart-contexts](documentation/validation/cart-contexts.png)                       | Pass                                                                                          |
| blog/admin.py               | ![blog-admin](documentation/validation/blog-admin.png)                             | Pass                                                                                          |
| blog/contexts.py            | ![blog-contexts](documentation/validation/blog-contexts.png)                       | Pass                                                                                          |
| blog/forms.py               | ![blog-forms](documentation/validation/blog-forms.png)                             | Pass                                                                                          |
| blog/models.py              | ![blog-models](documentation/validation/blog-models.png)                           | Pass                                                                                          |
| blog/urls.py                | ![blog-urls](documentation/validation/blog-urls.png)                               | Pass                                                                                          |
| blog/views.py               | ![blog-views](documentation/validation/blog-views.png)                             | Pass                                                                                          |
| cart/views.py               | ![car-views](documentation/validation/car-views.png)                               | Pass                                                                                          |
| cart/urls.py                | ![cart-urls](documentation/validation/cart-urls.png)                               | Pass                                                                                          |
| checkout/admin.py           | ![checkout-admin](documentation/validation/checkout-admin.png)                     | Pass                                                                                          |
| checkout/forms.py           | ![checkout-forms](documentation/validation/checkout-forms.png)                     | Pass                                                                                          |
| checkout/models.py          | ![checkout-models](documentation/validation/checkout-models.png)                   | Pass                                                                                          |
| checkout/signals.py         | ![checkout-signals](documentation/validation/checkout-signals.png)                 | Pass                                                                                          |
| checkout/urls.py            | ![checkout-urls](documentation/validation/checkout-urls.png)                       | Pass                                                                                          |
| checkout/views.py           | ![checkout-views](documentation/validation/checkout-views.png)                     | Pass                                                                                          |
| checkout/webhook_handler.py | ![checkout-webhook_handler](documentation/validation/checkout-webhook_handler.png) | Pass                                                                                          |
| checkout/webhooks.py        | ![checkout-webhooks](documentation/validation/checkout-webhooks.png)               | Pass                                                                                          |
| home/urls.py                | ![home-urls](documentation/validation/home-urls.png)                               | Pass                                                                                          |
| home/views.py               | ![home-views](documentation/validation/home-views.png)                             | Pass                                                                                          |
| product/admin.py            | ![product-admin](documentation/validation/product-admin.png)                       | Pass                                                                                          |
| product/forms.py            | ![product-forms](documentation/validation/product-forms.png)                       | Pass                                                                                          |
| product/helper_tags.py      | ![product-helper_tags](documentation/validation/product-helper_tags.png)           | Pass                                                                                          |
| product/models.py           | ![product-models](documentation/validation/product-models.png)                     | Pass                                                                                          |
| product/urls.py             | ![product-urls](documentation/validation/product-urls.png)                         | Pass                                                                                          |
| product/views.py            | ![product-views](documentation/validation/product-views.png)                       | Pass                                                                                          |
| product/widgets.py          | ![product-widgets](documentation/validation/product-widgets.png)                   | Pass                                                                                          |
| profiles/admin.py           | ![profiles-admin](documentation/validation/profiles-admin.png)                     | Pass                                                                                          |
| profiles/forms.py           | ![profiles-forms](documentation/validation/profiles-forms.png)                     | Pass                                                                                          |
| profiles/models.py          | ![profiles-models](documentation/validation/profiles-models.png)                   | Pass                                                                                          |
| profiles/urls.py            | ![profiles-urls](documentation/validation/profiles-urls.png)                       | Pass                                                                                          |
| profiles/views.py           | ![profiles-views](documentation/validation/profiles-views.png)                     | Pass                                                                                          |
| review/admin.py             | ![review-admin](documentation/validation/review-admin.png)                         | Pass                                                                                          |
| review/forms.py             | ![review-forms](documentation/validation/review-forms.png)                         | Pass                                                                                          |
| review/models.py            | ![review-models](documentation/validation/review-models.png)                       | Pass                                                                                          |
| review/urls.py              | ![review-urls](documentation/validation/review-urls.png)                           | Pass                                                                                          |
| review/views.py             | ![review-views](documentation/validation/review-views.png)                         | Pass                                                                                          |
| sleep_healthily/urls.py     | ![sleep-healthily-urls](documentation/validation/sleep-healthily-urls.png)         | Pass                                                                                          |
| sleep_healthily/views.py    | ![sleep-healthily-views](documentation/validation/sleep-healthily-views.png)       | Pass                                                                                          |

## Performance

### Mobile performance

| Page URL            | Lighthouse Screenshot | Comments |
| ------------------- | --------------------- | -------- |
| [Homepage mobile]() |                       |          |

### Desktop performance

| Page URL             | Lighthouse Screenshot | Comments |
| -------------------- | --------------------- | -------- |
| [Homepage desktop]() |                       |          |

## Manual Testing

I carried out manual testing according to my user stories. I carried the tests out on Google Chrome, Mozilla Firefox and Safari on Macbook.

| User story - As a user, I can...                                   | Notes | Chrome | Firefox | Safari |
| ------------------------------------------------------------------ | ----- | ------ | ------- | ------ |
| **create an account** so that I can **have my preferences saved**. |       |        |         |        |

## Incomplete known bugs and UX improvements

The below are known bugs and possible areas of UX improvement I came across during testing.
