def get_paypal_id_link(paypal_data: dict) -> (str, str):
    paypal_id = paypal_data['id']
    approval_url = None

    for link in paypal_data['links']:
        if link['rel'] == 'approval_url':
            approval_url = link['href']

    return paypal_id, approval_url
