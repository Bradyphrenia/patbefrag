CREATE SEQUENCE "public"."befragung_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

SELECT setval('"public"."befragung_seq"', 1000, true);

