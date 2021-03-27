DROP TABLE IF EXISTS BusRoutes;
DROP TABLE IF EXISTS BusServices;
DROP TABLE IF EXISTS BusStops;

CREATE TABLE BusRoutes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ServiceNo TEXT,
    Operator TEXT,
    Direction INTEGER,
    StopSequence INTEGER,
    BusStopCode TEXT,
    Distance INTEGER,
    WD_FirstBus TEXT,
    WD_LastBus TEXT,
    SAT_FirstBus TEXT,
    SAT_LastBus TEXT,
    SUN_FirstBus TEXT,
    SUN_LastBus TEXT,
);

CREATE TABLE BusServices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
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
)

CREATE TABLE BusStops (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    BusStopCode TEXT,
    RoadName TEXT,
    Description TEXT,
    Latitude REAL,
    Longitude REAL,
)