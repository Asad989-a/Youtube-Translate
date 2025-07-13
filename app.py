import gradio as gr
from deep_translator import GoogleTranslator
import re
from saved_transcripts import saved_transcripts  # ✅ Import 100 video transcripts

# ✅ Extract video ID from YouTube URL
def extract_video_id(url):
    regex = r"(?:v=|\/)([0-9A-Za-z_-]{11})"
    match = re.search(regex, url)
    return match.group(1) if match else url.strip()

# ✅ Agent 1: Summarizer (Simulated)
def summarize_youtube(video_url):
    try:
        video_id = extract_video_id(video_url)

        if video_id not in saved_transcripts:
            return "❌ Transcript not available for this video.", "", ""

        summary = saved_transcripts[video_id]
        translation = GoogleTranslator(source='auto', target='es').translate(summary)
        video_embed_link = f"https://www.youtube.com/embed/{video_id}"
        return summary, translation, video_embed_link
    except Exception as e:
        return f"❌ Error: {str(e)}", "", ""

# ✅ Master Agent Workflow with Embedded YouTube Preview
def run_agents(url):
    summary, translation, embed = summarize_youtube(url)
    if embed:
        video_html = f'''
        <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;">
            <iframe src="{embed}" style="position:absolute;top:0;left:0;width:100%;height:100%;" 
                    frameborder="0" allowfullscreen></iframe>
        </div>
        '''
    else:
        video_html = ""
    return summary, translation, video_html

# ✅ Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("## 🎥 AI Agents: YouTube Summary + Spanish Translator + Youtube Video")
    gr.Markdown("🔗 Enter a YouTube video URL to simulate AI agent collaboration.")

    input_url = gr.Textbox(label="Paste YouTube Link")
    summary_output = gr.Textbox(label="🧠 English Summary")
    translation_output = gr.Textbox(label="🌍 Spanish Translation")
    video_output = gr.HTML()

    run_btn = gr.Button("🔍 Run Agents")
    run_btn.click(fn=run_agents, inputs=input_url, outputs=[summary_output, translation_output, video_output])

demo.launch()