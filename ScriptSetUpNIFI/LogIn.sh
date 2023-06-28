docker logs nifi | grep Generated > Credenziali.txt
extracted_info=$(grep -oE '\[.*\]' "Credenziali.txt" | sed 's/\[//;s/\]//'| tr '\n' '?')
# Stampa le informazioni estratte
IFS=? read -r info1 info2 info3 <<< "$extracted_info"
# Stampa le informazioni estratte
echo "$extracted_info"
echo "Informazione 1: $info1"
echo "Informazione 2: $info2"
echo "Informazione 3: $info3"
urlencode=$(echo "$info3" | jq -s -R -r @uri)
read -r casa <<< "$urlencode"
str="username=$info2&password=$urlencode"
str2="username=$info2&password=$info3"
len=${#str}
len_s=${#str2}
len2=$((len-3))
echo $str di cui dim $len
echo $str2 di cui dim $len_s
curl -i -s -k -X $'POST' \
    -H $'Host: localhost:8443' -H $'Content-Length: '$len2 -H $'Sec-Ch-Ua: ' -H $'Sec-Ch-Ua-Mobile: ?0' -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.134 Safari/537.36' -H $'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H $'Accept: */*' -H $'X-Requested-With: XMLHttpRequest' -H $'Request-Token: 8b70dad2-f285-46e3-adae-b22d63223358' -H $'Sec-Ch-Ua-Platform: \"\"' -H $'Origin: https://localhost:8443' -H $'Sec-Fetch-Site: same-origin' -H $'Sec-Fetch-Mode: cors' -H $'Sec-Fetch-Dest: empty' -H $'Referer: https://localhost:8443/nifi/login' -H $'Accept-Encoding: gzip, deflate' -H $'Accept-Language: it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7' -H $'Connection: close' \
    -b $'__Secure-Request-Token=8b70dad2-f285-46e3-adae-b22d63223358' \
    --data-binary $'username='$info2'&password='$urlencode \
    $'https://localhost:8443/nifi-api/access/token' --output file1.txt
s=$(head -n 14 file1.txt | grep Set-Cookie )
y=$(echo $s |tr ';' '\n' | grep __Secure-Authorization-Bearer| cut -c 43-)
bash CreazioneFlusso.sh $y
curl -i -s -k -X $'POST' \
    -H $'Host: localhost:8443' -H $'Content-Length: 91' -H $'Sec-Ch-Ua: ' -H $'Sec-Ch-Ua-Mobile: ?0' -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.134 Safari/537.36' -H $'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H $'Accept: */*' -H $'X-Requested-With: XMLHttpRequest' -H $'Request-Token: 2e2b8ddb-546d-482f-ae81-899928b9c6f6' -H $'Sec-Ch-Ua-Platform: \"\"' -H $'Origin: https://localhost:8443' -H $'Sec-Fetch-Site: same-origin' -H $'Sec-Fetch-Mode: cors' -H $'Sec-Fetch-Dest: empty' -H $'Referer: https://localhost:8443/nifi/login' -H $'Accept-Encoding: gzip, deflate' -H $'Accept-Language: it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7' -H $'Connection: close' \
    -b $'__Secure-Request-Token=2e2b8ddb-546d-482f-ae81-899928b9c6f6' \
    --data-binary $'username=3fd6aeff-c975-4c3f-8ca7-aa2603806b43&password=L%2FiyOW8FUORZAQ%2BNOtB1e39U17rg1Slz' \
    $'https://localhost:8443/nifi-api/access/token'