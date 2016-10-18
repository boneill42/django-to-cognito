# django-lambda-auth

Create a new User Pool

Use the following SQL to export from auth_user:
```
select username, first_name, last_name, email from auth_user where email like 'boneill%' 
into outfile '/tmp/auth_user.csv' fields terminated by ',' enclosed by '"' lines terminated by '\n';
```

Download the header.csv:
Cognito -> Manage User Pools -> Users -> Import -> Download CSV header

Run the cognito_etl script to transform the data into the respective format for Cognito.

Setup an import job 
Cognito -> Manage User Pools -> Users -> Import -> Create import job




