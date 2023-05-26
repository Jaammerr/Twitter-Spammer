# Twitter Message Spammer

## General information:

    The script was created to send the specified message to the specified twitter accounts.
    
    The script is based on synchronous requests with standard threads.
    Login to your account is carried out only with an authorization token, nothing else is required.

    - Why is the script not asynchronous ?
    The answer is quite simple, asynchronous requests are fast due to 
    the fact that they do not wait for a response from the server, 
    in the case of this spammer, this option is not suitable 
    because for each account a request is sent to the js 
    file to get the necessary tokens.

    - What type of proxy is supported ?
    Only HTTP. 

    - Are proxies without authorization supported ?
    No.



## Installation:
```Required python version 3.10-3.11```

Install requirements:
```bash
pip install -r requirements.txt
```

To run you need to open powershell or cmd:
```bash
python run.py
```

## Setup config:
All configuration files are located in the directory "files_data"

1) File accounts_data.txt:

```
# Example without proxy (Format: auth_token): 
a50f17992cc5c07ca3555fb8360dbfca6d514396
a50f45452cc5c07ca3555fb8360dbfca6d514396

# Example with proxy (Format: auth_token:ip:port:user:pass): 
a50f17992cc5c07ca3555fb8360dbfca6d514396:111.238.1.48:5975:username:password
a50f45452cc5c07ca3555fb8360dbfca6d514396:121.238.1.58:5975:username:password

# You can use all together, for example:
a50f17992cc5c07ca3555fb8360dbfca6d514396:111.238.1.48:5975:username:password
a50f17992cc5c07ca3555fb8360dbfca6d514396
```

2) File spam_links.txt (Format: https://twitter.com/username):
```
# The specified message will be sent to each link for each account:
https://twitter.com/username1
https://twitter.com/username2
https://twitter.com/username3
```

3) File spam_message.txt (Curly braces are used to randomize text):
```
# Example:
{Good afternoon|Hello|Good evening}, dear! My name is {Misha|Andrii|Vasia}

Each time the script sends a message, 1 phrase from brackets will be randomly selected:
Cycle 1 - Good afternoon, dear! My name is Misha
Cycle 2 - Good evening, dear! My name is Andrii
```

After running the "run.py" file you must select launch options

1. Whether to use a proxy:

[![2023-05-26-194132.png](https://i.postimg.cc/7Lvnj8RT/2023-05-26-194132.png)](https://postimg.cc/bZTn2Mpz)

2.  Enter delay between messages in seconds:

[![2023-05-26-194439.png](https://i.postimg.cc/HLQRht6d/2023-05-26-194439.png)](https://postimg.cc/SXxgXc0v)

3. Enter the maximum time in seconds to wait for a request response (Sometimes the twitter server takes a long time to respond):

[![2023-05-26-194448.png](https://i.postimg.cc/ZRb7Dz9x/2023-05-26-194448.png)](https://postimg.cc/jW14L94D)

## Support/Offers

TG - https://t.me/Jaammerr

Email - andlolkek@gmail.com
