# okProxy

okProxy is the easiest way to validate a list of proxies and select the working ones


### Format
```bash
######################
### proxy-list.txt ###
######################

IP [1]
|
| Port [2]
|   |
|   | Country [3]
|   |   |
|   |   | Anonymity [4]
|   |   |  |
|   |   |  |  Type [5]
|   |   |  |   |_ _ _ _
|   |   |  |_ _ _ _ _  | Google passed [6]
|   |   |_ _ _ _ _   | |  |
|   |_ _ _ _ _    |  | |  |
|             |   |  | |  |
200.2.125.90:8080 AR-N-S! +


1. IP address
2. Port number
3. Country code
4. Anonymity
   N = No anonymity
   A = Anonymity
   H = High anonymity
5. Type
     = HTTP
   S = HTTP/HTTPS
   ! = incoming IP different from outgoing IP
6. Google passed
   + = Yes
   – = No


#############################
### proxy-list-status.txt ###
#############################

IP [1]
|
| Status [2]
|   |_ _ _ _ _
|             |
200.2.125.90: success


1. IP address
2. Status
   success = low latency (0-9 seconds)
   failure = high latency (10+ seconds)
```

### Proxy server data
* [Proxy list](http://spys.me/proxy.txt)

### Credits
NoBaseCode - Mohamed LAABID