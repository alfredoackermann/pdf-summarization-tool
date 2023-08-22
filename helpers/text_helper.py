from io import StringIO
import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')

def split_text(text, chunk_size=5000):
  '''
  Splits the given text into chunks of approximately the specified chunk size.

  Args:
  text (str): The text to split.

  chunk_size (int): The desired size of each chunk (in characters).

  Returns:
  List[str]: A list of chunks, each of approximately the specified chunk size.
  '''

  chunks = []
  current_chunk = StringIO()
  current_size = 0
  sentences = sent_tokenize(text)
  for sentence in sentences:
    sentence_size = len(sentence)
    if sentence_size > chunk_size:
      while sentence_size > chunk_size:
        chunk = sentence[:chunk_size]
        chunks.append(chunk)
        sentence = sentence[chunk_size:]
        sentence_size -= chunk_size
        current_chunk = StringIO()
        current_size = 0
    if current_size + sentence_size < chunk_size:
      current_chunk.write(sentence)
      current_size += sentence_size
    else:
      chunks.append(current_chunk.getvalue())
      current_chunk = StringIO()
      current_chunk.write(sentence)
      current_size = sentence_size
  if current_chunk:
    chunks.append(current_chunk.getvalue())
  return chunks