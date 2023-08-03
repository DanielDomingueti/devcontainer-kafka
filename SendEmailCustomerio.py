import customerio

api_key = 'api_key_secret'
site_id = 'site_id_secret'
unique_customer_id = 'customer_id_secret'

def sendEmail(transactional_message_id, subject, body):
    custIo = customerio.CustomerIO(site_id, api_key)

    custIo.send_request(
        method='post',
        path='/api/v1/customers/{unique_customer_id}/events',
        data={
            'name': 'Onboarding email',
            'data': {
                'transactional_message_id': transactional_message_id,
                'subject': subject,
                'body': body
            }
        }
    )