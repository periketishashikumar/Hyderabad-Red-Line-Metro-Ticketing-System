This Django-based web app generates QR code tickets for metro travel. Users select departure and destination stations, receive a QR code via email, and scan it using OpenCV for station validation. If scanned at the wrong station, the system notifies the user. Built with Python, Django, OpenCV, and SQLite, it enhances metro travel convenience.

# Phase 1: User Options & Navigation
The application provides users with two primary options—Travel and Validate—accessible from the main interface. In addition, an About and Contact section is included in the navigation bar for users to learn more about the system and reach out for assistance.
![intro](https://github.com/user-attachments/assets/052fcf21-1504-40d7-8a31-e926dd3b8dfd)

# Phase 2: Travel Selection & Input Details
Before scanning the QR code, the user selects the Travel option. In this section, they choose their departure station, destination station, and enter their email address. This ensures that each journey is uniquely identified and linked to the respective user for further validation and tracking.
![travel](https://github.com/user-attachments/assets/83095c42-b736-44b5-bfa3-a6af8e2b8468)

# Phase 3: Email Generation & QR Code Generation 
Upon submitting the travel details, the system generates a QR code and sends it to the user’s email. Along with the QR code, the email includes additional travel insights, such as fuel savings (petrol saved in liters), CO₂ emissions reduction (carbon footprint savings), total ticket price, and total kilometers to be traveled. These insights enhance user awareness about the environmental and financial benefits of metro travel.
![mail](https://github.com/user-attachments/assets/2d9368a2-8891-4c2c-adb9-13b5b798be12)

# Phase 4: Journey Validation (QR Code Scanning)
After receiving the QR code, the user navigates to the Validate section to scan their QR code. This validation ensures that the user is at the correct station during both entry and exit, preventing unauthorized access or incorrect travel.
![validate](https://github.com/user-attachments/assets/47059460-9787-458a-bc8f-92eb77eea08e)

# Phase 5: Entry & Exit Scanning
The validation phase consists of two scanning options—Entry Scan and Exit Scan. When entering the metro, the user selects Entry Scan to verify and log their journey start. Similarly, upon reaching their destination, they choose Exit Scan to confirm their travel completion. If scanned at the wrong station, the system notifies them and provides the correct station details.
![scaning](https://github.com/user-attachments/assets/e5726b57-fedf-4b88-8d06-e9fb7819beb5)

