docker logs nifi | grep Generated > ciao.txt
extracted_info=$(grep -oE '\[.*\]' "ciao.txt" | sed 's/\[//;s/\]//'| tr '\n' '?')
# Stampa le informazioni estratte
IFS=? read info1 info2 info3 <<< "$extracted_info"
# Stampa le informazioni estratte
echo "$extracted_info"
echo "Informazione 1: $info1"
echo "Informazione 2: $info2"
echo "Informazione 3: $info3"
x=$(curl --write-out '%header{Set-Cookie}' -i -s -k -X $'POST' \
    -H $'Host: localhost:8443' -H $'Content-Length: 87' -H $'Sec-Ch-Ua: ' -H $'Sec-Ch-Ua-Mobile: ?0' -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.134 Safari/537.36' -H $'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H $'Accept: */*' -H $'X-Requested-With: XMLHttpRequest' -H $'Request-Token: 8b70dad2-f285-46e3-adae-b22d63223358' -H $'Sec-Ch-Ua-Platform: \"\"' -H $'Origin: https://localhost:8443' -H $'Sec-Fetch-Site: same-origin' -H $'Sec-Fetch-Mode: cors' -H $'Sec-Fetch-Dest: empty' -H $'Referer: https://localhost:8443/nifi/login' -H $'Accept-Encoding: gzip, deflate' -H $'Accept-Language: it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7' -H $'Connection: close' \
    -b $'__Secure-Request-Token=8b70dad2-f285-46e3-adae-b22d63223358' \
    --data-binary $'username='$info2'&password='$info3 \
    $'https://localhost:8443/nifi-api/access/token' --output fil1.txt)
y=$(echo $x |tr ';' '\n' | grep __Secure-Authorization-Bearer| cut -c 31-)
echo $y
sh CreazioneFlusso.sh $y
