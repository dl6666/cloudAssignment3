twitt = load '$INPUT' as (message:chararray);
filtered = FILTER twitt BY (SUBSTRING(message,0,1) == '@');
indexed = RANK filtered;
timestamped = FOREACH indexed GENERATE ($0)/189700 AS timestamp,message;
parsed = FOREACH timestamped GENERATE timestamp, FLATTEN( TOKENIZE(message) ) AS word;
hashtaged = FILTER parsed BY UPPER(word) MATCHES '#\\s*(\\w+)';
taggroups = GROUP hashtaged BY (timestamp, word);
tagcount = FOREACH taggroups GENERATE FLATTEN(group) AS (timestamp, hashtag), COUNT( hashtaged ) AS count;
grouped = GROUP tagcount BY timestamp;
top5 = foreach grouped {
        sorted = order tagcount by count desc;
        top    = limit sorted 20;
        generate flatten(top);
};
STORE top5 INTO '$OUTPUT/forpart2';
