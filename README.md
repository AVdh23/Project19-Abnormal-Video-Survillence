# Project 19 - Vehicle Crash Detection

This project aims to develop a system for detecting vehicle crashes in video surveillance footage, with the goal of enhancing road safety. The project utilizes machine learning techniques to identify abnormal activities indicative of a crash and provides accurate predictions.


## Project Updates

### Day 1

Today's Progress:
1. Developed an encoder-decoder model specifically designed for detecting abnormal activities in video surveillance footage.
2. Collected a total of 38 videos for the training dataset to ensure a diverse and comprehensive training experience.
3. Carefully selected and curated 28 videos for the testing dataset to evaluate the model's performance on unseen data.
4. Divided the collected dataset into separate training and testing sets for effective model evaluation.
5. Created NPZ files to efficiently store and manage the training and testing data.

Next Steps:
1. Proceed with training the model using the carefully prepared training dataset.
2. Evaluate the model's performance on the dedicated testing dataset, measuring its accuracy in detecting abnormal activities.
3. Continuously refine and optimize the model based on insights gained from the evaluation process.
4. Stay dedicated and committed to achieving accurate and reliable abnormal activity detection in video surveillance.

### Day 2

Today's Progress:
1. Started the day with a busy schedule, participating in a machine learning hackathon.
2. Despite the limited time available, managed to make some progress on the project.
3. Developed a code snippet to convert a video into individual frames for further processing.
4. Made updates to the GitHub repository, ensuring smooth collaboration and version control.
5. Explored alternative models due to compatibility issues with the current model.
6. Faced challenges and spent considerable time troubleshooting, but remained persistent.

Next Steps:
1. Continue investigating and resolving the compatibility issues with the existing model.
2. Consider exploring a new approach involving action motion detection for improved anomaly detection.
3. Stay focused and determined to overcome obstacles and make progress in the project.
4. Attend to the ongoing machine learning hackathon and make the most out of the learning experience.

### Day 3

Today's Progress:
1. Acknowledged the difficulties encountered in the previous approach and contemplated a potential change in the project topic.
2. Explored the idea of developing a system to detect vehicle crashes, aiming to enhance road safety.
3. Conducted extensive research to identify suitable datasets for training and testing the crash detection system.
4. Balanced project work with other commitments, including participating in a hackathon and managing household chores.

Next Steps:
1. Finalize the decision to shift the project's focus towards vehicle crash detection.
2. Identify relevant datasets containing diverse examples of vehicle crashes for comprehensive training.
3. Refocus project objectives and establish clear steps and milestones to guide the development process.
4. Dive deeper into studying the necessary concepts and techniques required to build an accurate crash detection system.
5. Maintain commitment to the ongoing hackathon, leveraging the opportunity for learning and growth.

### Day 4

Today's Progress:
1. Started the day with a pleasant breakfast invitation from my parents' house, embracing family time and planning for a future trip.
2. Made significant progress in the project, achieving promising results.
3. Discovered a suitable dataset for vehicle crash detection: [HWID12 Highway Incidents Detection Dataset](https://lnkd.in/dz7N3gpG).
4. Developed a camera.py file responsible for accurately predicting vehicle crashes based on trained models.
5. Invested approximately 3 hours in refining the prediction process, ensuring accurate and reliable results.
6. Trained the model on individual frames from the dataset and successfully applied the prediction to videos.
7. Implemented necessary adjustments and optimizations for improved performance.

Next Steps:
1. Finalize and document the project's outcomes, methodologies, and insights.
2. Celebrate the completion of this exciting project and reflect on the lessons learned.
3. Channel the enthusiasm and momentum gained into upcoming projects and continue exploring new ideas.
4. Maintain a growth mindset, embracing challenges, and seeking further opportunities to enhance skills and knowledge.

### Day 5

Today's Progress:
1. Added boundary boxes to the main project, ensuring clear visualization of detected vehicle crashes.
2. Uploaded all the relevant project files to GitHub, organizing them for easy access and collaboration.
3. Created a comprehensive readme.md page, detailing the project's purpose, methodology, and usage instructions.
4. Spent time editing the readme.md files for Project 1 and Project 2, ensuring clarity and completeness.
5. Dedicated a significant portion of the day to preparations and arrangements for an upcoming road trip.

Total Time Invested:
Day 1: 3 hours
Day 2: 5 hours
Day 3: 4 hours
Day 4: 4 hours
Day 5: 2 hours

Thank you for joining me on this journey. Stay motivated and keep pursuing your passions!


## Demo Video 
-------------------------

![Demo](https://github.com/ChildEater69/Project19-Abnormal-Video-Survillence/assets/115105709/e173d2be-2268-45e9-be6d-055672c5e9bd)







## Usage

To use this project, follow these steps:
1. Clone the repository: `git clone https://github.com/your-username/project-19.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Download the HWID12 Highway Incidents Detection Dataset from [here](https://lnkd.in/dz7N3gpG) and extract it to the project's root directory.
4. Train the model by running `python train.py`.
5. Once the model is trained, you can use it for prediction by running `python camera.py`.

## Contributing

Contributions to this project are welcome! If you have any ideas or suggestions for improvement, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
