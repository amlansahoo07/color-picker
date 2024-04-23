# Color Picker OpenCV

This project demonstrates how to perform color detection using the HSV color space in OpenCV. It allows users to adjust HSV thresholds using trackbars to detect specific colors in an image.

<img width="575" alt="image" align="center" src="https://github.com/amlansahoo07/color-picker/assets/35356517/19bfbe61-8c3f-44d1-8514-dd669a8f4d26">


## Requirements

- Python 3.x
- OpenCV
- NumPy
  
You can install the dependencies using pip:
```bash
pip install opencv-python numpy
```


## Features

- Convert an image to the HSV color space.
- Adjust HSV thresholds using trackbars to isolate specific colors.
- Visualize the original image, its HSV representation, the mask, and the resulting masked image.


## Usage

1. Clone the repository and navigate to the project directory.
2. Run the main script: ```python main.py```
3. Adjust the trackbars to set HSV thresholds and observe the color detection in real-time.


## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.


## Attribution

The stackImages function in `main.py` is borrowed from the cvzone library by Computer Vision Zone. Website: [Computer Vision Zone](https://www.computervision.zone/)


## Acknowledgements

This project was completed following the tutorial by [Murtaza's Workshop - Robotics and AI](https://youtu.be/WQeoO7MI0Bs?si=dom7y75a0-W2B9xu&t=3375). I would like to express my gratitude for their clear explanation and guidance throughout the project.


## License

This project is licensed under the [MIT License](LICENSE).
