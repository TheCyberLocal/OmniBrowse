# OmniBrowser Development Guide

## Feature List

### Navigation Bar

#### Top Level (Browser Tabs)
- **Browser Tabs**: Tabs for each browser in the following order:
  - Omni
  - Chrome
  - Edge
  - Brave
  - Firefox
  - DuckDuckGo
  - Ask
  - Aol
- **Tab Highlighting**: The currently selected browser tab is highlighted.
- **URL Change**: Each tab changes the main URL of the OmniBrowser site to reflect the selected browser (e.g., `/chrome`, `/edge`).

#### Bottom Level
- **Search Bar**: A search input bar that spans the center of the screen.
- **Clear Button**: Located on the far left to reset the search and tabs, returning to the Omni tab.
- **Light/Dark Mode Toggle**: A toggle button on the far right to switch between light and dark modes.

### Search Functionality
- **Search Initiation**: When a search is initiated, all browser tabs load the search results in the background.
- **Omni Tab**: Aggregates the top result from each browser.

### Result Display
- **Result Container**:
  - An image on the left side, displaying the first image inside the website link (like a preview of content).
  - The web page name (link) on the top right.
  - A snippet of page content below the link.

### Pagination
- **Infinite Scrolling**:
  - Each browser tab supports infinite scrolling, loading results in chunks of 10.
  - The Omni tab continues scrolling indefinitely, fetching the next set of results from all browsers in order.

### URL Handling within Browser Tabs
- **Tab-Specific URL Bar**:
  - Each tab displays a URL bar directly underneath the navigation bar and above the results, showing the URL of the current page within that tab.
  - Navigation within a tab (clicking on links in the results) updates this tab-specific URL bar but does not change the main OmniBrowser URL.
  - Each tab's URL bar includes left and right arrows to navigate through its individual URL history.
  - Submitting a search in the Omni search bar resets the histories of all individual browser tabs.

### User Experience Enhancements
- **Persistent State**:
  - Save the state of the application (active tab, search queries, tab URLs) in local storage so that it persists across sessions.

### Light/Dark Mode
- **Theme Toggle**:
  - A toggle button on the far right of the navigation bar to switch between light and dark modes.

### Performance and Optimization
- **Background Loading**:
  - Optimize tab switching by preloading search results in the background.
- **Lazy Loading**:
  - Implement lazy loading for search results to improve performance, especially when dealing with a large number of results.

### Backend Filing Structure
OmniBrowse/
├── backend/
│   ├── config/
│   │   └── config.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── search_controller.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── search_result.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── search_routes.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── search_service.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── fetch_utils.py
│   ├── app.py
│   └── requirements.txt
└── README.md
