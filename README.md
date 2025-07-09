YouTube Transcript Summarizer
This Python script extracts the transcript of a YouTube video and generates a concise summary using LangChain and Google's Gemini 2.5 Pro model. It processes large transcripts by splitting them into chunks and summarizing them with a map-reduce approach.
Features

Fetches transcripts from YouTube videos using the youtube_transcript_api.
Splits transcripts into manageable chunks with LangChain's RecursiveCharacterTextSplitter.
Summarizes the transcript using Google's gemini-2.5-pro model via LangChain's map_reduce chain.
Handles errors for invalid URLs, unavailable transcripts, or API issues.

Prerequisites

Python 3.10 or higher
A Google Cloud API key with access to the Gemini 2.5 Pro model (available through Google AI Studio or Google Cloud Console).
A YouTube video URL with an available transcript (manual or auto-generated captions).

Installation


Install Dependencies:Install the required Python packages using pip:
pip install youtube-transcript-api langchain langchain-google-genai langchain-core


Set Up Google API Key:

Obtain a Google API key with access to the Gemini 2.5 Pro model.
Store the API key securely (do not hardcode it in the script). You can use an environment variable or a .env file with python-dotenv (optional but recommended):pip install python-dotenv

Create a .env file in the project root:GOOGLE_API_KEY=your-api-key-here





Usage

Run the Script:python SubYoutube.py


Provide Inputs:
Enter your Google API key when prompted (or load it from a .env file if configured).
Enter a YouTube video URL (e.g., https://www.youtube.com/watch?v=dQw4w9WgXcQ).


View Output:
The script fetches the transcript, splits it into chunks, and generates a summary.
The summary is printed to the console.



Example
$ python SubYoutube.py
Please enter your Google API key: [your-api-key]
Please enter the YouTube video URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Number of chunks: 8
Summary:
[Generated summary of the video transcript]

Code Overview

Transcript Extraction: Uses youtube_transcript_api to fetch the video transcript.
Text Splitting: Splits the transcript into chunks of 1000 characters with 100-character overlap using LangChain’s RecursiveCharacterTextSplitter.
Summarization: Processes chunks with a map_reduce chain, summarizing each chunk with gemini-2.5-pro and combining results into a final summary.
Error Handling: Checks for invalid URLs, empty transcripts, and API errors.

Notes

API Key Security: Never hardcode your Google API key in the script or share it publicly. Use environment variables or a .env file.
Transcript Availability: The YouTube video must have captions (manual or auto-generated) for the script to work.
Model Access: Ensure your API key has access to gemini-2.5-pro. If unavailable, try gemini-2.5-pro-preview or check available models in Google AI Studio.
Dependencies: Keep langchain, langchain-google-genai, and langchain-core updated:pip install --upgrade langchain langchain-google-genai langchain-core youtube-transcript-api



Troubleshooting

Error: 404 models/gemini-2.5-pro is not found:
Verify your API key has access to gemini-2.5-pro in Google Cloud Console.
Try gemini-2.5-pro-preview by updating the model name in the script.


Error: 'str' object has no attribute 'page_content':
Ensure you’re using the latest version of the script, which converts chunks to Document objects.


Empty Transcript: Confirm the YouTube video has captions enabled.
API Rate Limits: Check your Google Cloud Console for quota limits if you encounter rate-related errors.

Contributing
Contributions are welcome! Please open an issue or submit a pull request with improvements or bug fixes.
License
This project is licensed under the MIT License. See the LICENSE file for details.
