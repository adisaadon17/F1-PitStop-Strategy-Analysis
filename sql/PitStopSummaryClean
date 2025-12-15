/*
    View Name: analytics.PitStop_summary_clean
    Objective:
        Clean and standardize pit stop data in order to analyze pit lane efficiency
        by team. Keeps only realistic pit stops between 10 and 100 seconds and
        links each stop to its race, constructor, and driver.

    Used In Power BI:
        "Average Total Pit Lane Duration by Team"

    Source Tables:
        dbo.pitstops, dbo.results, dbo.constructors,
        dbo.races, dbo.drivers
*/

CREATE OR ALTER VIEW analytics.PitStop_summary_clean AS
SELECT
    p.raceId,
    ra.name AS raceName,
    c.name AS constructorName,
    CONCAT(d.forename, ' ', d.surname) AS driverName,
    CAST(p.milliseconds / 1000.0 AS DECIMAL(10, 3)) AS pitDurationSec
FROM dbo.pitstops AS p
INNER JOIN dbo.results AS r
    ON r.raceId = p.raceId
    AND r.driverId = p.driverId
INNER JOIN dbo.constructors AS c
    ON c.constructorId = r.constructorId
INNER JOIN dbo.races AS ra
    ON ra.raceId = p.raceId
INNER JOIN dbo.drivers AS d
    ON d.driverId = p.driverId
WHERE p.milliseconds BETWEEN 10000 AND 100000;

