# Make Images always facing towards the camera
- [Three.js-Object3D-Sprite](https://github.com/VisSieve/main/tree/Zhiyang-Doc/Visualization/Use%20of%203.js%20in%20Observable%20Framework)

```js
const map = new THREE.TextureLoader().load( 'sprite.png' );
const material = new THREE.SpriteMaterial( { map: map } );

const sprite = new THREE.Sprite( material );
scene.add( sprite );
```

## full-working example with 100 images

```js

import * as THREE from 'npm:three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

// import three.js

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 2000);
const renderer = new THREE.WebGLRenderer();
renderer.setSize(0.97 * document.getElementById("3d").offsetWidth, 0.97 * document.getElementById("3d").offsetWidth / 16 * 9);
document.getElementById("3d").appendChild(renderer.domElement);
if(renderer.domElement){
  document.getElementById("loading").style.display = "none";
}

const light = new THREE.AmbientLight(0x404040); // soft white light
scene.add(light);


fetch('https://zhiyangwang.site/viz-data/image_tsne_projections.json')
    .then(response => response.json())
    .then(data => {
        data.forEach(item => {
            const textureLoader = new THREE.TextureLoader();
            const imageUrl = `https://zhiyangwang.site/viz-data/100-imgs/MES101${item.idx.toString().padStart(2, '0')}.jpg`;
            textureLoader.load(imageUrl, texture => {
                const material = new THREE.MeshBasicMaterial({ map: texture });
                const planeGeometry = new THREE.PlaneGeometry(1, 1); 
                const plane = new THREE.Mesh(planeGeometry, material);

                // Set position based on JSON data
                plane.position.x = item.x;
                plane.position.y = item.y;
                plane.position.z = 0; 
                

                scene.add(plane);
            });
        });
    });

// Adjust camera
camera.position.z = 5;

function animate() {
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
}

animate();


```