



//<!--    const sendFrame = (dataURL) => {-->
//<!--        fetch("/upload_frame", {-->
//<!--            method: "POST",-->
//<!--            body: JSON.stringify({ image: dataURL }),-->
//<!--            headers: {-->
//<!--                "Content-Type": "application/json",-->
//<!--            },-->
//<!--        })-->
//<!--        .then((response) => response.json())-->
//<!--        .then((data) => {-->
//<!--            console.log("Frame uploaded successfully:", data);-->
//<!--        })-->
//<!--        .catch((error) => {-->
//<!--            console.error("Error uploading frame:", error);-->
//<!--        });-->
//<!--    };-->
//<!--    toggleButton.addEventListener("click", () => {-->
<!--        if (isCapture) {-->
<!--            stopVideoStream(); // Stop the video stream if it's active-->
<!--            isCapture=false-->
<!--        } else {-->
<!--            startVideoStream(); // Start the video stream if it's not active-->
<!--            isCapture=true-->
//<!--        }-->
//    });
//
//<!--    const captureFrames = () => {-->
//<!--        if (!isCapture) return;-->
//
//<!--        canvas.width = video.videoWidth;-->
//<!--        canvas.height = video.videoHeight;-->
//<!--        context.drawImage(video, 0, 0, canvas.width, canvas.height);-->
//
//<!--        const dataURL = canvas.toDataURL("image/png");-->
//<!--        console.log("_____________", dataURL)-->
//<!--                sendFrame(dataURL);-->
//<!--
//<!--        // Capture frames continuously-->
//<!--        captureFramesInterval = setInterval(() => {-->
//<!--            if (isCapture) {-->
//<!--                canvas.width = video.videoWidth;-->
//<!--                canvas.height = video.videoHeight;-->
//<!--                context.drawImage(video, 0, 0, canvas.width, canvas.height);-->
//
//<!--                const dataURL = canvas.toDataURL("image/png");-->
//<!--                sendFrame(dataURL);-->
//<!--            } else {-->
//<!--                clearInterval(captureFramesInterval); // Stop capturing if isCapture is false-->
//<!--            }-->
//<!--        }, 1000); // Adjust the interval time (in milliseconds) as needed-->
//<!--
//<!--    };-->