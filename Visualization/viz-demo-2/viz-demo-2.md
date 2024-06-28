---
title: base version-label-babel
toc: false
---
<style>
boad
#threeD{
    display: flex;
    justify-content: center; /* Center items horizontally */
    align-items: center; /* Center items vertically */

}
@keyframes fadeInScaleUp {
  0% {
    opacity: 0;
    transform: scale(0.95);
  }
  100% {
    opacity: 1;
    transform: scale(1);
  }
}
@keyframes fadeOutScaleDown {
  0% {
    opacity: 1;
    transform: scale(1);
  }
  100% {
    opacity: 0;
    transform: scale(0.5);
  }
}

.hidden {
  visibility: hidden;
  opacity: 0;
  transition: visibility 0s 0.5s, opacity 0.5s linear; 
}

.visible {
  visibility: visible;
  opacity: 1;
  transition: opacity 0.5s linear; 
}
.fade-in{
 animation: fadeInScaleUp 0.5s ease-in-out forwards; 

}
.fade-out {
  animation: fadeOutScaleDown 0.5s ease-in-out forwards;
}

#loading{
    display: none;
    position: absolute;
    /* margin: auto; */
    justify-content: center; /* Center items horizontally */
    align-items: center; /* Center items vertically */
    background-color: #f7f7f7;
    scale: 0.95;
}

.loadingContent {
  position: relative;
  top: 1.8%;
  width: 90%;
  height: 90%;
  padding-top: 10%;
  display: flex;
  margin: auto;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
  background-color: #fff7f7; /* Light background color */
  box-shadow: 0 4px 8px rgba(0,0,0,0.1); /* Subtle shadow for depth */
  border-radius: 10px; /* Slightly rounded corners */
  padding: 20px;
  box-sizing: border-box;
}

.contentTitle {
  font-size: 24px; /* Larger font for visibility */
  font-weight: bold;
  color: #333; /* Dark color for contrast */
  text-align: center;
  margin-bottom: 10px;
}

.contentInfo, .contentInstruction {
  font-size: 16px;
  color: #555; /* Slightly lighter color for info and instructions */
  text-align: center;
  margin: 5px 0; /* Spacing for clean separation */
}

.enterButton {
  align-self: center; /* Center the button container */
  margin-top: 20px;
}

/* Ensure the button class is applied as needed */
.enterButton button {
  --b: 3px;   /* border thickness */
  --s: .45em; /* size of the corner */
  --color: #373B44;
  
  padding: calc(.5em + var(--s)) calc(.9em + var(--s));
  color: var(--color);
  --_p: var(--s);
  background:
    conic-gradient(from 90deg at var(--b) var(--b), #0000 90deg, var(--color) 0)
    var(--_p) var(--_p)/calc(100% - var(--b) - 2*var(--_p)) calc(100% - var(--b) - 2*var(--_p));
  transition: .3s linear, color 0s, background-color 0s;
  outline: var(--b) solid #0000;
  outline-offset: .6em;
  font-size: 16px;

  border: 0;

  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
}

.enterButton button:hover,
.enterButton button:focus-visible {
  --_p: 0px;
  outline-color: var(--color);
  outline-offset: .05em;
}

.enterButton button:active {
  background: var(--color);
  color: #fff;
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

# Viz Sieves-Bubble

```js
import * as THREE from 'npm:three';
import { CSS2DRenderer,CSS2DObject } from 'three/addons/renderers/CSS2DRenderer.js';
// import { FontLoader } from 'three/addons/loaders/FontLoader.js';
// import { TextGeometry } from 'three/addons/geometries/TextGeometry.js';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
// import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
let imagePositions = [];
let groupLabelPosition = [];
let groupLabel = [];
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
renderer.domElement.classList.add("hidden");
renderer.setSize(canvasWidth, canvasHeight);
document.getElementById("threeD").appendChild(renderer.domElement);
renderer.domElement.style.borderRadius = "10px";
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
const loadingDiv = document.getElementById('loading');
const threeD = document.getElementById('threeD');
const enterButton = document.getElementById('enter');
loadingDiv.style.width = `${threeD.offsetWidth}px`;
loadingDiv.style.height = `${threeD.offsetHeight}px`;
loadingDiv.style.display = "flex";


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
  fetch('https://zhiyangwang.site/giant-viz-data/group.json')
    .then(response => response.json())
    .then(handleGroupData);
  setupClickEvent(sprites, camera, renderer);
  setupHoverEvent(sprites, camera, renderer);
  setupClickEventGroup(groupLabel, camera, renderer);
  setupCameraControl(camera, renderer)
  animate();
   enterButton.addEventListener('click',()=>{
    loadingDiv.classList.remove("fade-in");
    loadingDiv.classList.add("fade-out");
    // loadingDiv.style.display = 'none';
    renderer.domElement.classList.remove("hidden");
    renderer.domElement.classList.add("visible");
    loadingDiv.style.pointerEvents = 'none';
  });


  resetButton.addEventListener('click', () =>{
    if(isCameraMoving) return;
    moveCamera(initialCameraPosition, initialLookAtPosition);
    console.log("rest button clicked");
     unSelectSprite();
    resetButton.style.display = 'none';
    
  });
 
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
         if(focusSprite){
          unSelectSprite();
         }
        isDragging = true;
        dragButton = e.button;
        previousMousePosition.x = e.clientX;
        previousMousePosition.y = e.clientY;
    });

    // Add mousemove event listener for handling camera rotation
    renderer.domElement.addEventListener('mousemove', function(e) {
        if (!isDragging || isCameraMoving) return;
         if(focusSprite){
          unSelectSprite();
         }
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
         if(focusSprite){
          unSelectSprite();
         }
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
                  if(sprites == groupLabel){

                  }else{}
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

function unSelectSprite(){
  if (focusSprite) {
                focusSprite.scale.divideScalar(1.4);
                focusSprite.position.y -= 2;
                if (focusSprite.userData.labelObject) {
                    focusSprite.userData.labelObject.element.style.visibility = 'hidden'; // Hide label
                }
                focusSprite = null;
            }
}


// Camera Moving trigger and label display when clciked the sprites
// ----------------------------------------------------------------


// groupLabel move control
// ----------------------------------------------------------------
function setupClickEventGroup(sprites, camera, renderer) {
    const raycaster = new THREE.Raycaster();
    const mouse = new THREE.Vector2();

    renderer.domElement.addEventListener('mousemove', event => {
        const rect = renderer.domElement.getBoundingClientRect();
        mouse.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
        mouse.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;

        raycaster.setFromCamera(mouse, camera);
        const intersects = raycaster.intersectObjects(sprites);

        if (intersects.length > 0) {
            renderer.domElement.style.cursor = 'pointer';
            const selectedSprite = intersects[0].object;
            selectedSprite.scale.set(14, 7, 1.4); // Enlarge sprite on hover
        } else {
            renderer.domElement.style.cursor = 'auto';
            sprites.forEach(sprite => {
                sprite.scale.set(10, 5, 1);
            });
        }
    });

    renderer.domElement.addEventListener('click', event => {
        const rect = renderer.domElement.getBoundingClientRect();
        mouse.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
        mouse.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;

        raycaster.setFromCamera(mouse, camera);
        const intersects = raycaster.intersectObjects(sprites);

        if (intersects.length > 0) {
            const selectedSprite = intersects[0].object;

            // Calculate camera move target position
            const targetPosition = new THREE.Vector3(selectedSprite.position.x, selectedSprite.position.y + 10, selectedSprite.position.z);
            const lookAtPosition = new THREE.Vector3(selectedSprite.position.x, 0, selectedSprite.position.z);
            
            moveCamera(targetPosition, lookAtPosition);
        }
    }, false);
}

//----------------------------------------------------------------
// groupLabel move control





// Camera Moving functions
// ----------------------------------------------------------------
function moveCamera(target, lookAtPosition) {
    if (isCameraMoving) return;
    isCameraMoving = true;

    let delta = 0.1; // Initial interpolation factor
    const epsilon = 0.1; // Distance threshold
    const labelVisibilityThreshold = 0.5; // Label visibility threshold
    let lastFrameTime = Date.now();

    // Adjust delta for faster movement if moving to initial position
    if (target === initialCameraPosition) {
        delta = 0.3; // Increase interpolation factor for faster movement
    }

    function updateCameraPosition() {
        let now = Date.now();
        let elapsed = now - lastFrameTime;

        if (elapsed > (1000 / 60)) {
            lastFrameTime = now - (elapsed % (1000 / 60));
            let distance = camera.position.distanceTo(target);

            if (distance > epsilon) {
                camera.position.lerp(target, delta);
                // Update view direction during movement
                camera.lookAt(lookAtPosition);
                raycaster.setFromCamera(mouse, camera);
                requestAnimationFrame(updateCameraPosition);

                // Control label visibility
                if (focusSprite && distance < labelVisibilityThreshold) {
                    let opacity = (labelVisibilityThreshold - distance) / labelVisibilityThreshold;
                    focusSprite.userData.labelObject.element.style.opacity = opacity;
                }
            } else {
                camera.position.copy(target);
                // Set final view direction after movement ends
                // camera.lookAt(lookAtPosition);
                raycaster.setFromCamera(mouse, camera);
                isCameraMoving = false;

                // Show or hide reset button based on target position
                if (target !== initialCameraPosition) {
                    resetButton.style.display = "flex"; // Show reset button
                } else {
                    resetButton.style.display = "none"; // Hide reset button
                }

                // Ensure label visibility
                if (focusSprite) {
                    focusSprite.userData.labelObject.element.style.opacity = 1;
                }
            }
        } else {
            requestAnimationFrame(updateCameraPosition);
        }
    }

    updateCameraPosition();
}


// ----------------------------------------------------------------
// Camera Moving functions



// Encapsulate function to handle data and create sprites and lines
// ----------------------------------------------------------------

// Function to create text texture
function createTextTexture(text) {
    const canvas = document.createElement('canvas');
    const context = canvas.getContext('2d');
    canvas.width = 256*2;
    canvas.height = 128*2;

    // Create radial gradient background
    const gradient = context.createRadialGradient(canvas.width / 2, canvas.height / 2, 10, canvas.width / 2, canvas.height / 2, 60);
    gradient.addColorStop(0, 'rgba(255, 255, 255, 0.8)');  // Start color
    gradient.addColorStop(1, 'rgba(255, 255, 255, 0.1)');  // End color

    context.fillStyle = gradient;
    context.beginPath();
    context.arc(canvas.width / 2, canvas.height / 2, 60, 0, 2 * Math.PI);
    context.fill();

    // Set text properties
    context.textAlign = 'center'; // Center align text
    context.textBaseline = 'middle'; // Middle baseline
    context.fillStyle = '#000000'; // Text color
    context.font = '24px Arial';
    context.fillText(text, canvas.width / 2, canvas.height / 2); // Draw text at canvas center

    return new THREE.CanvasTexture(canvas);
}

// Encapsulate function to handle data and create sprites and lines
function handleGroupData(data) {
    data.forEach(item => {
        const { idx, label, x, z } = item;

        // Create sprite with text
        const textTexture = createTextTexture(label);
        const spriteMaterial = new THREE.SpriteMaterial({ map: textTexture, transparent: true });
        const sprite = new THREE.Sprite(spriteMaterial);
        sprite.position.set(x, 16, z);
        sprite.scale.set(10, 5, 1); // Set appropriate sprite size
        scene.add(sprite);
        groupLabel.push(sprite);

        // Create dashed line
        const material = new THREE.LineDashedMaterial({ color: 0x0000ff, dashSize: 0.5, gapSize: 0.5, scale: 1, linewidth: 1 });
        const points = [];
        points.push(new THREE.Vector3(x, 15, z)); // Start from sprite center
        points.push(new THREE.Vector3(x, 0, z));  // Project down to ground
        const geometry = new THREE.BufferGeometry().setFromPoints(points);
        const line = new THREE.Line(geometry, material);
        line.computeLineDistances();
        scene.add(line);
    });
}


// Encapsulate function to handle data and create sprites and lines


```

<!-- html formating -->
<div  id="loading" class="fade-in">

<div class="loadingContent">
<div class="contentTitle">Viz Sieves - 3D Exploration</div>
<div class="contentInfo">this is an Info</div>
<div class="contentInstruction">this is an instruction</div>
<div class="enterButton"><button id="enter">Let's Go</button>
</div>
</div>
</div>

<div class = "card" id="threeD">
<button id='resetButton' class="button-55" class="fade-in" >Go Back</button>
</div>


<div class="card">

</div>