-- Import in hbtn_0c_0 database this table dump: download (same as Temperatures #0)
-- Script that displays the max temperature of each state (ordered by State name).

SELECT state, MAX(value) FROM temperatures GROUP BY state ORDER BY state;
