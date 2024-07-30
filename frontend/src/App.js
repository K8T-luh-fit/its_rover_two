import React, { useState, useEffect, useRef } from "react";
import io from 'socket.io-client';
import logo from './logo.png';
import cameraRep from './camerarep.gif'
import sensorPic from './sensorNerd.png'
import image1 from './image1.jpg'
import image2 from './image2.jpg'
import image3 from './image3.jpg'
import image4 from './image4.jpg'
import image5 from './image5.png'
import image6 from './image6.jpg'
import image7 from './image7.jpg'
import image8 from './image8.jpg'
import image9 from './groupPic.jpg'

const socket = io('http://localhost:8000');

function App() {
  const keyDownCurrent = useRef(false);
  const [temp, setTemp] = useState(null);
  const [ultrasonic, setUltrasonic] = useState(null);
  const [humidity, setHumidity] = useState(null);


  useEffect(() => {
    // Listen for temperature updates
    socket.on('temp', (data) => {
      setTemp(data);
    });

    // Listen for ultrasonic updates
    socket.on('ultrasonic', (data) => {
       setUltrasonic(data);
     });

    // Listen for humidity updates
    socket.on('humidity', (data) => {
      setHumidity(data);
    });

    
    // Clean up the socket listeners on component unmount
    return () => {
      socket.off('temp');
      socket.off('ultrasonic');
      socket.off('humidity');
    };
  }, []);


  const sendDirection = (direction) => {
    socket.emit('send-direction', direction);
  };

  const stopFunction = (stop) => {
    socket.emit('stop', stop);
  }

  useEffect(() => {
    const handleKeyDown = (event) => {
      if (!keyDownCurrent.current) {
        sendDirection(event.key);
        keyDownCurrent.current = true;
      }
        
    }
  
    const handleKeyUp = (event) => {
      if (keyDownCurrent.current) {
        stopFunction("stop");
        keyDownCurrent.current = false;
      }
    }
    // Add keydown and keyup event listeners
    window.addEventListener('keydown', handleKeyDown);
    window.addEventListener('keyup', handleKeyUp);

    // Clean up event listeners on component unmount
    return () => {
      window.removeEventListener('keydown', handleKeyDown);
      window.removeEventListener('keyup', handleKeyUp);
    };
  }, []);

  // const sendArmValue = (value) => {
  //   socket.emit('send-arm-value', value);
  // };

  return (
    <>
      <div className="Header">
        <img src={logo} alt="" id="logo1"/>
      </div>

      <div className="cameraContent">
        <img src={cameraRep} alt="" id="camPic"/>
        <div className="camTitle">
          <h1>camera</h1>
        </div>
        <div className="cameraFrame">
          <iframe src="http://192.168.50.237/" ></iframe>
        </div>

        <h1>rover controls</h1>
        <p> <strong>w</strong>: forward, <strong>a</strong>: left, <strong>s</strong>: backward, <strong>d</strong>: right,
        <strong> up arrow</strong>: claw up, <strong>down arrow</strong>: claw down, <strong>1</strong>: open claw, <strong>2</strong>: close claw</p>
      </div>

      <div className="sensorData">
        <div ClassName="sensorTitle">
          <h1>Sensor Data</h1>
        </div>
        <div className="contentContainer">
        <div className="sensorTags">
          <p>Temperature: {temp !== null ? temp : 'Loading...'}</p>
         <p>Ultrasonic: {ultrasonic !== null ? ultrasonic : 'Loading...'}</p>
          <p>Humidity: {humidity !== null ? humidity : 'Loading...'}</p>
        </div>
        <div className="nerdPic">
          <img src={sensorPic} alt="" id="nerd"/>
        </div>
        </div>
      </div>

      <div className="log">
        <div className="docTitle">
          <h1>Design Process Documentation</h1>
        </div>
        <div className="docContent">
          <p>Rover the Moon includes four members, Adrian (bioengineering), Shervin (computer science), Brian (electrical engineering), and Kaitlyn (electrical engineering). Given their dedicated fields (majors) being applied to mission, team members had to venture out of there scope to complete the following task: Have movement of claw and chassis itself, Have sensors display temperature, humidity, distance, A camera streaming field of view, Handle different terrain, Fit within size constraint. Successes within the team included having great chemistry. All members contributed greatly to the design processes, researching ways for how the rover should be designed, specifically the suspension design for the wheels. What came with the mechanical aspect were creating measurements for the necessary components, but also creating brackets for support. This included under the motor placements and for attaching the motor. There are also measured compartments for the sensors and camera mount, made through laser printing. The necessary acrylic was used for the wheel attachments and the base. Struggles that were seen within the field were not having all compartments for certain sensors and power supply for the camera. 
          There were also failures in printing the claw parts. For electrical engineering, power was supplied through a lithium battery, that was connected to one driver controller, where its port of 5v and 12.5v was connected to designated power rails, with a common ground rail. All motors, servos, and sensors were able to receive power, but failed to receive enough to support the rover. During testing of individual parts, the motors worked, but failed to move when assembled to the car. For the coding process, it was a new language for the team, so it was a tedious learning process having to figure out the syntax for all parts of the rover through Thonny software, as well as the MQTT broker communication. The communication was successful as terminals for both backend and frontend sides were showing messages successful communication. Overall, the project demonstrated the team's ability to collaboratively overcome challenges and innovate across disciplines, showcasing their determination and adaptability in bringing Rover the Moon to life despite encountering various technical hurdles.</p>
          <img src={image9} alt="Photo 9" id="pic9"/>
        </div>
      </div>

      <div className="photoGallery">
      <div className="photoTitle">
        <h1>Photo Gallery</h1>
      </div>
      <div className="photos">
        <img src={image1} alt="Photo 1" id="pic1"/>
        <img src={image2} alt="Photo 2" id="pic2"/>
        <img src={image3} alt="Photo 3" id="pic3"/>
        <img src={image4} alt="Photo 4" id="pic4"/>
        <img src={image5} alt="Photo 5" id="pic5"/>
        <img src={image6} alt="Photo 6" id="pic6"/>
        <img src={image7} alt="Photo 7" id="pic7"/>
        <img src={image8} alt="Photo 8" id="pic8"/>
      </div>
    </div>
    </>
  );
}

export default App;
