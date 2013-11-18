=============== Contenidos ===============

├── gtk2 ----------------------> Código para gtk2
│   ├── lazy-video-player.py
│   ├── VideoCapture.py
│   ├── VideoController.py
│   └── VideoUI.py
└── gtk3 ----------------------> Código para gtk3
    ├── lazy-video-player.py
    ├── VideoCapture.py
    ├── VideoController.py
    └── VideoUI.py


=============== Dependencias ===============

Webcam conectada a ordenador!

=== Sistemas Linux ===

Se recomienda la instalación por paquetes mediante apt/synaptic/...

Lista de paquetes a instalar para algunas distros ubuntu:

**** UBUNTU 12.04 TLS
python-opencv (2.3.1-7) [universe] Python bindings for the computer vision library
python-numpy (1:1.6.1-6ubuntu1) Numerical Python adds a fast array facility to the Python language
libopencv-calib3d-dev (2.3.1-7) [universe] development files for libopencv-calib3d
libopencv-calib3d2.3 (2.3.1-7) [universe] computer vision Camera Calibration library
libopencv-contrib-dev (2.3.1-7) [universe] development files for libopencv-contrib
libopencv-contrib2.3 (2.3.1-7) [universe] computer vision contrib library
libopencv-core-dev (2.3.1-7) [universe] development files for libopencv-core
libopencv-core2.3 (2.3.1-7) [universe] computer vision core library
libopencv-dev (2.3.1-7) [universe] development files for opencv
libopencv-features2d-dev (2.3.1-7) [universe] development files for libopencv-features2d
libopencv-features2d2.3 (2.3.1-7) [universe] computer vision Feature Detection and Descriptor Extraction library
libopencv-flann-dev (2.3.1-7) [universe] development files for libopencv-flann
libopencv-flann2.3 (2.3.1-7) [universe] computer vision Clustering and Search in Multi-Dimensional spaces library
libopencv-gpu-dev (2.3.1-7) [universe] development files for libopencv-gpu
libopencv-gpu2.3 (2.3.1-7) [universe] computer vision GPU Processing library
libopencv-highgui-dev (2.3.1-7) [universe] development files for libopencv-highgui
libopencv-highgui2.3 (2.3.1-7) [universe] computer vision High-level GUI and Media I/O library
libopencv-imgproc-dev (2.3.1-7) [universe] development files for libopencv-imgproc
libopencv-imgproc2.3 (2.3.1-7) [universe] computer vision Image Processing library
libopencv-legacy-dev (2.3.1-7) [universe] development files for libopencv-legacy
libopencv-legacy2.3 (2.3.1-7) [universe] computer vision legacy library
libopencv-ml-dev (2.3.1-7) [universe] development files for libopencv-ml
libopencv-ml2.3 (2.3.1-7) [universe] computer vision Machine Learning library
libopencv-objdetect-dev (2.3.1-7) [universe] development files for libopencv-objdetect
libopencv-objdetect2.3 (2.3.1-7) [universe] computer vision Object Detection library
libopencv-video-dev (2.3.1-7) [universe] development files for libopencv-video
libopencv-video2.3 (2.3.1-7) [universe] computer vision Video analysis library

**** UBUNTU 13.04
python-numpy (1:1.7.1-1ubuntu1) Numerical Python adds a fast array facility to the Python language
python-opencv (2.4.2+dfsg-0exp2ubuntu1) [universe] Python bindings for the computer vision library
libopencv-calib3d-dev (2.4.2+dfsg-0exp2ubuntu1) [universe] development files for libopencv-calib3d
libopencv-calib3d2.4 (2.4.2+dfsg-0exp2ubuntu1) [universe] computer vision Camera Calibration library
libopencv-contrib-dev (2.4.2+dfsg-0exp2ubuntu1) [universe] development files for libopencv-contrib
libopencv-contrib2.4 (2.4.2+dfsg-0exp2ubuntu1) [universe] computer vision contrib library
libopencv-core-dev (2.4.2+dfsg-0exp2ubuntu1) [universe] development files for libopencv-core
libopencv-core2.4 (2.4.2+dfsg-0exp2ubuntu1) [universe] computer vision core library
libopencv-dev (2.4.2+dfsg-0exp2ubuntu1) [universe] development files for opencv
libopencv-features2d-dev (2.4.2+dfsg-0exp2ubuntu1) [universe] development files for libopencv-features2d
libopencv-features2d2.4 (2.4.2+dfsg-0exp2ubuntu1) [universe] computer vision Feature Detection and Descriptor Extraction library
libopencv-flann-dev (2.4.2+dfsg-0exp2ubuntu1) [universe] development files for libopencv-flann
libopencv-flann2.4 (2.4.2+dfsg-0exp2ubuntu1) [universe] computer vision Clustering and Search in Multi-Dimensional spaces library
libopencv-highgui-dev (2.4.2+dfsg-0exp2ubuntu1) [universe] development files for libopencv-highgui
libopencv-highgui2.4 (2.4.2+dfsg-0exp2ubuntu1) [universe] computer vision High-level GUI and Media I/O library
libopencv-imgproc-dev (2.4.2+dfsg-0exp2ubuntu1) [universe] development files for libopencv-imgproc
libopencv-imgproc2.4 (2.4.2+dfsg-0exp2ubuntu1) [universe] computer vision Image Processing library
libopencv-legacy-dev (2.4.2+dfsg-0exp2ubuntu1) [universe] development files for libopencv-legacy
libopencv-legacy2.4 (2.4.2+dfsg-0exp2ubuntu1) [universe] computer vision legacy library
libopencv-ml-dev (2.4.2+dfsg-0exp2ubuntu1) [universe] development files for libopencv-ml
libopencv-ml2.4 (2.4.2+dfsg-0exp2ubuntu1) [universe] computer vision Machine Learning library
libopencv-objdetect-dev (2.4.2+dfsg-0exp2ubuntu1) [universe] development files for libopencv-objdetect
libopencv-objdetect2.4 (2.4.2+dfsg-0exp2ubuntu1) [universe] computer vision Object Detection library
libopencv-photo-dev (2.4.2+dfsg-0exp2ubuntu1) [universe] development files for libopencv-photo2.4
libopencv-photo2.4 (2.4.2+dfsg-0exp2ubuntu1) [universe] computer vision computational photography library
libopencv-stitching-dev (2.4.2+dfsg-0exp2ubuntu1) [universe] development files for libopencv-stitching2.4
libopencv-stitching2.4 (2.4.2+dfsg-0exp2ubuntu1) [universe] computer vision image stitching library
libopencv-ts-dev (2.4.2+dfsg-0exp2ubuntu1) [universe] development files for libopencv-ts2.4
libopencv-ts2.4 (2.4.2+dfsg-0exp2ubuntu1) [universe] computer vision ts library
libopencv-video-dev (2.4.2+dfsg-0exp2ubuntu1) [universe] development files for libopencv-video
libopencv-video2.4 (2.4.2+dfsg-0exp2ubuntu1) [universe] computer vision Video analysis library
libopencv-videostab-dev (2.4.2+dfsg-0exp2ubuntu1) [universe] development files for libopencv-videostab2.4
libopencv-videostab2.4 (2.4.2+dfsg-0exp2ubuntu1) [universe] computer vision video stabilization library


=== Mac ===

http://geekytheory.com/opencv-en-mac-osx/

=== Windows ===

http://opencvpython.blogspot.com.es/2012/05/install-opencv-in-windows-for-python.html


=============== Ejecución ===============

$ ./lazy-video-player.py


