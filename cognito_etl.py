import csv

with open('headers.csv') as f:
    content = f.readlines()
headers = content[0].strip().split(',')

# auth_user.csv headers
data_fields = ['name', 'given_name', 'family_name', 'email']
with open('import.csv', 'wb') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(headers)
    with open('auth_user.csv', 'rb') as infile:
        data = csv.reader(infile)
        print data
        for row in data:
            out = []
            for header in headers:
                if header == 'cognito:username':
                    out.append(row[data_fields.index('name')])
                elif header == 'cognito:mfa_enabled':
                    out.append('false')
                elif header == 'email_verified':
                    out.append('true')
                elif header == 'phone_number_verified':
                    out.append('false')
                else:
                    try:
                        i = data_fields.index(header)
                        # print("[{}]->[{}]".format(header,row[i]))
                        out.append(row[i])
                    except ValueError:
                        # print("[{}]->[none]".format(header))
                        out.append("")
            writer.writerow(out)

