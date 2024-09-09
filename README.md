# Facial CheckIn

Facial CheckIn automates attendance tracking using facial recognition technology. The project leverages OpenCV for face recognition, Azure Blob services for image storage, Azure SQL for attendance data management, and Azure Communication Services to email attendance reports. This system provides a secure, efficient, and contactless method for recording and managing attendance.

## Project Title: **Facial CheckIn**

### Project Details

- **Project Demo URL:** [Link to Project Demo](https://facial-attendance.azurewebsites.net/)
- **Demo Video URL:** [Link to the Demo Video](https://drive.google.com/file/d/1MJERXzDJjAEjfj6DORplq28HgrzV4VA3/view?usp=sharing)
- **GitHub Repository URL:** [GitHub Repository Link](https://github.com/Palash-Doshi-Git/Facial-CheckIn.git)
- **Industry:** Technology

### Azure Services Used

#### Core Azure Services
1. **Azure App Service:**  
   Hosted the front-end (HTML, CSS, JS) for user interaction and back-end (Flask) for processing facial recognition and handling attendance records.

2. **Azure SQL Database:**  
   Used for storing user details and attendance records, ensuring efficient data management and retrieval.

3. **Azure Blob Storage:**  
   Manages images captured during face recognition, providing secure and scalable storage.

4. **Azure Communication Services:**  
   Facilitates emailing of the attendance sheet after the attendance process is completed. This service ensures that attendance records are sent to relevant recipients efficiently.

#### OpenCV (Open Source Computer Vision Library)
   Used for detecting and recognizing faces in real-time. It captures and processes video frames to identify faces and match them against stored data.

### Problem Statement

Traditional methods for tracking attendance are often manual, time-consuming, and prone to errors. Facial CheckIn addresses these issues by providing an automated, contactless solution that uses facial recognition technology to accurately record and manage attendance.

### Project Description

Facial CheckIn allows users to mark their attendance by recognizing their face through a camera using OpenCV. The system captures images, processes them for facial recognition, and updates attendance records stored in Azure SQL Database. Images are managed in Azure Blob Storage, and attendance sheets are emailed to designated recipients using Azure Communication Services.

#### Key Features
- Real-time Face Recognition with OpenCV
- Image Storage in Azure Blob Storage
- Attendance Data Management with Azure SQL Database
- Automated Email Reports via Azure Communication Services
- User-friendly Web Interface
- Secure and Contactless Attendance

#### Future Enhancements
- Enhance facial recognition accuracy with advanced machine learning algorithms.
- Integrate mobile apps for broader access to the attendance system.
- Allow export of attendance data in various formats (CSV, Excel).
- Implement features for collaborative attendance tracking in large organizations.
- Introduce predictive analytics to identify trends in attendance data.
- Enable users to upload photos of receipts for verification in certain scenarios.

### Core Azure Services

#### Azure App Service
Provides scalable and reliable hosting for the web application, ensuring smooth deployment and integration with other Azure services.

#### Azure SQL Database
Manages and stores user and attendance data, ensuring fast access and data consistency.

#### Azure Blob Storage
Stores captured images securely, allowing for scalable and organized image management.

#### Azure Communication Services
Sends automated emails containing attendance sheets to relevant recipients, streamlining communication and reporting.

### OpenCV

#### OpenCV for Face Recognition
OpenCV handles real-time face detection and recognition, processing video frames to identify and verify users for attendance purposes.

### Screenshots

#### Azure App Service
**Description:** Hosting environment for the web application.  
![App Service Delpoment](https://github.com/user-attachments/assets/319be415-9612-46d3-be5f-ca550bf0cddc)

#### Azure SQL Database
**Description:** Data storage and management for attendance records.  
![Azure Mysql Server](https://github.com/user-attachments/assets/1272df12-327c-432c-aba9-6e520d955595)

#### Azure Blob Storage
**Description:** Image storage for facial recognition data.  
![Blob storage](https://github.com/user-attachments/assets/34745291-b451-4f0c-8c75-6f2d7e2fd6c1)

#### Azure Communication Services
**Description:** Emailing attendance reports to recipients.  
![Email Comm Service](https://github.com/user-attachments/assets/b98e6c41-98a5-43f1-a3d1-68f6c4e0dd3d)

#### Facial Check-IN UI
**Description:** Real-time face detection and recognition system.  
![Facial CheckIn UI](https://github.com/user-attachments/assets/08c35486-c6d0-4a27-a88e-67d7c4aa94e1)


### Final Project Statement
Facial CheckIn is a comprehensive and modern solution for attendance management. By leveraging Azure Blob Storage, Azure SQL, OpenCV, and Azure Communication Services, the system offers an efficient, secure, and automated way to record and manage attendance, making it ideal for organizations seeking to streamline their processes.

