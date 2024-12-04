Spotify Playlists Analysis Script
-----------------------------------------

This script analyzes your Spotify playlists, retrieves the most played songs from multiple playlists, and creates a "Top 100 Songs" playlist. It counts the number of times each song has been played and includes the play count in the final playlist.

### Features

-   Extracts top 100 songs played across multiple playlists.
-   Counts the number of times each song has been played.
-   Creates a new playlist, "DJ 2024 Top 100 Songs," with the most played songs.
-   Outputs additional statistics (e.g., total duration, top artists, top genres).

* * * * *

### **Prerequisites**

1.  **Python 3.x**: Ensure you have Python 3 installed on your machine.
2.  **Spotify Developer Account**: You will need a Spotify Developer account to access the API.
3.  **Spotify API Credentials**: You need a **Client ID** and **Client Secret** from your Spotify Developer account.

* * * * *

### **Step 1: Set Up a Spotify Developer Account**

1.  **Create a Spotify Developer Account**:

    -   Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
    -   Log in with your Spotify account or create one if you don't have one.
    -   Click on **Create an App** to generate your **Client ID** and **Client Secret**.
2.  **Create a New Application**:

    -   Fill in the app details (you can give it any name).
    -   Accept the terms and conditions.
    -   Click **Create** to get your **Client ID** and **Client Secret**.

* * * * *

### **Step 2: Set Up Spotify API Credentials**

1.  **Install Dependencies**:

    -   Ensure that you have Python and pip installed on your system.
    -   Install the `spotipy` library, which is used to interact with the Spotify API.

    ```bash
    pip install spotipy
    ```

2.  **Set Up Environment Variables**:

    -   The script uses environment variables to store your **Client ID** and **Client Secret** securely. Set them up in your terminal.
    -   In your terminal, run the following commands (replace `your_client_id` and `your_client_secret` with your actual credentials):

    **For Linux/macOS**:

    ```bash
    export SPOTIPY_CLIENT_ID='your_client_id'
    export SPOTIPY_CLIENT_SECRET='your_client_secret'
    export SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'
    ```

    **For Windows** (Command Prompt):
    
    ```bash
    set SPOTIPY_CLIENT_ID=your_client_id
    set SPOTIPY_CLIENT_SECRET=your_client_secret
    set SPOTIPY_REDIRECT_URI=http://localhost:8888/callback
    ```

3.  **Verify Environment Variables**:

    -   You can check that the environment variables are set correctly by running:

        ```bash
        echo $SPOTIPY_CLIENT_ID   # Linux/macOS
        echo %SPOTIPY_CLIENT_ID%   # Windows
    If they return your Client ID, the setup is correct.

* * * * *

### **Step 3: Prepare the Playlist URIs File**

1.  **Format the Playlist URIs**:
    -   Create a `.txt` file (e.g., `playlists.txt`) with one Spotify playlist URI per line.
    -   Example:

        ```makefile
        spotify:playlist:37i9dQZF1DXcBWIGoYBM5M
        spotify:playlist:5FJXhjdILmRA2z5bvz4nzf
    -   The script will read the URIs from this file to gather data on the playlists.

* * * * *

### **Step 4: Running the Script**

1.  **Save the Script**:

    -   Save the provided Python script as `dj_analysis_with_counts.py`.
2.  **Run the Script**:

    -   In the terminal, navigate to the folder where you saved the script.
    -   Run the script:

        ```terminal
        python3 dj_analysis_with_counts.py
        ```

3.  **Provide the URIs File**:

    -   When prompted, provide the file path to your `.txt` file containing the playlist URIs.

    Example:

    ```css
    Enter the path to the file containing playlist URIs: playlists.txt
    ```

4.  **Output**:

    -   The script will analyze the playlists and generate the "DJ Bro's 2024 Top 100 Songs" playlist.
    -   It will display statistics such as the total duration, top artists, and genres.
    -   The new playlist will appear in your Spotify account with the top 100 songs.

* * * * *

### **Notes**

-   The script uses the **Spotipy** library to interact with the Spotify API, allowing you to fetch playlist data and create new playlists.
-   If you encounter any issues related to API rate limits or authentication, refer to the [Spotify Developer Documentation](https://developer.spotify.com/documentation/web-api/).

* * * * *

### **Troubleshooting**

-   **Authentication Issues**:

    -   Make sure your Spotify Developer credentials are correctly set in the terminal.
    -   Ensure that your redirect URI matches the one you set in the Spotify Developer Dashboard.
-   **File Not Found**:

    -   If the `.txt` file is not found, double-check the file path you provide when running the script.

* * * * *

### **License**

This project is licensed under the MIT License - see the LICENSE file for details.