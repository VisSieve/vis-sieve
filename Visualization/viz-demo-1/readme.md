# viz-demo-1

## features

- preloaded low resolution images via the altas
- dynamic loading the high resolution images based on camera positioning
- dynamic loading label based on clicked images
- free camera moving via mouse movement


## Struture of the code

- section-1: the basic info definition of the code
- section-2(CSS): style the design of dom elements
- section-3(js): the key parts of the visualization
    - 3-1: import libs(3.js) and its dependencies
    - 3-2: define variables
    - 3-3: loaded json files(contains poistion of each images) and altas 
    - 3-4: ``` function init() ``` function to load the 3d canvas
    - 3-5: ``` function animate() ``` function to keep the canvas responsive
    - 3-6: ``` function setupCameraControl() ``` function to set the camera move freely
    - 3-7: ``` function updateTextures() ``` function to update the texture with the new high resolution image
    - 3-8: ``` function setupHoverEvent() ``` function to make images change size to mouse over it
    - 3-9: ``` function setupClickEvent() ``` function to make the camera will move based on the click event and controls the label display 
        - The click is based on three.js Raycaster
    - 3-10: ``` function moveCamera() ``` function to move the camera, which will be called by setupClickEvent();
    - 3-11: ```<button id='resetButton' class="button-55" >Go Back</button>``` is used to make the camera back to initial position

## Run the code

- Install Obseravable Framework
- install three.js ```npm install --save three```
- put the viz-demo-1.md to the src directory and ```npm run dev```