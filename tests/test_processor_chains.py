# -*- coding: utf-8 -*-

"""Testing the processor chains for `ocrd_butler` package."""

import pytest
from ocrd_butler.chains.chain_configuration import chain_config
from ocrd_butler.chains.processor_chains import processor_chains

def test_chains_configuration():
    """ Test our chain definition. """
    processors = chain_config.keys()
    assert "TesserocrSegmentRegion" in processors
    assert "TesserocrSegmentLine" in processors
    assert "TesserocrSegmentWord" in processors
    assert "TesserocrRecognize" in processors

def test_predefined_chains():
    """ Test our chain definition. """
    assert len(processor_chains) == 1

    tesserocr_chain = processor_chains[0]
    processors = [list(p.keys())[0] for p in tesserocr_chain["processors"]]
    assert "TesserocrRecognize" in processors

    assert tesserocr_chain["processors"][-1]["TesserocrRecognize"]["parameters"]["model"] == "deu"
