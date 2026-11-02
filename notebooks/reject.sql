INSTALL httpfs;
LOAD httpfs;

CREATE OR REPLACE TABLE hmeq AS
SELECT *
FROM read_csv(
    'https://raw.githubusercontent.com/sassoftware/sas-viya-dmml-pipelines/refs/heads/master/data/hmeq.csv',
    store_rejects = true,
    rejects_table = 'hmeq_rejects',
    rejects_scan = 'hmeq_reject_scans'
);