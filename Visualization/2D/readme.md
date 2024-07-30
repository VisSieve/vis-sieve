# Visualizzation Code Overview

This the documentation for visualization database that facilitates searching, sorting, and other operations for users to navigate through. 

## Key Features

- 2 filters for searching visualizations, Topics and Chart Type
- Image clickable for bigger high-resolusion view with detals(Paper, Domain, etc.)


# Code Requirements

- [Observable Framework]("https://observablehq.com/framework/getting-started") (with importing in DuckDB)
- [Well Structured Database](https://github.com/VisSieve/main/blob/Zhiyang-Doc/Visualization/demo-project/src/dbStructure.md)
- Thanks to PhotoSwipe main CSS by Dmytro Semenov | photoswipe.com

## Database Code Structure

- Visualization Types Definition

    - List of various visualization types is defined and stored in an array named `visualizationTypes`.

- Import Libraries

    - The `DuckDB` library is imported to handle database operations.

- Initialize Database Connection

    - DuckDB client instance is created and connected to a local database file `(/data/publications_princeton.db)`.

- Database Query Function: `initialDB`

    - Function initialDB is defined to query `publication` and `figure` data from the database, joining tables and selecting columns.

- The function returns the query results as an `array`.

- Database Query Function: `countTopics`

    - Function `countTopics` is defined to query topic data from the database, selecting columns.
    - The function returns the query results as an `array`.

- Fetch and Process Data

    - The `countTopics` function is called to get the topics array.
    - The `initialDB` function is called to get the publication data array (database).

- Get Object By ID

    - Utility function `getObjectById` is defined to find an object in an array by its ID.

- Gallery Initialization

    - The `gallery` function is defined to initialize and manage the gallery view.

    - Elements are selected from the DOM.

- Set Modal Size

    - The modal size is adjusted to match the gallery container size if the main Observable element is loaded.

- Create Gallery Items

    - Function `createGalleryItems` is defined to create and append gallery items to the gallery element.
    - Each gallery item is linked to a publication, with click events to open a modal displaying the publication image and details.
    - The background color of each gallery item is set based on the `ChartType` using the `setLinkBackground` function.

- Lazy Loading Images

    - Function `initializeLazyLoading` is defined to lazy load images as they enter the viewport using the [Intersection Observer API](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API).
    
- Create Filters

    - Function `createFilters` is defined to populate filter dropdowns based on unique `primary_topic_id` and `ChartType` values from the data.
    - The filter dropdowns are populated with options corresponding to the visualization types and topics.

- Filter Images

    - Function `filterImages` is defined to filter gallery items based on selected filter values.
    If the `label1` filter is selected, the gallery items are also sorted by `ChartType`.

- Clear Filters

    - The `clearFiltersBtn` click event resets the filters and shows all gallery items.

- Modal Close Events

    - The modal is closed when the close button (`span`) is clicked or when clicking outside the modal.

- Gallery Function Execution

    - The `gallery` function is called to execute the gallery initialization process.
