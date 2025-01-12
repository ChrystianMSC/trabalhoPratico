import './App.css'
import * as THREE from 'three'
import { useEffect, useRef } from 'react';
import { OrbitControls } from 'three/examples/jsm/Addons.js';
import { useDispatch, useSelector } from 'react-redux';
import { setTorusColor } from './redux/appSlice';
import axios from 'axios';
import { useState } from 'react';
import TopBar from './TopBar';


function App() {
  const canvasRef = useRef<HTMLCanvasElement | null>(null);
  const torusRef: any = useRef(null);
  const dispatch = useDispatch();
  const torusColor = useSelector((state : any) => state.app.torusColor);

  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/colors/')
        .then(response => setData(response.data))
        .catch(error => console.error('Error fetching data:', error));
  }, []);
  
  useEffect(() => {
    if (typeof window !== 'undefined') {
      const scene = new THREE.Scene();
      const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
      const canvas = canvasRef.current;
      if (!canvas) {
        console.error("Canvas element is not available.");
        return;
      }
      const renderer = new THREE.WebGLRenderer({
        canvas,
      });
  
      renderer.setPixelRatio(window.devicePixelRatio);
      renderer.setSize(window.innerWidth, window.innerHeight);
      camera.position.setZ(30);
  
      const geometry = new THREE.TorusGeometry(10, 3, 16, 100);
      const material = new THREE.MeshStandardMaterial({ color: torusColor });
      const torus = new THREE.Mesh(geometry, material);
      torusRef.current = torus;
      scene.add(torus);
  
      const pointLight = new THREE.PointLight(0xffffff, 10000);
      pointLight.position.set(20, 20, 20);
  
      const ambientLight = new THREE.AmbientLight(0xffffff);
      scene.add(pointLight, ambientLight);
  
      const lightHelper = new THREE.PointLightHelper(pointLight);
      const gridHelper = new THREE.GridHelper(200, 50);
      scene.add(lightHelper, gridHelper);
  
      const controls = new OrbitControls(camera, renderer.domElement)
  
      function animate() {
        requestAnimationFrame(animate);
        
        torus.rotation.x += 0.01;
        torus.rotation.y += 0.005;
        torus.rotation.z += 0.01;
  
        controls.update();
  
        renderer.render(scene, camera);
      }
  
      animate();
  
      return () => {
        renderer.dispose();
      };
    }
  }, [torusColor]);

  const changeColor = () => {
    const newColor = `#${Math.floor(Math.random() * 16777215).toString(16)}`;
    dispatch(setTorusColor(newColor));
    
    axios.post('http://127.0.0.1:8000/api/colors/', { color: newColor })
        .then(() => {
            // Refresh the list of colors after adding a new one
            axios.get('http://127.0.0.1:8000/api/colors/')
                .then(response => setData(response.data))
                .catch(error => console.error('Error fetching data:', error));
        })
        .catch(error => console.error('Error saving color:', error));
  };
  
  return (
    <>
      <TopBar />
      <canvas id="bg" ref={canvasRef}></canvas>
      <button onClick={changeColor} style={{ position: 'absolute', top: '10px', left: '10px', zIndex: '10' }}>
        Change Torus Color
      </button>
      <div style={{ position: 'absolute', top: '100px', maxHeight: '500px', overflowY: 'auto', width: '200px', backgroundColor: 'rgba(0, 0, 0, 0.7)'}}>
        <ul>
            {data.map((item: any) => (
                <li key={item.id} style={{ cursor: 'pointer', color: item.color }} 
                    onClick={() => dispatch(setTorusColor(item.color))}>
                    {item.color}
                </li>
            ))}
        </ul>
      </div>

    </>
  )
}

export default App
