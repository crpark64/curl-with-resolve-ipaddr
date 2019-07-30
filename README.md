# curl-with-resolve-ipaddr
Using pycurl with connect to resolved ip address.

# Download pycurl for windows from github
- Downlaod Url: https://github.com/pycurl/downloads/tree/master/7.43.0
- In my case Python 3.5 to 32 bit system.
    - File (x86): pycurl-7.43.0-cp35-none-win32.whl
    - File (x64): pycurl-7.43.0-cp35-none-win32.whl

# Install
c:\ ... > python -m pip install pycurl-7.43.0-cp35-none-win32.whl

# Edit Source
Please edit and test the lower one with source.


    protocol		= 'http://'
    targetDomain	= 'jsonplaceholder.typicode.com'
    uri				= '/posts'
    destIP			= '172.64.129.28'
    destPort		= '443'


The real address of jsonplaceholder.typicode.com is 172.64.129.28, but you can edit destIp and connect it to 8.8.8.8.



# Usage
- c:\ ... > python.exe curl.py

- Result
- Status: 201
- Total Time: 0.843552
- Primary IP: 172.64.129.28 Port: 80
- Result Body
{
  "hello": "world",
  "id": 101
}

