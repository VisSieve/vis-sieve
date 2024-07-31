# Dynamiclly load the images
## js code
```js
import * as THREE from 'npm:three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

let imagePositions = [];
fetch('https://zhiyangwang.site/giant-viz-data/image_tsne_projections.json')
  .then(response => response.json())
  .then(data => {
    imagePositions = data;
    init();
  });

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();
renderer.setSize(0.97 * document.getElementById("3d").offsetWidth, 0.97 * document.getElementById("3d").offsetWidth / 16 * 9);
document.getElementById("3d").appendChild(renderer.domElement);

const controls = new OrbitControls(camera, renderer.domElement);
let sprites = []; // This array will hold our sprites
const loadDistance = 10; // Distance within which to load textures

const size = 150;
const divisions = 50;

const gridHelper = new THREE.GridHelper( size, divisions );
scene.add( gridHelper );

const axesHelper = new THREE.AxesHelper( 100 );
scene.add( axesHelper );

function init() {
  imagePositions.forEach(item => {
    const spriteMaterial = new THREE.SpriteMaterial({ color: 0xffffff });
    const sprite = new THREE.Sprite(spriteMaterial);
    sprite.position.set(item.x*2, Math.random(), item.y*2);
    sprite.userData = { idx: item.idx, loaded: false };
    scene.add(sprite);
    sprites.push(sprite);
  });

  camera.position.set(50, 50, 150); // Set initial camera position

  animate();
}

function animate() {
  requestAnimationFrame(animate);
  updateTextures();
  renderer.render(scene, camera);
}

function updateTextures() {
  sprites.forEach(sprite => {
    const distance = camera.position.distanceTo(sprite.position);
    if (distance < loadDistance && !sprite.userData.loaded) {
      const loader = new THREE.TextureLoader();
      loader.load(`https://zhiyangwang.site/giant-viz-data/15000-imgs/animals-${sprite.userData.idx+1}.jpg`, texture => {
        sprite.material.map = texture;
        sprite.material.needsUpdate = true;
        sprite.userData.loaded = true;
      });
    } else if (distance >= loadDistance && sprite.userData.loaded) {
      sprite.material.map = null;
      sprite.material.needsUpdate = true;
      sprite.userData.loaded = false;
    }
  });
}

controls.update();


```

## html code

```html


<div class = "card" id="3d">

</div>

``` 