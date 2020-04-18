## **Mail From CLI**

this tool helps me to send mail from terminal. I picked Python cos I'm comfortable with it. for using this you need to have SMTP client. 

also you need to define followings as environment variable for using script.

must have for basics:

- **FROM**
- **SMTP_HOST**
- **SMTP_PORT**
- **SMTP_PASS**

must have for using send to kindle services of [Amazon](https://www.amazon.com/gp/sendtokindle/).

- **TO_KINDLE** : your kindle email adress

you can easily set them with using simple bash script like below.

```
    #!/bin/zsh

    export FROM=test@test.com;
    export TO_KINDLE=test@kindle.com

    export SMTP_HOST=127.0.0.1;
    export SMTP_PORT=1001;
    export SMTP_PASS=MY_FANC_PASS;
```

you can prepare your environment with sourcing this bash script.

```
    source prepare_my_environment.sh
```

## **Usage**

#### Send mail without attachment
```
    # python send_mail.py [the mail of reciever] [subject] [body]

    python send_mail.py test@test.com "subject" "check this out dude?" attachment.pdf
```


#### Send mail with attachment
```
    # python send_mail.py [the mail of reciever] [subject] [body] [attachment]

    python send_mail.py test@test.com "subject" "check this out dude?" attachment.pdf
```

#### Send supported docs to your Kindle
```
    # python send_mail.py [attachment]

    python send_mail.py attachment.pdf
```