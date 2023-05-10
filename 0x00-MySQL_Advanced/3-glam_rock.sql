-- lists all bads with glam_rock as their main style ranked my their longevity
SELECT band_name, (IFNULL(split, '2023') - formed) AS lifespan
FROM metal_bands WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;
