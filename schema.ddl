DROP SCHEMA IF EXISTS AXON_DATA;

CREATE SCHEMA AXON_DATA;

CREATE TABLE AXON_DATA.EVENT
(
    ID       int primary key not null unique auto_increment,
    NAME     varchar(255)    not null,
    LOCATION varchar(255)    not null,
    ZIPCODE  int             not null,
    CREATED  TIMESTAMP       not null default CURRENT_TIMESTAMP,
    UPDATED  TIMESTAMP       not null default CURRENT_TIMESTAMP
);

CREATE TABLE AXON_DATA.ATTENDEE
(
    ID      int primary key not null unique auto_increment,
    NAME    varchar(255)    not null,
    EMAIL   varchar(255)    not null,
    PHONE   varchar(255)    not null,
    COMPANY varchar(255),
    CREATED TIMESTAMP       not null default CURRENT_TIMESTAMP,
    UPDATED TIMESTAMP       not null default CURRENT_TIMESTAMP
);

CREATE TABLE AXON_DATA.BOOTH
(
    ID      int primary key not null unique auto_increment,
    NAME    varchar(255)    not null,
    CREATED TIMESTAMP       not null default CURRENT_TIMESTAMP,
    UPDATED TIMESTAMP       not null default CURRENT_TIMESTAMP
);

CREATE TABLE AXON_DATA.BOOTH_INTERACTION
(
    ID          int primary key not null unique auto_increment,
    ATTENDEE_ID int             not null,
    EVENT_ID    int             not null,
    BOOTH_ID    int             not null,
    CREATED     TIMESTAMP       not null default CURRENT_TIMESTAMP,
    UPDATED     TIMESTAMP       not null default CURRENT_TIMESTAMP,
    FOREIGN KEY (ATTENDEE_ID) REFERENCES ATTENDEE (ID),
    FOREIGN KEY (EVENT_ID) REFERENCES EVENT (ID),
    FOREIGN KEY (BOOTH_ID) REFERENCES BOOTH (ID)
);

CREATE TABLE AXON_DATA.CURRENT_BADGE_ASSIGNMENTS
(
    BADGE_ID    int primary key not null unique,
    ATTENDEE_ID int null,
    CREATED     TIMESTAMP       not null default CURRENT_TIMESTAMP,
    UPDATED     TIMESTAMP       not null default CURRENT_TIMESTAMP,
    FOREIGN KEY (ATTENDEE_ID) REFERENCES ATTENDEE (ID)
);

CREATE TABLE AXON_DATA.CURRENT_EVENT
(
    EVENT_ID int primary key not null unique
)
