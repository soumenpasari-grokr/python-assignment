'''
func : returns company name from a given email
@param string email_address - provided email address
@return string name of the company from email address
'''
def get_company_name(email_address):
    # getting @ character position
    start_position = email_address.find('@')
    # getting position of the string '.com'
    end_position = email_address.rfind('.')
    return email_address[start_position+1:end_position]

mail_address = 'soumen.pasari@datagrokr.in'

print(get_company_name(mail_address))