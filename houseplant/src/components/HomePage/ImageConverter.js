// src/ImageConverter.js
import React, { useState, useRef } from 'react';

const classifyImage = async (file) => {
  const formData = new FormData();
  formData.append('file', file);

  // Choose the endpoint based on environment
  const ai_endpoint = process.env.REACT_APP_AI_ENDPOINT;

  try {
    const response = await fetch(ai_endpoint, {
      method: 'POST',
      body: formData,
    });

    if (response.ok) {
      const result = await response.json();
      return result;
    } else {
      const errorMessage = await response.text();
      console.error("classifyImage Error:", errorMessage);
      return "";
    }
  } catch (error) {
    console.error("classifyImage Error:", error);
    return "";
  }
};

const getPlantInformation = async (plantName) => {
  const encodedQuery = encodeURIComponent(plantName);
  const url = `${process.env.REACT_APP_MONGODB_ENDPOINT}/?query=${encodedQuery}`;
  console.log("Sending plant name to the server:", plantName);
  try {
    const response = await fetch(url);
    if (response.ok) {
      const plantInformation = await response.json();
      return plantInformation;
    } else {
      const errorMessage = await response.text();
      console.error("getPlantInformation Error:", errorMessage);
      return "";
    }
  } catch (error) {
    console.error("getPlantInformation Error:", error);
    return "";
  }
};

const PlantFinder = () => {
  const [image, setImage] = useState(null);
  const [prediction, setPrediction] = useState(null); // Fixed spelling here
  const [imageUrls, setImageUrls] = useState([]);
  const fileInputRef = useRef(null);

  const handleImageUpload = async (event) => {
    const file = event.target.files[0];
    if (file) {
      // Set image preview URL
      setImage(URL.createObjectURL(file));

      // Classify the image
      const result = await classifyImage(file);
      if (result && result.predicted_class) {
        console.log("Plant Name:", result.predicted_class);
        // Get additional plant information
        const plantInformation = await getPlantInformation(result.predicted_class);
        console.log("Plant Information:", plantInformation);
        if (plantInformation && plantInformation.image_paths) {
          setImageUrls(plantInformation.image_paths);
          setPrediction(result.predicted_class);
        }
      } else {
        console.error("No predicted_class found in result");
      }
    }
  };

  const handleButtonClick = () => {
    const choice = window.confirm("Do you want to capture an image?");
    if (choice) {
      fileInputRef.current.setAttribute('capture', 'camera');
    } else {
      fileInputRef.current.removeAttribute('capture');
    }
    fileInputRef.current.click();
  };

  return (
    <div style={{ textAlign: 'center' }}>
      <div style={{ backgroundColor: 'black' }}>
        <div style={{ padding: '10px', width: '100%' }}>
          <div style={{ color: 'white', fontSize: '1.5em', textAlign: 'left', paddingBottom: '5px' }}>
            UPLOAD PHOTOS OF YOUR HOUSE PLANT AND KNOW MORE ABOUT THEM
          </div>
        </div>
      </div>

      <h2>Upload/Capture an Image</h2>
      <div>
        <button style={{ backgroundColor: '#b53836', padding: '1.5rem' }} onClick={handleButtonClick}>
          Upload File
        </button>
        <input
          ref={fileInputRef}
          style={{ display: 'none' }}
          type="file"
          accept="image/*"
          onChange={handleImageUpload}
        />
      </div>

      {/* Display image preview */}
      {image && <img src={image} alt="Original" style={{ maxWidth: '300px', marginTop: '20px' }} />}

      {/* Display prediction */}
      {prediction && (
        <div style={{ marginTop: '20px' }}>
          <h1>The Name of the Plant is: {prediction}</h1>
        </div>
      )}

      {/* Display plant images */}
      <div
        id="image-container"
        style={{
          display: 'flex',
          flexWrap: 'wrap',
          justifyContent: 'center',
          marginTop: '20px',
        }}
      >
        {imageUrls.length > 0 &&
          imageUrls.map((url, index) => (
            <div key={index} style={{ margin: '10px' }}>
              <img src={url} alt={`Plant ${index + 1}`} style={{ width: '200px', height: 'auto' }} />
            </div>
          ))}
      </div>

      <div style={{ paddingBottom: '0px' }}>
        This Website was made by Rashidul Islam, actively looking for opportunities to show his skills. Thanks
      </div>
    </div>
  );
};

export default PlantFinder;
