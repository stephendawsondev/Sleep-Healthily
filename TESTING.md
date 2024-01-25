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

I used the [Code Institute PEP8 Validator](https://pep8ci.herokuapp.com/) to check that my Python code is PEP8 compliant. I validated any files that were either modified or create by me. Here is a table of the validated code, which shows the file validated, a screenshot and a description of any warnings:

| File                        | Screenshot | Description |
| --------------------------- | ---------- | ----------- |
| sleep_healthily/settings.py |            |             |

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
