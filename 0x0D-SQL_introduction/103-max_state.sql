-- Show the max temperatire of each state
-- Ordered by state name
SELECT `state`, MAX(`value`) AS `max_temp`
FROM `temperature`
GROUP BY `state`
ORDER BY `state`;
