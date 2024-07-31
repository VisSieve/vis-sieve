# Use of 3.js in Observable Framework

1. ## npm/ install three.js - [official doc](https://threejs.org/docs/index.html#manual/en/introduction/Installation)
```
npm install --save three
```
2. ## code in the Observable Framework Markdown.

### use the css code to style your html dom element (must at the beginning of the code)
```
<!-- use css to style your html dom element -->
<style>

#3d{
    display: flex;
    justify-content: center; /* Center items horizontally */
    align-items: center; /* Center items vertically */
}

</style>
```

### import 3.js (must import the lib before any js coding)
- note: you should use 'npm:three' instead of 'three' in observable framework


```js

import * as THREE from 'npm:three';

```

### same way to code three.js 

```js

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );

const renderer = new THREE.WebGLRenderer();
renderer.setSize(0.97*document.getElementById("3d").offsetWidth, 0.97*document.getElementById("3d").offsetWidth/16*9 );
renderer.setAnimationLoop( animate );

// Add the canvas to the DOM, MAKE SURE the canvas is rendered to the exact dom element we want.
document.getElementById("3d").appendChild( renderer.domElement);

var geometry = new THREE.IcosahedronGeometry();
var loader = new THREE.TextureLoader();
// Specify the path to an image
var url = 'https://s3.amazonaws.com/duhaime/blog/tsne-webgl/assets/cat.jpg';
// Load an image file into a MeshLambert material
var material = new THREE.MeshLambertMaterial({
  map: loader.load(url)
});
const cube = new THREE.Mesh( geometry, material );
scene.add( cube );
const light = new THREE.AmbientLight( 0xffffff); // soft white light
scene.add( light );
camera.position.z = 5;



function animate() {

	cube.rotation.x += 0.01;
	cube.rotation.y += 0.01;
	renderer.render( scene, camera );

}
// Specify the size of the canvas




```
### create a dom element in this markdown  
   - Give it an id so we can find it in the js code



```
<div class = "card" id="3d">

</div>

```