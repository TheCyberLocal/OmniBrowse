# OmniBrowser Development Guide

## Feature List

### Navigation Bar

#### Top Level (Browser Tabs)
- **Browser Tabs**: Tabs for each browser in the following order:
  - Omni
  - Google
  - Bing
  - Brave
  - Yahoo
  - DuckDuckGo
  - Ask
  - Aol
- **Tab Highlighting**: The currently selected browser tab is highlighted.
- **URL Change**: Each tab changes the main URL of the OmniBrowser site to reflect the selected browser (e.g., `/chrome`, `/edge`).

#### Bottom Level
- **Search Bar**: A search input bar that spans the center of the screen.
- **Light/Dark Mode Toggle**: A toggle button on the far right to switch between light and dark modes.

### Search Functionality
- **Search Initiation**: When a search is initiated, all browser tabs load the search results in the background.
- **Omni Tab**: Aggregates the top result from each browser.

### Result Display
- **Result Container**:
  - An image on the right side, displaying the first image inside the website link (like a preview of content).
  - The web page name (link) on the top left.
  - A snippet of page content below the link.
  - Later the snippet will be loaded as a content summary.
  - Selecting a result will open the website in a new tab.
  - Selecting "extended summary" will generate a new and longer description.

### Pagination
- **Infinite Scrolling**:
  - Each browser tab supports infinite scrolling, loading results in chunks.
  - The Omni tab continues scrolling indefinitely, fetching the next set of results from all browsers in order when necessary.

### User Experience Enhancements
- **Persistent State**:
  - Save the state of the application (active tab, search queries, tab URLs) in local storage so that it persists across sessions.

### Light/Dark Mode
- **Theme Toggle**:
  - A toggle button on the far right of the navigation bar to switch between light and dark (default) modes.

### Performance and Optimization
- **Background Loading**:
  - Optimize tab switching by preloading search results in the background.
- **Lazy Loading**:
  - Implement lazy loading for search results to improve performance, especially when dealing with a large number of results.
