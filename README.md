## epcqrcode

An EPC-QRCode generator in ERPNext.

EPC-QRCodes (European Payments Council Quick Response Codes) are used to initiate SEPA credit transfers.
They encode all necessary data (IBAN, amount, recipient) and may be placed on invoices to eliminate the error-prone typing of payment Information.

## Installation

From the frappe-bench folder, execute

    $ bench get-app https://github.com/4metrics/epcqrcode.git
    $ bench --site YOUR_SITE install-app epcqrcode

where `YOUR_SITE` is e.g. erp.example.com

## Usage

After installing the custom app, an HTTP endpoint for generating EPC-QRCodes as PNG images will be available in your ERPNext instance under `/api/method/epcqrcode.generator.get_code`.
The endpoint directly serves PNG images and takes the following query parameters to generate the QRCode

* name: the recipients name
* iban: the recipients International Bank Account Number (IBAN)
* bic: the recipients Bank Identifier Code (BIC), optional and only required for non-EEA countries
* amount: the amount to transfer in EUR (no other currencies are supported by EPC-QRCodes)
* text: the remittance information (either text or reference required)
* reference: the remittance information (either text or reference required)
* purpose: the SEPA purpose code (optional)
* scale: the scaling factor number for sizing the generated QRCode (optional)
* border: the border size number which adds padding to the generated QRCode (optional)

You can use this endpoint as source to an image, e.g., within a custom HTML print format, to place an EPC-QRCode in your sales invoice.
With this, you can also make use of Jinja template variables, e.g., to use the sales invoice number as payment reference in the QRCode.

```
{% set bank_iban = frappe.db.get_value("Bank Account", filters={"company": doc.company}, fieldname="iban") %}
<div style="margin-top: 10px;">
  <img width="110" height="110" src="/api/method/epcqrcode.generator.get_code?name={{ doc.company | urlencode }}&reference={{ doc.name }}&iban={{ bank_iban }}&amount={{ doc.grand_total }}&scale=4&border=0">
  <p>Zahlen mit QR-Code</p>
</div>
```

As the QRCode is embedded as an HTML image, the QRCode also works on the PDF print. Other solutions, such as SVGs, images with data URIs or canvas rendered elements don't work in ERPNext on the PDF prints.

## Example

A screenshot of how this could look like on a sales invoice

![example](https://user-images.githubusercontent.com/15350076/163834196-143db56e-7c85-4181-9de5-20f47d472009.png)

## Update

From the frappe-bench folder, run updates with 

    $ bench update

## Compatibility

The custom app works with all ERPNext versions from 13.26.0 to 15.4.0.

## License 

MIT License, refer to LICENSE

The copyright is owned by 4metrics and contributors. 
The software comes as-is without any warranty.
