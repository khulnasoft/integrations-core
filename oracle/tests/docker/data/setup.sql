ALTER SESSION SET "_ORACLE_SCRIPT" = TRUE;
CREATE USER khulnasoft IDENTIFIED BY Oracle123;
GRANT CONNECT TO khulnasoft;
GRANT SELECT ON GV_$PROCESS TO khulnasoft;
GRANT SELECT ON gv_$sysmetric TO khulnasoft;
GRANT SELECT ON sys.dba_data_files TO khulnasoft;
GRANT SELECT ON sys.dba_tablespaces TO khulnasoft;
GRANT SELECT ON sys.dba_tablespace_usage_metrics TO khulnasoft;
EXIT;
