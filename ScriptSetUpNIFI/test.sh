POST /nifi-api/process-groups/fdeb9f26-0188-1000-edca-df7f0c07fd61/process-groups/upload HTTP/1.1
Host: localhost:8443
Cookie: __Secure-Request-Token=2279c67b-7038-40d4-9fbb-d85bef414c97; __Secure-Authorization-Bearer=eyJraWQiOiJkNmE5ZGE3Ny00N2U2LTRhMWEtYWZlMS1kYjQ5ODllZDgzNTgiLCJhbGciOiJQUzUxMiJ9.eyJzdWIiOiJlMzM1N2Y2NS0zZDQxLTQ5NGQtYTRmNS1lZDZhNDc0MGQ5YmMiLCJhdWQiOiJTaW5nbGVVc2VyTG9naW5JZGVudGl0eVByb3ZpZGVyIiwibmJmIjoxNjg3ODkwMTA5LCJpc3MiOiJTaW5nbGVVc2VyTG9naW5JZGVudGl0eVByb3ZpZGVyIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiZTMzNTdmNjUtM2Q0MS00OTRkLWE0ZjUtZWQ2YTQ3NDBkOWJjIiwiZXhwIjoxNjg3OTE4OTA5LCJpYXQiOjE2ODc4OTAxMDksImp0aSI6IjdhZmQ5ZGE4LTllY2YtNGE5Ni1hZjUwLWNmMWM2YjAwNzFlNyJ9.dsy76PGl1d5ROiyxnIzmtVgCpuiRRdqg-2jdgqL6LCQ14ZlHIw9oJNSDE1CgzuQDriPKGBUoZz_7egYQCnM-CRf22M1Qz_Upa3xIRuZDUeX9mtXrBOZ-L4ksoeT3-S-9RJvYPLeD_ogFKvqn0VWD9q3lrACVzo1LiSfixJflzBFy0GFPw72fCFnCzaSPHEdktlAcANg_LMdCNMnqiP7VXIS4f1LVtJsdJMuoh5jrrKFuywzTImMTp2DKBiOOE-FVkKLuKWQa1wRvB-zoCLoItVNP-b-llENUyU2N1fdi93qjtI75GqwR2XaxbS6-yRvqMXsBQ3xk1nRADx1YZO9icUXjERGVPNvt1rbz1WZ6j_gZ7QJyYApwewlg0SO6Yadeppa07QjD9Gl18rBfPM_HkrswpmcqThzrcl3vvZy-vDKY4c5LudXVbAdw-iZfOwAI3_smDRheJd89vKg5hFipfQRMTiweDu4uYREZoF_vMtw1wfYikScIFhKIEOwZ-Hr_VbpcAvvtGSY6vzHRd1snZX7SoqZjFFOolvkEXQsf_yfH_U8lJSlDFJil0nLT-vPXSsH-xIu6ZfoySOclEn3Nn5VvgQ1CPrgjCQRuC_cmH4DmVamk9RXJOFXs_v08jIIKFpvm6YlE0ssnEIGx66bO67JT80PS9UvCkcwS77eoWco
Content-Length: 23606
Sec-Ch-Ua: 
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.134 Safari/537.36
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryCun1xx5QB9NAgADp
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
Request-Token: 2279c67b-7038-40d4-9fbb-d85bef414c97
Sec-Ch-Ua-Platform: ""
Origin: https://localhost:8443
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://localhost:8443/nifi/
Accept-Encoding: gzip, deflate
Accept-Language: it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7
Connection: close

------WebKitFormBoundaryCun1xx5QB9NAgADp
Content-Disposition: form-data; name="file"; filename="Gruop1.json"
Content-Type: application/json

{"flowContents":{"identifier":"b3c3f60e-3aae-3f99-8d99-c6d0c0e8151c","instanceIdentifier":"fc5d3eb0-0188-1000-3b7d-ff090780d619","name":"Gruop1","comments":"","position":{"x":688.0,"y":248.0},"processGroups":[],"remoteProcessGroups":[],"processors":[{"identifier":"eeede5f1-555f-3723-ae83-1c0d483a19a8","instanceIdentifier":"4095603d-59dd-35e5-23a4-9de02578bba0","name":"RouteText","comments":"","position":{"x":886.50390625,"y":390.0},"type":"org.apache.nifi.processors.standard.RouteText","bundle":{"group":"org.apache.nifi","artifact":"nifi-standard-nar","version":"1.21.0"},"properties":{"Routing Strategy":"Route to each matching Property Name","Ignore Leading/Trailing Whitespace":"true","Matching Strategy":"Matches Regular Expression","match":"^(.*?),(.*?),(.*?),(.*?),(..*)$","Character Set":"UTF-8","Ignore Case":"false","Grouping Regular Expression":null},"propertyDescriptors":{"Routing Strategy":{"name":"Routing Strategy","displayName":"Routing Strategy","identifiesControllerService":false,"sensitive":false},"Ignore Leading/Trailing Whitespace":{"name":"Ignore Leading/Trailing Whitespace","displayName":"Ignore Leading/Trailing Whitespace","identifiesControllerService":false,"sensitive":false},"Matching Strategy":{"name":"Matching Strategy","displayName":"Matching Strategy","identifiesControllerService":false,"sensitive":false},"match":{"name":"match","displayName":"match","identifiesControllerService":false,"sensitive":false},"Character Set":{"name":"Character Set","displayName":"Character Set","identifiesControllerService":false,"sensitive":false},"Ignore Case":{"name":"Ignore Case","displayName":"Ignore Case","identifiesControllerService":false,"sensitive":false},"Grouping Regular Expression":{"name":"Grouping Regular Expression","displayName":"Grouping Regular Expression","identifiesControllerService":false,"sensitive":false}},"style":{},"schedulingPeriod":"0 sec","schedulingStrategy":"TIMER_DRIVEN","executionNode":"ALL","penaltyDuration":"30 sec","yieldDuration":"1 sec","bulletinLevel":"WARN","runDurationMillis":0,"concurrentlySchedulableTaskCount":1,"autoTerminatedRelationships":["original","unmatched"],"scheduledState":"ENABLED","retryCount":10,"retriedRelationships":[],"backoffMechanism":"PENALIZE_FLOWFILE","maxBackoffPeriod":"10 mins","componentType":"PROCESSOR","groupIdentifier":"b3c3f60e-3aae-3f99-8d99-c6d0c0e8151c"},{"identifier":"9946a90f-63d4-3427-89ba-e139db2ea33e","instanceIdentifier":"5db36517-8a80-36cd-6cd6-e6a99184607d","name":"ReplaceText","comments":"","position":{"x":1430.50390625,"y":398.0},"type":"org.apache.nifi.processors.standard.ReplaceText","bundle":{"group":"org.apache.nifi","artifact":"nifi-standard-nar","version":"1.21.0"},"properties":{"Regular Expression":"^((.*?),(.*?),(.*?),00:00:00.000,(.*))$","Replacement Value":"","Evaluation Mode":"Line-by-Line","Text to Prepend":null,"Line-by-Line Evaluation Mode":"All","Character Set":"UTF-8","Maximum Buffer Size":"1 MB","Replacement Strategy":"Regex Replace","Text to Append":null},"propertyDescriptors":{"Regular Expression":{"name":"Regular Expression","displayName":"Search Value","identifiesControllerService":false,"sensitive":false},"Replacement Value":{"name":"Replacement Value","displayName":"Replacement Value","identifiesControllerService":false,"sensitive":false},"Evaluation Mode":{"name":"Evaluation Mode","displayName":"Evaluation Mode","identifiesControllerService":false,"sensitive":false},"Text to Prepend":{"name":"Text to Prepend","displayName":"Text to Prepend","identifiesControllerService":false,"sensitive":false},"Line-by-Line Evaluation Mode":{"name":"Line-by-Line Evaluation Mode","displayName":"Line-by-Line Evaluation Mode","identifiesControllerService":false,"sensitive":false},"Character Set":{"name":"Character Set","displayName":"Character Set","identifiesControllerService":false,"sensitive":false},"Maximum Buffer Size":{"name":"Maximum Buffer Size","displayName":"Maximum Buffer Size","identifiesControllerService":false,"sensitive":false},"Replacement Strategy":{"name":"Replacement Strategy","displayName":"Replacement Strategy","identifiesControllerService":false,"sensitive":false},"Text to Append":{"name":"Text to Append","displayName":"Text to Append","identifiesControllerService":false,"sensitive":false}},"style":{},"schedulingPeriod":"0 sec","schedulingStrategy":"TIMER_DRIVEN","executionNode":"ALL","penaltyDuration":"30 sec","yieldDuration":"1 sec","bulletinLevel":"WARN","runDurationMillis":25,"concurrentlySchedulableTaskCount":1,"autoTerminatedRelationships":["failure"],"scheduledState":"ENABLED","retryCount":10,"retriedRelationships":[],"backoffMechanism":"PENALIZE_FLOWFILE","maxBackoffPeriod":"10 mins","componentType":"PROCESSOR","groupIdentifier":"b3c3f60e-3aae-3f99-8d99-c6d0c0e8151c"},{"identifier":"fde7cda2-8a31-3d43-872a-6fa314c50312","instanceIdentifier":"8d075d15-9415-3e99-4bed-07958fc4fcc9","name":"ReplaceText","comments":"","position":{"x":1438.50390625,"y":142.0},"type":"org.apache.nifi.processors.standard.ReplaceText","bundle":{"group":"org.apache.nifi","artifact":"nifi-standard-nar","version":"1.21.0"},"properties":{"Regular Expression":"(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*)","Replacement Value":"$1,$2,$22,$24,$27","Evaluation Mode":"Line-by-Line","Text to Prepend":null,"Line-by-Line Evaluation Mode":"All","Character Set":"UTF-8","Maximum Buffer Size":"1 MB","Replacement Strategy":"Regex Replace","Text to Append":null},"propertyDescriptors":{"Regular Expression":{"name":"Regular Expression","displayName":"Search Value","identifiesControllerService":false,"sensitive":false},"Replacement Value":{"name":"Replacement Value","displayName":"Replacement Value","identifiesControllerService":false,"sensitive":false},"Evaluation Mode":{"name":"Evaluation Mode","displayName":"Evaluation Mode","identifiesControllerService":false,"sensitive":false},"Text to Prepend":{"name":"Text to Prepend","displayName":"Text to Prepend","identifiesControllerService":false,"sensitive":false},"Line-by-Line Evaluation Mode":{"name":"Line-by-Line Evaluation Mode","displayName":"Line-by-Line Evaluation Mode","identifiesControllerService":false,"sensitive":false},"Character Set":{"name":"Character Set","displayName":"Character Set","identifiesControllerService":false,"sensitive":false},"Maximum Buffer Size":{"name":"Maximum Buffer Size","displayName":"Maximum Buffer Size","identifiesControllerService":false,"sensitive":false},"Replacement Strategy":{"name":"Replacement Strategy","displayName":"Replacement Strategy","identifiesControllerService":false,"sensitive":false},"Text to Append":{"name":"Text to Append","displayName":"Text to Append","identifiesControllerService":false,"sensitive":false}},"style":{},"schedulingPeriod":"0 sec","schedulingStrategy":"TIMER_DRIVEN","executionNode":"ALL","penaltyDuration":"30 sec","yieldDuration":"1 sec","bulletinLevel":"WARN","runDurationMillis":25,"concurrentlySchedulableTaskCount":1,"autoTerminatedRelationships":["failure"],"scheduledState":"ENABLED","retryCount":10,"retriedRelationships":[],"backoffMechanism":"PENALIZE_FLOWFILE","maxBackoffPeriod":"10 mins","componentType":"PROCESSOR","groupIdentifier":"b3c3f60e-3aae-3f99-8d99-c6d0c0e8151c"},{"identifier":"7e16b8aa-b22e-3a42-9ea8-a000d729b019","instanceIdentifier":"171019e6-c67d-37cc-f3fb-45c0b5dbc5e9","name":"ConsumeKafka_2_6","comments":"","position":{"x":454.50390625,"y":142.0},"type":"org.apache.nifi.processors.kafka.pubsub.ConsumeKafka_2_6","bundle":{"group":"org.apache.nifi","artifact":"nifi-kafka-2-6-nar","version":"1.21.0"},"properties":{"header-name-regex":null,"Commit Offsets":"true","group.id":"test2","bootstrap.servers":"kafka:29092","topic_type":"names","sasl.kerberos.principal":null,"sasl.kerberos.service.name":null,"kerberos-credentials-service":null,"max-uncommit-offset-wait":"1 secs","sasl.mechanism":"GSSAPI","honor-transactions":"true","kerberos-user-service":null,"message-header-encoding":"UTF-8","message-demarcator":null,"sasl.username":null,"max.poll.records":"10000","aws.profile.name":null,"security.protocol":"PLAINTEXT","ssl.context.service":null,"sasl.token.auth":"false","sasl.kerberos.keytab":null,"Communications Timeout":"60 secs","topic":"user","separate-by-key":"false","key-attribute-encoding":"utf-8","auto.offset.reset":"latest"},"propertyDescriptors":{"header-name-regex":{"name":"header-name-regex","displayName":"Headers to Add as Attributes (Regex)","identifiesControllerService":false,"sensitive":false},"Commit Offsets":{"name":"Commit Offsets","displayName":"Commit Offsets","identifiesControllerService":false,"sensitive":false},"group.id":{"name":"group.id","displayName":"Group ID","identifiesControllerService":false,"sensitive":false},"bootstrap.servers":{"name":"bootstrap.servers","displayName":"Kafka Brokers","identifiesControllerService":false,"sensitive":false},"topic_type":{"name":"topic_type","displayName":"Topic Name Format","identifiesControllerService":false,"sensitive":false},"sasl.kerberos.principal":{"name":"sasl.kerberos.principal","displayName":"Kerberos Principal","identifiesControllerService":false,"sensitive":false},"sasl.kerberos.service.name":{"name":"sasl.kerberos.service.name","displayName":"Kerberos Service Name","identifiesControllerService":false,"sensitive":false},"kerberos-credentials-service":{"name":"kerberos-credentials-service","displayName":"Kerberos Credentials Service","identifiesControllerService":true,"sensitive":false},"max-uncommit-offset-wait":{"name":"max-uncommit-offset-wait","displayName":"Max Uncommitted Time","identifiesControllerService":false,"sensitive":false},"sasl.mechanism":{"name":"sasl.mechanism","displayName":"SASL Mechanism","identifiesControllerService":false,"sensitive":false},"honor-transactions":{"name":"honor-transactions","displayName":"Honor Transactions","identifiesControllerService":false,"sensitive":false},"kerberos-user-service":{"name":"kerberos-user-service","displayName":"Kerberos User Service","identifiesControllerService":true,"sensitive":false},"message-header-encoding":{"name":"message-header-encoding","displayName":"Message Header Encoding","identifiesControllerService":false,"sensitive":false},"message-demarcator":{"name":"message-demarcator","displayName":"Message Demarcator","identifiesControllerService":false,"sensitive":false},"sasl.username":{"name":"sasl.username","displayName":"Username","identifiesControllerService":false,"sensitive":false},"max.poll.records":{"name":"max.poll.records","displayName":"Max Poll Records","identifiesControllerService":false,"sensitive":false},"aws.profile.name":{"name":"aws.profile.name","displayName":"AWS Profile Name","identifiesControllerService":false,"sensitive":false},"security.protocol":{"name":"security.protocol","displayName":"Security Protocol","identifiesControllerService":false,"sensitive":false},"ssl.context.service":{"name":"ssl.context.service","displayName":"SSL Context Service","identifiesControllerService":true,"sensitive":false},"sasl.token.auth":{"name":"sasl.token.auth","displayName":"Token Authentication","identifiesControllerService":false,"sensitive":false},"sasl.kerberos.keytab":{"name":"sasl.kerberos.keytab","displayName":"Kerberos Keytab","identifiesControllerService":false,"sensitive":false,"resourceDefinition":{"cardinality":"SINGLE","resourceTypes":["FILE"]}},"Communications Timeout":{"name":"Communications Timeout","displayName":"Communications Timeout","identifiesControllerService":false,"sensitive":false},"topic":{"name":"topic","displayName":"Topic Name(s)","identifiesControllerService":false,"sensitive":false},"separate-by-key":{"name":"separate-by-key","displayName":"Separate By Key","identifiesControllerService":false,"sensitive":false},"sasl.password":{"name":"sasl.password","displayName":"Password","identifiesControllerService":false,"sensitive":true},"key-attribute-encoding":{"name":"key-attribute-encoding","displayName":"Key Attribute Encoding","identifiesControllerService":false,"sensitive":false},"auto.offset.reset":{"name":"auto.offset.reset","displayName":"Offset Reset","identifiesControllerService":false,"sensitive":false}},"style":{},"schedulingPeriod":"0 sec","schedulingStrategy":"TIMER_DRIVEN","executionNode":"ALL","penaltyDuration":"30 sec","yieldDuration":"1 sec","bulletinLevel":"WARN","runDurationMillis":0,"concurrentlySchedulableTaskCount":1,"autoTerminatedRelationships":[],"scheduledState":"ENABLED","retryCount":10,"retriedRelationships":[],"backoffMechanism":"PENALIZE_FLOWFILE","maxBackoffPeriod":"10 mins","componentType":"PROCESSOR","groupIdentifier":"b3c3f60e-3aae-3f99-8d99-c6d0c0e8151c"},{"identifier":"c0d97cd8-d44d-38e3-8aed-be50a0db70da","instanceIdentifier":"df8b347c-8e45-3acb-52c2-6666e25a5407","name":"PublishKafka_2_6","comments":"","position":{"x":379.751953125,"y":390.0},"type":"org.apache.nifi.processors.kafka.pubsub.PublishKafka_2_6","bundle":{"group":"org.apache.nifi","artifact":"nifi-kafka-2-6-nar","version":"1.21.0"},"properties":{"compression.type":"none","attribute-name-regex":null,"bootstrap.servers":"kafka:29092","sasl.kerberos.principal":null,"sasl.kerberos.service.name":null,"kerberos-credentials-service":null,"kafka-key":null,"partition":null,"sasl.mechanism":"GSSAPI","max.block.ms":"5 sec","message-header-encoding":"UTF-8","kerberos-user-service":null,"message-demarcator":null,"transactional-id-prefix":null,"ack.wait.time":"5 secs","sasl.username":null,"use-transactions":"true","acks":"all","aws.profile.name":null,"security.protocol":"PLAINTEXT","ssl.context.service":null,"max.request.size":"1 MB","sasl.token.auth":"false","Failure Strategy":"Route to Failure","partitioner.class":"org.apache.kafka.clients.producer.internals.DefaultPartitioner","sasl.kerberos.keytab":null,"topic":"user2","key-attribute-encoding":"utf-8"},"propertyDescriptors":{"compression.type":{"name":"compression.type","displayName":"Compression Type","identifiesControllerService":false,"sensitive":false},"attribute-name-regex":{"name":"attribute-name-regex","displayName":"Attributes to Send as Headers (Regex)","identifiesControllerService":false,"sensitive":false},"bootstrap.servers":{"name":"bootstrap.servers","displayName":"Kafka Brokers","identifiesControllerService":false,"sensitive":false},"sasl.kerberos.principal":{"name":"sasl.kerberos.principal","displayName":"Kerberos Principal","identifiesControllerService":false,"sensitive":false},"sasl.kerberos.service.name":{"name":"sasl.kerberos.service.name","displayName":"Kerberos Service Name","identifiesControllerService":false,"sensitive":false},"kerberos-credentials-service":{"name":"kerberos-credentials-service","displayName":"Kerberos Credentials Service","identifiesControllerService":true,"sensitive":false},"kafka-key":{"name":"kafka-key","displayName":"Kafka Key","identifiesControllerService":false,"sensitive":false},"partition":{"name":"partition","displayName":"Partition","identifiesControllerService":false,"sensitive":false},"sasl.mechanism":{"name":"sasl.mechanism","displayName":"SASL Mechanism","identifiesControllerService":false,"sensitive":false},"max.block.ms":{"name":"max.block.ms","displayName":"Max Metadata Wait Time","identifiesControllerService":false,"sensitive":false},"message-header-encoding":{"name":"message-header-encoding","displayName":"Message Header Encoding","identifiesControllerService":false,"sensitive":false},"kerberos-user-service":{"name":"kerberos-user-service","displayName":"Kerberos User Service","identifiesControllerService":true,"sensitive":false},"message-demarcator":{"name":"message-demarcator","displayName":"Message Demarcator","identifiesControllerService":false,"sensitive":false},"transactional-id-prefix":{"name":"transactional-id-prefix","displayName":"Transactional Id Prefix","identifiesControllerService":false,"sensitive":false},"ack.wait.time":{"name":"ack.wait.time","displayName":"Acknowledgment Wait Time","identifiesControllerService":false,"sensitive":false},"sasl.username":{"name":"sasl.username","displayName":"Username","identifiesControllerService":false,"sensitive":false},"use-transactions":{"name":"use-transactions","displayName":"Use Transactions","identifiesControllerService":false,"sensitive":false},"acks":{"name":"acks","displayName":"Delivery Guarantee","identifiesControllerService":false,"sensitive":false},"aws.profile.name":{"name":"aws.profile.name","displayName":"AWS Profile Name","identifiesControllerService":false,"sensitive":false},"security.protocol":{"name":"security.protocol","displayName":"Security Protocol","identifiesControllerService":false,"sensitive":false},"ssl.context.service":{"name":"ssl.context.service","displayName":"SSL Context Service","identifiesControllerService":true,"sensitive":false},"max.request.size":{"name":"max.request.size","displayName":"Max Request Size","identifiesControllerService":false,"sensitive":false},"sasl.token.auth":{"name":"sasl.token.auth","displayName":"Token Authentication","identifiesControllerService":false,"sensitive":false},"Failure Strategy":{"name":"Failure Strategy","displayName":"Failure Strategy","identifiesControllerService":false,"sensitive":false},"partitioner.class":{"name":"partitioner.class","displayName":"Partitioner class","identifiesControllerService":false,"sensitive":false},"sasl.kerberos.keytab":{"name":"sasl.kerberos.keytab","displayName":"Kerberos Keytab","identifiesControllerService":false,"sensitive":false,"resourceDefinition":{"cardinality":"SINGLE","resourceTypes":["FILE"]}},"topic":{"name":"topic","displayName":"Topic Name","identifiesControllerService":false,"sensitive":false},"sasl.password":{"name":"sasl.password","displayName":"Password","identifiesControllerService":false,"sensitive":true},"key-attribute-encoding":{"name":"key-attribute-encoding","displayName":"Key Attribute Encoding","identifiesControllerService":false,"sensitive":false}},"style":{},"schedulingPeriod":"0 sec","schedulingStrategy":"TIMER_DRIVEN","executionNode":"ALL","penaltyDuration":"30 sec","yieldDuration":"1 sec","bulletinLevel":"WARN","runDurationMillis":0,"concurrentlySchedulableTaskCount":1,"autoTerminatedRelationships":["success","failure"],"scheduledState":"ENABLED","retryCount":10,"retriedRelationships":[],"backoffMechanism":"PENALIZE_FLOWFILE","maxBackoffPeriod":"10 mins","componentType":"PROCESSOR","groupIdentifier":"b3c3f60e-3aae-3f99-8d99-c6d0c0e8151c"}],"inputPorts":[],"outputPorts":[],"connections":[{"identifier":"ee185c33-41c4-36cb-95fe-3c88c0093fe8","instanceIdentifier":"b23b174c-d0d1-3ff6-5cd4-fc90686a32c4","name":"","source":{"id":"9946a90f-63d4-3427-89ba-e139db2ea33e","type":"PROCESSOR","groupId":"b3c3f60e-3aae-3f99-8d99-c6d0c0e8151c","name":"ReplaceText","comments":"","instanceIdentifier":"5db36517-8a80-36cd-6cd6-e6a99184607d"},"destination":{"id":"eeede5f1-555f-3723-ae83-1c0d483a19a8","type":"PROCESSOR","groupId":"b3c3f60e-3aae-3f99-8d99-c6d0c0e8151c","name":"RouteText","comments":"","instanceIdentifier":"4095603d-59dd-35e5-23a4-9de02578bba0"},"labelIndex":1,"zIndex":0,"selectedRelationships":["success"],"backPressureObjectThreshold":10000,"backPressureDataSizeThreshold":"1 GB","flowFileExpiration":"0 sec","prioritizers":[],"bends":[],"loadBalanceStrategy":"DO_NOT_LOAD_BALANCE","partitioningAttribute":"","loadBalanceCompression":"DO_NOT_COMPRESS","componentType":"CONNECTION","groupIdentifier":"b3c3f60e-3aae-3f99-8d99-c6d0c0e8151c"},{"identifier":"fef1c1c4-b797-3d3f-90b3-cdd0f145f060","instanceIdentifier":"1a33f1a7-8252-361d-9cfd-77940b205dfb","name":"","source":{"id":"7e16b8aa-b22e-3a42-9ea8-a000d729b019","type":"PROCESSOR","groupId":"b3c3f60e-3aae-3f99-8d99-c6d0c0e8151c","name":"ConsumeKafka_2_6","comments":"","instanceIdentifier":"171019e6-c67d-37cc-f3fb-45c0b5dbc5e9"},"destination":{"id":"fde7cda2-8a31-3d43-872a-6fa314c50312","type":"PROCESSOR","groupId":"b3c3f60e-3aae-3f99-8d99-c6d0c0e8151c","name":"ReplaceText","comments":"","instanceIdentifier":"8d075d15-9415-3e99-4bed-07958fc4fcc9"},"labelIndex":1,"zIndex":0,"selectedRelationships":["success"],"backPressureObjectThreshold":10000,"backPressureDataSizeThreshold":"1 GB","flowFileExpiration":"0 sec","prioritizers":[],"bends":[],"loadBalanceStrategy":"DO_NOT_LOAD_BALANCE","partitioningAttribute":"","loadBalanceCompression":"DO_NOT_COMPRESS","componentType":"CONNECTION","groupIdentifier":"b3c3f60e-3aae-3f99-8d99-c6d0c0e8151c"},{"identifier":"6f960a9f-0c53-3b51-a359-3e93928029db","instanceIdentifier":"2b06f33a-8447-399d-bc7c-ce8c9cefe52b","name":"match","source":{"id":"eeede5f1-555f-3723-ae83-1c0d483a19a8","type":"PROCESSOR","groupId":"b3c3f60e-3aae-3f99-8d99-c6d0c0e8151c","name":"RouteText","comments":"","instanceIdentifier":"4095603d-59dd-35e5-23a4-9de02578bba0"},"destination":{"id":"c0d97cd8-d44d-38e3-8aed-be50a0db70da","type":"PROCESSOR","groupId":"b3c3f60e-3aae-3f99-8d99-c6d0c0e8151c","name":"PublishKafka_2_6","comments":"","instanceIdentifier":"df8b347c-8e45-3acb-52c2-6666e25a5407"},"labelIndex":1,"zIndex":0,"selectedRelationships":["match","matched"],"backPressureObjectThreshold":10000,"backPressureDataSizeThreshold":"1 GB","flowFileExpiration":"0 sec","prioritizers":[],"bends":[],"loadBalanceStrategy":"DO_NOT_LOAD_BALANCE","partitioningAttribute":"","loadBalanceCompression":"DO_NOT_COMPRESS","componentType":"CONNECTION","groupIdentifier":"b3c3f60e-3aae-3f99-8d99-c6d0c0e8151c"},{"identifier":"d73dbfa7-dfb0-3556-8893-89d9e136ec58","instanceIdentifier":"bf1863b6-4f2d-32a7-1e6a-61751217e873","name":"","source":{"id":"fde7cda2-8a31-3d43-872a-6fa314c50312","type":"PROCESSOR","groupId":"b3c3f60e-3aae-3f99-8d99-c6d0c0e8151c","name":"ReplaceText","comments":"","instanceIdentifier":"8d075d15-9415-3e99-4bed-07958fc4fcc9"},"destination":{"id":"9946a90f-63d4-3427-89ba-e139db2ea33e","type":"PROCESSOR","groupId":"b3c3f60e-3aae-3f99-8d99-c6d0c0e8151c","name":"ReplaceText","comments":"","instanceIdentifier":"5db36517-8a80-36cd-6cd6-e6a99184607d"},"labelIndex":1,"zIndex":0,"selectedRelationships":["success"],"backPressureObjectThreshold":10000,"backPressureDataSizeThreshold":"1 GB","flowFileExpiration":"0 sec","prioritizers":[],"bends":[],"loadBalanceStrategy":"DO_NOT_LOAD_BALANCE","partitioningAttribute":"","loadBalanceCompression":"DO_NOT_COMPRESS","componentType":"CONNECTION","groupIdentifier":"b3c3f60e-3aae-3f99-8d99-c6d0c0e8151c"}],"labels":[],"funnels":[],"controllerServices":[],"variables":{},"defaultFlowFileExpiration":"0 sec","defaultBackPressureObjectThreshold":10000,"defaultBackPressureDataSizeThreshold":"1 GB","componentType":"PROCESS_GROUP","flowFileConcurrency":"UNBOUNDED","flowFileOutboundPolicy":"STREAM_WHEN_AVAILABLE"},"externalControllerServices":{},"parameterContexts":{},"flowEncodingVersion":"1.0","parameterProviders":{},"latest":false}
------WebKitFormBoundaryCun1xx5QB9NAgADp
Content-Disposition: form-data; name="disconnectedNodeAcknowledged"

false
------WebKitFormBoundaryCun1xx5QB9NAgADp
Content-Disposition: form-data; name="groupName"

Gruop1
------WebKitFormBoundaryCun1xx5QB9NAgADp
Content-Disposition: form-data; name="positionX"

294
------WebKitFormBoundaryCun1xx5QB9NAgADp
Content-Disposition: form-data; name="positionY"

81
------WebKitFormBoundaryCun1xx5QB9NAgADp
Content-Disposition: form-data; name="clientId"

fe17296c-0188-1000-92b5-0cb9e75d034c
------WebKitFormBoundaryCun1xx5QB9NAgADp--