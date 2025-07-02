---
title: File search
hide:
    - navigation
    # - toc
    # - footer
---


# File search

## About

To index text inside files (.txt, .sql, .excel, .pptx, .docx, .pdf...) in a flexible way, for:

- Document classification.
- File and folder content search, e.g. finding old code, names of sheets in excel files, columns used in database, attachement in .msg files, comments written in .pptx files.
- Preparing text corpus in a selective manner (e.g. extract only the top headings of powerpoint slides...) for LLM training


## Structure

File search is a scan of major file types to give control over text corpus usage for further analysis.


## Demo

- `example\fs_build.py`: Demo to build a text corpus of major file types.
- `example\fs_query.py`: Functions to explore the text corpus.
- `example\fs_classification.py`: Demo on parsing .sql code from the corpus combined with database information schema to classify and organize .sql codebase. 

