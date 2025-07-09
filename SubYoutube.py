import os
from youtube_transcript_api import YouTubeTranscriptApi
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.documents import Document

def get_youtube_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([d['text'] for d in transcript_list])
        return transcript
    except Exception as e:
        return str(e)

def main():
    """
    This script takes a YouTube video URL, extracts its transcript,
    and generates a summary using LangChain and Gemini 2.5 Pro.
    """
    print("hi arash")
    api_key = input("Please enter your Google API key: ")
    if not api_key:
        print("Error: API key cannot be empty.")
        return
    
    os.environ["GOOGLE_API_KEY"] = api_key
    print("hi arash 2")
    
    youtube_url = input("Please enter the YouTube video URL: ")
    if "=" in youtube_url:
        video_id = youtube_url.split("=")[1]
    else:
        print("Invalid YouTube URL format.")
        return

    your_subtitle_text = get_youtube_transcript(video_id)

    if "Could not retrieve a transcript for the video" in your_subtitle_text:
        print(your_subtitle_text)
        return
    elif not your_subtitle_text.strip():
        print("Error: Transcript is empty.")
        return

    try:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=100
        )
        chunks = splitter.split_text(your_subtitle_text)
        print(f"Number of chunks: {len(chunks)}")  # Debugging

        # Convert chunks to Document objects
        documents = [Document(page_content=chunk) for chunk in chunks]

        # Use gemini-2.5-pro model
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0)
        chain = load_summarize_chain(llm, chain_type="map_reduce")
        
        # Use invoke with the list of Document objects
        summary = chain.invoke(documents)
        print("\nSummary:")
        # Check if summary is a dictionary and extract output_text
        if isinstance(summary, dict) and 'output_text' in summary:
            print(summary['output_text'])
        else:
            print(summary)
    except Exception as e:
        print(f"Error during summarization: {str(e)}")

if __name__ == "__main__":
    main()