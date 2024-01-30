-- khulnasoft user
CREATE LOGIN khulnasoft WITH PASSWORD = 'Password12!';
CREATE USER khulnasoft FOR LOGIN khulnasoft;
GRANT SELECT on sys.dm_os_performance_counters to khulnasoft;
GRANT VIEW SERVER STATE to khulnasoft;
GRANT CONNECT ANY DATABASE to khulnasoft;
GRANT VIEW ANY DEFINITION to khulnasoft;

-- test users
CREATE LOGIN bob WITH PASSWORD = 'Password12!';
CREATE USER bob FOR LOGIN bob;
GRANT CONNECT ANY DATABASE to bob;
CREATE LOGIN fred WITH PASSWORD = 'Password12!';
CREATE USER fred FOR LOGIN fred;
GRANT CONNECT ANY DATABASE to fred;
GO

-- Create test database for integration tests
-- only bob and fred have read/write access to this database
CREATE DATABASE khulnasoft_test;
GO
USE khulnasoft_test;
-- This table is pronounced "things" except we've replaced "th" with the greek lower case "theta" to ensure we
-- correctly support unicode throughout the integration.
CREATE TABLE khulnasoft_test.dbo.ϑings (id int, name varchar(255));
INSERT INTO khulnasoft_test.dbo.ϑings VALUES (1, 'foo'), (2, 'bar');
CREATE USER bob FOR LOGIN bob;
CREATE USER fred FOR LOGIN fred;
CREATE CLUSTERED INDEX thingsindex ON khulnasoft_test.dbo.ϑings (name);
GO

EXEC sp_addrolemember 'db_datareader', 'bob'
EXEC sp_addrolemember 'db_datareader', 'fred'
EXEC sp_addrolemember 'db_datawriter', 'bob'
GO

CREATE PROCEDURE bobProc AS
BEGIN
    SELECT * FROM ϑings;
END;
GO

CREATE PROCEDURE bobProcParams @P1 INT = NULL, @P2 nvarchar(8) = NULL AS
BEGIN
    SELECT * FROM ϑings WHERE id = @P1;
    SELECT id FROM ϑings WHERE name = @P2;
END;
GO

GRANT EXECUTE on bobProcParams to bob;
GRANT EXECUTE on bobProc to bob;
GRANT EXECUTE on bobProc to fred;
GO

CREATE PROCEDURE procedureWithLargeCommment AS
/* 
author: Khulnasoft 
usage: some random comments
test: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
description: bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
this comment has no actual meanings, just to test large sp with truncation
the quick brown fox jumps over the lazy dog, the quick brown fox jumps over the lazy dog, the quick brown fox jumps over the lazy dog
*/
BEGIN
    SELECT * FROM ϑings;
END;
GO
GRANT EXECUTE on procedureWithLargeCommment to bob;
GRANT EXECUTE on procedureWithLargeCommment to fred;
GO

-- create an offline database to have an unavailable database to test with
CREATE DATABASE unavailable_db;
GO
ALTER DATABASE unavailable_db SET OFFLINE;
GO

-- create a a restricted database to ensure the agent gracefully handles not being able to connect
-- to it
CREATE DATABASE restricted_db;
GO
ALTER DATABASE restricted_db SET RESTRICTED_USER
GO

-- create test procedure for metrics loading feature
USE master;
GO
CREATE PROCEDURE pyStoredProc AS
BEGIN
    CREATE TABLE #Khulnasoft
    (
        [metric] varchar(255) not null,
        [type] varchar(50) not null,
        [value] float not null,
        [tags] varchar(255)
    )
    SET NOCOUNT ON;
    INSERT INTO #Khulnasoft (metric, type, value, tags) VALUES
                                                         ('sql.sp.testa', 'gauge', 100, 'foo:bar,baz:qux'),
                                                         ('sql.sp.testb', 'gauge', 1, 'foo:bar,baz:qux'),
                                                         ('sql.sp.testb', 'gauge', 2, 'foo:bar,baz:qux');
    SELECT * FROM #Khulnasoft;
END;
GO
GRANT EXECUTE on pyStoredProc to khulnasoft;
GO

CREATE PROCEDURE exampleProcWithoutNocount AS
BEGIN
    CREATE TABLE #Hello
    (
        [value] int not null,
    )
    INSERT INTO #Hello VALUES (1)
    select * from #Hello;
END;
GO
GRANT EXECUTE on exampleProcWithoutNocount to khulnasoft;
GO

CREATE PROCEDURE encryptedProc WITH ENCRYPTION AS
BEGIN
    select count(*) from sys.databases;
END;
GO
GRANT EXECUTE on encryptedProc to bob;
GO

-- create test procedure with multiple queries
CREATE PROCEDURE multiQueryProc AS
BEGIN
    declare @total int = 0;
    select @total = @total + count(*) from sys.databases where name like '%_';
    select @total = @total + count(*) from sys.sysobjects where type = 'U';
    select @total;
END;
GO
GRANT EXECUTE on multiQueryProc to bob;
GO

-- test procedure with IF ELSE branches and temp tables
CREATE PROCEDURE conditionalPlanTest
 @Switch INTEGER
AS
BEGIN
 SET NOCOUNT ON
 CREATE TABLE #Ids (Id INTEGER PRIMARY KEY)

 IF (@Switch > 0)
  BEGIN
   INSERT INTO #Ids (Id) VALUES (1)
  END 

 IF (@Switch > 1)
  BEGIN
   INSERT #Ids (Id) VALUES (2)
  END

 SELECT * FROM #Ids
END
GO
GRANT EXECUTE on conditionalPlanTest to bob;
GO
