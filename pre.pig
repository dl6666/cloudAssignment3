twitt = load '$INPUT' as (message:chararray);
filtered = FILTER twitt BY (SUBSTRING(message,0,1) == '@');
STORE filtered INTO '$OUTPUT/filtered';
