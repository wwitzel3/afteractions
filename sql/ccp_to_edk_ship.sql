SELECT invtypes.typeid,
  invtypes.graphicid,
  kb3_ships.shp_id
FROM invtypes,
  kb3_ships
WHERE invtypes.typeid  = kb3_ships.shp_id
AND graphicid != 0
GROUP BY graphicid