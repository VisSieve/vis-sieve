---
title: Image Gallery
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
    background-color: #f0f2f5;
    font-family: 'Arial', sans-serif;
    height: 85vh;
    max-height: 900px;
    overflow: scroll;
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
    padding: 10px;
    background-color: #eee;
    text-align: center;
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    position: sticky;
    top:0;
    z-index: 100;
}

.filter-select {
    padding: 5px 10px;
    margin: 5px;
    cursor: pointer;
    border: 2px solid #aaa; /* Improved style for select boxes */
    border-radius: 5px;
}

.modal {
    display: none;
    position: absolute;
    z-index: 1001;
    left: 0;
    top: 2.5%;
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

#loading{
    display: none;
    position: absolute;
    /* margin: auto; */
    justify-content: center; /* Center items horizontally */
    align-items: center; /* Center items vertically */
    background-color: transparent;
    z-index: 100001;
}

.loadingContent {
  position: relative;
  /* top: 1.8%; */
  width: 100%;
  height: 100%;
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

</style>

# Gallery-Test

```js

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
    const loadingDiv = document.getElementById('loading');
    const enterButton = document.getElementById('enter');
    loadingDiv.style.width = `${galleryContainer.offsetWidth}px`;
    loadingDiv.style.height = `${galleryContainer.offsetHeight}px`;
    loadingDiv.style.display = "flex";
   
    if(observableMain){
    console.log(observableMain.offsetWidth);
    modal.style.width = `${galleryContainer.offsetWidth}px`;
    modal.style.height = `${galleryContainer.offsetHeight}px`;

    }else{
    console.log("not loaded");
    }

    fetch('https://zhiyangwang.site/figure-data/figure-label.json')
        .then(response => response.json())
        .then(data => {
            createGalleryItems(data);
            createFilters(data, label1Select, 'label_1');
            createFilters(data, label2Select, 'label_2');
            enterFunc();
            // Initialize an object to hold the counts of each label_01 and label_02 combination
            const combinationCounts = {};

            // data.forEach(item => {
            // const key = `${item.label_1}-${item.label_2}`;
            // if (!combinationCounts[key]) {
            // combinationCounts[key] = { label_1: item.label_1, label_2: item.label_2, count: 0 };
            // }
            // combinationCounts[key].count++;
            // });

            // // Convert the combinationCounts object into an array
            // traffic = Object.values(combinationCounts);
            // console.log(JSON.stringify(traffic));
        })
        .catch(error => console.error('Error fetching data:', error));

   function enterFunc() {
    enterButton.addEventListener('click',()=>{
    loadingDiv.classList.remove("fade-in");
    loadingDiv.classList.add("fade-out");
    // loadingDiv.style.display = 'none';
    galleryContainer.classList.remove("hidden");
    galleryContainer.classList.add("visible");
    loadingDiv.style.pointerEvents = 'none';
    });
   }
    function createGalleryItems(items) {
        items.forEach(item => {
            const link = document.createElement('a');
            link.href = '#';
            link.classList.add('gallery-item');
            link.dataset.label_1 = item.label_1; // Store label_1
            link.dataset.label_2 = item.label_2; // Store label_2
            link.innerHTML = `
                <img data-src="${item.server_path}" alt="Photo" class="lazy-load">
                <div class="description">Index: ${item.idx}, ${item.label_1}, ${item.label_2}</div>
            `;
            setLinkBackground(link, item.label_2); // Set background based on label_2
            galleryElement.appendChild(link);

            link.onclick = function (e) {
                e.preventDefault();
                modal.style.display = "flex";
                modalImg.src = item.server_path;
                captionText.innerHTML = `Index: ${item.idx}, ${item.label_1}, ${item.label_2}`;
            };
        });
        initializeLazyLoading();
    }


   function setLinkBackground(linkElement, label) {
    if (label >= '00000' && label <= '00040') {
        // Calculate a unique hue from 0 to 360 for each label
        let hue = ((parseInt(label.substring(3)) / 41) * 360).toFixed(0);
        linkElement.style.backgroundColor = `hsl(${hue}, 75%, 60%)`;
    } else {
        switch (label) {
            case 'TypeB':
                linkElement.style.backgroundColor = '#ddffdd';
                break;
            case 'TypeC':
                linkElement.style.backgroundColor = '#ddddff';
                break;
            default:
                linkElement.style.backgroundColor = 'transparent';
        }
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
            option.text = label;
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
            const label2A = a.dataset.label_2;
            const label2B = b.dataset.label_2;
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

function heatMap(data,{ width }) {
  return Plot.plot({
    title: "HeatMap",
    width,
    height: 600,
    marginLeft: 120,
    padding: 0,
    x: { label: null, type: "band" },
    y: { label: null, type: "band" }, // Set y-axis type to "band"
    color: { legend: true, zero: true },
    marks: [
      Plot.cell(
        data,
        Plot.group(
          { fill: "median" },
          { x: "label_1", y: "label_2", fill: "count", inset: 0.5, sort: { y: "fill" }, tip: true, }
        )
      ),
      Plot.crosshair(data, {x: "label_1", y: "label_2"})
   
    ]
  });
}


gallery();

```

```js
const distribution = FileAttachment("data/distribution.json").json({typed: true});
```

<div  id="loading" class="fade-in">

<div class="loadingContent">
<div class="contentTitle">Viz Sieves - Gallery-Test</div>
<div class="contentInfo">this is an Info</div>
<div class="contentInstruction">this is an instruction</div>
<div class="enterButton"><button id="enter">Let's Go</button>
</div>
</div>
</div>

<div class="gallery-container card hidden">
<div id="filter-bar">
    <select id="label1-filter" class="filter-select"><option>All</option></select>
    <select id="label2-filter" class="filter-select"><option>All</option></select>
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
<div class="card heatmapDom">
${resize((width) => heatMap(distribution,{width}))}
</div>