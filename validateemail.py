# pip install py3-validate-email
from validate_email import validate_email
from tqdm import tqdm


with open('emails.txt','r',encoding='utf-8') as f:
    data = f.readlines()

def validate(email):
    try:
        status = validate_email(email_address=email,
                                check_format=True,
                                check_blacklist=False,
                                check_dns=True,
                                dns_timeout=3,
                                check_smtp=True,
                                smtp_timeout=3,
                                smtp_helo_host=None,
                                smtp_from_address=None,
                                smtp_debug=False)
        return status
    except KeyboardInterrupt:
        print('stopping')


lis = list(range(len(data)))

with tqdm(total=len(data)) as p:

    for x in lis:
        
        email = data[x].strip('\n')
        
        status = validate(email)

        if status == True:
            with open('true emails.txt','a',encoding='utf-8') as f:
                f.write(email)
                f.write('\n')
        else:
            with open('false emails.txt','a',encoding='utf-8') as f:
                f.write(email)
                f.write('\n')
        try:
            p.update(1)
        except KeyboardInterrupt:
            print('interrupt')
            p.close()
