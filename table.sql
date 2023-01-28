CREATE TABLE "public"."befragung" (
  "id" int4 NOT NULL DEFAULT nextval('befragung_seq'::regclass),
  "jahr" varchar(4) COLLATE "pg_catalog"."default",
  "monat" varchar(2) COLLATE "pg_catalog"."default",
  "geschlecht" varchar(255) COLLATE "pg_catalog"."default",
  "lokal" varchar(255) COLLATE "pg_catalog"."default",
  "empfarzt" bool,
  "empfangeh" bool,
  "eigen" bool,
  "wohnort" bool,
  "andere" bool,
  "notearzt" int2,
  "notepflege" int2,
  "notephysio" int2,
  "notesozial" int2,
  "notegesamt" int2,
  "anspruch" varchar(255) COLLATE "pg_catalog"."default",
  "empfehlen" varchar(255) COLLATE "pg_catalog"."default",
  CONSTRAINT "befragung_pkey" PRIMARY KEY ("id")
)
;

