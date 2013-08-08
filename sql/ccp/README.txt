These tables need to be loaded for after-actions to work.
Easiest way to do that is to pipe the file in to your mysql command line client.

$ mysql -uuser afteractions < inca10-invCategories-mysql5-v1.sql
$ mysql -uuser afteractions < inca10-invFlags-mysql5-v1.sql
$ mysql -uuser afteractions < inca10-invGroups-mysql5-v1.sql 
$ mysql -uuser afteractions < inca10-invTypes-mysql5-v1.sql 
$ mysql -uuser afteractions < inca10-mapConstellations-mysql5-v1.sql 
$ mysql -uuser afteractions < inca10-mapRegions-mysql5-v1.sql 
$ mysql -uuser afteractions < inca10-mapSolarSystems-mysql5-v1.sql 

