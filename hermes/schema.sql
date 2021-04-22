DROP TABLE IF EXISTS BusRoutes;
DROP TABLE IF EXISTS BusServices;
DROP TABLE IF EXISTS BusStops;

CREATE TABLE BusRoutes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    BusServiceNo TEXT,
    StopSequence INTEGER,
    BusStopCode TEXT,
    Distance INTEGER,
    WD_FirstBus TEXT,
    WD_LastBus TEXT,
    SAT_FirstBus TEXT,
    SAT_LastBus TEXT,
    SUN_FirstBus TEXT,
    SUN_LastBus TEXT,
    FOREIGN KEY (BusServiceNo) REFERENCES BusServices (ServiceNo),
    FOREIGN KEY (BusStopCode) REFERENCES BusStops (StopCode)
);

CREATE TABLE BusServices (
    ServiceNo TEXT,
    Operator TEXT,
    Direction INTEGER,
    Category TEXT,
    OriginCode TEXT,
    DestinationCode TEXT,
    AM_Peak_Freq TEXT,
    AM_Offpeak_Freq TEXT,
    PM_Peak_Freq TEXT,
    PM_Offpeak_Freq TEXT,
    LoopDesc TEXT,
    PRIMARY KEY (ServiceNo, Direction)
);

CREATE TABLE BusStops (
    BusStopCode TEXT,
    RoadName TEXT,
    Description TEXT,
    Latitude REAL,
    Longitude REAL,
    PRIMARY KEY (BusStopCode)
);