-- Classroom Management System Seed Data
-- Prepared for Jiya Merja (DSAI Project)

USE classroom_db;

-- 1. Insert Users (Parents of Students and Teachers)
INSERT INTO Users (userID, name, email) VALUES
(101, 'Jiya Merja', 'jiya.merja@iiitb.ac.in'),
(102, 'Aryan Sharma', 'aryan.s@example.com'),
(103, 'Priya Singh', 'priya.v@university.edu'),
(104, 'Dr. Amit Kumar', 'amit.kumar@faculty.edu'),
(105, 'Prof. Sarah John', 'sarah.j@faculty.edu'),
(106, 'Rohan Gupta', 'rohan.g@example.com'),
(107, 'Ananya Iyer', 'ananya.i@example.com');

-- 2. Insert Students
INSERT INTO Students (studentID, enrollmentDate, GPA, major) VALUES
(101, '2025-08-01', 3.85, 'Data Science and AI'),
(102, '2025-08-01', 3.60, 'Computer Science'),
(103, '2025-08-15', 3.90, 'Data Science and AI'),
(106, '2025-09-01', 3.45, 'Electronics'),
(107, '2025-09-01', 3.70, 'Data Science and AI');

-- 3. Insert Teachers
INSERT INTO Teachers (teacherID, department, salary, specialization) VALUES
(104, 'Computer Science', 85000.00, 'Machine Learning'),
(105, 'Mathematics', 82000.00, 'Statistical Inference');

-- 4. Insert Classrooms
INSERT INTO Classrooms (roomID, floor, capacity) VALUES
(1, 1, 40),
(2, 1, 35),
(3, 2, 60),
(4, 3, 25);

-- 5. Insert SmartBoards (1-to-1 with Classrooms)
INSERT INTO SmartBoards (serialNo, brand, installationDate, roomID) VALUES
('SB-9901', 'Samsung', '2024-01-10', 1),
('SB-9902', 'Samsung', '2024-01-10', 2),
('SB-8840', 'ViewSonic', '2024-05-22', 3);

-- 6. Insert Courses
INSERT INTO Courses (courseID, title, creditValue) VALUES
(501, 'Introduction to AI', 4),
(502, 'Database Systems', 3),
(503, 'Advanced Calculus', 4);

-- 7. Insert Modules for Courses
INSERT INTO Module (moduleID, courseID, title, content) VALUES
(1, 501, 'Neural Networks', 'Introduction to Perceptrons and Multi-layer Networks'),
(2, 501, 'Search Algorithms', 'BFS, DFS, and A* search strategies'),
(3, 502, 'SQL Basics', 'DDL and DML commands'),
(4, 502, 'Normalization', '1NF, 2NF, 3NF and BCNF');

-- 8. Insert TimeSlots
INSERT INTO TimeSlots (slotID, startTime, endTime) VALUES
(1, '09:00:00', '10:30:00'),
(2, '11:00:00', '12:30:00'),
(3, '14:00:00', '15:30:00');

-- 9. Insert Enrollments
INSERT INTO Enrollments (studentID, courseID, grade, enrollmentStatus) VALUES
(101, 501, 'A', 'Completed'),
(101, 502, NULL, 'Enrolled'),
(103, 501, 'A-', 'Completed'),
(102, 502, 'B+', 'Completed'),
(107, 501, NULL, 'Enrolled');

-- 10. Insert ClassSessions
INSERT INTO ClassSessions (sessionID, topic, duration, roomID, courseID, slotID, teacherID) VALUES
(2001, 'Deep Learning Intro', 90, 1, 501, 1, 104),
(2002, 'Relational Algebra', 90, 2, 502, 2, 104),
(2003, 'Limits and Continuity', 90, 3, 503, 1, 105);
