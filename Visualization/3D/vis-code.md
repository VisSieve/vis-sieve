---
toc: false
title: Explore Visualizations in 3D Back UP
---


# Explore Visualizations in 3D Back UP


<!-- below is the css for the decoration -->

<style>
.disabled{
    pointer-events: none;
}
.heatmapContainer{
    overflow-x: scroll;
    height: 800px;
}
.heatmapDom{
    width: 100% !important;
    height: 100%;
    scale: 0.5;
    margin: auto;
    
}
#threeD{
    display: flex;
    /* background: #EEEEEE; */
background: rgb(224,142,31);
background: linear-gradient(0deg, rgba(224,142,31,1) 0%, rgba(185,185,185,1) 100%);
    justify-content: center; /* Center items horizontally */
    align-items: center; /* Center items vertically */

}

#mapContainer {
    z-index: 100000;
    position: absolute;
    justify-content: center; /* Center items horizontally */
    align-items: center; /* Center items vertically */

}

.close-button {
  position: absolute;
  top: 10px;
  right: 10px;
  cursor: pointer;
  background-color: transparent;
  color: black;
  padding: 5px;
  border-radius: 50%;
  font-size: 16px;
  font-family: "Arial",
  line-height: 16px;
  text-align: center;
  width: 30px;
  height: 30px;
  z-index: 1000; /* Ensure the button is on top */
}
#map-title{
  position: absolute;
  top: 3%;
  right: 10%;
  width: 80%;
  height: 10%;
  background-color: transparent;
  color: black;
  font-family: "Helvetica Neue";
  font-weight: bold;
  font-size: 30px;
  line-height: 16px;
  text-align: center;
  z-index: 1000; /* Ensure the button is on top */
}
.full-content {
  width: 100%;
  height: 100%;
  background-color: rgba(255, 255, 255, 0.1); /* Optional: to see the full-content area */
  border-radius: 10px;
  overflow: hidden;
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

#loading {
    display: none;
    position: absolute;
    justify-content: center; /* Center items horizontally */
    align-items: center; /* Center items vertically */
    background-color: transparent;
    scale: 0.95;
}

.loadingContent {
  position: relative;
  top: 1.8%;
  width: 95%;
  height: 95%;
  padding-top: 10%;
  display: flex;
  margin: auto;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
  background-color: white; /* Set to transparent since we will use the pseudo-element for background */
  box-shadow: 0 4px 8px rgba(0,0,0,0.1); /* Subtle shadow for depth */
  border-radius: 10px; /* Slightly rounded corners */
  padding: 20px;
  box-sizing: border-box;
  z-index: 1; /* Ensure content is above the pseudo-element */
}

.loadingContent:before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  /* background-color: #f7f7f7;
  opacity: 0.1;
  background-image:  linear-gradient(#626484 1.8px, transparent 1.8px), 
                     linear-gradient(90deg, #626484 1.8px, transparent 1.8px), 
                     linear-gradient(#626484 0.9px, transparent 0.9px), 
                     linear-gradient(90deg, #626484 0.9px, #e5e5f7 0.9px); */
  background-size: 45px 45px, 45px 45px, 9px 9px, 9px 9px;
  background-position: -1.8px -1.8px, -1.8px -1.8px, -0.9px -0.9px, -0.9px -0.9px;
  border-radius: 10px; /* Match border radius with parent */
  z-index: -1; /* Ensure it is behind the content */
}

.contentTitle {
  font-size: 24px; /* Larger font for visibility */
  font-weight: bold;
  color: #333; /* Dark color for contrast */
  text-align: center;
  margin-bottom: 10px;
}

.contentInfo, .contentInstruction {
  font-size: 18px;
  width: 80%;
  color: #555; /* Slightly lighter color for info and instructions */
  text-align: center;
  margin: 5px 0; /* Spacing for clean separation */
}

.instructionDetails {
  width: 100%; /* Full width for the container */
  box-shadow: 0 4px 8px rgba(0,0,0,0.1); /* Subtle shadow for depth */
  border-radius: 10px;
  display: flex;
  background-color: #f7f7f7;
  flex-direction: column;
  align-items: flex-start; /* Align items to flex-start */
  padding: 10px;
  box-sizing: border-box;
}

.contentInstruction ul {
  width: 100%; /* Full width for the list */
  padding: 0; /* Remove default padding */
  margin: 0; /* Remove default margin */
  list-style: none; /* Remove default list styling */
}

.contentInstruction ul li {
  width: 130%; /* Full width for the list items */
  margin-bottom: 10px; /* Spacing between list items */
  text-align: left; /* Align text to the left */
 
  text-overflow: ellipsis; /* Add ellipsis for overflow text */
}

.contentInstruction ul li strong {
  font-weight: bold; /* Bold font for essential parts */
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

#resetButton, #mapButton {
    position: absolute;
    width: 8%;
    top: 17%; /* Adjust top position as needed */
    right: 2%; /* Adjust right position as needed */
    z-index: 100;
    display: none;
    text-align: center; /* Center text horizontally */
    align-items: center; /* Center text vertically */
    justify-content: center; /* Center text horizontally */
    display: none; /* Enable flexbox */
}

/* Adjust top position for mapButton */
#mapButton {
    top: 10%;
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
/* CSS */
/* CSS */
.button-16 {
  background-color: #f8f9fa;
  border: 1px solid #f8f9fa;
  border-radius: 4px;
  color: #3c4043;
  cursor: pointer;
  font-family: arial,sans-serif;
  font-size: 14px;
  height: 36px;
  line-height: 27px;
  min-width: 54px;
  padding: 0 16px;
  text-align: center;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  white-space: pre;
  transition: opacity 0.5s ease-in-out, border-color 0.2s ease, box-shadow 0.2s ease, color 0.2s ease;
  opacity: 0; /* Initial opacity */
}

.button-16:hover {
  border-color: #dadce0;
  box-shadow: rgba(0, 0, 0, .1) 0 1px 1px;
  color: #202124;
}

.button-16:focus {
  border-color: #4285f4;
  outline: none;
}

</style>

<!-- below is the css for the decoration -->

<!-- https://observablehq.com/framework/lib/duckdb -->
<!-- duckdb with ob reference -->

```js
// Declare labels

let visualizationTypes = [
    "Violin",
    "Density",
    "Histogram",
    "Boxplot",
    "Ridgeline",
    "Scatter",
    "Heatmap",
    "Correlogram",
    "Bubble",
    "Connected scatter",
    "Density 2d",
    "Barplot",
    "Spider / Radar",
    "Wordcloud",
    "Parallel",
    "Lollipop",
    "Circular Barplot",
    "Treemap",
    "Venn diagram",
    "Doughnut",
    "Pie chart",
    "Dendrogram",
    "Circular packing",
    "Sunburst",
    "Line plot",
    "Area",
    "Stacked area",
    "Streamchart",
    "Map",
    "Choropleth",
    "Hexbin map",
    "Cartogram",
    "Connection",
    "Bubble map",
    "Chord diagram",
    "Network",
    "Sankey",
    "Arc diagram",
    "Edge bundling",
    "Complex",
    "Scientific Viz",
    "Other-1",
    "Other-2",
    "Other-3",
    "Other-4"
];
// Declare labels

// import libs
import * as d3 from "npm:d3";
import {scaleSequential, interpolateViridis} from "npm:d3-scale-chromatic@3";
import * as duckdb from "npm:@duckdb/duckdb-wasm";
// import libs

// import data
const db = await DuckDBClient.of({base: FileAttachment("/data/publications_princeton.db")});
// import data

// data extraction by the defined data function 
const publicationDB = await initialDB(db)
const chartPos = await countChartPos(db);
// console.log(chartPos);
const topicsArray = await countTopics(db);

const getObjectById = (data,id) => {
    return data.find(item => item.id === id);
};
const getObjectByIdx = (data,id) => {
    return data.find(item => item.idx === id);
};
const getObjectByIdFigure = (data,id) => {
    return data.find(item => item.figure_id === id);
};
// data extraction

// ----------------------------------------------------------------
// ----------------------------------------------------------------
// Database handling functions


// Function to initialize the database and fetch the publication data
async function initialDB(db) {
    try {
        const results = await db.query(`
            SELECT 
                f.id AS figure_id, 
                p.id AS paper_id, 
                p.title, 
                p.doi, 
                p.publication_date, 
                p.oa_url, 
                p.pdf_path, 
                p.inst_id, 
                p.primary_topic_id,
                f.local_path, 
                f.server_path, 
                fp.name, 
                fp.int_value AS ChartType,  
                fp.string_value AS Something, 
                fp.xPos, 
                fp.yPos, 
                fp.zPos
            FROM 
                base.figure f
            LEFT JOIN 
                base.paper p ON f.paper_id = p.id
            LEFT JOIN 
                base.figure_property fp ON f.id = fp.figure_id
            ORDER BY 
                f.id;
        `);
        
        const resultsArray = results.toArray();
    
        // return resultsArray;
        return JSON.stringify(resultsArray, null, 2);
        
        // publicationDB = JSON.stringify(resultsArray, null, 2);
    } catch (error) {
        console.error("Error executing query:", error);
    }
}


async function countChartPos(db) {
    try {
        const results = await db.query(`
            SELECT 
                int_value, 
                AVG(figure_property.xPos) AS xPos, 
                AVG(figure_property.yPos) AS yPos, 
                AVG(figure_property.zPos) AS zPos, 
                COUNT(*) AS count 
            FROM 
                base.figure_property 
            GROUP BY 
                int_value
            ORDER BY 
                int_value;
        `);

        const resultsArray = results.toArray();
        const output = resultsArray.map(row => ({
            idx: row.int_value,
            x: row.xPos/10,
            y: row.yPos,
            z: row.zPos/10,
            count: row.count,
            label: visualizationTypes[row.int_value]
        }));
        
        return output;
    } catch (error) {
        console.error("Error executing query:", error);
        throw error;
    }
}

// count avg position


async function countTopics(db) {
    try {
 
        const results = await db.query(`
            SELECT 
               id,
               name,
               subfield,
               field,
               domain,
            FROM 
                base.topic
            ORDER BY 
                id;
        `);

        const resultsArray = results.toArray();
        return resultsArray;
    } catch (error) {
        console.error("Error executing query:", error);
        throw error;
    }
}

// Database handling
// ----------------------------------------------------------------
// ----------------------------------------------------------------




// ----------------------------------------------------------------
// ----------------------------------------------------------------



// below is the details of 3D data viz
// ----------------------------------------------------------------
// ----------------------------------------------------------------
// ----------------------------------------------------------------
// ----------------------------------------------------------------
// ----------------------------------------------------------------

import * as THREE from 'npm:three';
import { CSS2DRenderer,CSS2DObject } from 'three/addons/renderers/CSS2DRenderer.js';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';



// global variables
let imagePositions;
let sprites = [];
    const colors = [
        // "#e6194B", "#3cb44b", "#ffe119", "#4363d8", "#f58231", "#911eb4", "#46f0f0", "#f032e6",
        // "#bcf60c", "#fabebe", "#008080", "#e6beff", "#9a6324", "#fffac8", "#800000", "#aaffc3",
        // "#808000", "#ffd8b1", "#000075", "#808080", "#fa8072", "#4682b4", "#6a5acd", "#20b2aa",
        // "#9400d3", "#ff6347", "#40e0d0", "#ee82ee", "#dda0dd", "#b0c4de", "#ff7f50", "#6495ed",
        // "#deb887", "#5f9ea0", "#7fff00", "#d2691e", "#ff69b4", "#1e90ff", "#228b22", "#ffc0cb",
        // "#8a2be2", "#a52a2a", "#8b008b", "#b8860b", "#66cdaa", "#ff4500", "#daa520", "#98fb98",
        // "#afeeee", "#db7093"
         "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF",
          "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF", "#E7EBEF"
    ];
const scaleRatio = 2.3;

const raycaster = new THREE.Raycaster(); 
const mouse = new THREE.Vector2();

let focusSprite = null; // Currently focused sprite
let initialCameraPosition = new THREE.Vector3(); // Initial position of the camera
let initialLookAtPosition = new THREE.Vector3();
let isCameraMoving = false;

let canvasWidth = 0.97 * document.getElementById("threeD").offsetWidth;
let canvasHeight = 0.97 * document.getElementById("threeD").offsetWidth / 16 * 10;

const resetButton = document.getElementById('resetButton');

// global variables

async function loadDataAndInitialize() {
  try {
    // Fetch the data from your database or API
    const publicationDB = await initialDB(db);
    // Process the data as needed
    imagePositions = JSON.parse(publicationDB);
 
    // Load atlases and initialize
    loadAtlases(init);
  } catch (error) {
    console.error('Error loading data:', error);
  }
}
// Call the function to execute the logic
loadDataAndInitialize();

// modify based on the extact atlases drawn
const atlases = [
  { url: 'https://zhiyangwang.site/fakeData/atlas-1.jpg', grid: { x: 64, y: 64 }, count: 4096 },
  { url: 'https://zhiyangwang.site/fakeData/atlas-2.jpg', grid: { x: 64, y: 64 }, count: 4096 },
  { url: 'https://zhiyangwang.site/fakeData/atlas-3.jpg', grid: { x: 64, y: 64 }, count: 3384 },
  { url: 'https://zhiyangwang.site/fakeData/atlas-4.jpg', grid: { x: 64, y: 35 }, count: 1463 }
];

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 10000);
camera.position.set(0, 35, -135);
initialLookAtPosition.set(0, 0, 0);
camera.lookAt(initialLookAtPosition);
initialCameraPosition.copy(camera.position);
const renderer = new THREE.WebGLRenderer();
renderer.domElement.classList.add("hidden");
renderer.setSize(canvasWidth, canvasHeight);
document.getElementById("threeD").appendChild(renderer.domElement);
renderer.domElement.style.borderRadius = "10px";
renderer.setClearColor( 0xE77500, 0 );


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
const loadDistance = 5;
const size = 30000;
const divisions = 1000;
// scene.add(new THREE.GridHelper(size, divisions));
// scene.add(new THREE.AxesHelper(100));


// ----------------------------------------------------------------
// ----------------------------------------------------------------


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
  // console.log(atlases)
}

// ----------------------------------------------------------------
// ----------------------------------------------------------------



// ----------------------------------------------------------------
// ----------------------------------------------------------------


function init() {
const loadingDiv = document.getElementById('loading');
const threeD = document.getElementById('threeD');
const enterButton = document.getElementById('enter');
loadingDiv.style.width = `${threeD.offsetWidth}px`;
loadingDiv.style.height = `${threeD.offsetHeight}px`;
loadingDiv.style.display = "flex";
const mapContainer = document.getElementById("mapContainer");
mapContainer.style.width = `${canvasWidth}px`;
mapContainer.style.height =`${canvasHeight}px`;
const mapDom = document.getElementById("full-map");
generateScatterPlot(map, canvasWidth, canvasHeight*0.95, mapDom);


    imagePositions.forEach(item => {
    let atlasIndex = 0;
    let imageIndex = item.figure_id;
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
    sprite.position.set(item.xPos / 10, item.yPos/100, item.zPos /10);
    sprite.scale.set(5,5,5);
    sprite.scale.divideScalar(2.5);
    sprite.className = "sprite";
    sprite.userData = {
    idx: item.figure_id,
    name: item.name,
    paper_title: item.title,
    doi: item.doi,
    server_path: item.server_path,
    atlasIndex: atlasIndex, highResLoaded: false,
    chartType: item.ChartType,
    topic: item.primary_topic_id
    };
    scene.add(sprite);
    sprites.push(sprite);
  });
  
  setupClickEvent(sprites, camera, renderer);
  // setupCameraControl(camera, renderer);
  animate();
   enterButton.addEventListener('click',()=>{
    loadingDiv.classList.remove("fade-in");
    loadingDiv.classList.add("fade-out");
    renderer.domElement.classList.remove("hidden");
    renderer.domElement.classList.add("visible");
    loadingDiv.style.pointerEvents = 'none';
    mapContainer.classList.remove("hidden");
    mapContainer.classList.add("fade-in");

  });
  
    const mapOpenButton = document.getElementById("mapButton");
  const mapCloseButton = document.getElementById("closeButton");
    mapCloseButton.addEventListener("click", function() {
    //  console.log("clicked");
    mapContainer.classList.add("hidden");
    mapContainer.classList.add("fade-out");
    mapContainer.classList.remove("fade-in");
    mapContainer.classList.add("disabled");
    mapOpenButton.style.display = 'flex';

    });

  mapOpenButton.addEventListener("click", function() {
    //  console.log("clicked");
     unSelectSprite();
    mapContainer.classList.remove("hidden");
    mapContainer.classList.remove("fade-out");
    mapContainer.classList.add("fade-in");
    mapContainer.classList.remove("disabled");
    mapOpenButton.style.display = 'none';

    });
  resetButton.addEventListener('click', () =>{
    if(isCameraMoving) return;
    moveCamera(initialCameraPosition, initialLookAtPosition);
    // console.log("rest button clicked");
     unSelectSprite();
    resetButton.style.display = 'none';
    
  });




}
// ----------------------------------------------------------------
// ----------------------------------------------------------------



// ----------------------------------------------------------------
// ----------------------------------------------------------------


function animate() {
  requestAnimationFrame(animate);

  updateTextures();
    
  renderer.render(scene, camera);

}

// ----------------------------------------------------------------
// ----------------------------------------------------------------


// ----------------------------------------------------------------
// ----------------------------------------------------------------
// Free Move Camera function 
function setupCameraControl(camera, renderer) {
    let isDragging = false;
    let dragButton = 0; // 0 for left button, 2 for right button
    let previousMousePosition = { x: 0, y: 0 };
    const rotationSpeed = 0.005; // Speed of the camera rotation
    let angularVelocityY = 0;
    let angularVelocityX = 0;
    const angularDamping = 0.95; // Increased damping for smoother motion
    let zoomVelocity = 0;
    const zoomDamping = 0.9;
    const maxY = 150;
    const minY = 0;
    const maxXZ = 200;
    const minXZ = -200;

    // Orbit-like control variables
    let spherical = new THREE.Spherical();
    let target = new THREE.Vector3();

    function checkBoundaries() {
        const position = camera.position;
        if (position.y > maxY) {
            position.y = maxY;
        }
        if (position.x > maxXZ) {
            position.x = maxXZ;
        }
        if (position.z > maxXZ) {
            position.z = maxXZ;
        }
    }

    function updateCamera() {
        if (isCameraMoving) return; // If the camera is automatically moving, stop manual update.

        // Apply damping to angular velocities
        angularVelocityY *= angularDamping;
        angularVelocityX *= angularDamping;

        // Update spherical coordinates
        spherical.setFromVector3(camera.position.clone().sub(target));
        spherical.theta -= angularVelocityY;
        spherical.phi -= angularVelocityX;
        spherical.makeSafe();

        if(isDragging) {
        // Apply updated spherical coordinates
        camera.position.setFromSpherical(spherical).add(target);
        camera.lookAt(target);
        }
        // Zoom control
        if (zoomVelocity !== 0) {
            camera.translateZ(-zoomVelocity);
            zoomVelocity *= zoomDamping;
        }

        checkBoundaries(); // Ensure camera remains within boundaries
    }

    renderer.domElement.addEventListener('mousedown', function (e) {
        if (isCameraMoving) return; // Disable manual control if the camera is automatically moving.
        if (focusSprite) {
           console.log("unselect here");
            unSelectSprite();
        }
        isDragging = true;
        dragButton = e.button;
        previousMousePosition.x = e.clientX;
        previousMousePosition.y = e.clientY;
    });

    renderer.domElement.addEventListener('mousemove', function (e) {
        if (!isDragging || isCameraMoving) return;
        if (focusSprite) {
            unSelectSprite();
        }
        const deltaX = e.clientX - previousMousePosition.x;
        const deltaY = e.clientY - previousMousePosition.y;
        angularVelocityY = deltaX * rotationSpeed;
        angularVelocityX = deltaY * rotationSpeed;
        previousMousePosition.x = e.clientX;
        previousMousePosition.y = e.clientY;
    });

    renderer.domElement.addEventListener('mouseup', function (e) {
        isDragging = false;
    });

    renderer.domElement.addEventListener('wheel', function (e) {
        if (isCameraMoving) return;
        if (focusSprite) {
            unSelectSprite();
        }
        zoomVelocity += e.deltaY * -0.02; 
    });

    renderer.domElement.addEventListener('contextmenu', function (e) {
        e.preventDefault();
    });

    renderer.setAnimationLoop(() => {
        updateCamera();
        renderer.render(scene, camera);
    });

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
// ----------------------------------------------------------------
// ----------------------------------------------------------------




// Dynamic Load the Texture based on the camera position
// ----------------------------------------------------------------
// ----------------------------------------------------------------
// ----------------------------------------------------------------


function updateTextures() {
  sprites.forEach(sprite => {
    const distance = camera.position.distanceTo(sprite.position);
    if (distance < loadDistance && !sprite.userData.highResLoaded) {
          enhanceSpriteWithText(sprite)
    }
  });
}

// ----------------------------------------------------------------
// ----------------------------------------------------------------
// ----------------------------------------------------------------
// Dynamic Load the Texture based on the camera position







// Camera Moving and label display when clciked
// ----------------------------------------------------------------
// ----------------------------------------------------------------
// ----------------------------------------------------------------

function setupClickEvent(sprites, camera, renderer) {
    renderer.domElement.addEventListener('click', event => {
        if (isCameraMoving) return;
        const rect = renderer.domElement.getBoundingClientRect();
        mouse.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
        mouse.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;

        raycaster.setFromCamera(mouse, camera);
        const intersects = raycaster.intersectObjects(sprites);

        if (intersects.length > 0) {
            const selectedSprite = intersects[0].object;
            // console.log(selectedSprite);

            // Manage focus sprite transformations
            if (focusSprite && focusSprite !== selectedSprite) {
                unSelectSprite();
            }

            // Select new sprite
            if (!focusSprite || focusSprite !== selectedSprite) {
                selectSprite(selectedSprite);
            }
        } else {
            // Reset focus and remove button if clicked outside of any sprites
            unSelectSprite();
        }
    }, false);
}

function unSelectSprite(){
    if (focusSprite) {
        // console.log("trigger unselect")
        focusSprite.scale.divideScalar(scaleRatio);
        focusSprite.position.y -= 5;
        focusSprite = null;
        const btnContainer = document.getElementById('btn-container');
        if (btnContainer) btnContainer.remove();
    }
}

function selectSprite(sprite) {
    sprite.scale.multiplyScalar(scaleRatio);
    sprite.position.y += 5;
    focusSprite = sprite;
    // console.log("selectSprite is triggered" )
    // console.log(focusSprite);
    enhanceSpriteWithText(focusSprite);
    const targetPosition = new THREE.Vector3(sprite.position.x + 2.5, sprite.position.y + 2.5, sprite.position.z +2.5);

    const lookAtPosition = new THREE.Vector3(sprite.position.x, sprite.position.y, sprite.position.z);
  
    moveCamera(targetPosition, lookAtPosition);
  
    if (!document.getElementById('btn-container')) {
        const container = document.createElement('div');
        container.id = 'btn-container';
        container.style.position = 'absolute';
        container.style.left = '50%';
        container.style.bottom = '5%';
        container.style.transform = 'translateX(-50%)';
        container.style.zIndex = 1000;
        container.style.opacity = 0; // Initial opacity for transition
        container.style.display = 'flex';
        container.style.justifyContent = 'space-between';
        container.style.alignItems = 'center';
        container.style.width = '400px'; 
        container.style.height = '60px'; 
        container.style.backgroundColor = '#ffffff'; 
        container.style.border = 'none'; // No border
        container.style.borderRadius = '12px'; // Border radius
        container.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.1), 0 8px 16px rgba(0, 0, 0, 0.1)'; // 3D Box shadow
        container.style.padding = '0 10px'; // Padding

        const createButton = (id, text) => {
            const btn = document.createElement('button');
            btn.id = id;
            btn.textContent = text;
            btn.style.padding = '10px 15px'; // Button padding
            btn.style.margin = '0 5px'; // Button margin
            btn.style.border = 'none'; // Remove border
            btn.style.borderRadius = '8px'; // Button border radius
            btn.style.backgroundColor = '#E7EBEF'; // Soft blue background color
            btn.style.color = '#000000'; // Button text color
            btn.style.fontSize = '14px'; // Button font size
            btn.style.cursor = 'pointer'; // Pointer cursor on hover
            btn.style.transition = 'background-color 0.3s, transform 0.3s'; // Transition effect
            btn.onmouseover = () => btn.style.backgroundColor = '#e2b87f'; // Hover background color
            btn.onmouseout = () => btn.style.backgroundColor = '#E7EBEF'; // Default background color
            btn.onmousedown = () => btn.style.transform = 'scale(0.95)'; // Click scale effect
            btn.onmouseup = () => btn.style.transform = 'scale(1)'; 
            return btn;
        };

        const arrowLeft = createButton('arrow-left-btn', '◄');
        const fullSizeBtn = createButton('full-size-btn', 'Full Size');
        const detailsBtn = createButton('details-btn', 'Details');
        const learnMoreBtn = createButton('learn-more-btn', 'Learn More');
        const arrowRight = createButton('arrow-right-btn', '►');

        container.appendChild(arrowLeft);
        container.appendChild(fullSizeBtn);
        container.appendChild(detailsBtn);
        container.appendChild(learnMoreBtn);
        container.appendChild(arrowRight);

        const threeDElement = document.getElementById('threeD');
        threeDElement.appendChild(container);

        // Add event listeners for the buttons
        learnMoreBtn.addEventListener('click', () => {
            window.open(focusSprite.userData.doi);
        });

        fullSizeBtn.addEventListener('click', () => {
             window.open(focusSprite.userData.server_path);
        });

        detailsBtn.addEventListener('click', () => {
            window.open(focusSprite.userData.server_path);
        });

        arrowLeft.addEventListener('click', () => {
            // console.log('arrow left clicked');
            changeSprite(focusSprite, -1);
        });

        arrowRight.addEventListener('click', () => {
            // console.log('arrow right clicked');
            changeSprite(focusSprite, 1);
        });

    }
}

function changeSprite(focusSprite, direction) {

    if (!focusSprite) return;
      const currentIndex = focusSprite.userData.idx;

    if (currentIndex == null) return; // Ensure the index exists
     unSelectSprite();
    let newIndex = currentIndex + direction;
    // console.log("triggered new idx", newIndex);

    let newSprite = sprites.find(sprite => sprite.userData.idx === newIndex);
    // console.log("find from change Sprite: ");
    // console.log(newSprite);
      while (!newSprite) {
          newIndex += direction;
          newSprite = sprites.find(sprite => sprite.userData.idx === newIndex);
      }

if (newSprite) {
    selectSprite(newSprite);
} else {
    // console.log("No correct sprite found.");
}

}



function enhanceSpriteWithText(focusSprite) {
  const loader = new THREE.TextureLoader();
  loader.setCrossOrigin('anonymous');  // Ensure CORS compliance !!!important
  loader.load(`${focusSprite.userData.server_path}`, texture => {
    const canvas = document.createElement('canvas');
    canvas.width = 1024;  // Higher resolution for better clarity
    canvas.height = 1024;  // Maintain the 4:3 ratio
    const context = canvas.getContext('2d');
    const image = new Image();
    image.crossOrigin = 'anonymous';

    image.onload = () => {
      // Clear the canvas and fill it with a white background
      context.clearRect(0, 0, canvas.width, canvas.height);
      context.fillStyle = 'white';
      context.fillRect(0, 0, canvas.width, canvas.height);

      const aspectRatio = image.width / image.height;
      let drawWidth, drawHeight;

      // Determine the drawing width and height while maintaining the aspect ratio
      if (canvas.width / canvas.height < aspectRatio) {
          drawWidth = canvas.width;
          drawHeight = canvas.width / aspectRatio;
      } else {
          drawWidth = canvas.height * aspectRatio;
          drawHeight = canvas.height;
      }

      // Calculate the position to center the image
      const x = (canvas.width - drawWidth) / 2;
      const y = (canvas.height * 0.80 - drawHeight) / 2;

      // Draw the image
      context.drawImage(image, x, y, drawWidth, drawHeight);

      // Set up the text area
      context.fillStyle = "#ffffff";

      context.fillRect(0, canvas.height * 0.80, canvas.width, canvas.height * 0.20);

      context.fillStyle = "#000";  // Black text for visibility
      context.font = "48px Arial";  // Larger, clear font
      context.textBaseline = "top";
      context.textAlign = "left";
      const padding = 5;  // Adjust padding for better spacing

      // Display text with better spacing
      const textBaseLine = canvas.height * 0.80 + padding;
      context.fillText(`Chart Type: ${focusSprite.userData.name}`, padding, textBaseLine+20);
      context.font = "32px Arial";
      context.fillText(`Field: ${getObjectById(topicsArray, focusSprite.userData.topic).field}`, padding, textBaseLine + 80);
      context.fillText(`SubField: ${getObjectById(topicsArray, focusSprite.userData.topic).subfield}`, padding, textBaseLine + 130);

      // Convert canvas to texture
      const canvasTexture = new THREE.CanvasTexture(canvas);
      focusSprite.material.map = canvasTexture;
      focusSprite.material.needsUpdate = true;
      focusSprite.userData.highResLoaded = true;
    };

    image.src = `${focusSprite.userData.server_path}`;

    // Make the canvas clickable
    canvas.addEventListener('click', () => {
      alert(`Clicked on: ${focusSprite.userData.name}`);
    });
  });
}



// Camera Moving trigger and label display when clciked the sprites
// ----------------------------------------------------------------
// ----------------------------------------------------------------
// ----------------------------------------------------------------





// Camera Moving functions
// ----------------------------------------------------------------
// ----------------------------------------------------------------
// ----------------------------------------------------------------

function create3DVector(x,y,z){
   const vector =  new THREE.Vector3(x, y, z);
   return vector
}
function moveCamera(target, lookAtPosition) {
    if (isCameraMoving) return; // Prevents multiple movements at the same time
    isCameraMoving = true;

    const epsilon = 0.01; // Distance threshold for stopping
    const baseDuration = 1000; // Base duration for the animation in milliseconds
    const startPosition = camera.position.clone();
    const startQuaternion = camera.quaternion.clone();
    const targetQuaternion = new THREE.Quaternion().setFromRotationMatrix(
        new THREE.Matrix4().lookAt(target, lookAtPosition, camera.up)
    );
    const totalDistance = startPosition.distanceTo(target);
    const duration = baseDuration + (totalDistance * 5); // Dynamic duration based on distance
    const startTime = performance.now();

    // Easing function for smooth transitions
    function easeInOutQuad(t) {
        return t < 0.5 ? 2 * t * t : -1 + (4 - 2 * t) * t;
    }

    // Update the camera's position and orientation
    function updateCameraPosition() {
        const now = performance.now();
        const elapsed = now - startTime;
        const t = Math.min(elapsed / duration, 1); // Ensure t is within [0, 1]
        const distance = camera.position.distanceTo(target);

        if (distance > epsilon) {
            const easedT = easeInOutQuad(t);
            camera.position.lerpVectors(startPosition, target, easedT);
            camera.quaternion.slerpQuaternions(startQuaternion, targetQuaternion, easedT);
            // console.log("I am moving!");
            requestAnimationFrame(updateCameraPosition);
        } else {
            // Snap to final position and orientation
            camera.position.copy(target);
            camera.quaternion.copy(targetQuaternion);
            // console.log("last move!");
            camera.lookAt(lookAtPosition);

          
            
            // Show or hide reset button based on target position
            resetButton.style.display = (target !== initialCameraPosition) ? "flex" : "none";

            // Ensure button container is visible
            const btnContainer = document.getElementById('btn-container');
            if (btnContainer) {
                btnContainer.style.opacity = 1;
            }
            isCameraMoving = false;
         
        }
    }

    updateCameraPosition();
}

// ----------------------------------------------------------------
// ----------------------------------------------------------------
// ----------------------------------------------------------------



// generate map functions
// ----------------------------------------------------------------
// ----------------------------------------------------------------
// ----------------------------------------------------------------

async function countMap(db) {
    try {
        // console.log("start");
        const results = await db.query(`
            SELECT 
               figure_id,
               int_value,
               xPos,
               yPos,
               zPos,
            FROM 
                base.figure_property
            ORDER BY 
                figure_id;
        `);

        const resultsArray = results.toArray();
        // console.log("end");
        return resultsArray;
    } catch (error) {
        console.error("Error executing query:", error);
        throw error;
    }
}
const map = await countMap(db);

// Create a color scale using d3.scaleOrdinal
const colorScale = d3.scaleOrdinal()
    .domain(d3.range(0, 45)) // Assuming int_value ranges from 0 to 44
    .range(colors);

function generateScatterPlot(data, w, h, parentDom) {
    // Check for any potential issues in data
    if (data.some(d => d.xPos === undefined || d.zPos === undefined || isNaN(d.int_value))) {
        console.error("Data contains undefined or NaN values", data);
        return;
    }

    // Plot configuration
    const plot = Plot.plot({
        width: w,
        height: h,
        marks: [
            Plot.dot(data, {
                x: d => -d.xPos / 10,
                y: d => d.zPos / 10,
                fill: d => colorScale(d.int_value),
          
                fillOpacity: 0.9,
                r: 4,
                // Add an attribute for int_value
                title: d => `int_value: ${d.int_value}` // Tooltip, not for attribute
            }),
            Plot.image(chartPos, {
            x: d => -d.x,
            y: d => d.z,
            src: "https://github.com/JimmyXwtx/3dVis/blob/master/src/data/grey-box.png?raw=true",
            width: 120,
            title: "Name"
          }),
            Plot.text(chartPos, {
                x: d => -d.x,
                y: d => d.z,
                text: d => d.label,
                textAnchor: "middle",
                fontSize: "17px",
                dy: -5,
                fill: "black",
  
                // Add an attribute for int_value
                title: d => `int_value: ${d.int_value}` // Tooltip, not for attribute
            })
        ],
        x: { axis: null },
        y: { axis: null },
        facet: { axis: null },
        style: {
            border: "none"
        },
        id: "scatter-plot"
    });
    plot.style.position = "absolute";
    plot.style.scale = "93%";
    plot.style.top = "6%";
    parentDom.appendChild(plot);

    // Add custom attributes to the dots and text elements
    const svg = parentDom.querySelector('svg');
    if (svg) {
        // Add attributes to dots and set up event listeners
        svg.querySelectorAll('circle').forEach((circle, index) => {
            const intValue = data[index].int_value;
            circle.setAttribute('data-int-value', intValue);
            circle.addEventListener('click', (event) => {
                
                const index = Number(circle.getAttribute('data-int-value'));
                if(index){
                const targetGroup = getObjectByIdx(chartPos, index);
                const targetPosition = create3DVector(targetGroup.x, 2, targetGroup.y);
                const lookAtPosition = create3DVector(0, 0, 0);

                // console.log('Clicked dot int_value:', targetPosition);
                moveCamera(targetPosition, lookAtPosition);
     
                const mapContainer = document.getElementById("mapContainer");
                const mapOpenButton = document.getElementById("mapButton");
                mapContainer.classList.add("hidden");
                mapContainer.classList.add("fade-out");
                mapContainer.classList.remove("fade-in");
                mapContainer.classList.add("disabled");
                mapOpenButton.style.display = 'flex';
               
                }
             
              
                event.stopPropagation(); // Prevents the event from bubbling up
            });
        });

        // Add attributes to text elements and set up event listeners
        svg.querySelectorAll('text').forEach((text, index) => {
            const intValue = data[index].int_value;
            text.setAttribute('data-int-value', intValue);
            text.addEventListener('click', (event) => {
                // console.log('Clicked text int_value:', text.getAttribute('data-int-value'));
                const index = Number(text.getAttribute('data-int-value'));
                if(index){
                const targetGroup = getObjectByIdx(chartPos, index);
                const targetPosition = create3DVector(targetGroup.x, 2, targetGroup.y);
                const lookAtPosition = create3DVector(0, 0, 0);

                // console.log('Clicked dot int_value:', targetPosition);
                moveCamera(targetPosition, lookAtPosition);
     
                const mapContainer = document.getElementById("mapContainer");
                const mapOpenButton = document.getElementById("mapButton");
                mapContainer.classList.add("hidden");
                mapContainer.classList.add("fade-out");
                mapContainer.classList.remove("fade-in");
                mapContainer.classList.add("disabled");
                mapOpenButton.style.display = 'flex';
               
                }
             
                event.stopPropagation(); // Prevents the event from bubbling up

                
            });
        });
    }
}




// ----------------------------------------------------------------
// ----------------------------------------------------------------
// ----------------------------------------------------------------
// generate map functions



```
<div  id="loading" class="fade-in">
<div class="loadingContent">
<div class="contentTitle">Vis Sieve - 3D Exploration</div>
<div class="contentInfo">Vis-sieve is a project that aims to analyze the use of visualizations in academia. Here is a 3D Space for you to navigate to explore the visualizations used in academia.</div>
<div class="contentInstruction">
<div class="instructionDetails">
  <ul>
    <li><strong>Map Navigation:</strong> Click on each type of visualization to view that group of images.</li>
    <li><strong>3D Space Interaction:</strong> Use the mouse to move around and scroll to zoom in/out.</li>
    <li><strong>Viewing Details:</strong> Click on an interesting image to see more details.</li>
    <li><strong>Image Navigation:</strong> After selecting an image, use the navigation space bar below to view the full image, see details, or access related papers. You can also use the arrow keys (◄ ►) to navigate.</li>
  </ul>
</div>
</div>

<div class="enterButton"><button id="enter">Let's Go</button>
</div>
</div>
</div>



<div class = "card" id="threeD">
<button id='mapButton' class="button-55" class="fade-in" >Map</button>
<button id='resetButton' class="button-55" class="fade-in" >Go Back</button>
<div id="mapContainer" class="hidden">
  <span id="closeButton" class="close-button">&#10005;</span>
  <span id="map-title"> Which Chart Type You Like To Explore?</span>
  <div class="full-content" id="full-map">
  </div>
</div>


</div>







