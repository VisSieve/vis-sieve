---
title: db-Demo
toc: false
theme: "cotton"
---
<style>
.heatmapContainer{
    overflow-x: scroll;
    height: 800px;

}
.heatmapDom{
    width: 120vw !important;
}

</style>
# DB Demo
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
const paperTopics = [
  "Artificial Intelligence in Healthcare",
  "Climate Change Mitigation Strategies",
  "Renewable Energy Technologies",
  "Cybersecurity Threats and Solutions",
  "The Future of Quantum Computing",
  "The Impact of Social Media on Mental Health",
  "Nanotechnology Applications",
  "Blockchain Technology and Cryptocurrencies",
  "Genetic Engineering and CRISPR",
  "Sustainable Agriculture Practices",
  "The Role of Education in Economic Development",
  "Autonomous Vehicles and Transportation",
  "Space Exploration and Colonization",
  "The Ethics of Artificial Intelligence",
  "Renewable Energy Storage Solutions",
  "Global Water Scarcity and Solutions",
  "Advances in Biomedical Engineering",
  "The Future of Work in the Age of Automation",
  "The Psychology of Consumer Behavior",
  "Environmental Impact of Plastic Waste",
  "Smart Cities and Urban Planning",
  "The Role of Big Data in Business",
  "The Evolution of E-commerce",
  "Climate Change and Its Impact on Biodiversity",
  "Digital Privacy and Data Protection",
  "Virtual Reality in Education",
  "The Future of 3D Printing",
  "Mental Health in the Workplace",
  "The Impact of Globalization on Local Cultures",
  "Sustainable Development Goals",
  "The Role of Government in Regulating Technology",
  "Cyberbullying and Online Harassment",
  "The Future of Renewable Energy",
  "Human Rights in the Digital Age",
  "The Impact of Artificial Intelligence on Employment",
  "The Future of Personalized Medicine",
  "Environmental Policies and Their Effectiveness",
  "The Role of Social Enterprises",
  "Technological Innovations in Agriculture",
  "The Impact of Climate Change on Human Health",
  "The Future of Digital Marketing",
  "Renewable Energy Policy and Implementation",
  "The Ethics of Genetic Modification",
  "The Role of Women in STEM",
  "The Impact of Technology on Education",
  "The Future of Urban Mobility",
  "The Role of Artificial Intelligence in Cybersecurity",
  "The Impact of Environmental Regulations on Industry",
  "The Future of Smart Home Technology",
  "The Role of Artificial Intelligence in Climate Research"
];
// Declare labels

// import libs
import * as d3 from "npm:d3";
import * as duckdb from "npm:@duckdb/duckdb-wasm";
// import libs

// import data
const db = await DuckDBClient.of({base: FileAttachment("/data/publications_princeton_int_3.db")});
// import data

// data extraction
const publicationDB = await inititalDB(db)
const distributionJson = await countDistribution(db);
const crossDistributionJson = await countDistributionAcrossTable(db);
const chartPos = await countPos(db);
// data extraction

// ----------------------------------------------------------------
// ----------------------------------------------------------------
// Database handling functions


// Function to initialize the database and fetch the publication data
async function inititalDB(db) {
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
                p.topics,
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

// Function to count the distribution of (int_value, string_value) pairs
async function countDistribution(db) {
    try {
        const results = await db.query(`
            SELECT 
                int_value, 
                string_value, 
                COUNT(*) as count 
            FROM 
                base.figure_property 
            GROUP BY 
                int_value, 
                string_value
            ORDER BY 
                int_value, 
                string_value;
        `);
        
        const resultsArray = results.toArray();
        return resultsArray; // Return array directly instead of JSON string !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    } catch (error) {
        console.error("Error executing query:", error);
    }
}

// cross table,  not handling the 0 data
async function countDistributionAcrossTableEasy(db) {
    try {
        const results = await db.query(`
            SELECT 
                fp.int_value, 
                p.topics, 
                COUNT(*) as count 
            FROM 
                base.figure f
                JOIN base.figure_property fp ON f.id = fp.figure_id 
                JOIN base.paper p ON f.paper_id = p.id
            GROUP BY 
                fp.int_value, 
                p.topics
            ORDER BY 
                fp.int_value, 
                p.topics;
        `);
        
        const resultsArray = results.toArray();
        JSON.stringify(resultsArray);
        return resultsArray; // Return array directly instead of JSON string
    } catch (error) {
        console.error("Error executing query:", error);
    }
}
// cross table,  not handling the 0 data



// complex code that handling the results to fill 0
async function countDistributionAcrossTable(db) {
    try {
        // Execute the query
        const results = await db.query(`
            SELECT 
                fp.int_value, 
                p.topics, 
                COUNT(*) as count 
            FROM 
                base.figure f
                JOIN base.figure_property fp ON f.id = fp.figure_id 
                JOIN base.paper p ON f.paper_id = p.id
            GROUP BY 
                fp.int_value, 
                p.topics
            ORDER BY 
                fp.int_value, 
                p.topics;
        `);
        
        // Convert the results to an array
        const resultsArray = results.toArray();

        // Determine unique int_values and topics
        const intValues = [...new Set(resultsArray.map(row => row.int_value))];
        const topics = [...new Set(resultsArray.map(row => row.topics))];

        // Create a map for easy lookup
        const resultMap = new Map();
        resultsArray.forEach(row => {
            resultMap.set(`${row.int_value}-${row.topics}`, row.count);
        });

        // Fill in missing combinations with 0
        const completeResultsArray = [];
        intValues.forEach(intValue => {
            topics.forEach(topic => {
                const key = `${intValue}-${topic}`;
                completeResultsArray.push({
                    int_value: intValue,
                    topics: topic,
                    count: resultMap.get(key) || 0
                });
            });
        });

        // Return the complete array
        return completeResultsArray;
    } catch (error) {
        console.error("Error executing query:", error);
    }
}


// count the avg position

async function countPos(db) {
    try {
        const results = await db.query(`
            SELECT 
                int_value, 
                AVG(figure_property.xPos) as xPos, 
                AVG(figure_property.yPos) as yPos, 
                AVG(figure_property.zPos) as zPos, 
                COUNT(*) as count 
            FROM 
                base.figure_property 
            GROUP BY 
                int_value
            ORDER BY 
                int_value;
        `);

        const resultsArray = results.toArray();
        const output = {};

        resultsArray.forEach(row => {
            output[row.int_value] = {
                xPos: row.xPos,
                yPos: row.yPos,
                zPos: row.zPos,
                count: row.count
            };
        });

        return output;
    } catch (error) {
        console.error("Error executing query:", error);
    }
}

// count avg position


// Database handling
// ----------------------------------------------------------------
// ----------------------------------------------------------------




// ----------------------------------------------------------------
// ----------------------------------------------------------------

// Function to draw the heatmap with crosshair and interactivity
function heatMap(data, { width }) {
    const plot = Plot.plot({
        title: "Distribution of Vizs",
        width,
        height: 2000,
        marginLeft: 100,
        // marginRight: 60,
        x: { axis: "top", label: "Chart Type", type: "band", tickFormat: i => visualizationTypes[i] },
        y: { axis: "left", label: "String Value", type: "band", tickFormat: i => paperTopics[i] },
        color: {
            type: "linear",
            legend: true,
            domain: d3.extent(data, d => d.count),
            range: ["white", "#39db7f"]
        },
        marks: [
            Plot.cell(data, {
                x: "int_value",
                y: "topics",
                fill: "count",
                // title: d => `Chart Type: ${visualizationTypes[d.int_value]}\nTopics: ${paperTopics[d.topics]}\nCount: ${d.count}`
            }),
            Plot.text(data, {
                x: "int_value",
                y: "topics",
                text: d => (d.count !== null && d.count !== undefined) ? d.count.toString() : '0',
                fill: "darkblue",
                dy: 5
            }),
        ]
    });

    // Append the plot to the body (or another container)
    d3.select("body").append(() => plot);

    // Select all rect elements and add event listeners with explicit data binding
    d3.select(plot).selectAll("rect")
        .each(function(d, i) {
            // Bind the full data object to each rect element
            d3.select(this).datum(data[i]);
        })
        .on("mouseover", function(event, d) {
        // d3.select(this).attr("stroke", "black").attr("stroke-width", 2);
        
        // Create a tooltip div if it doesn't exist
        let tooltip = d3.select("body").selectAll(".tooltip").data([null]);
        tooltip = tooltip.enter()
                         .append("div")
                         .attr("class", "tooltip")
                         .style("position", "absolute")
                         .style("background-color", "white")
                         .style("border", "2px solid black")
                         .style("border-radius", "8px")
                         .style("padding", "10px")
                         .style("font-size", "16px")
                         .style("box-shadow", "0 0 10px rgba(0, 0, 0, 0.5)")
                         .style("pointer-events", "none")
                         .merge(tooltip);

        tooltip.style("left", (event.pageX + 5) + "px")
               .style("top", (event.pageY - 28) + "px")
               .style("opacity", 1)
               .html(`Chart Type: ${visualizationTypes[d.int_value]}<br>Topic: ${paperTopics[d.topics]}`);

        // console.log('Mouseover data:', event.currentTarget); // Diagnostic log
    })
    .on("mouseout", function(event, d) {
        d3.select(this).attr("stroke", null).attr("stroke-width", null);

        // Hide tooltip
        d3.select("body").selectAll(".tooltip")
            .style("opacity", 0);
    })
        .on("click", function(event, d) {
            console.log(`Position: ${chartPos[d.int_value].xPos}`);
        });

    return plot;
}
// Function to draw the heatmap with crosshair and interactivity

// ----------------------------------------------------------------
// ----------------------------------------------------------------



```

<div Class = "heatmapContainer card">
<div class="heatmapDom">
${resize((width) => heatMap(crossDistributionJson,{width}))}
</div>
</div>