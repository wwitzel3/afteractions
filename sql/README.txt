This folder contains the modified versions of the CCP EVE Dump that is needed for afteractions.
This includes things like Systems, Ships, and Modules. These tables are heavily modified and
are not good representations of the actual DB dumps from CCP.

 - Queb
 
This query was used to generate the slot position for modules.

create table invslots as select invtypes.typeid, dgmtypeeffects.effectid
from invtypes, dgmtypeeffects where invtypes.typeid = dgmtypeeffects.typeid and effectid in (11,12,13,2663,3772);

A PK was added to the typeid column and a FK was added to effectid that references the invposition table below.

CREATE TABLE invpositions
(
  effectid smallint NOT NULL,
  "name" character(15),
  CONSTRAINT invposition_pkey PRIMARY KEY (effectid)
)
WITH (OIDS=FALSE);
ALTER TABLE invpositions OWNER TO postgres;

This table was seeded with the following information.

0;"None           "
11;"Low Slot       "
12;"High Slot      "
13;"Medium Slot    "
2663;"Rig Slot       "
3772;"Subsystem Slot "
