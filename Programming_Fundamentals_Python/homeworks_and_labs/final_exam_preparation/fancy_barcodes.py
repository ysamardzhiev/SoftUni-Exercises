import re


def barcode_validation(current_barcode):
    match = re.search(r"@#+[A-Z][a-zA-Z0-9]{4,}[A-Z]@#+", current_barcode)
    if match:
        return True
    return False


def determine_group(current_barcode):
    match = re.findall(r"\d+", current_barcode)
    if match:
        return ''.join(match)
    return '00'


barcodes_count = int(input())

for _ in range(barcodes_count):
    barcode = input()
    if barcode_validation(barcode):
        product_group = determine_group(barcode)
        print(f"Product group: {product_group}")
    else:
        print('Invalid barcode')