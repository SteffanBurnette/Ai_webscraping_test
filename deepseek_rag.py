import os
from langchain.vectorstores import chroma
from lanchain_core.prompts import ChainPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from lanchain_core.runnables import RunnablePassthrough

from lanchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import ChatOllama #Allows m to interact with the deepseek model

llm = ChatOllama(model="deepseek-r1:1.5b", temperature = 0)
llm_json_mode = ChatOllama(model="deepseek-r1:1.5b", temperature = 0, format = "json")

#Will summarize the webscrapped data
#msg = llm.invoke("Summarize the text: " + result.markdown)

# Docling imports
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions, TesseractCliOcrOptions
from docling.document_converter import DocumentConverter, PdfFormatOption, WordFormatOption, SimplePipeline

# LangChain imports
from langchain_community.document_loaders import UnstructuredMarkdownLoader, WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

#A helper fuunction that will detect document formats
def get_document_format(file_path) -> InputFormat:
    """Determine the document format based on file extension"""
    try:
        file_path = str(file_path)
        extension = os.path.splitext(file_path)[1].lower()

        format_map = {
            '.pdf': InputFormat.PDF,
            '.docx': InputFormat.DOCX,
            '.doc': InputFormat.DOCX,
            '.pptx': InputFormat.PPTX,
            '.html': InputFormat.HTML,
            '.htm': InputFormat.HTML
        }
        return format_map.get(extension, None)
    except:
        return "Error in get_document_format: {str(e)}"

#The document conversion function
def convert_document_to_markdown(doc_path) -> str:
    """Convert document to markdown using simplified pipeline"""
    try:
        # Convert to absolute path string
        input_path = os.path.abspath(str(doc_path))
        print(f"Converting document: {doc_path}")

        # Create temporary directory for processing
        with tempfile.TemporaryDirectory() as temp_dir:
            # Copy input file to temp directory
            temp_input = os.path.join(temp_dir, os.path.basename(input_path))
            shutil.copy2(input_path, temp_input)

            # Configure pipeline options
            pipeline_options = PdfPipelineOptions()
            pipeline_options.do_ocr = False  # Disable OCR temporarily
            pipeline_options.do_table_structure = True

            # Create converter with minimal options
            converter = DocumentConverter(
                allowed_formats=[
                    InputFormat.PDF,
                    InputFormat.DOCX,
                    InputFormat.HTML,
                    InputFormat.PPTX,
                ],
                format_options={
                    InputFormat.PDF: PdfFormatOption(
                        pipeline_options=pipeline_options,
                    ),
                    InputFormat.DOCX: WordFormatOption(
                        pipeline_cls=SimplePipeline
                    )
                }
            )

            # Convert document
            print("Starting conversion...")
            conv_result = converter.convert(temp_input)

            if not conv_result or not conv_result.document:
                raise ValueError(f"Failed to convert document: {doc_path}")

            # Export to markdown
            print("Exporting to markdown...")
            md = conv_result.document.export_to_markdown()

            # Create output path
            output_dir = os.path.dirname(input_path)
            base_name = os.path.splitext(os.path.basename(input_path))[0]
            md_path = os.path.join(output_dir, f"{base_name}_converted.md")

            # Write markdown file
            print(f"Writing markdown to: {base_name}_converted.md")
            with open(md_path, "w", encoding="utf-8") as fp:
                fp.write(md)

            return md_path
    except:
        return f"Error converting document: {doc_path}"