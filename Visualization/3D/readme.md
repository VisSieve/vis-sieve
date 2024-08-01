# 3d Interactive Viz

- 3D Ubreracruce Viz is the experimental showcase for the datasets collected and analysed in Vis-sievs Project that utilizes Three.js and D3.js for web-based 3D visualization.

## Repository Layout

- [vis-code.md](./vis-code.md) is the latest functional code, if you want the code can directly being used, look [this](https://github.com/JimmyXwtx/3dVis)
- [Archive](./archive/) conatains the previous version of codes
- [Key features](./keyfeatures/) gives you the basic understanding of key features

## Key Features

- 3D Canavs allows you do naviage around, each image is clickable, just mouse needed for interaction
- Dynamic Loading Image, before getting close to image or select images, only low resolution images preview will be loaded
- selected image will display its details(chartType, Topic, Domain, etc...), also users can use the pop up navbar to see high Resolution Image or see the full paper

## Code Structure

Tools: 
- Observable Framework
- D3.js
- Three.js

## Direct Use of the Code

- Download the code from this [repo](https://github.com/JimmyXwtx/3dVis)
- `npm install` or `npm i` in termninal to install all dependencies
- `npm run dev` for development
- `npm run build` for deployment

- Structure of the files

- `import` Statements:
    - Imports necessary libraries and modules (d3, d3-scale-chromatic, duckdb).
- `initialDB(db)`:
    - Connects to a database and fetches publication data including paper details and figure properties.
    - Processes query results and converts them to a JSON format for easier manipulation.
- `countChartPos(db)`:
    - Executes a query to calculate average positions and counts for chart types in the database.
    - Maps the results to a structured format that includes positions and labels derived from the visualizationTypes array.
- `countTopics(db)`:
    - Queries the database to retrieve topic information such as id, name, subfield, and field.
    - Returns the array of topics for later use in enriching sprite data.
- `loadDataAndInitialize()`:
    - Initializes data loading from the database and sets up the 3D visualization environment.
    - Calls loadAtlases() to load texture atlases and subsequently initializes the 3D scene using init().
- `loadAtlases(callback)`:
    - Loads image textures from specified URLs, storing them in an atlases array.
    - Executes a callback function (usually init) once all textures are loaded.
- `init()`:
    - Prepares the 3D visualization scene by setting up camera, renderer, and controls.
    - Places sprites in the scene based on loaded data and attaches high-resolution textures and interactivity features.
- `setupCameraControl(camera, renderer)`:
    - Enables interactive control over the camera, allowing free movement, rotation, and zoom based on user input.
    - Implements checks to prevent camera movement out of predefined boundaries.
- `setupClickEvent(sprites, camera, renderer)`:
    - Adds event listeners to the renderer to handle mouse clicks, identifying sprites under the cursor and selecting them.
    - Manages focus on sprites, allowing for detailed inspection and interaction.
- `selectSprite(sprite) and unSelectSprite()`:
    - Manage selection and deselection of sprites, modifying their scale and position to highlight or reset.
    - Dynamically adds a UI panel for detailed actions related to the selected sprite.
- `moveCamera(target, lookAtPosition)`:
    - Smoothly transitions the camera towards a target position while maintaining a view directed towards a specified lookAt position.
    - Uses easing functions to smooth out the camera movement.
- `updateTextures()`:
    - Periodically checks the distance of each sprite from the camera and loads higher-resolution textures for close sprites.
    - Enhances the visual quality of sprites when viewed at closer range.
- `generateScatterPlot(data, w, h, parentDom)`:
    - Utilizes D3.js to create a scatter plot based on sprite positions and visualization types.
    - Implements additional interactivity by linking plot elements with 3D sprite positions, enhancing the exploration experience.


