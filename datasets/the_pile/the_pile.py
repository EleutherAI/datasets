"""The Pile: An 800GB Dataset of Diverse Text for Language Modeling"""

from __future__ import absolute_import, division, print_function

import json
import os

import datasets

import io
import zstandard

def _readjsonlzstdfiles(fs):
    for f in fs:
        with open(f, 'rb') as fh:
            cctx = zstandard.ZstdDecompressor()
            reader = io.BufferedReader(cctx.stream_reader(fh))
            for line in reader:
                yield json.loads(line)

_CITATION = """\
@article{pile,
  title={The {P}ile: An 800GB Dataset of Diverse Text for Language Modeling},
  author={Gao, Leo and Biderman, Stella and Black, Sid and Golding, Laurence and Hoppe, Travis and Foster, Charles and Phang, Jason and He, Horace and Thite, Anish and Nabeshima, Noa and Presser, Shawn and Leahy, Connor},
  journal={arXiv preprint},
  year={2020}
}
"""
# todo: update with arxiv number

_DESCRIPTION = """\
 The Pile: An 800GB Dataset of Diverse Text for Language Modeling
 The Pile is a 825 GiB diverse, open source language modelling data set that consists of 22 smaller, high-quality datasets combined together.
"""


class ThePileConfig(datasets.BuilderConfig):
    """BuilderConfig for ThePile."""

    def __init__(self, **kwargs):
        """BuilderConfig for ThePile.
        Args:
          **kwargs: keyword arguments forwarded to super.
        """
        super(ThePileConfig, self).__init__(**kwargs)


class ThePileDataset(datasets.GeneratorBasedBuilder):
    """The Pile: An 800GB Dataset of Diverse Text for Language Modeling."""

    _N_TRAIN_FILES = 30

    _TRAIN_FILES = [os.path.join('train', '%02d.jsonl.zst' % i) for i in range(_N_TRAIN_FILES)]
    _VAL_FILE = "val.jsonl.zst"
    _TEST_FILE = "test.jsonl.zst"
    _TRAIN_DL_URLS = ['https://the-eye.eu/public/AI/pile/train/%02d.jsonl.zst' % i for i in range(_N_TRAIN_FILES)]
    _VAL_DL_URLS =  ['https://the-eye.eu/public/AI/pile/val.jsonl.zst']
    _TEST_DL_URLS = ['https://the-eye.eu/public/AI/pile/test.jsonl.zst']
        

    BUILDER_CONFIGS = [
        ThePileConfig(
            name="ThePile",
            version=datasets.Version("1.0.0"),
            description="The Pile: An 800GB Dataset of Diverse Text for Language Modeling",
        ),
    ]

    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(
                {
                    "text": datasets.Value("string"),
                    "set": datasets.features.ClassLabel(names=['Pile-CC', 'PubMed Central', 'Books3', 'OpenWebText2', 'ArXiv', 'Github', 'FreeLaw', 'StackExchange', 'USPTO Backgrounds', 'PubMed Abstracts', 'Gutenberg (PG-19)', 'OpenSubtitles', 'Wikipedia (en)', 'DM Mathematics', 'Ubuntu IRC', 'BookCorpus2', 'EuroParl', 'HackerNews', 'YoutubeSubtitles', 'PhilPapers', 'NIH ExPorter', 'Enron Emails']),
                }
            ),
            supervised_keys=None,
            homepage="http://pile.eleuther.ai/",
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        # TODO: checksums

        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN, gen_kwargs={"urls": self._TRAIN_DL_URLS, 'dl_manager': dl_manager}
            ),
            datasets.SplitGenerator(
                name=datasets.Split.VALIDATION, gen_kwargs={"urls": self._VAL_DL_URLS, 'dl_manager': dl_manager}
            ),
            datasets.SplitGenerator(
                name=datasets.Split.TEST, gen_kwargs={"urls": self._TEST_DL_URLS, 'dl_manager': dl_manager}
            ),
        ]

    def _generate_examples(self, urls, dl_manager):
        """Generate Pile examples."""
        filepaths = dl_manager.download(urls)
        
        for id_, row in enumerate(_readjsonlzstdfiles(filepaths)):
                yield id_, {"text": row['text'], "set": row["meta"]["pile_set_name"]}