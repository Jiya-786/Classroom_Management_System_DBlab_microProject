
CREATE TABLE Users (
    userID INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);


CREATE TABLE Students (
    studentID INT PRIMARY KEY,
    enrollmentDate DATE NOT NULL,
    GPA DECIMAL(3,2),
    major VARCHAR(100)
);


CREATE TABLE Teachers (
    teacherID INT PRIMARY KEY,
    department VARCHAR(100) NOT NULL,
    salary DECIMAL(10,2),
    specialization VARCHAR(100)
);


CREATE TABLE Classrooms (
    roomID INT PRIMARY KEY,
    floor INT NOT NULL,
    capacity INT NOT NULL CHECK (capacity > 0)
);


CREATE TABLE SmartBoards (
    serialNo VARCHAR(50) PRIMARY KEY,
    brand VARCHAR(50) NOT NULL,
    installationDate DATE,
    roomID INT NOT NULL UNIQUE -- Enforces 1-to-1 relationship
);


CREATE TABLE Courses (
    courseID INT PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    creditValue INT DEFAULT 3
);


CREATE TABLE Module (
    moduleID INT PRIMARY KEY,
    courseID INT NOT NULL,
    title VARCHAR(150) NOT NULL,
    content TEXT
);


CREATE TABLE TimeSlots (
    slotID INT PRIMARY KEY,
    startTime TIME NOT NULL,
    endTime TIME NOT NULL,
    CHECK (endTime > startTime)
);


CREATE TABLE ClassSessions (
    sessionID INT PRIMARY KEY,
    topic VARCHAR(200) NOT NULL,
    duration INT NOT NULL, -- in minutes
    roomID INT,            -- NULL allowed based on business rule #10
    courseID INT NOT NULL,
    slotID INT NOT NULL,
    teacherID INT NOT NULL
);


CREATE TABLE Enrollments (
    studentID INT NOT NULL,
    courseID INT NOT NULL,
    grade VARCHAR(2),
    enrollmentStatus VARCHAR(20) DEFAULT 'Enrolled',
    PRIMARY KEY (studentID, courseID)
);
