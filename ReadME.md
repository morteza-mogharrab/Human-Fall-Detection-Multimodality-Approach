# Human Fall Detection Using Multimodal Approach

## Overview
This research project aims to comprehensively reimplement and analyze existing work on human fall detection systems that leverage multimodal data sources, such as vision (RGB or depth cameras), wearable sensors, and ambient sensors. By conducting a thorough review and synthesis of prior studies, we seek to identify best practices, methodological strengths and limitations, and potential areas for improvement. To enhance the credibility of our work, we considered using various models (CNN, LSTM, Transformer, etc.) and datasets (UP-Fall, Notch, Smart-Fall, etc.). We also utilized and tested available closed-source APIs, such as Caude.AI APIs, for potential situations where we might want to quickly and easily set up this project.

## Goals
This research comprehensively examines multimodal human fall detection systems through a three-pronged approach:

1. **Synthesize Existing Knowledge**: A critical review and comparison of prior studies will be conducted to identify common themes, highlight contradictions, and pinpoint any gaps in existing research.
2. **Determine Best Practices**: Dissecting the methodologies, findings, and conclusions of the reviewed studies to determine the most effective, reliable, and insightful approaches, techniques, and practices for multimodal fall detection systems.
3. **Identify Methodological Improvements**: A methodological critique will be performed, meticulously evaluating data collection processes, preprocessing methods, model architectures, and evaluation metrics used in prior research. This analysis aims to pinpoint areas where methodological improvements can be made, ultimately enhancing the rigor, reliability, and validity of future research in this domain.

## Scope
While the development and implementation of new models are not the primary focus of our project, the findings and recommendations derived from this analysis may inform and guide future research efforts in this field. Our report will serve as a valuable resource for researchers and practitioners working on developing or improving multimodal human fall detection systems, providing a solid foundation of knowledge and best practices.

## Project Structure
This repository contains multiple sub-projects, each focusing on a specific aspect or approach to human fall detection using multimodal data. Each sub-project has its own directory with its respective code, data, and documentation. The sub-projects are as follows:

1. **Fall-Detection using Claude-ai**
2. **CNN-based Fall Detection on UP-FALL dataset**
3. **Fall_Detection_using_multihorizon_forecasting**
4. **Federated-Learning-based-Fall-Detection-with-Multimodal-Data-Fusion**
5. **Multi-camera-multi-person-and-real-time-fall-detection-using-LSTM**
6. **PoseEstimation-based-Fall-Detection**
7. **Vision Transformer and CNN-based Fall Detection**

## Getting Started
Each sub-project has its own README file with detailed instructions on how to set up the environment, install dependencies, and run the code. Please refer to the respective sub-project directory for more information.

## Contributing
-Parts of the project implementation have been carried out by the researchers mentioned in the papers below, while other parts have been contributed by our team as follows:

Morteza Mogharrab - mogharra@ualberta.ca
Ritika Ritika - ritika7@ualberta.ca
Sai Sarath Movva - saisarat@ualberta.ca

## References
-We primarily consulted the following publications for the project's implementation:

[1]Kim, I., Kim, D., Kwon, S., Lee, S., & Lee, J. (2022). Fall Detection using Biometric Information Based on Multi-Horizon Forecasting. In Proceedings of the 2022 26th International Conference on Pattern Recognition (ICPR). IEEE. DOI: 10.1109/ICPR56361.2022.9956568
[2] Qi, P., Chiaro, D., & Piccialli, F. (2023). FL-FD: Federated learning- based fall detection with multimodal data fusion. Journal of Sensors and Actuators A: Physical. Advance online publication.
[3] Taufeequea, M., Koitaa, S., Spicherb, N., & Deserno, T. M. (2021).
Multi-camera, multi-person, and real-time fall detection using long short term memory. In T. M. Deserno & B. J. Park (Eds.), Medical Imaging 2021: Imaging Informatics for Healthcare, Research, and Applications (Vol. 11601, p. 1160109). SPIE. DOI: 10.1117/12.2580700
[4] Balram, A., Puthanveettil, T., Singh, A., & Hundekari, K. (Year). Striking the Balance: Human Pose Estimation based Optimal Fall Recognition.
[5] Ha, T. V., Nguyen, H., Huynh, S. T., Nguyen, T. T., & Nguyen, B. T. (Year). Fall detection using multimodal data. arXiv, arXiv:2205.05918 [cs.CV]. Retrieved from https://doi.org/10.48550/arXiv.2205.05918
[6] Chi, T.-H., Liu, K.-C., Hsieh, C.-Y., Tsao, Y., & Chan, C.-T. (Year). PreFallKD: Pre-Impact Fall Detection via CNN-ViT Knowl- edge Distillation. arXiv, arXiv:2303.03634 [eess.SP]. Retrieved from https://doi.org/10.48550/arXiv.2303.03634

## License
This project is licensed under the [MIT License](LICENSE).