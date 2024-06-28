# viz-demo-2-bugFixed-bubbleFeatures

## New-features

- create bubble for each group images
- click bubble for each group will bring camera to the group
- Intro Page before showing the canavs
- fix bug in viz-demo-1: "labdel doss not disappear when camera mosve out"
- fix bug in viz-demo-1: "the back button works not properly."


## Existing-features

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


- Section-1: Basic Information Definition

    -   Title: Base Version-Label
    -   Table of Contents (TOC): Disabled

- Section-2 (CSS): Style the Design of DOM Elements

    -   Flex display settings for various div elements, centering both horizontally and vertically.
    -   Keyframe animations for fade-in and fade-out effects.
    -   Styling for loading indicators, buttons, labels, and visibility transitions.

- Section-3 (JavaScript): Key Parts of the Visualization

    - 3-1: Import Libraries (Three.js) and Dependencies

        -   THREE from Three.js for 3D rendering.
        -   OrbitControls for camera control.
        -   CSS2DRenderer for overlaying HTML elements as labels on 3D objects.

    - 3-2: Define Variables

        -   Arrays and variables for storing image positions, textures, sprite references, and other UI elements.

    - 3-3: Load JSON Files

        -   Load and parse JSON for image positions and sprite grouping.

    - 3-4: ```function init()```

        -   Setup the 3D scene, camera, renderer, and initial configurations.
        -   Load all atlases and initialize event listeners for UI interactions.

    - 3-5: ```function animate()```

        -   Animation loop for rendering the scene and updating textures based on camera distance.

    - 3-6: ```function setupCameraControl()```

        -   Configures free camera movement using mouse interactions.
        -   Applies rotation and zoom based on user input.

    - 3-7: ```function updateTextures()```

        -   Dynamically load high-resolution textures for sprites when the camera is near.

    - 3-8: ```function setupHoverEvent()```

        -   Changes sprite size on hover to enhance interactive visual feedback.

    - 3-9: ```function setupClickEvent()```

        -   Moves the camera based on the sprite clicked using Three.js Raycaster.
        -   Manages labels for clicked sprites.

    - 3-10: ```function moveCamera()```

        -   Smoothly transitions camera to target positions, handling interactive animations and resetting views.

    - 3-11: ```#resetButton```

        -   A button to reset the camera to its initial position, enhancing user navigation control.

- HTML Formatting

    -   Loading, instruction, and information divs styled and animated to guide user interaction.
    -   Primary interactive area within a div styled as a 3D rendering canvas.

## Run the code

- Install Obseravable Framework
- install three.js ```npm install --save three```
- put the viz-demo-1.md to the src directory and ```npm run dev```