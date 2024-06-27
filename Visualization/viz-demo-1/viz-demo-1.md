---
title: base versino
toc: false
---
<style>
boad
#threeD{
    display: flex;
    justify-content: center; /* Center items horizontally */
    align-items: center; /* Center items vertically */
    display: none;
}
.sprite-label{
  background-color: rgba(255, 255, 255, 0.9);
  transition: opacity 0.5s ease-in-out;
  opacity: 0; // Start with hidden labels
  padding-bottom: 10px;
  border-radius: 10px 10px 10px 10px; /* Rounded corners on the top */
  display: flex;
  margin: auto;
  align-items: center; /* Vertically center the content */
  justify-content: center; /* Horizontally align content to the left */
  position: relative;
  top: 40%;
  box-shadow: rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px;
  

}
.label-content{
  background-color: transparent !important;
  height: 80%;
  width: 90%;
  display: flex;
  margin: auto;
  align-items: center; /* Vertically center the content */
  justify-content: center; /* Horizontally align content to the left */
  font-size: 20px;
  font-weight: bold;
  pointer-events: auto;

}
#resetButton {
    position: absolute;
    top: 10%; /* Adjust top position as needed */
    right: 2%; /* Adjust left position as needed */
    z-index: 100;
    display: none;
}

.button-55 {
  align-self: center;
  background-color: #fff;
  background-image: none;
  background-position: 0 90%;
  background-repeat: repeat no-repeat;
  background-size: 4px 3px;
  border-radius: 15px 225px 255px 15px 15px 255px 225px 15px;
  border-style: solid;
  border-width: 2px;
  box-shadow: rgba(0, 0, 0, .2) 15px 28px 25px -18px;
  box-sizing: border-box;
  color: #41403e;
  cursor: pointer;
  display: inline-block;
  font-family: Neucha, sans-serif;
  font-size: 1rem;
  line-height: 23px;
  outline: none;
  padding: .75rem;
  text-decoration: none;
  transition: all 235ms ease-in-out;
  border-bottom-left-radius: 15px 255px;
  border-bottom-right-radius: 225px 15px;
  border-top-left-radius: 255px 15px;
  border-top-right-radius: 15px 225px;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
}

.button-55:hover {
  box-shadow: rgba(0, 0, 0, .3) 2px 8px 8px -5px;
  transform: translate3d(0, 2px, 0);
}

.button-55:focus {
  box-shadow: rgba(0, 0, 0, .3) 2px 8px 4px -6px;
}

</style>

# Viz Sieves

```js
import * as THREE from 'npm:three';
import { CSS2DRenderer,CSS2DObject } from 'three/addons/renderers/CSS2DRenderer.js';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
// import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
let imagePositions = [];
let sprites = [];
const raycaster = new THREE.Raycaster();
const mouse = new THREE.Vector2();
let focusSprite = null; // Currently focused sprite
let initialCameraPosition = new THREE.Vector3(); // Initial position of the camera
let initialLookAtPosition = new THREE.Vector3();
let isCameraMoving = false;
 const resetButton = document.getElementById('resetButton');
  // resetButton.style.visibility = 'visible';
const labelRenderer = new CSS2DRenderer();
let canvasWidth = 0.97 * document.getElementById("threeD").offsetWidth;
let canvasHeight = 0.97 * document.getElementById("threeD").offsetWidth / 16 * 10;
labelRenderer.setSize(canvasWidth, canvasHeight);
labelRenderer.domElement.style.position = 'absolute';
labelRenderer.domElement.style.top = '10%';
labelRenderer.domElement.style.pointerEvents = 'none';
document.getElementById("threeD").appendChild(labelRenderer.domElement);
fetch('https://zhiyangwang.site/giant-viz-data/image_tsne_projections.json')
  .then(response => response.json())
  .then(data => {
    imagePositions = data;
    loadAtlases(init); // Load all atlases before initializing
  });

const atlases = [
  { url: 'https://zhiyangwang.site/giant-viz-data/atlas-1.jpg', grid: { x: 64, y: 64 }, count: 4096 },
  { url: 'https://zhiyangwang.site/giant-viz-data/atlas-2.jpg', grid: { x: 64, y: 64 }, count: 4096 },
  { url: 'https://zhiyangwang.site/giant-viz-data/atlas-3.jpg', grid: { x: 64, y: 64 }, count: 4096 },
  { url: 'https://zhiyangwang.site/giant-viz-data/atlas-4.jpg', grid: { x: 64, y: 25 }, count: 1463 }
];

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 10000);
camera.position.set(100, 15, 0);
initialLookAtPosition.set(0, 0, 0);
camera.lookAt(initialLookAtPosition);
initialCameraPosition.copy(camera.position);
const renderer = new THREE.WebGLRenderer();
renderer.setSize(canvasWidth, canvasHeight);
document.getElementById("threeD").appendChild(renderer.domElement);
renderer.setClearColor( 0xf2d7d5, 0.8);

const myDiv = document.getElementById("threeD")
myDiv.addEventListener('mouseenter', function() {
    // Disable scrolling and zooming when mouse enters the div
    document.body.style.overflow = 'hidden'; 
    document.addEventListener('wheel', disableScrollAndZoom, { passive: false });
});
myDiv.addEventListener('mouseleave', function() {
    // Enable scrolling and remove the event listener for zoom when mouse leaves the div
    document.body.style.overflow = 'auto';
    document.removeEventListener('wheel', disableScrollAndZoom, { passive: false });
});

function disableScrollAndZoom(event) {
    // This will prevent scrolling and zooming (CTRL + wheel)
    event.preventDefault();
}
// const controls = new OrbitControls(camera, renderer.domElement);
const loadDistance = 10;
const size = 150;
const divisions = 50;
scene.add(new THREE.GridHelper(size, divisions));
// scene.add(new THREE.AxesHelper(100));

function loadAtlases(callback) {
  let loadedCount = 0;
  atlases.forEach((atlas, index) => {
    const loader = new THREE.TextureLoader();
    loader.load(atlas.url, texture => {
      atlases[index].texture = texture;
      loadedCount++;
      if (loadedCount === atlases.length) {
        callback(); // Initialize the scene once all atlases are loaded
      }
    });
  });
  console.log(atlases)
}
function init() {


    imagePositions.forEach(item => {
    let atlasIndex = 0;
    let imageIndex = item.idx;
    let cumulativeCount = 0;

    for (let i = 0; i < atlases.length; i++) {
      cumulativeCount += atlases[i].count;
      if (imageIndex < cumulativeCount) {
        atlasIndex = i;
        imageIndex -= (cumulativeCount - atlases[i].count);
        break;
      }
    }

    const atlas = atlases[atlasIndex];
    const atlasX = imageIndex % atlas.grid.x;
    const atlasY = Math.floor(imageIndex / atlas.grid.x);
    const width = 1 / atlas.grid.x;
    const height = 1 / atlas.grid.y;

     const spriteMaterial = new THREE.SpriteMaterial({
      map: atlas.texture.clone(), // Clone the texture to ensure independent mapping
      color: 0xffffff
    });

    spriteMaterial.map.repeat.set(width, height);
    spriteMaterial.map.offset.set(atlasX * width, 1 - (atlasY + 1) * height);

    const sprite = new THREE.Sprite(spriteMaterial);
    sprite.position.set(item.x * 2, Math.random()*2, item.y * 2);
    sprite.scale.set(1.5,1.5,1.5);
    sprite.className = "sprite";
    sprite.userData = { idx: item.idx, atlasIndex: atlasIndex, highResLoaded: false };
    const spriteLabel = document.createElement('div');
    scene.add(sprite);
    sprites.push(sprite);
  });
  const loadingDiv = document.getElementById('loading');
  const threeD = document.getElementById('threeD');
  loadingDiv.style.display = 'none';
  threeD.style.display = 'flex';
  resetButton.addEventListener('click', () =>{
    moveCamera(initialCameraPosition, initialLookAtPosition);
    console.log("rest button clicked");
     if (focusSprite.userData.labelObject) {
                    focusSprite.userData.labelObject.element.style.visibility = 'hidden'; // Hide label
                }
                focusSprite = null;
  
    resetButton.style.display = 'none';
  });
  setupClickEvent(sprites, camera, renderer);
  setupHoverEvent(sprites, camera, renderer);
  setupCameraControl(camera, renderer)
  animate();
 
}


function animate() {
  requestAnimationFrame(animate);
  updateTextures();

  renderer.render(scene, camera);
  labelRenderer.render(scene, camera);
}
// ----------------------------------------------------------------
// Free Move Camera function 
function setupCameraControl(camera, renderer) {
    let isDragging = false;
    let dragButton = 0; // 0 for left button, 2 for right button
    let previousMousePosition = { x: 0, y: 0 };
    const rotationSpeed = 0.005; // Speed of the camera rotation
    let angularVelocityY = 0;
    let angularVelocityZ = 0;
    const angularDamping = 0.9;
    let zoomVelocity = 0;
    const zoomDamping = 0.9;

    // Function to update camera rotation and zoom based on mouse movement
    function updateCamera() {
        if (isCameraMoving) return; // If the camera is automatically moving, stop manual update.

        if (angularVelocityY !== 0) {
         camera.rotateOnWorldAxis(new THREE.Vector3(0, 1, 0), angularVelocityY); 
         angularVelocityY *= angularDamping;
        }
        if (angularVelocityZ !== 0) {
            camera.rotateOnWorldAxis(new THREE.Vector3(0, 0, 1), angularVelocityZ);
            angularVelocityZ *= angularDamping;
        }
        if (zoomVelocity !== 0) {
            camera.translateZ(-zoomVelocity); // Corrected zoom direction
            zoomVelocity *= zoomDamping;
        }
    }

    // Add mousedown event listener for initiating drag
    renderer.domElement.addEventListener('mousedown', function(e) {
        if (isCameraMoving) return; // Disable manual control if the camera is automatically moving.
        isDragging = true;
        dragButton = e.button;
        previousMousePosition.x = e.clientX;
        previousMousePosition.y = e.clientY;
    });

    // Add mousemove event listener for handling camera rotation
    renderer.domElement.addEventListener('mousemove', function(e) {
        if (!isDragging || isCameraMoving) return;

        const deltaX = e.clientX - previousMousePosition.x;
        const deltaY = e.clientY - previousMousePosition.y;

        if (dragButton === 0) { // Left mouse button for horizontal rotation (around Y axis)
            angularVelocityY = deltaX * rotationSpeed;
        } else if (dragButton === 2) { // Right mouse button for vertical rotation (around Z axis)
            angularVelocityZ = deltaY * rotationSpeed;
        }

        previousMousePosition.x = e.clientX;
        previousMousePosition.y = e.clientY;
    });

    // Add mouseup event listener to stop dragging
    renderer.domElement.addEventListener('mouseup', function(e) {
        isDragging = false;
    });

    // Add mousewheel event listener for zoom control
    renderer.domElement.addEventListener('wheel', function(e) {
        if (isCameraMoving) return;
        zoomVelocity += e.deltaY * -0.02; // Adjust zoom sensitivity as needed
    });

    // Prevent right-click menu to enable right-click dragging
    renderer.domElement.addEventListener('contextmenu', function(e) {
        e.preventDefault();
    });

    // Set animation loop to continuously render the scene
    renderer.setAnimationLoop(() => {
        updateCamera();
        renderer.render(scene, camera);
    });

    // Cleanup function to remove event listeners
    return function cleanup() {
        renderer.domElement.removeEventListener('mousedown', null);
        renderer.domElement.removeEventListener('mousemove', null);
        renderer.domElement.removeEventListener('mouseup', null);
        renderer.domElement.removeEventListener('wheel', null);
        renderer.domElement.removeEventListener('contextmenu', null);
        renderer.setAnimationLoop(null);
    };
}

const cleanupControls = setupCameraControl(camera, renderer);

// Free Move Camera function 
// ----------------------------------------------------------------




// Dynamic Load the Texture based on the camera position
// ----------------------------------------------------------------


function updateTextures() {
  sprites.forEach(sprite => {
    const distance = camera.position.distanceTo(sprite.position);
    if (distance < loadDistance && !sprite.userData.highResLoaded) {
      const loader = new THREE.TextureLoader();
      loader.load(`https://zhiyangwang.site/giant-viz-data/15000-imgs/animals-${sprite.userData.idx+1}.jpg`, texture => {
        sprite.material.map = texture;
        sprite.material.needsUpdate = true;
        sprite.userData.highResLoaded = true;
      });
    } 
  });
}


// ----------------------------------------------------------------
// Dynamic Load the Texture based on the camera position



// Hover Event to make the interaction more vivid
// ----------------------------------------------------------------

function setupHoverEvent(sprites, camera, renderer) {
    let lastHovered = null;  // Track the last hovered sprite to reset its size

    renderer.domElement.addEventListener('mousemove', event => {
        event.preventDefault();

        const rect = renderer.domElement.getBoundingClientRect();
        mouse.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
        mouse.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;

        raycaster.setFromCamera(mouse, camera);
        const intersects = raycaster.intersectObjects(sprites);

        if (intersects.length > 0) {
            const hoveredSprite = intersects[0].object;
            // Ensure the hovered sprite is not the currently selected/focused sprite
            if (hoveredSprite !== focusSprite) {
                if (lastHovered !== hoveredSprite) {
                    if (lastHovered && lastHovered !== focusSprite) {
                        lastHovered.scale.divideScalar(1.1);  // Reset the last hovered sprite
                    }
                    hoveredSprite.scale.multiplyScalar(1.1);  // Scale up the newly hovered sprite
                    lastHovered = hoveredSprite;
                }
            }
        } else if (lastHovered && lastHovered !== focusSprite) {
            lastHovered.scale.divideScalar(1.1);  // Reset if no sprite is hovered
            lastHovered = null;
        }
    }, false);
}

// ----------------------------------------------------------------
// Hover Event to make the interaction more vivid






// Camera Moving and label display when clciked
// ----------------------------------------------------------------

function setupClickEvent(sprites, camera, renderer) {
    renderer.domElement.addEventListener('click', event => {
        if(isCameraMoving) return;
        const rect = renderer.domElement.getBoundingClientRect();
        mouse.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
        mouse.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;

        raycaster.setFromCamera(mouse, camera);
        const intersects = raycaster.intersectObjects(sprites);

        if (intersects.length > 0) {
            const selectedSprite = intersects[0].object;

            // Reset previous focused sprite
            if (focusSprite && focusSprite !== selectedSprite) {
                focusSprite.scale.divideScalar(1.4);
                focusSprite.position.y -= 2;
                if (focusSprite.userData.labelObject) {
                    focusSprite.userData.labelObject.element.style.visibility = 'hidden'; // Hide label
                }
            }

            // Select new sprite
            if (!focusSprite || focusSprite !== selectedSprite) {
                selectedSprite.scale.multiplyScalar(1.4);
                selectedSprite.position.y += 2;
                focusSprite = selectedSprite;

                // Create label if it doesn't exist
                if (!selectedSprite.userData.labelObject) {
                    const spriteLabel = document.createElement('div');
                    spriteLabel.className = 'sprite-label';
                    // spriteLabel.style.width = `${0.34*canvasWidth}px`;
                    // spriteLabel.style.height = `${0.1*canvasHeight}px`;
                    spriteLabel.style.width = `${0.5*canvasWidth}px`;
                    spriteLabel.style.height = `${0.1*canvasHeight}px`;
                    console.log(selectedSprite.userData);
                    // spriteLabel.textContent = `Index: ${selectedSprite.userData.idx}, X: ${selectedSprite.position.x.toFixed(2)}, Y: ${selectedSprite.position.y.toFixed(2)}`;
                    let labelContentDiv = document.createElement('div');
                    labelContentDiv.className = 'label-content';
                    labelContentDiv.textContent = `Index: ${selectedSprite.userData.idx}, X: ${selectedSprite.position.x.toFixed(2)}, Y: ${selectedSprite.position.y.toFixed(2)}`;

                    // Append the div element to spriteLabel
                    spriteLabel.appendChild(labelContentDiv);
                    spriteLabel.style.visibility = 'visible'; // Make label visible
                    

                    const labelObject = new CSS2DObject(spriteLabel);
                    labelObject.position.set(0, 0, 0); // Position label right below the sprite
                    
                    selectedSprite.add(labelObject);
                    selectedSprite.userData.labelObject = labelObject; // Store reference to label object
                } else {
                    // Show existing label
                    selectedSprite.userData.labelObject.element.style.visibility = 'visible';
                }

                // Calculate camera move target position
                const targetPosition = new THREE.Vector3(selectedSprite.position.x + 1, selectedSprite.position.y + 2, selectedSprite.position.z);
                const lookAtPosition = new THREE.Vector3(selectedSprite.position.x, selectedSprite.position.y, selectedSprite.position.z);
                moveCamera(targetPosition, lookAtPosition);
            }
        } else {
            // If no sprite is selected
            if (focusSprite) {
                focusSprite.scale.divideScalar(1.4);
                focusSprite.position.y -= 2;
                if (focusSprite.userData.labelObject) {
                    focusSprite.userData.labelObject.element.style.visibility = 'hidden'; // Hide label
                }
                focusSprite = null;
            }
            // Move camera back to the initial position and look at the initial look at position
            // moveCamera(initialCameraPosition, initialLookAtPosition);
        }
    }, false);
}



// Camera Moving trigger and label display when clciked the sprites
// ----------------------------------------------------------------


// Camera Moving fucntions
// ----------------------------------------------------------------

function moveCamera(target, lookAtPosition) {
    if (isCameraMoving) return; // 确保不重复调用移动相机的函数
    isCameraMoving = true;
    let delta = 0.1; 
    const epsilon = 0.1;
    const labelVisibilityThreshold = 0.5; // 标签显示阈值
    let lastFrameTime = Date.now(); // 用于帧率控制
 
    if (target !== initialCameraPosition) {
        resetButton.style.display = "flex"; // 显示重置按钮
    }else{
        let delta = 0.3; 
    }

    function updateCameraPosition() {
        let now = Date.now();
        let elapsed = now - lastFrameTime;

        if (elapsed > (1000 / 60)) { // 控制最大帧率约为60fps
            lastFrameTime = now - (elapsed % (1000 / 60));
            let distance = camera.position.distanceTo(target);
            if (distance > epsilon) {
                camera.position.lerp(target, delta);
                camera.lookAt(lookAtPosition);
                raycaster.setFromCamera(mouse, camera);
                requestAnimationFrame(updateCameraPosition);

                // 控制标签可见性
                if (focusSprite && distance < labelVisibilityThreshold) {
                    let opacity = (labelVisibilityThreshold - distance) / labelVisibilityThreshold;
                    focusSprite.userData.labelObject.element.style.opacity = opacity;
                }
            } else {
                camera.position.copy(target);
                camera.lookAt(lookAtPosition);
                raycaster.setFromCamera(mouse, camera);
                isCameraMoving = false;
                if (focusSprite) {
                    focusSprite.userData.labelObject.element.style.opacity = 1; // 确保标签完全可见
                }
            }
        } else {
            requestAnimationFrame(updateCameraPosition);
        }
    }

    updateCameraPosition();
}


// ----------------------------------------------------------------
// Camera Moving fucntions



```

<!-- html formating -->
<div class = "card"  id="loading">Loading...</div>

<div class = "card" id="threeD">
<button id='resetButton' class="button-55" >Go Back</button>
</div>


<div class="card">

</div>