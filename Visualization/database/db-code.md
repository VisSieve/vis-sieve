---
title: Visualization Database
toc: false
---


<style>

/*! PhotoSwipe main CSS by Dmytro Semenov | photoswipe.com */

.pswp {
  --pswp-bg: #000;
  --pswp-placeholder-bg: #222;
  

  --pswp-root-z-index: 100000;
  
  --pswp-preloader-color: rgba(79, 79, 79, 0.4);
  --pswp-preloader-color-secondary: rgba(255, 255, 255, 0.9);
  
  /* defined via js:
  --pswp-transition-duration: 333ms; */
  
  --pswp-icon-color: #fff;
  --pswp-icon-color-secondary: #4f4f4f;
  --pswp-icon-stroke-color: #4f4f4f;
  --pswp-icon-stroke-width: 2px;

  --pswp-error-text-color: var(--pswp-icon-color);
}


/*
	Styles for basic PhotoSwipe (pswp) functionality (sliding area, open/close transitions)
*/

.pswp {
	position: fixed;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	z-index: var(--pswp-root-z-index);
	display: none;
	touch-action: none;
	outline: 0;
	opacity: 0.003;
	contain: layout style size;
	-webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}

/* Prevents focus outline on the root element,
  (it may be focused initially) */
.pswp:focus {
  outline: 0;
}

.pswp * {
  box-sizing: border-box;
}

.pswp img {
  max-width: none;
}

.pswp--open {
	display: block;
}

.pswp,
.pswp__bg {
	transform: translateZ(0);
	will-change: opacity;
}

.pswp__bg {
  opacity: 0.005;
	background: var(--pswp-bg);
}

.pswp,
.pswp__scroll-wrap {
	overflow: hidden;
}

.pswp__scroll-wrap,
.pswp__bg,
.pswp__container,
.pswp__item,
.pswp__content,
.pswp__img,
.pswp__zoom-wrap {
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
}

.pswp__img,
.pswp__zoom-wrap {
	width: auto;
	height: auto;
}

.pswp--click-to-zoom.pswp--zoom-allowed .pswp__img {
	cursor: -webkit-zoom-in;
	cursor: -moz-zoom-in;
	cursor: zoom-in;
}

.pswp--click-to-zoom.pswp--zoomed-in .pswp__img {
	cursor: move;
	cursor: -webkit-grab;
	cursor: -moz-grab;
	cursor: grab;
}

.pswp--click-to-zoom.pswp--zoomed-in .pswp__img:active {
  cursor: -webkit-grabbing;
  cursor: -moz-grabbing;
  cursor: grabbing;
}

/* :active to override grabbing cursor */
.pswp--no-mouse-drag.pswp--zoomed-in .pswp__img,
.pswp--no-mouse-drag.pswp--zoomed-in .pswp__img:active,
.pswp__img {
	cursor: -webkit-zoom-out;
	cursor: -moz-zoom-out;
	cursor: zoom-out;
}


/* Prevent selection and tap highlights */
.pswp__container,
.pswp__img,
.pswp__button,
.pswp__counter {
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

.pswp__item {
	/* z-index for fade transition */
	z-index: 1;
	overflow: hidden;
}

.pswp__hidden {
	display: none !important;
}

/* Allow to click through pswp__content element, but not its children */
.pswp__content {
  pointer-events: none;
}
.pswp__content > * {
  pointer-events: auto;
}


/*

  PhotoSwipe UI

*/

/*
	Error message appears when image is not loaded
	(JS option errorMsg controls markup)
*/
.pswp__error-msg-container {
  display: grid;
}
.pswp__error-msg {
	margin: auto;
	font-size: 1em;
	line-height: 1;
	color: var(--pswp-error-text-color);
}

/*
class pswp__hide-on-close is applied to elements that
should hide (for example fade out) when PhotoSwipe is closed
and show (for example fade in) when PhotoSwipe is opened
 */
.pswp .pswp__hide-on-close {
	opacity: 0.005;
	will-change: opacity;
	transition: opacity var(--pswp-transition-duration) cubic-bezier(0.4, 0, 0.22, 1);
	z-index: 10; /* always overlap slide content */
	pointer-events: none; /* hidden elements should not be clickable */
}

/* class pswp--ui-visible is added when opening or closing transition starts */
.pswp--ui-visible .pswp__hide-on-close {
	opacity: 1;
	pointer-events: auto;
}

/* <button> styles, including css reset */
.pswp__button {
	position: relative;
	display: block;
	width: 50px;
	height: 60px;
	padding: 0;
	margin: 0;
	overflow: hidden;
	cursor: pointer;
	background: none;
	border: 0;
	box-shadow: none;
	opacity: 0.85;
	-webkit-appearance: none;
	-webkit-touch-callout: none;
}

.pswp__button:hover,
.pswp__button:active,
.pswp__button:focus {
  transition: none;
  padding: 0;
  background: none;
  border: 0;
  box-shadow: none;
  opacity: 1;
}

.pswp__button:disabled {
  opacity: 0.3;
  cursor: auto;
}

.pswp__icn {
  fill: var(--pswp-icon-color);
  color: var(--pswp-icon-color-secondary);
}

.pswp__icn {
  position: absolute;
  top: 14px;
  left: 9px;
  width: 32px;
  height: 32px;
  overflow: hidden;
  pointer-events: none;
}

.pswp__icn-shadow {
  stroke: var(--pswp-icon-stroke-color);
  stroke-width: var(--pswp-icon-stroke-width);
  fill: none;
}

.pswp__icn:focus {
	outline: 0;
}

/*
	div element that matches size of large image,
	large image loads on top of it,
	used when msrc is not provided
*/
div.pswp__img--placeholder,
.pswp__img--with-bg {
	background: var(--pswp-placeholder-bg);
}

.pswp__top-bar {
	position: absolute;
	left: 0;
	top: 0;
	width: 100%;
	height: 60px;
	display: flex;
  flex-direction: row;
  justify-content: flex-end;
	z-index: 10;

	/* allow events to pass through top bar itself */
	pointer-events: none !important;
}
.pswp__top-bar > * {
  pointer-events: auto;
  /* this makes transition significantly more smooth,
     even though inner elements are not animated */
  will-change: opacity;
}


/*

  Close button

*/
.pswp__button--close {
  margin-right: 6px;
}


/*

  Arrow buttons

*/
.pswp__button--arrow {
  position: absolute;
  top: 0;
  width: 75px;
  height: 100px;
  top: 50%;
  margin-top: -50px;
}

.pswp__button--arrow:disabled {
  display: none;
  cursor: default;
}

.pswp__button--arrow .pswp__icn {
  top: 50%;
  margin-top: -30px;
  width: 60px;
  height: 60px;
  background: none;
  border-radius: 0;
}

.pswp--one-slide .pswp__button--arrow {
  display: none;
}

/* hide arrows on touch screens */
.pswp--touch .pswp__button--arrow {
  visibility: hidden;
}

/* show arrows only after mouse was used */
.pswp--has_mouse .pswp__button--arrow {
  visibility: visible;
}

.pswp__button--arrow--prev {
  right: auto;
  left: 0px;
}

.pswp__button--arrow--next {
  right: 0px;
}
.pswp__button--arrow--next .pswp__icn {
  left: auto;
  right: 14px;
  /* flip horizontally */
  transform: scale(-1, 1);
}

/*

  Zoom button

*/
.pswp__button--zoom {
  display: none;
}

.pswp--zoom-allowed .pswp__button--zoom {
  display: block;
}

/* "+" => "-" */
.pswp--zoomed-in .pswp__zoom-icn-bar-v {
  display: none;
}


/*

  Loading indicator

*/
.pswp__preloader {
  position: relative;
  overflow: hidden;
  width: 50px;
  height: 60px;
  margin-right: auto;
}

.pswp__preloader .pswp__icn {
  opacity: 0;
  transition: opacity 0.2s linear;
  animation: pswp-clockwise 600ms linear infinite;
}

.pswp__preloader--active .pswp__icn {
  opacity: 0.85;
}

@keyframes pswp-clockwise {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}


/*

  "1 of 10" counter

*/
.pswp__counter {
  height: 30px;
  margin-top: 15px;
  margin-inline-start: 20px;
  font-size: 14px;
  line-height: 30px;
  color: var(--pswp-icon-color);
  text-shadow: 1px 1px 3px var(--pswp-icon-color-secondary);
  opacity: 0.85;
}

.pswp--one-slide .pswp__counter {
  display: none;
}
.gallery-container{
    margin: 0;
    padding: 0;
    background-color: transparent;
    font-family: 'Arial', sans-serif;
    height: 85vh;
    max-height: 900px;
    overflow: scroll;
    border: none;
}
.gallery-container:before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: #f7f7f7;
  opacity: 0.1;
  background-image:  linear-gradient(#626484 1.8px, transparent 1.8px), 
                     linear-gradient(90deg, #626484 1.8px, transparent 1.8px), 
                     linear-gradient(#626484 0.9px, transparent 0.9px), 
                     linear-gradient(90deg, #626484 0.9px, #e5e5f7 0.9px);
  background-size: 45px 45px, 45px 45px, 9px 9px, 9px 9px;
  background-position: -1.8px -1.8px, -1.8px -1.8px, -0.9px -0.9px, -0.9px -0.9px;
  border-radius: 10px; /* Match border radius with parent */
  z-index: -1; /* Ensure it is behind the content */
}
.my-gallery {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 0.8fr));
    gap: 10px;
    padding: 10px;
}
.my-gallery a {
    display: flex;
    flex-direction: column;
    justify-content: flex-end; /* Align items to bottom but ensure flex properties apply correctly */
    align-items: center; /* Center align the items */
    border: 1px solid #ccc;
    border-radius: 8px;
    overflow: hidden;
    position: relative;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    height: 240px; /* Fixed height for uniformity */
}
.my-gallery a:hover {
    box-shadow: 0 8px 16px rgba(0,0,0,0.2);
    scale: 1.02;
    transition: all 0.5s;
}
.my-gallery img {
    width: 80%; /* Limit width but ensure center alignment */
    height: auto; /* Keep the height proportional */
    margin: auto; /* Center the image horizontally */
    align-self: center; /* Center align the image specifically */
}


.description {
    width: 100%;
    text-align: center;
    padding: 5px;
    background-color: #fff;
    border-top: 1px solid #ccc;
}
#filter-bar {

    background-color: #f1f3f4; 
    text-align: center;
    display: flex;
    align-items: center; /* Ensures all elements are vertically aligned in the center */
    justify-content: space-around;
    flex-wrap: nowrap; /* Prevents wrapping to ensure horizontal alignment */
    position: sticky;
    top: 0;
    z-index: 100;
    border-radius: 12px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.05); /* Updated shadow for a more subtle effect */
    border: 1px solid #d0d7de; /* Lighter border color for a modern look */
}

.filter-select {
    padding: 8px 12px;
    margin: 0 10px; /* Uniform margin for alignment */
    cursor: pointer;
    border: none;
    border-radius: 6px;
    appearance: none;
    background-color: #ffffff;
    background-image: url('data:image/svg+xml;utf8,<svg fill="%23333" height="20" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg"><path d="M7 10l5 5 5-5z"/></svg>'); /* Smaller and darker arrow for a sleek look */
    background-repeat: no-repeat;
    background-position: right 10px center;
    background-size: 20px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    transition: background-color 0.3s, box-shadow 0.3s;
}

.filter-select:hover {
    background-color: #e6e6e6; /* Tech-inspired hover color */
    box-shadow: 0 2px 4px rgba(0,0,0,0.15);
}

button#clear-filters {
    padding: 8px 20px;
    margin: 0 10px;
    cursor: pointer;
    border: none;
    border-radius: 6px;
    background-color: #007bff; /* Bright blue for a techy button */
    color: white;
    font-weight: bold; /* Makes the text stand out more */
    transition: background-color 0.3s;
}

button#clear-filters:hover {
    background-color: #0056b3; /* Deeper blue on hover */
}

.modal {
    display: none;
    position: absolute;
    z-index: 1001;
    left: 0;
    top: 0;
    border-radius: 10px;
    /* width: 100%;
    height: 100%; */
    overflow: auto;
    align-items: center;
    justify-content: center;
    background-color: rgb(0,0,0,0.9);

}
.modal-img-caption {
    /* background-color: grey; */
    height: 90%;
    width: 90%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    padding: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    border-radius: 10px;
}

.modal-content {
    display: block;
    max-width: 90%;
    max-height: 70%;
    width: auto;
    height: auto;
    margin-bottom: 10px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -o-user-select: none;
  user-select: none;
}


.caption {
    max-width: 80%;
    /* max-width: 700px; */
    height: auto;
    white-space: initial;
    text-align: center;
    color: #333;
    font-size: 18px;
    padding: 10px;
    background-color: #f9f9f9;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.close {
    position: absolute;
    top: 15px;
    right: 35px;
    color: #f1f1f1;
    font-size: 40px;
    font-weight: bold;
    cursor: pointer;
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


</style>



```js
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

import * as duckdb from "npm:@duckdb/duckdb-wasm";
// import libs

// import data
const db = await DuckDBClient.of({base: FileAttachment("/data/publications_princeton.db")});
// import data

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
    
        return resultsArray;
        // return JSON.stringify(resultsArray, null, 2);
        
        // publicationDB = JSON.stringify(resultsArray, null, 2);
    } catch (error) {
        console.error("Error executing query:", error);
    }
}

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
        `);

        const resultsArray = results.toArray();
        return resultsArray;
    } catch (error) {
        console.error("Error executing query:", error);
        throw error;
    }
}

const topicsArray = await countTopics(db);

const getObjectById = (data,id) => {
    return data.find(item => item.id === id);
};

const database = await initialDB(db);



let traffic = [];



function gallery() {
    const observableMain = document.getElementById('observablehq-main');
    const galleryElement = document.querySelector('.my-gallery');
    const galleryContainer = document.querySelector('.gallery-container');
    const label1Select = document.getElementById('label1-filter');
    const label2Select = document.getElementById('label2-filter');
    const clearFiltersBtn = document.getElementById('clear-filters');
    const modal = document.getElementById('myModal');
    const modalImg = document.getElementById('img01');
    const captionText = document.querySelector('.caption');
    const span = document.getElementsByClassName("close")[0];
   
   
    if(observableMain){
    console.log(observableMain.offsetWidth);
    modal.style.width = `${galleryContainer.offsetWidth}px`;
    modal.style.height = `${galleryContainer.offsetHeight}px`;

    }else{
    console.log("not loaded");
    }

    const publicationDB = database; 
    createGalleryItems(publicationDB);
    createFilters(publicationDB, label1Select, 'primary_topic_id');
    createFilters(publicationDB, label2Select, 'ChartType');


    function createGalleryItems(items) {
        items.forEach(item => {
            const link = document.createElement('a');
            link.href = '#';
            link.classList.add('gallery-item');
            link.dataset.primary_topic_id = item.primary_topic_id; // Updated field name
            link.dataset.ChartType = item.ChartType; // Field name unchanged
            link.innerHTML = `
                <img data-src="${item.server_path}" alt="Photo" class="lazy-load">
                <div class="description"> ${item.title}</div>
            `; // Updated text to use new field names
            setLinkBackground(link, item.ChartType); // Set background based on ChartType
            galleryElement.appendChild(link);

            link.onclick = function (e) {
                e.preventDefault();
                modal.style.display = "flex";
                modalImg.src = item.server_path;
                captionText.innerHTML = `Chart: ${visualizationTypes[item.ChartType]} <br> ${item.Something}<br> <a target="_blank" href="${item.doi}">${item.title}</a>`;
            };
        });
        initializeLazyLoading();
    }
function setLinkBackground(linkElement, label) {
    const colors = [
        "#e6194B", "#3cb44b", "#ffe119", "#4363d8", "#f58231", "#911eb4", "#46f0f0", "#f032e6",
        "#bcf60c", "#fabebe", "#008080", "#e6beff", "#9a6324", "#fffac8", "#800000", "#aaffc3",
        "#808000", "#ffd8b1", "#000075", "#808080", "#fa8072", "#4682b4", "#6a5acd", "#20b2aa",
        "#9400d3", "#ff6347", "#40e0d0", "#ee82ee", "#dda0dd", "#b0c4de", "#ff7f50", "#6495ed",
        "#deb887", "#5f9ea0", "#7fff00", "#d2691e", "#ff69b4", "#1e90ff", "#228b22", "#ffc0cb",
        "#8a2be2", "#a52a2a", "#8b008b", "#b8860b", "#66cdaa", "#ff4500", "#daa520", "#98fb98",
        "#afeeee", "#db7093"
    ];

    if (label >= 0 && label <= 49) {
        // Convert Hex color to RGBA and apply 20% opacity
        let color = colors[label];
        let rgba = `rgba(${parseInt(color.slice(1, 3), 16)}, ${parseInt(color.slice(3, 5), 16)}, ${parseInt(color.slice(5, 7), 16)}, 0.2)`;
        linkElement.style.backgroundColor = rgba;
    } else {
        linkElement.style.backgroundColor = 'transparent';
    }
}


    function initializeLazyLoading() {
        const lazyImages = document.querySelectorAll('.lazy-load');
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const image = entry.target;
                    image.src = image.dataset.src;
                    observer.unobserve(image);
                }
            });
        });

        lazyImages.forEach(image => {
            imageObserver.observe(image);
        });
    }

    function createFilters(data, selectElement, labelType) {
        const labelSet = new Set(data.map(item => item[labelType]));
        labelSet.forEach(label => {
            const option = document.createElement('option');
            option.value = label;
            if(labelType == 'ChartType'){
            option.text = visualizationTypes[label];
            }else{
          const retrievedObject = getObjectById(topicsArray, label);
          if (retrievedObject) {
              const objectString = JSON.stringify(retrievedObject);
              option.text = retrievedObject.name;
          } else {
              console.log("No object found for label:", label);
              option.text = "Default Name";  
          }


              
            }
            
            selectElement.appendChild(option);
        });
        selectElement.onchange = () => filterImages(selectElement.value, labelType);
    }
 function filterImages(label, type) {
    const links = Array.from(galleryElement.querySelectorAll('a')); // Convert NodeList to Array for sorting
    // Filter operation
    links.forEach(link => {
        const itemLabel = link.dataset[type];
        link.style.display = itemLabel === label || label === "All" ? 'flex' : 'none';
    });

    // Sort operation based on label_2 if the filter is for label_1
    if (type === 'label_1') {
        links.sort((a, b) => {
            const label2A = a.dataset.ChartType;
            const label2B = b.dataset.ChartType;
            if (label2A < label2B) return -1;
            if (label2A > label2B) return 1;
            return 0;
        });

        // Re-append links to galleryElement in the new order
        links.forEach(link => {
            if (link.style.display === 'flex') { // Only re-append if the item is visible
                galleryElement.appendChild(link);
            }
        });
    }
}



    clearFiltersBtn.onclick = function() {
        document.querySelectorAll('a').forEach(a => {
            a.style.display = 'flex'; // Ensure flex is restored to keep alignment
        });
        label1Select.selectedIndex = 0;
        label2Select.selectedIndex = 0;
    };

    span.onclick = function() {
        modal.style.display = "none";
    };

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    };
}

gallery();

```



<div class="gallery-container card">
<div id="filter-bar">
<div id="topic"> Topic: <select id="label1-filter" class="filter-select"><option>All</option></select></div>
<div id="chart"> Chart: <select id="label2-filter" class="filter-select"><option>All</option></select></div>
 
<button id="clear-filters">Clear Filters</button>

</div>

<div class="my-gallery" itemscope itemtype="http://schema.org/ImageGallery"></div>

<div id="myModal" class="modal">
<div class="modal-img-caption">
    <span class="close">&times;</span>
    <img class="modal-content" id="img01">
    <div class="caption"></div>
</div>
</div>
</div>
