-- rank country origins of bands odedered by the number of (non-unique) fans
SELECT origin, SUM(fans) AS nb_fans FROM metal_bands GROUP BY origin ORDER BY SUM(fans) DESC;
