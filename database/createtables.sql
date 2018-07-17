CREATE TABLE Game(
    GameID      INT NOT NULL AUTO_INCREMENT,
    title       VARCHAR(30),
    MainGenre   VARCHAR(15),
    online      bit default 0,
    NumPlayers  INT default 0,
    PRIMARY KEY(GameID)
);

CREATE TABLE Publisher(
    PubID       INT NOT NULL AUTO_INCREMENT,
    PubName     VARCHAR(30),
    location    VARCHAR(15),
    founded     INT,
    PRIMARY KEY(PubID)
);

CREATE TABLE Studio(
    StudioID    INT NOT NULL AUTO_INCREMENT,
    StudioName  VARCHAR(30),
    location    VARCHAR(15),
    founded     INT,
    PRIMARY KEY(StudioID)
);

CREATE TABLE Contributor(
    ContrID     INT NOT NULL AUTO_INCREMENT,
    FirstName   VARCHAR(20),
    LastName    VARCHAR(20),
    PRIMARY KEY(ContrID)
);

CREATE TABLE Region(
    RegionID    INT NOT NULL AUTO_INCREMENT,
    name        VARCHAR(20),
    PRIMARY KEY(RegionID)
);

CREATE TABLE Console(
    ConsoleID   INT NOT NULL AUTO_INCREMENT,
    name        VARCHAR(20),
    online      BIT default 0,
    numPorts    INT,
    maker       VARCHAR(20),
    Discont     BIT default 0,
    PRIMARY KEY(ConsoleID)
);

CREATE TABLE GameRelease(
    ReleaseID   INT NOT NULL AUTO_INCREMENT,
    RelDate     DATE,
    GameID      INT,
    ConsoleID   INT,
    RegionID    INT,
    PRIMARY KEY(ReleaseID),
    FOREIGN KEY (GameID) REFERENCES Game(GameID),
    FOREIGN KEY (ConsoleID) REFERENCES Console(ConsoleID),
    FOREIGN KEY (RegionID) REFERENCES Region(RegionID)
);

CREATE TABLE Publishes(
    GameID      INT,
    PubID       INT,
    PRIMARY KEY(GameID, PubID),
    FOREIGN KEY (GameID) REFERENCES Game(GameID),
    FOREIGN KEY (PubID) REFERENCES Publisher(PubID)
);

CREATE TABLE Develops(
    StudioID    INT,
    GameID      INT,
    PRIMARY KEY(GameID, StudioID),
    FOREIGN KEY (GameID) REFERENCES Game(GameID),
    FOREIGN KEY (StudioID) REFERENCES Studio(StudioID)
);

CREATE TABLE Contributes(
    GameID      INT,
    ContrID     INT,
    PRIMARY KEY(GameID, ContrID),
    FOREIGN KEY (GameID) REFERENCES Game(GameID),
    FOREIGN KEY (ContrID) REFERENCES Contributor(ContrID)
);
